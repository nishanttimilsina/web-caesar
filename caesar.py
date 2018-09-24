from helpers import rotate_character

def encrypt(text, rot):
    return_string = ""

    for x in text:
        return_string = return_string + rotate_character(x, rot)

    return return_string

def main():

    print(encrypt('Hello, World!', 5))

if __name__ == "__main__":
    main()