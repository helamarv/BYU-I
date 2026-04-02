def main():
    provinces_list = read_txt("provinces.txt")
    print(provinces_list)

    provinces_list_len = len(provinces_list)
    provinces_list_len -= 1

    # remove last line
    provinces_list = remove_lines(provinces_list_len, provinces_list) 

    # remove first line
    provinces_list = remove_lines(0, provinces_list)

    replaces("AB", "Alberta", provinces_list)

    word = "Alberta"

    counter = find_count_word(word, provinces_list)
    print()
    print(f"{word} occurs {counter} times in the modified list.")


def read_txt(file):
    text_list = []

    with open(file, mode="rt") as text_file:
        for line in text_file:
            clean_line = line.strip()
            text_list.append(clean_line)

        return text_list

def remove_lines(index, items):
    items.pop(index)
    return items

def replaces(old_string, new_string, items):
    for item in range(len(items)):
        if items[item] == old_string:
            items[item] = new_string

def find_count_word(word, items):
    counter=0
    for item in items:
        if item == word:
            counter += 1
    return counter



if __name__ == "__main__":
    main()