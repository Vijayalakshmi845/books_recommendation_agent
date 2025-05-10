import cohere  # type: ignore

# Initialize Cohere client with your API key
co = cohere.Client('2id2UIjBoWXkB2qLrLix0brN1mw0GDzSiF3vmdeC')  # Replace with your actual key

# Ask user what kind of books they liked
liked_books = input("Enter the names of books you liked: ")

# Prepare message
message = f"I liked these books: {liked_books}. Can you recommend 5 similar books with a short reason for each?"

# Use chat endpoint
response = co.chat(
    model='command-r-plus',  # Or 'command-r' if that's your plan
    message=message
)

# Print the response
print("\n📚 Recommended Books:\n")
print(response.text.strip())