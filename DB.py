import sqlite3
from random import randint
from Factor_table import *

rand_code = []

class DataBase():
    def __init__(self, connection):
        self.cnnt = connection
                                ## Creating a table for all of the stuff is in warehouse
        self.cnnt.execute('''CREATE TABLE IF NOT EXISTS Anbar_stuffs_table
        (stuff_name text not null,
        stuff_kind text not null,
        stuff_money text not null,
        stuff_code integer not null,
        stuff_num integer not null);''')

        self.cnnt.execute('''CREATE TABLE IF NOT EXISTS Manager_info_table
        (name text not null,
        username text not null,
        password text not null);''')

                                ## Creating a table for the customer info
        self.cnnt.execute('''CREATE TABLE IF NOT EXISTS Customer_info_table
        (name text not null,
        username text not null,
        password text not null,
        email text not null);''')
                                ## Creating a table for the warehouse keeper info
        self.cnnt.execute('''CREATE TABLE IF NOT EXISTS Warehousekeeper_info_table
        (name text not null,
        username text not null,
        password text not null,
        email text not null);''')
                                ## Creating a table for all the factor 
        self.cnnt.execute('''CREATE TABLE IF NOT EXISTS Factor_table
        (stuff text not null,
        stuff_code text not null,
        stuff_money text not null,
        username text not null,
        date text not null,
        warehousekeeper_username text not null);''')

        self.cnnt.execute('''CREATE TABLE IF NOT EXISTS Temporary
        (temp_stuff_name text not null,
        temp_stuff_money text not null,
        temp_stuff_kind text not null,
        temp_stuff_code integer not null);''')
        self.cnnt.commit()
    
    ##Add new customer
    def add_new_customer(self, name, username, password, email=''):
        self.cnnt.execute('''INSERT INTO Customer_info_table (name, username, password, email) \
            VALUES (?, ?, ?, ?);''', (name, username, password, email))
        self.cnnt.commit()

    ##Add new warehouse keeper
    def add_new_warehouse_keeper(self, name, username, password, email=''):
        self.cnnt.execute('''INSERT INTO Warehousekeeper_info_table (name, username, password, email) \
            VALUES (?, ?, ?, ?);''', (name, username, password, email))
        self.cnnt.commit()

    def add_new_manager(self, name, username, password):
        self.cnnt.execute('''INSERT INTO Manager_info_table (name, username, password) \
            VALUES (?, ?, ?);''', (name, username, password))
        self.cnnt.commit()

    ##Add new stuff
    def add_stuff(self, name_stuff, kind_stuff, money_stuff, num_stuff):
        self.rand_num_code = randint(0, 999999999999)
        T = True
        while T:
            if self.rand_num_code in rand_code:
                self.rand_num_code = randint(0, 999999999999)
            else:
                T = False
                rand_code.append(self.rand_num_code)
        self.cnnt.execute('''INSERT INTO Anbar_stuffs_table (stuff_name, stuff_kind, stuff_money, stuff_code, stuff_num) \
            VALUES (?, ?, ?, ?, ?);''', (name_stuff, kind_stuff, money_stuff, self.rand_num_code, num_stuff))
        self.cnnt.commit()

    def add_item_details_temporary(self, temp_namee, temp_moneyy, temp_kindd, temp_code):
        self.cnnt.execute('''INSERT INTO Temporary (temp_stuff_name, temp_stuff_money, temp_stuff_kind, temp_stuff_code) \
            VALUES (?, ?, ?, ?);''', (temp_namee, temp_moneyy, temp_kindd, temp_code))
        self.cnnt.commit()

    ##Add new factor
    def add_factor(self, username, stuff, stuff_code, stuff_money, date, warehousekeeper_username):
        self.cnnt.execute('''INSERT INTO Factor_table (username, stuff, stuff_code, stuff_money, date, warehousekeeper_username) \
            VALUES (?, ?, ?, ?, ?, ?);''', (username, stuff, stuff_code, stuff_money, date, warehousekeeper_username))
        self.cnnt.commit()
    
    ## Conditions to undeerstand if the user is exist and password is right
    def if_customer_username_and_password_is_correct(self, username, password):
        self.cursor = self.cnnt.execute('''SELECT username, password from Customer_info_table''')
        for row in self.cursor:
            if username == row[0] and password == row[1]:
                return True

    ## Conditions to undeerstand if the user is exist and password is right
    def if_warehouse_keeper_username_and_password_correct(self, username, password):
        self.cursor = self.cnnt.execute('''SELECT username, password from Warehousekeeper_info_table''')
        for row in self.cursor:
            if username == row[0] and password == row[1]:
                return True

    ## Conditions to undeerstand if the user is exist and password is right    
    def if_manager_username_and_password_correct(self, username, password):
        self.cursor = self.cnnt.execute('''SELECT username, password from Manager_info_table''')
        for row in self.cursor:
            if username == row[0] and password == row[1]:
                return True

    ## Conditions to undeerstand if the username is exist or not
    def if_this_username_exists_in_customers(self, username):
        self.cursor = self.cnnt.execute('''SELECT username from Customer_info_table''')
        for self.row in self.cursor:
            if username == self.row[0]:
                return True
        return False
    
    def update_item_selected(self, update_item_code, name, kind, money, num):
        self.cnnt.execute("UPDATE Anbar_stuffs_table set stuff_name = ? where stuff_code = ?", (name, update_item_code))
        self.cnnt.execute("UPDATE Anbar_stuffs_table set stuff_kind = ? where stuff_code = ?", (kind, update_item_code))
        self.cnnt.execute("UPDATE Anbar_stuffs_table set stuff_money = ? where stuff_code = ?", (money, update_item_code))
        self.cnnt.execute("UPDATE Anbar_stuffs_table set stuff_num = ? where stuff_code = ?", (num, update_item_code))
        self.cnnt.commit()
    
    def update_user_info(self, name, username, password, email, first_username):
        self.cnnt.execute("UPDATE Customer_info_table set name = ? where username = ?", (name, first_username))
        self.cnnt.execute("UPDATE Customer_info_table set password = ? where username = ?", (password, first_username))
        self.cnnt.execute("UPDATE Customer_info_table set email = ? where username = ?", (email, first_username))
        self.cnnt.execute("UPDATE Customer_info_table set username = ? where username = ?", (username, first_username))
        self.cnnt.commit()
    
    def update_housekeeper_info(self, name, username, password, email, first_username):
        self.cnnt.execute("UPDATE Warehousekeeper_info_table set name = ? where username = ?", (name, first_username))
        self.cnnt.execute("UPDATE Warehousekeeper_info_table set password = ? where username = ?", (password, first_username))
        self.cnnt.execute("UPDATE Warehousekeeper_info_table set email = ? where username = ?", (email, first_username))
        self.cnnt.execute("UPDATE Warehousekeeper_info_table set username = ? where username = ?", (username, first_username))
        self.cnnt.commit()
    
    def delete_housekeeper_selected_from_database(self, username):
        self.cnnt.execute('''DELETE FROM Warehousekeeper_info_table where username = ?''', (username, ))
        self.cnnt.commit()

    def delete_user_selected_from_database(self, username):
        self.cnnt.execute('''DELETE FROM Customer_info_table where username = ?''', (username, ))
        self.cnnt.commit()

    def delete_item_selected(self, dlt_code):
        self.cnnt.execute('''DELETE FROM Anbar_stuffs_table where stuff_code = ?''', (dlt_code, ))
        self.cnnt.commit()

    def delete_item_from_temp_factor(self, item_code):
        self.cnnt.execute('''DELETE FROM Temporary where temp_stuff_code = ?''', (item_code, ))
        self.cnnt.commit()
    
    def delete_items_from_temp(self):
        self.cnnt.execute('''DELETE FROM Temporary''')
        self.cnnt.commit()