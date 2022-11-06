def cal_sales(quantities, count):
    product = 0
    if count == 1:
        product = 2.94 * quantities
    if count == 2:
        product = 4.50 * quantities
    if count == 3:
        product = 9.98 * quantities
    if count == 4:
        product = 4.49 * quantities
    if count == 5:
        product = 6.87 * quantities
    return product


quantity = int(input("Enter price"))
product_no = int(input("Enter product number"))
total = 0
while quantity != 0:
    total += cal_sales(quantity, product_no)
    quantity = int(input("Enter quantity sold"))
    product_no = int(input("Enter product number"))
else:
    print(f'Total: {total}')
