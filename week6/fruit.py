def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")

    fruit_list.reverse()
    print(f"Reverse: {fruit_list}")


    fruit_list.append('orange')
    print(f"List with Orange : {fruit_list}")

    i = fruit_list.index('apple')
    # print(i)
    fruit_list.insert(i, 'cherry')
    print(f"List with cherry on position before apple: {fruit_list}")

    fruit_list.remove('banana')
    print(f"List without banana : {fruit_list}")

    fruit_list.pop()
    print(f"pop : {fruit_list}")

    fruit_list.sort()
    print(f"List wit sort : {fruit_list}")

    fruit_list.clear()
    print(f"Clear List : {fruit_list}")


if __name__ == "__main__":
    main()
