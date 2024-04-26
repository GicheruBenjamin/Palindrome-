def is_palindrome(input_string):
    # Remove spaces, punctuation, and convert to lowercase
    processed_string = ''.join(char.lower() for char in input_string if char.isalnum())

    # Check if the processed string is equal to its reverse
    return processed_string == ''.join(reversed(processed_string))

# Get user input
user_input = input("Enter a number, phrase, or word: ")

# Check if the input is a palindrome and print the result
if is_palindrome(user_input):
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")

          
