import csv

def main():
    KEY_INDEX = 0
    NAME_INDEX = 1
    students =  read_dictionary('students.csv', KEY_INDEX)
    # print(students)

    inumber = input("Pelase enter an I-Number: ")
    inumber=inumber.replace("-", "")

    if not inumber.isdigit():
        print("Invalid I-Number!")

    elif len(inumber) != 9:
        print("An I-Number must be 9 digits long")
    
    else:
        if inumber in students:

            student=students[inumber]
            name=student[NAME_INDEX]

            print(f"The student's name is {name}")
        else:
            print("No such student")
    

def read_dictionary(filename, keycolumn_index):
    # pass
    s_dictionary={}
    with open(filename, 'rt') as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ",")
        next(csvreader)
        for row in  csvreader:
            key_value = row[keycolumn_index]
            s_dictionary[key_value] = row
    return s_dictionary


if __name__ == "__main__":
    main()