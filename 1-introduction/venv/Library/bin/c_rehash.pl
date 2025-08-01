#!/usr/bin/env perl

# WARNING: do not edit!
# Generated by makefile from tools\c_rehash.in
# Copyright 1999-2022 The OpenSSL Project Authors. All Rights Reserved.
#
# Licensed under the Apache License 2.0 (the "License").  You may not use
# this file except in compliance with the License.  You can obtain a copy
# in the file LICENSE in the source distribution or at
# https://www.openssl.org/source/license.html

# Perl c_rehash script, scan all files in a directory
# and add symbolic links to their hash values.

my $dir = "C:\\Program Files\\Common Files\\ssl";
my $prefix = "c:/Users/yuvra/Desktop/Repos/AIML-Learning-Journey/venv\\Library";

my $errorcount = 0;
my $openssl = $ENV{OPENSSL} || "openssl";
my $pwd;
my $x509hash = "-subject_hash";
my $crlhash = "-hash";
my $verbose = 0;
my $symlink_exists=eval {symlink("",""); 1};
my $removelinks = 1;

##  Parse flags.
while ( $ARGV[0] =~ /^-/ ) {
    my $flag = shift @ARGV;
    last if ( $flag eq '--');
    if ( $flag eq '-old') {
        $x509hash = "-subject_hash_old";
        $crlhash = "-hash_old";
    } elsif ( $flag eq '-h' || $flag eq '-help' ) {
        help();
    } elsif ( $flag eq '-n' ) {
        $removelinks = 0;
    } elsif ( $flag eq '-v' ) {
        $verbose++;
    }
    else {
        print STDERR "Usage error; try -h.\n";
        exit 1;
    }
}

sub help {
    print "Usage: c_rehash [-old] [-h] [-help] [-v] [dirs...]\n";
    print "   -old use old-style digest\n";
    print "   -h or -help print this help text\n";
    print "   -v print files removed and linked\n";
    exit 0;
}

eval "require Cwd";
if (defined(&Cwd::getcwd)) {
    $pwd=Cwd::getcwd();
} else {
    $pwd=`pwd`;
    chomp($pwd);
}

# DOS/Win32 or Unix delimiter?  Prefix our installdir, then search.
my $path_delim = ($pwd =~ /^[a-z]\:/i) ? ';' : ':';
$ENV{PATH} = "$prefix/bin" . ($ENV{PATH} ? $path_delim . $ENV{PATH} : "");

if (! -x $openssl) {
    my $found = 0;
    foreach (split /$path_delim/, $ENV{PATH}) {
        if (-x "$_/$openssl") {
            $found = 1;
            $openssl = "$_/$openssl";
            last;
        }
    }
    if ($found == 0) {
        print STDERR "c_rehash: rehashing skipped ('openssl' program not available)\n";
        exit 0;
    }
}

if (@ARGV) {
    @dirlist = @ARGV;
} elsif ($ENV{SSL_CERT_DIR}) {
    @dirlist = split /$path_delim/, $ENV{SSL_CERT_DIR};
} else {
    $dirlist[0] = "$dir/certs";
}

if (-d $dirlist[0]) {
    chdir $dirlist[0];
    $openssl="$pwd/$openssl" if (!-x $openssl);
    chdir $pwd;
}

foreach (@dirlist) {
    if (-d $_ ) {
        if ( -w $_) {
            hash_dir($_);
        } else {
            print "Skipping $_, can't write\n";
            $errorcount++;
        }
    }
}
exit($errorcount);

sub copy_file {
    my ($src_fname, $dst_fname) = @_;

    if (open(my $in, "<", $src_fname)) {
        if (open(my $out, ">", $dst_fname)) {
            print $out $_ while (<$in>);
            close $out;
        } else {
            warn "Cannot open $dst_fname for write, $!";
        }
        close $in;
    } else {
        warn "Cannot open $src_fname for read, $!";
    }
}

