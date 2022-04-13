from sample import *
from datetime import *


def add_store_from_user_input():
    store_id = input("Enter store id:  ")
    store_name = input("Enter store name:  ")
    add_store(store_id, store_name)


def add_customer_from_user_input():
    customer_fname = input("Enter the customers first name:  ")
    customer_lname = input("Enter the customers last name:  ")
    customer_email = input("Enter the customers email:  ")
    home_phone = input("Enter the customers home phone number:  ")
    cell_number = input("Enter the customers cell_phone_number:  ")
    add_customer(customer_fname, customer_lname, customer_email, home_phone, cell_number)


def add_order_from_user_input():
    customer_id = int(input("Enter the customer id:  "))
    product_id = int(input("Enter the product id:  "))
    order_desc = input("Enter order description:  ")
    order_id = input("Enter order id:  ")
    price = float(input("Enter items price:  "))
    total_cost = float(price * 1.15)
    current_date = date.today()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    quantity_bought = input(f"Enter amount of item bought:  " )
    add_order(customer_id, product_id, order_desc, order_id, total_cost, current_date, current_time, quantity_bought)


def add_product_from_user_input():
    vendor_id = input("Enter the vendor id:  ")
    store_id = input("Enter store id:  ")
    product_name = input("Enter the products name:  ")
    product_desc = input("Enter the product desc:  ")
    quantity_on_hand = input("Enter the quantity on hand:  ")
    price = input("Enter the price:  ")
    add_product(vendor_id, store_id, product_name, product_desc, quantity_on_hand, price)


def remove_store_from_user_input():
    store_id = input("Enter store id:  ")
    remove_store(store_id)


def remove_customer_from_user_input():
    customer_id = input("Enter the customer_id: ")
    remove_customer(customer_id)


def remove_order_record_from_user_input():
    order_id = input("Enter the order id: ")
    remove_order_record(order_id)


def remove_product_from_user_input():
    product_id = input("Enter the product id: ")
    remove_product(product_id)


def update_store_from_user_input():
    current_store_name = input("Enter the current store name:  ")
    new_store_name = input("Enter the new store name:  ")
    update_store(current_store_name, new_store_name)
    print(f'Store name updated to {new_store_name}')


def update_product_from_user_input():
    product_name = input("Enter product's name:  ")
    quantity_on_hand = input("Enter quantity on hand:  ")
    update_product(product_name, quantity_on_hand)
    print(f"{product_name}'s quantity on hand is now {quantity_on_hand}")


def update_customer_lname_from_user_input():
    customer_id = input("Enter customer id:  ")
    customer_lname = input("Enter customer's new last name:  ")
    update_customer_lname(customer_id, customer_lname)
    print(f"Customer {customer_id} now has the last name '{customer_lname}'")


def update_customer_email_from_user_input():
    customer_id = input("Enter customer id:  ")
    customer_email = input("Enter customer's new email:  ")
    update_customer_email(customer_id, customer_email)
    print(f"Customer {customer_id} now has the email of '{customer_email}'")


def update_customer_home_phone_from_user_input():
    customer_id = input("Enter customer id:  ")
    home_phone = input("Enter customer's new home phone number:  ")
    update_customer_home_phone(customer_id, home_phone)
    print(f"Customer {customer_id} now has the home phone number of '{home_phone}'")


def update_customer_cell_number_from_user_input():
    customer_id = input("Enter customer id:  ")
    cell_number = input("Enter customer's new cell phone number:  ")
    update_customer_cell_number(customer_id, cell_number)
    print(f"Customer {customer_id} now has a cell phone number of '{cell_number}'")


def list_all_products():
    product_list = generate_product_list()
    for product in product_list:
        print(product)


def list_out_of_stock_products():
    out_of_stock_list = generate_out_of_stock_products()
    for product in out_of_stock_list:
        print(product)


def list_active_customers():
    active_customer_list = generate_customers_active_last_month()
    for customer in active_customer_list:
        print(customer)


def display_menu():
    print("MENU: ")
    print("1.  Add Store")
    print("2.  Add Customer")
    print("3.  Add Order")
    print("4.  Add Product")
    print("5.  Remove Store")
    print("6.  Remove Customer")
    print("7.  Remove Order")
    print("8.  Remove Product")
    print("9.  Update Store")
    print("10.  Update Product")
    print("11.  Update Customer's last name")
    print("12.  Update Customer's email")
    print("13.  Update Customer's home phone number")
    print("14.  Update Customer's cell phone number")
    print("15.  View all products")
    print("16.  View products that are out of stock")
    print("17.  View active customers")
    print("0.  Quit")
    print("========================================")
    print()


def main():
    while True:
        display_menu()
        choice = input("Enter your choice:  ")
        print()
        if choice == "1":
            add_store_from_user_input()
            print()
        elif choice == "2":
            add_customer_from_user_input()
            print()
        elif choice == "3":
            add_order_from_user_input()
            print()
        elif choice == "4":
            add_product_from_user_input()
            print()
        elif choice == "5":
            remove_store_from_user_input()
            print()
        elif choice == "6":
            remove_customer_from_user_input()
            print()
        elif choice == "7":
            remove_order_record_from_user_input()
            print()
        elif choice == "8":
            remove_product_from_user_input()
            print()
        elif choice == "9":
            update_store_from_user_input()
            print()
        elif choice == "10":
            update_product_from_user_input()
            print()
        elif choice == "11":
            update_customer_lname_from_user_input()
            print()
        elif choice == "12":
            update_customer_email_from_user_input()
            print()
        elif choice == "13":
            update_customer_home_phone_from_user_input()
            print()
        elif choice == "14":
            update_customer_cell_number_from_user_input()
            print()
        elif choice == "15":
            list_all_products()
            print()
        elif choice == "16":
            list_out_of_stock_products()
            print()
        elif choice == "17":
            list_active_customers()
            print()
        elif choice == "0":
            print("Bye!")
            break
        else:
            print("Invalid Choice.  Try Again.")


if __name__ == '__main__':
    main()