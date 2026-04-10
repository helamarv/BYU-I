import csv

def main():
    PRODUCTS_KEY_INDEX=0
    PRODUCTS_NAME_INDEX=1
    PRODUCTS_PRICE_INDEX=2

    REQUEST_KEY_INDEX=0
    REQUEST_QUANTITY_INDEX=1



    products_dict =  read_dictionary('products.csv', PRODUCTS_KEY_INDEX)
    print("All Products")
    print(products_dict)

    # ---------------------------
    req_list=[]
    with open("request.csv", 'rt') as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ",")
        next(csvreader)
        for row in csvreader:
            req_list.append(row)

    print(f"Requested Items")
    # print(req_list)

    for req in req_list:
        key = req[REQUEST_KEY_INDEX]
        prod = products_dict[key]
        
        name = prod[PRODUCTS_NAME_INDEX]
        quant = req[REQUEST_QUANTITY_INDEX]
        price = prod[PRODUCTS_PRICE_INDEX]
        
        print(f"{name}: {quant} @ {price}")

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