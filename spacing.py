def add_space(char, width, spaces):
    # char: character to be printed
    # width: number of times the character is to be printed
    # spaces: number of new lines to add below after printing the character
    print((str(char) * int(width)) + ("\n" * int(spaces)))