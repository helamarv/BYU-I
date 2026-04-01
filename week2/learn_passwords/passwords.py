LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\","`", "~"]


def main():
    password=""
    while True:
        password = input("Write your password: ")
        if password == "Q" or password == "q":
            print("You quit")
            break

        strength = password_strength(password,min_length=10,strong_length=16)
        if strength == None:
            strength = 0
        print(f"The password strength is = {strength}")

def word_in_file(word,filename,case_sensitive):
    with open(filename, "r",encoding="utf-8") as file:
        for item in file:    
            if case_sensitive == True:
                if item.strip() == word:
                    print('Password is a commonly used password and is not secure.')
                    return True
            else:
                if item.strip().lower() == word:
                    print('Password is a dictionary word and is not secure.')
                    return True
 
        return False                


def word_has_character(word,character_list):
    for character in word:
        if character in character_list:
            return True
    return False

def word_complexity(word):
    lower_char = word_has_character(word, LOWER)
    upper_char = word_has_character(word, UPPER)
    special_char = word_has_character(word, SPECIAL)
    digits_char = word_has_character(word, DIGITS)

    complexity = 1

    if lower_char == True :
        # CREATIVITY
        print("Your password has lower case letters!")
        complexity += 1
    if special_char == True:
        # CREATIVITY
        print("Your password has special characters!")
        complexity += 1
    if upper_char == True:
        # CREATIVITY
        print("Your password has upper case letters!")
        complexity += 1
    if digits_char == True:
        # CREATIVITY
        print("Your password has numbers!")
        complexity += 1
    
    if word == "":
        return 0
    elif lower_char == False and upper_char == False and special_char == False and digits_char == False:
        return 0
    else:
        return complexity



def password_strength(password,min_length,strong_length):
    
    # aftertought
    dictionary = r"C:\cse111\Week 2\wordlist.txt"
    word_in_dictionary = word_in_file(password, dictionary, False)
    if word_in_dictionary == True:
        return 0
    
    # iloveny
    passwords_dictionary = r"C:\cse111\Week 2\toppasswords.txt"
    word_in_passwords = word_in_file(password, passwords_dictionary, True)
    if word_in_passwords == True:
        return 0 

    # checks min length password
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1
    
    # checks min length strong password
    if len(password) >=strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5
    
    # word complexity
    complexity = 0
    complexity = word_complexity(password)

    return complexity

if __name__ == "__main__":
    main()
