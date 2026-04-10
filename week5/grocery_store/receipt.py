# Exceeding the Requirements
# Write code to print a reminder of how many days until the New Years Sale begins (Jan 1) at the bottom of the receipt.

import csv
import datetime


def main():
    try:

        PRODUCTS_KEY_INDEX=0
        PRODUCTS_NAME_INDEX=1
        PRODUCTS_PRICE_INDEX=2

        REQUEST_KEY_INDEX=0
        REQUEST_QUANTITY_INDEX=1

        STORE_NAME = "HRV Store"

        PRODUCTS_FILE = "products.csv"
        REQUEST_FILE = "request.csv"

        try:
            products_dict =  read_dictionary(PRODUCTS_FILE, PRODUCTS_KEY_INDEX)
        except FileNotFoundError:
            print("Error: missing file")
            print(f"[Errno 2] No such file or directory: '{PRODUCTS_FILE}'")
            return
        except PermissionError:
            print("Error: permission denied")
            print(f"[Errno 3] Permission denied: '{PRODUCTS_FILE}'")
            return

        req_list=[]
        try:
            with open(REQUEST_FILE, 'rt') as csvfile:
                csvreader = csv.reader(csvfile, delimiter = ",")
                next(csvreader)
                for row in csvreader:
                    req_list.append(row)
        except FileNotFoundError:
            print("Error: missing file")
            print(f"[Errno 2] No such file or directory: '{REQUEST_FILE}'")
            return
        except PermissionError:
            print("Error: permission denied")
            print(f"[Errno 3] Permission denied: '{REQUEST_FILE}'")
            return


        quantity_items = 0
        sum_each_item = 0
        sum_price_items = 0
        taxes = 0

        print(F"{STORE_NAME}")

        for req in req_list:
                key = req[REQUEST_KEY_INDEX]
                prod = products_dict[key]
                
                name = prod[PRODUCTS_NAME_INDEX]
                quant = req[REQUEST_QUANTITY_INDEX]
                quantity_items += int(quant)

                price = prod[PRODUCTS_PRICE_INDEX]
                sum_each_item = float(price) * int(quant)
                sum_price_items += float(sum_each_item)
                
                print(f"{name}: {quant} @ {price}")

        
        taxes = sum_price_items * 0.06
        total = sum_price_items + taxes

        print(f"Number of Items: {quantity_items}")
        print(f"Subtotal: {sum_price_items:.2f}")
        print(f"Sales Tax: {taxes:.2f}")
        print(f"Total: {total:.2f}")
        print(f"Thank you for shopping at the {STORE_NAME}.")

        date = datetime.datetime.now()
        formated_date = date.strftime("%a %b  %d %X %Y")
        print(formated_date)

        # Exceeding the Requirements
        next_year = date.year + 1
        new_year = datetime.datetime(next_year, 1, 1)
        days_until_NYS = new_year - date
        print(f"Days until NEW YEARS SALE (Jan 1) : {days_until_NYS.days}")

    except KeyError as e:
        print(f"Error: unknown product ID in the request.csv file")
        print(e)
        return


def read_dictionary(filename, key_column_index):
    s_dictionary={}
    with open(filename, 'rt') as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ",")
        next(csvreader)
        for row in  csvreader:
            key_value = row[key_column_index]
            s_dictionary[key_value] = row
    return s_dictionary


if __name__ == "__main__":
    main()