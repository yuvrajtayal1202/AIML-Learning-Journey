# tclConfig.sh --
#
# This shell script (for sh) is generated automatically by Tcl's
# configure script.  It will create shell variables for most of
# the configuration options discovered by the configure script.
# This script is intended to be included by the configure scripts
# for Tcl extensions so that they don't have to figure this all
# out for themselves.
#
# The information in this file is specific to a single platform.

TCL_DLL_FILE="tcl86t.dll"

# Tcl's version number.
TCL_VERSION='8.6'
TCL_MAJOR_VERSION='8'
TCL_MINOR_VERSION='6'
TCL_PATCH_LEVEL='8.6.14'

# C compiler to use for compilation.
TCL_CC='cl.exe'

# -D flags for use with the C compiler.
TCL_DEFS='-nologo -c /D_ATL_XP_TARGETING  /DHAVE_CPUID=1 -W3 -wd4090 -wd4146 -wd4311 -wd4312 -FpC:\b\abs_7cplcn7ppb\croot\tk_1748849403747\work\tcl8.6.14\win\Release_AMD64_VC1929\tcl_ThreadedDynamic\  -fp:strict -O2 -GS -GL -MD -I"C:\b\abs_7cplcn7ppb\croot\tk_1748849403747\work\tcl8.6.14\win\..\win" -I"C:\b\abs_7cplcn7ppb\croot\tk_1748849403747\work\tcl8.6.14\win\..\generic"  -I"C:\b\abs_7cplcn7ppb\croot\tk_1748849403747\work\tcl8.6.14\win\..\libtommath"  /DTCL_TOMMATH /DMP_PREC=4 /Dinline=__inline /DHAVE_ZLIB=1 /D_CRT_SECURE_NO_DEPRECATE /D_CRT_NONSTDC_NO_DEPRECATE /DMP_FIXED_CUTOFFS /DSTDC_HEADERS /DUSE_NMAKE=1 /DHAVE_STDINT_H=1 /DHAVE_INTTYPES_H=1 /DHAVE_STDBOOL_H=1 /DTCL_THREADS=1 /DUSE_THREAD_ALLOC=1 /DNDEBUG /DTCL_CFG_OPTIMIZED /DTCL_CFG_DO64BIT   /DBUILD_tcl'

# If TCL was built with debugging symbols, generated libraries contain
# this string at the end of the library name (before the extension).
TCL_DBGX=t

# Default flags used in an optimized and debuggable build, respectively.
TCL_CFLAGS_DEBUG='-nologo -c -W3 -YX -FpC:\b\abs_7cplcn7ppb\croot\tk_1748849403747\work\tcl8.6.14\win\Release_AMD64_VC1929\tcl_ThreadedDynamic\ -MDd'
TCL_CFLAGS_OPTIMIZE='-nologo -c -W3 -YX -FpC:\b\abs_7cplcn7ppb\croot\tk_1748849403747\work\tcl8.6.14\win\Release_AMD64_VC1929\tcl_ThreadedDynamic\ -MD'

# Default linker flags used in an optimized and debuggable build, respectively.
TCL_LDFLAGS_DEBUG='-nologo -machine:AMD64 -debug -debugtype:cv'
TCL_LDFLAGS_OPTIMIZE='-nologo -machine:AMD64 -release -opt:ref -opt:icf,3'

# Flag, 1: we built a shared lib, 0 we didn't
TCL_SHARED_BUILD=1

# The name of the Tcl library (may be either a .a file or a shared library):
TCL_LIB_FILE='tcl86t.lib'

# Flag to indicate whether shared libraries need export files.
TCL_NEEDS_EXP_FILE=''

# Deprecated. Same as TCL_UNSHARED_LIB_SUFFIX
TCL_EXPORT_FILE_SUFFIX='86t.lib'

# Additional libraries to use when linking Tcl.
TCL_LIBS='kernel32.lib advapi32.lib netapi32.lib user32.lib userenv.lib ws2_32.lib ucrt.lib netapi32.lib user32.lib userenv.lib ws2_32.lib'

# Top-level directory in which Tcl's platform-independent files are
# installed.
TCL_PREFIX='C:/Users/yuvra/Desktop/Repos/AIML-Learning-Journey/venv\Library'

# Top-level directory in which Tcl's platform-specific files (e.g.
# executables) are installed.
TCL_EXEC_PREFIX='C:/Users/yuvra/Desktop/Repos/AIML-Learning-Journey/venv\Library\bin'

# Flags to pass to cc when compiling the components of a shared library:
TCL_SHLIB_CFLAGS=''

# Flags to pass to cc to get warning messages
TCL_CFLAGS_WARNING='-W3'

# Extra flags to pass to cc:
TCL_EXTRA_CFLAGS='-YX'

# Base command to use for combining object files into a shared library:
TCL_SHLIB_LD='link -nologo -machine:AMD64  -ltcg -release -opt:ref -opt:icf,3 -nodefaultlib:libucrt.lib -dll'

# Base command to use for combining object files into a static library:
TCL_STLIB_LD='lib -nologo'

