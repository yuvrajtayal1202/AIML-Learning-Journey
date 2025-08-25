from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Create the template correctly
chat_template = ChatPromptTemplate.from_messages([
    ('system', "You are a helping customer service guide"),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{query}'),
])

# Initialize chat history
chat_history = []

# Load chat history from file
with open('chat_history.txt', 'r') as f:
    chat_history.extend([line.strip() for line in f.readlines()])

# Print chat history
print(chat_history)

# Example of filling the template with values
prompt = chat_template.invoke({
    "chat_history": chat_history,
    "query": "I need help with my order status"
})

print(prompt)
