# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

# Create a function to read the contents of the file
def read_file_content(filename):
    # [assignment] Add your code here 
    # Open the file  and return the read file
    file = open(filename, "r")
    return file.read()

# Create a function to count the words in the file
def count_words():
    # Save the opeened file to a variable
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    # Initialize a dictionary to store all the words and their frequencies
    dictionary = {}

    # Convert the file to a list of words
    words  = text.split()
    
    # Loop through the list
    for word in words:
        # Check if the current word already exists in the dictionary
        if word in dictionary:
            # If it does, increment the frequency 
            dictionary[word] += 1
        else:
            # If it doesn't, set it to a frequency of 1
            dictionary[word]  = 1
            # Return the dictionary
    return dictionary

# Call the function
print(count_words())