# Either '$LIBS' (if dependent libraries should be included when linking
# shared libraries) or an empty string.  See Tcl's configure.in for more
# explanation.
TCL_SHLIB_LD_LIBS='kernel32.lib advapi32.lib netapi32.lib user32.lib userenv.lib ws2_32.lib ucrt.lib netapi32.lib user32.lib userenv.lib ws2_32.lib'

# Suffix to use for the name of a shared library.
TCL_SHLIB_SUFFIX='.dll'

# Library file(s) to include in tclsh and other base applications
# in order to provide facilities needed by DLOBJ above.
TCL_DL_LIBS=''

# Flags to pass to the compiler when linking object files into
# an executable tclsh or tcltest binary.
TCL_LD_FLAGS=''

# Flags to pass to cc/ld, such as "-R /usr/local/tcl/lib", that tell the
# run-time dynamic linker where to look for shared libraries such as
# libtcl.so.  Used when linking applications.  Only works if there
# is a variable "LIB_RUNTIME_DIR" defined in the Makefile.
TCL_CC_SEARCH_FLAGS=''
TCL_LD_SEARCH_FLAGS=''

# Additional object files linked with Tcl to provide compatibility
# with standard facilities from ANSI C or POSIX.
TCL_COMPAT_OBJS=''

# Name of the ranlib program to use.
TCL_RANLIB=''

# -l flag to pass to the linker to pick up the Tcl library
TCL_LIB_FLAG='tcl86t.lib'

# String to pass to linker to pick up the Tcl library from its
# build directory.
TCL_BUILD_LIB_SPEC='C:\b\abs_7cplcn7ppb\croot\tk_1748849403747\work\tcl8.6.14\win\Release_AMD64_VC1929\tcl86t.lib'

# String to pass to linker to pick up the Tcl library from its
# installed directory.
TCL_LIB_SPEC='C:/Users/yuvra/Desktop/Repos/AIML-Learning-Journey/venv\Library\lib\tcl86t.lib'

# String to pass to the compiler so that an extension can
# find installed Tcl headers.
TCL_INCLUDE_SPEC='-IC:/Users/yuvra/Desktop/Repos/AIML-Learning-Journey/venv\Library\include'

# Indicates whether a version numbers should be used in -l switches
# ("ok" means it's safe to use switches like -ltcl7.5;  "nodots" means
# use switches like -ltcl75).  SunOS and FreeBSD require "nodots", for
# example.
TCL_LIB_VERSIONS_OK='nodots'

# String that can be evaluated to generate the part of a shared library
# name that comes after the "libxxx" (includes version number, if any,
# extension, and anything else needed).  May depend on the variables
# VERSION and SHLIB_SUFFIX.  On most UNIX systems this is
# ${VERSION}${SHLIB_SUFFIX}.
TCL_SHARED_LIB_SUFFIX='86t.dll'

# String that can be evaluated to generate the part of an unshared library
# name that comes after the "libxxx" (includes version number, if any,
# extension, and anything else needed).  May depend on the variable
# VERSION.  On most UNIX systems this is ${VERSION}.a.
TCL_UNSHARED_LIB_SUFFIX='86t.lib'

# Location of the top-level source directory from which Tcl was built.
# This is the directory that contains a README file as well as
# subdirectories such as generic, unix, etc.  If Tcl was compiled in a
# different place than the directory containing the source files, this
# points to the location of the sources, not the location where Tcl was
# compiled.
TCL_SRC_DIR='C:\b\abs_7cplcn7ppb\croot\tk_1748849403747\work\tcl8.6.14\win\..'

# List of standard directories in which to look for packages during
# "package require" commands.  Contains the "prefix" directory plus also
# the "exec_prefix" directory, if it is different.
TCL_PACKAGE_PATH=''

# Tcl supports stub.
TCL_SUPPORTS_STUBS=1

# The name of the Tcl stub library (.a):
TCL_STUB_LIB_FILE='tclstub86.lib'

# -l flag to pass to the linker to pick up the Tcl stub library
TCL_STUB_LIB_FLAG='tclstub86.lib'

# String to pass to linker to pick up the Tcl stub library from its
# build directory.
TCL_BUILD_STUB_LIB_SPEC='-LC:\b\abs_7cplcn7ppb\croot\tk_1748849403747\work\tcl8.6.14\win\Release_AMD64_VC1929 tclstub86.lib'

# String to pass to linker to pick up the Tcl stub library from its
# installed directory.
TCL_STUB_LIB_SPEC='-LC:/Users/yuvra/Desktop/Repos/AIML-Learning-Journey/venv\Library\lib tclstub86.lib'

# Path to the Tcl stub library in the build directory.
TCL_BUILD_STUB_LIB_PATH='C:\b\abs_7cplcn7ppb\croot\tk_1748849403747\work\tcl8.6.14\win\Release_AMD64_VC1929\tclstub86.lib'

# Path to the Tcl stub library in the install directory.
TCL_STUB_LIB_PATH='C:/Users/yuvra/Desktop/Repos/AIML-Learning-Journey/venv\Library\lib\tclstub86.lib'

# Flag, 1: we built Tcl with threads enabled, 0 we didn't
TCL_THREADS=1

# Name of the zlib library that extensions should use
TCL_ZLIB_LIB_NAME='zdll.lib'
