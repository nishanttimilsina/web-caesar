def alphabet_position(letter):
    return (ord(letter.upper()) - 65)

def rotate_character(char, rot):
    if char.isalpha():
        if char.isupper():
            char = chr(65 + ((alphabet_position(char) + rot) % 26))
        else:
            char = chr(97 + ((alphabet_position(char) + rot) % 26))
    return char

def main():
    print(rotate_character('The crow', 'boom'))

if __name__ == "__main__":
    main()