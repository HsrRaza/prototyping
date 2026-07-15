import csv

total_sales = 0
product_sales= {}
product_quantity = {}
total_orders = 0


with open("02_phase/CsvAnalyzer/sales.csv", 'r') as file:
    reader = csv.DictReader(file)

    for row in reader :
        total_orders +=1

        quantity = int(row["Quantity"])
        price =float(row["Price"])
        
        revenue = quantity * price
        total_sales += revenue

        product = row["Product"]

        product_sales[product] = product_sales.get(product, 0) + revenue

        product_quantity[product] = product_quantity.get(product , 0) + quantity


best_product =max(product_quantity , key=product_quantity.get)
average_sales = total_sales /total_orders
        

print("\n Revenue By product")

print("-"*20)

for product , revenue in product_sales.items():
    print(f"{product:<10} ${revenue}")


print("\n Quantity Sold")
print("-" * 20)

for product , quantity in product_quantity.items():
    print(f"{product:<10} {quantity} ")

print("="*30)
print("SALES REPORT")
print("="* 30)

print(f"Total Orders   : {total_orders}")
print(f"Total Revenue  : ${total_sales}")
print(f"Average Sale   : ${average_sales:.2f}")
print(f"Best Product   :  {best_product}")

