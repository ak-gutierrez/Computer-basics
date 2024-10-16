def reverse_sentence():
    # Take input from the user
    sentence = input("Enter a sentence: ")
    
    # Split the sentence into words
    words = sentence.split()
    
    # Reverse the order of the words
    reversed_words = words[::-1]
    
    # Join the reversed words into a single string
    reversed_sentence = ' '.join(reversed_words)
    
    # Print the reversed sentence
    print("Reversed sentence:", reversed_sentence)

# Call the function
reverse_sentence()