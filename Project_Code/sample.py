import mysql.connector
from mysql.connector import connect
import datetime

hostname = "localhost"
user_name = "root"
pwd = "roottoor"


def execute_and_commit(query):
    with connect(host=hostname, user=user_name, password=pwd) as mysql_connection_object:
        with mysql_connection_object.cursor() as mysql_cursor:
            mysql_cursor.execute(query)
            mysql_connection_object.commit()


def generate_product_list():
    with connect(host=hostname, user=user_name, password=pwd) as database:
        with database.cursor() as mycursor:
            mycursor.execute("SELECT * FROM project.product;")
            product_list = [f"Name\tQuantity",
                            f"====\t========"]
            for product in mycursor:
                product_list.append(f"{product[3]}\t{product[5]}")
        return product_list


def generate_out_of_stock_products():
    with connect(host=hostname, user=user_name, password=pwd) as database:
        with database.cursor() as mycursor:
            mycursor.execute("SELECT * FROM project.product where quantity_on_hand <= 0;")
            out_of_stock_list = [f"Out of Stock",
                                 f"============"]
            for product in mycursor:
                out_of_stock_list.append(f"{product[3]}")
        return out_of_stock_list


def generate_customers_active_last_month():
    today = datetime.date.today()
    lastmonth = today - datetime.timedelta()
    with connect(host=hostname, user=user_name, password=pwd) as database:
        with database.cursor() as mycursor:
            mycursor.execute(f"""SELECT customer_fname, customer_lname FROM project.customers as cust INNER 
                                JOIN project.orders as orders ON cust.customer_id = orders.customer_id 
                                INNER JOIN project.invoice as inv ON orders.order_id = inv.order_id where 
                                inv.date >= {lastmonth};""")
            active_customer_list = [f"Active Customers",
                                    f"================"]
            for customer in mycursor:
                active_customer_list.append(f"{customer[0]} {customer[1]}")
        return active_customer_list


def add_store(store_id, store_name):
    add_store = f"""INSERT INTO project.store (store_id, store_name)
                                values ("{store_id}", "{store_name}");"""
    execute_and_commit(add_store)


def add_customer(customer_fname:str, customer_lname:str, customer_email:str, home_phone:str, cell_phone:str):
    add_customer = f"""INSERT INTO project.customers (customer_fname, customer_lname, customer_email, home_phone, cell_number)
                                  values ("{customer_fname}", "{customer_lname}", "{customer_email}", "{home_phone}", "{cell_phone}");"""
    execute_and_commit(add_customer)


def add_order(customer_id, product_id, order_desc, order_id, total_cost, date, time, quantity_bought):
    add_order = f"""INSERT INTO project.orders (customer_id, product_id, order_desc) values
                                  ("{customer_id}", "{product_id}",  "{order_desc}");"""
    add_invoice = f"""INSERT INTO project.invoice (order_id, total_cost, date, time) values
                                    ("{order_id}", "{total_cost}", "{date}", "{time}");"""
    update_product_with_order =  f'UPDATE project.product SET quantity_on_hand = quantity_on_hand - {quantity_bought} WHERE product_id = "{product_id}";'                               
    execute_and_commit(add_order)
    execute_and_commit(add_invoice)
    execute_and_commit(update_product_with_order)


def add_product(vendor_id, store_id, product_name, product_desc, quantity_on_hand, price):
    add_product = f"""INSERT INTO project.product (vendor_id, store_id, product_name, product_desc, quantity_on_hand, price)
                                          values ("{vendor_id}", "{store_id}", "{product_name}", "{product_desc}", "{quantity_on_hand}", "{price}");"""
    execute_and_commit(add_product)


def remove_store(store_id):
    delete_store_from_product = f"""DELETE FROM project.product WHERE store_id = {store_id}"""
    execute_and_commit(delete_store_from_product)
    delete_store_from_store = f"""DELETE FROM project.store WHERE store_id = {store_id}"""
    execute_and_commit(delete_store_from_store)


def remove_customer(customer_id):
    delete_customer_order_from_invoice = f"""delete project.invoice
                                            from project.invoice
                                            inner join project.orders ord ON invoice.order_id = ord.order_id
                                            INNER JOIN project.customers cust ON ord.customer_id = cust.customer_id
                                            where cust.customer_id = 2;"""
    execute_and_commit(delete_customer_order_from_invoice)
    delete_customer_from_orders = f"DELETE FROM project.orders WHERE customer_id = {customer_id};"
    execute_and_commit(delete_customer_from_orders)
    delete_customer_from_customer = f"DELETE FROM project.customers WHERE customer_id = {customer_id};"
    execute_and_commit(delete_customer_from_customer)


def remove_order_record(order_id):
    delete_invoice_record = f"DELETE FROM project.invoice WHERE order_id = {order_id}"
    execute_and_commit(delete_invoice_record)
    delete_order_record = f"DELETE FROM project.orders WHERE order_id = {order_id}"
    execute_and_commit(delete_order_record)
    
def remove_product(product_id):
    delete_product_from_orders = f"DELETE FROM project.product WHERE product_id = {product_id}"
    execute_and_commit(delete_product_from_orders)
    delete_product_from_product = f"DELETE FROM project.product WHERE product_id = {product_id}"
    execute_and_commit(delete_product_from_product)

def update_store(current_name, new_name):
    update_storename = f'UPDATE project.store SET store_name = "{new_name}" WHERE store_name = "{current_name}";'
    execute_and_commit(update_storename)

def update_product(product_name, quantity_on_hand):
    update_product_quantity = f'UPDATE project.product SET quantity_on_hand = "{quantity_on_hand}" WHERE product_name = "{product_name}";'
    execute_and_commit(update_product_quantity)

def update_customer_lname(customer_id, customer_lname):
    update_customer_lname = f'UPDATE project.customers SET customer_lname = "{customer_lname}" WHERE customer_id = "{customer_id}";'
    execute_and_commit(update_customer_lname)

def update_customer_email(customer_id, customer_email):
    update_customer_email = f'UPDATE project.customers SET customer_email = "{customer_email}" WHERE customer_id = "{customer_id}";'
    execute_and_commit(update_customer_email)

def update_customer_home_phone(customer_id, home_phone):
    update_customer_home_phone = f'UPDATE project.customers SET home_phone = "{home_phone}" WHERE customer_id = "{customer_id}";'
    execute_and_commit(update_customer_home_phone)

def update_customer_cell_number(customer_id, cell_number):
    update_customer_cell_number = f'UPDATE project.customers SET cell_number = "{cell_number}" WHERE customer_id = "{customer_id}";'
    execute_and_commit(update_customer_cell_number)