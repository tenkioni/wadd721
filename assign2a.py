import sqlite3
from prettytable import PrettyTable

def connect_db():
    conn = sqlite3.connect(r'c:\sqlite\db\bank.db')
    return conn

def list_all_branches(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM branch")
    headers = [description[0] for description in cursor.description]
    table = PrettyTable(headers) 
    rows = cursor.fetchall()
    for row in rows:
        table.add_row(row)  
    print(table) 

def count_accounts_greater_than(conn, amount):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM account WHERE balance > ?", (amount,))
    count = cursor.fetchone()[0]
    print(f'Number of accounts with balance greater than {amount}: {count}')

def find_customers_with_deposit(conn):
    cursor = conn.cursor()
    cursor.execute("""
    SELECT customer.customer_name, customer.customer_street, customer.customer_city, 
           depositor.account_number, account.balance
    FROM customer
    JOIN depositor ON customer.customer_name = depositor.customer_name
    JOIN account ON depositor.account_number = account.account_number
    """)
    headers = [description[0] for description in cursor.description]
    table = PrettyTable(headers) 
    rows = cursor.fetchall()
    for row in rows:
        table.add_row(row) 
    print(table) 

def add_new_customer(conn, customer_name, customer_street, customer_city):
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO customer (customer_name, customer_street, customer_city)
    VALUES (?, ?, ?)
    """, (customer_name, customer_street, customer_city))
    conn.commit()
    print(f"New customer {customer_name} added successfully.")

def add_new_account(conn, account_number, balance):
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO account (account_number, balance)
    VALUES (?, ?)
    """, (account_number, balance))
    conn.commit()
    print(f"New account {account_number} with balance {balance} added successfully.")

def link_customer_account(conn, customer_name, account_number):
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO depositor (customer_name, account_number)
    VALUES (?, ?)
    """, (customer_name, account_number))
    conn.commit()
    print(f"Linked customer {customer_name} to account {account_number}.")

def update_customer_address(conn, customer_name, new_street, new_city):
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE customer
    SET customer_street = ?, customer_city = ?
    WHERE customer_name = ?
    """, (new_street, new_city, customer_name))
    conn.commit()
    print(f"Address for customer {customer_name} updated successfully.")

def make_deposit(conn, customer_name, account_number, deposit_amount):
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE account
    SET balance = balance + ?
    WHERE account_number = ? AND account_number IN (
        SELECT account_number FROM depositor WHERE customer_name = ?
    )
    """, (deposit_amount, account_number, customer_name))
    print(f"{cursor.rowcount} rows updated.")
    conn.commit()
    print(f"Deposit of {deposit_amount} made to account {account_number} of customer {customer_name}.")

def list_all_customers(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customer")
    headers = [description[0] for description in cursor.description]
    table = PrettyTable(headers) 
    rows = cursor.fetchall()
    for row in rows:
        table.add_row(row) 
    print(table) 


def main():
    conn = connect_db()
    while True:
        print("""
        1. List all branches
        2. Count accounts with balance greater than specific amount
        3. Find customers with deposit
        4. Add new customer
        5. Update customer address
        6. Make a deposit
        7. List all customers
        0. Exit
        """)
        choice = input("Enter your choice: ")
        if choice == '1':
            list_all_branches(conn)
        elif choice == '2':
            amount = int(input("Enter the amount: "))
            count_accounts_greater_than(conn, amount)
        elif choice == '3':
            find_customers_with_deposit(conn)
        elif choice == '4':
            name = input("Enter customer name: ")
            street = input("Enter customer street: ")
            city = input("Enter customer city: ")
            add_new_customer(conn, name, street, city)
            account_number = input("Enter new account number: ")
            balance = float(input("Enter initial balance: "))
            add_new_account(conn, account_number, balance)
            link_customer_account(conn, name, account_number)
        elif choice == '5':
            name = input("Enter customer name: ")
            new_street = input("Enter new street: ")
            new_city = input("Enter new city: ")
            update_customer_address(conn, name, new_street, new_city)
        elif choice == '6':
            name = input("Enter customer name: ")
            account_number = input("Enter account number: ")
            deposit_amount = float(input("Enter deposit amount: "))
            make_deposit(conn, name, account_number, deposit_amount)
        elif choice == '7':
            list_all_customers(conn)
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()