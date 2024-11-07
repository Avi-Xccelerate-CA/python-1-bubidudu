#Week 1 Test

# For file with only numbers, you should only return one thing(i.e.the first 10 characters)

# For file with story,you NEED to return two things(i.e. a modified string AND a list)
#  you can return multiple values by simply return them separated by commas like the following
# def editor(fname):
#
#     return 'modifystring', [a,b,c,d]

# HINT: to call your function for the story.txt file, use the following command
# editor("./data/story.txt")
# return statement should be in the format below
# return 'modifystring', [a,b,c,d]



import re
from collections import Counter

def editor(fname):
    # Read the content of the file
    with open(fname, 'r') as file:
        content = file.read().strip()  # Remove any leading/trailing whitespace including newlines
    
    # Check if the content is numeric
    if content.isdigit():
        # Return the first 10 characters as a string without the comma
        return content[:10]  # Remove the comma to return a string
    
    # If it's a story, process the text
    else:
        # Convert to lowercase
        modified_string = content.lower()
        
        # Use regex to find words and count their frequencies
        words = re.findall(r'\b\w+\b', modified_string)
        word_counts = Counter(words)
        
        # Get the top 5 most common words
        top_five = [word for word, _ in word_counts.most_common(5)]
        
        # Return the modified string and the list of top 5 words
        return modified_string, top_five

# Example of how to call the function with the number file
if __name__ == "__main__":
    # Specify the path to the number.txt file in the data folder
    result = editor("data/number.txt")
    print(result)  # This should output '1857617284'

    result = editor("data/story.txt")
    print(result)  # This should output '1857617284'

    result = editor("data/story2.txt")
    print(result)  # This should output '1857617284'