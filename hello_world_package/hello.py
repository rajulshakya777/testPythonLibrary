import os

def say_hello():
    # Construct the file path
    file_path = os.path.join(os.path.dirname(__file__), 'data', 'sample.txt')
    
    # Read the content of the sample text file
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("The sample text file was not found.")
