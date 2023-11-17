import sys

def wc(file_path=None):
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
    else:
        # If no file is provided, read from standard input
        content = sys.stdin.read()

    lines = content.splitlines()
    words = content.split()
    characters = len(content)

    return len(lines), len(words), characters, file_path

if __name__ == "__main__":
    file_path = None

    # Check if a file path is provided as a command-line argument
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = 'foo'

    lines, words, characters, file_name = wc(file_path)

    # Print the results in the same format as the Unix wc command
    print(f"{lines}\t{words}\t{characters}", end='')

    if file_name:
        print(f"\t{file_name}")
    else:
        print()
 