sub hash_dir {
    my $dir = shift;
    my %hashlist;

    print "Doing $dir\n";

    if (!chdir $dir) {
        print STDERR "WARNING: Cannot chdir to '$dir', $!\n";
        return;
    }

    opendir(DIR, ".") || print STDERR "WARNING: Cannot opendir '.', $!\n";
    my @flist = sort readdir(DIR);
    closedir DIR;
    if ( $removelinks ) {
        # Delete any existing symbolic links
        foreach (grep {/^[\da-f]+\.r{0,1}\d+$/} @flist) {
            if (-l $_) {
                print "unlink $_\n" if $verbose;
                unlink $_ || warn "Can't unlink $_, $!\n";
            }
        }
    }
    FILE: foreach $fname (grep {/\.(pem|crt|cer|crl)$/} @flist) {
        # Check to see if certificates and/or CRLs present.
        my ($cert, $crl) = check_file($fname);
        if (!$cert && !$crl) {
            print STDERR "WARNING: $fname does not contain a certificate or CRL: skipping\n";
            next;
        }
        link_hash_cert($fname) if ($cert);
        link_hash_crl($fname) if ($crl);
    }

    chdir $pwd;
}

sub check_file {
    my ($is_cert, $is_crl) = (0,0);
    my $fname = $_[0];

    open(my $in, "<", $fname);
    while(<$in>) {
        if (/^-----BEGIN (.*)-----/) {
            my $hdr = $1;
            if ($hdr =~ /^(X509 |TRUSTED |)CERTIFICATE$/) {
                $is_cert = 1;
                last if ($is_crl);
            } elsif ($hdr eq "X509 CRL") {
                $is_crl = 1;
                last if ($is_cert);
            }
        }
    }
    close $in;
    return ($is_cert, $is_crl);
}

sub compute_hash {
    my $fh;
    if ( $^O eq "VMS" ) {
        # VMS uses the open through shell
        # The file names are safe there and list form is unsupported
        if (!open($fh, "-|", join(' ', @_))) {
            print STDERR "Cannot compute hash on '$fname'\n";
            return;
        }
    } else {
        if (!open($fh, "-|", @_)) {
            print STDERR "Cannot compute hash on '$fname'\n";
            return;
        }
    }
    return (<$fh>, <$fh>);
}

# Link a certificate to its subject name hash value, each hash is of
# the form <hash>.<n> where n is an integer. If the hash value already exists
# then we need to up the value of n, unless its a duplicate in which
# case we skip the link. We check for duplicates by comparing the
# certificate fingerprints

sub link_hash_cert {
    link_hash($_[0], 'cert');
}

# Same as above except for a CRL. CRL links are of the form <hash>.r<n>

sub link_hash_crl {
    link_hash($_[0], 'crl');
}

sub link_hash {
    my ($fname, $type) = @_;
    my $is_cert = $type eq 'cert';

    my ($hash, $fprint) = compute_hash($openssl,
                                       $is_cert ? "x509" : "crl",
                                       $is_cert ? $x509hash : $crlhash,
                                       "-fingerprint", "-noout",
                                       "-in", $fname);
    chomp $hash;
    $hash =~ s/^.*=// if !$is_cert;
    chomp $fprint;
    return if !$hash;
    $fprint =~ s/^.*=//;
    $fprint =~ tr/://d;
    my $suffix = 0;
    # Search for an unused hash filename
    my $crlmark = $is_cert ? "" : "r";
    while(exists $hashlist{"$hash.$crlmark$suffix"}) {
        # Hash matches: if fingerprint matches its a duplicate cert
        if ($hashlist{"$hash.$crlmark$suffix"} eq $fprint) {
            my $what = $is_cert ? 'certificate' : 'CRL';
            print STDERR "WARNING: Skipping duplicate $what $fname\n";
            return;
        }
        $suffix++;
    }
    $hash .= ".$crlmark$suffix";
    if ($symlink_exists) {
        print "link $fname -> $hash\n" if $verbose;
        symlink $fname, $hash || warn "Can't symlink, $!";
    } else {
        print "copy $fname -> $hash\n" if $verbose;
        copy_file($fname, $hash);
    }
    $hashlist{$hash} = $fprint;
}
