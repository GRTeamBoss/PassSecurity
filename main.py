#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import time
import sys
import sqlite3
from getopt import getopt
from hashlib import new, pbkdf2_hmac

import customtkinter as ctk
from customtkinter import W, CTk, CTkButton, CTkEntry, CTkFrame, CTkLabel, CTkScrollableFrame, CTkScrollbar



class Initialize:

    __Password = "$2y$19$NAT0VRqZ251lcHN3yKQpbuShyN3JO/xml98LXbRMvA6H9grtz4yVS"
    __Help = """
Usage: \033[92m>>> python3 main.py [\033[96moption\033[0m]\033[0m
\033[96moption\033[0m:
-h, --help . . . . . . . . . call help message
-d, --desktop. . . . . . . . start initialize desktop app
-t, --terminal . . . . . . . start initialize terminal app
    """


    def __init__(self):
        self.welcome()


    def welcome(self):
        content = sys.argv[1:];
        if type(content) == None:
            self.welcome()
            exit(1)
        else:
            o, _ = getopt(content, "hdt", ["help", "desktop", "terminal"])
            for k, _ in o:
                if k in ("-h", "--help"):
                    print(self.__Help)
                elif k in ("-d", "--desktop"):
                    Initialize_Desktop_App()
                elif k in ("-t", "--terminal"):
                    Initialize_Terminal_App()
                else:
                    print("[*] You wrote this -> ", " ".join(sys.argv[::]))
                    print("[*] Read this...")
                    print(self.__Help)


class Initialize_Desktop_App(CTk):


    def __init__(self) -> None:
        super().__init__()
        self.username = None
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.geometry("800x600")
        self.title("\u00a9 PassSecurity")
        self.start_app()
        self.mainloop()


    def change_frame(self, old_frame, new_frame):
        frame = {
            "create_user": self.create_user_frame,
            "authentication_user": self.authentication_user_frame
        }
        frame[old_frame].grid_forget()
        frame[new_frame].grid(row=0, column=0, sticky="ns", padx=40, pady=10)


    def start_app(self):
        self.create_user_frame = CTkFrame(self, corner_radius=0)
        self.create_user_frame.grid(row=0, column=0, sticky="ns", padx=40, pady=10)
        self.create_user_username_label = CTkLabel(self.create_user_frame, text="Username : ")
        self.create_user_username_label.grid(row=0, column=0, padx=20, pady=10)
        self.create_user_username_input = CTkEntry(self.create_user_frame, placeholder_text="input username...")
        self.create_user_username_input.grid(row=0, column=1, padx=20, pady=10)
        self.create_user_password_label = CTkLabel(self.create_user_frame, text="Password : ")
        self.create_user_password_label.grid(row=1, column=0, padx=20, pady=10)
        self.create_user_password_input = CTkEntry(self.create_user_frame, placeholder_text="input password...", show="*")
        self.create_user_password_input.grid(row=1, column=1, padx=20, pady=10)
        self.create_user_salt_label = CTkLabel(self.create_user_frame, text="Salt : ")
        self.create_user_salt_label.grid(row=2, column=0, padx=20, pady=10)
        self.create_user_salt_input = CTkEntry(self.create_user_frame, placeholder_text="input salt for encrypt your passwords...", show="*")
        self.create_user_salt_input.grid(row=2, column=1, padx=20, pady=10)
        self.create_user_confirm_button = CTkButton(self.create_user_frame, text="Create", command=self.create_user_sql)
        self.create_user_confirm_button.grid(row=3, column=0, padx=20, pady=10)
        self.create_user_change_button = CTkButton(self.create_user_frame, text="Login", command=self.change_frame_to_login)
        self.create_user_change_button.grid(row=4, column=0, padx=20, pady=10)
        self.create_user_alert_message = CTkLabel(self.create_user_frame, text = "")
        self.create_user_alert_message.grid(row=5, column=0, padx=20, pady=10)


        self.authentication_user_frame = CTkFrame(self, corner_radius=0)
        self.authentication_user_frame.grid_columnconfigure(0, weight=1)
        self.authentication_user_username_label = CTkLabel(self.authentication_user_frame, text="Username : ")
        self.authentication_user_username_label.grid(row=0, column=0, padx=20, pady=10)
        self.authentication_user_username_input = CTkEntry(self.authentication_user_frame, placeholder_text="input username...")
        self.authentication_user_username_input.grid(row=0, column=1, padx=20, pady=10)
        self.authentication_user_password_label = CTkLabel(self.authentication_user_frame, text="Password : ")
        self.authentication_user_password_label.grid(row=1, column=0, padx=20, pady=10)
        self.authentication_user_password_input = CTkEntry(self.authentication_user_frame, placeholder_text="input password...", show="*")
        self.authentication_user_password_input.grid(row=1, column=1, padx=20, pady=10)
        self.authentication_user_confirm_button = CTkButton(self.authentication_user_frame, text="Authentication", command=self.authentication_user_sql)
        self.authentication_user_confirm_button.grid(row=2, column=0, padx=20, pady=10)
        self.authentication_user_change_button = CTkButton(self.authentication_user_frame, text="Sign up", command=self.change_frame_to_sign_up)
        self.authentication_user_change_button.grid(row=3, column=0, padx=20, pady=10)
        self.authentication_user_alert_message = CTkLabel(self.authentication_user_frame, text = "")
        self.authentication_user_alert_message.grid(row=4, column=0, padx=20, pady=10)


        self.password_create_frame = CTkFrame(self, corner_radius=0)
        self.password_create_frame.grid_columnconfigure(0, weight=1)
        self.password_create_url_label = CTkLabel(self.password_create_frame, text="URI : ").grid(column=0, row=0, padx=40, pady=10)
        self.password_create_url_input = CTkEntry(self.password_create_frame, placeholder_text="input URI...").grid(column=1, row=0, padx=40, pady=10)
        self.password_create_app_label = CTkLabel(self.password_create_frame, text="App : ").grid(column=0, row=1, padx=40, pady=10)
        self.password_create_app_input = CTkEntry(self.password_create_frame, placeholder_text="input App Name...").grid(column=1, row=1, padx=40, pady=10)
        self.password_create_login_label = CTkLabel(self.password_create_frame, text="Login : ").grid(column=0, row=2, padx=40, pady=10)
        self.password_create_login_input = CTkEntry(self.password_create_frame, placeholder_text="input Login...").grid(column=1, row=2, padx=40, pady=10)


        self.dashboard_user_frame = CTkFrame(self, corner_radius=0)
        self.dashboard_user_frame.grid_columnconfigure(0, weight=1)
        count_passwords = len(SqliteAPI().search(f"select password from Password where owner=(select id from User where username='{self.username}');")[0])
        self.dashboard_user_lists = CTkScrollableFrame(self, corner_radius=0, orientation="vertical", height=30*count_passwords)
        self.dashboard_user_list_elements = []
        for i in range(count_passwords):
            _tmp = []
            info = SqliteAPI().search(f"select * from Password where id={i}")
            new_text= info[0][2] if info[0][1] == None else info[0][1]
            _tmp.append(CTkLabel(self.dashboard_user_frame, text=new_text).grid(column=0, row=i, padx=10, pady=4))
            _tmp.append(CTkLabel(self.dashboard_user_frame, text=info[0][4]).grid(column=1, row=i, padx=10, pady=4))
            _tmp.append(CTkLabel(self.dashboard_user_frame, text=info[0][3]).grid(column=2, row=i, padx=10, pady=4))
        username_sql = SqliteAPI().search("select username from User;")
        if type(username_sql) != None:
            self.change_frame_to_login()


    def create_user_sql(self):
        username = self.create_user_username_input.get()
        username_data = ""
        password = self.create_user_password_input.get()
        password_data = Encrypt().encrypt(password, username)
        salt = self.create_user_salt_input.get()
        salt_data = Encrypt().encrypt(salt, username)
        if len(username) == 0 or len(password) == 0 or len(salt) == 0:
            self.create_user_alert_message.configure(text="Please fill all field!", text_color="red")
        else:
            for item in username:
                username_data += str(ord(item))
            password = password_data
            salt = salt_data
            username_data = pbkdf2_hmac("SHA512", str(username_data).encode("utf-8"), str(password_data).encode("utf-8"), 5)
            username = ""
            for item in username_data:
                username += str(item)
            SqliteAPI().execute(f"insert into User (username, password, salt) values ('{username}', '{password_data}', '{salt_data}');", None)
            self.create_user_alert_message.configure(text="User created!", text_color="green")
            self.change_frame_to_login()


    def authentication_user_sql(self):
        username = self.authentication_user_username_input.get()
        username_data = ""
        password = self.authentication_user_password_input.get()
        password_data = Encrypt().encrypt(password, username)
        for item in username:
            username_data += str(ord(item))
        username_data = pbkdf2_hmac("SHA512", str(username_data).encode("utf-8"), str(password_data).encode("utf-8"), 5)
        username = ""
        for item in username_data:
            username += str(item)
        self.username = username
        username_sql = SqliteAPI().search(f"select username from User where username='{username}';")
        password_sql = SqliteAPI().search(f"select password from User where username='{username}';")
        if type(username_sql) == None:
            self.authentication_user_alert_message.configure(text="Wrong username or password!", text_color="red")
        else:
            if str(password_data) != password_sql[0][0]:
                self.authentication_user_alert_message.configure(text="Wrong username or password!", text_color="red")
            else:
                self.authentication_user_alert_message.configure(text="Correct!", text_color="green")


    def change_frame_to_sign_up(self):
        self.authentication_user_frame.grid_forget()
        self.create_user_frame.grid(column=0, row=0, sticky="ns", padx=40, pady=10)


    def change_frame_to_login(self):
        self.create_user_frame.grid_forget()
        self.authentication_user_frame.grid(column=0, row=0, sticky="ns", padx=40, pady=10)


class Initialize_Terminal_App:


    def __init__(self) -> None:
        pass


class SqliteAPI:

    """
    User(
        id integer auto increment primary key,
        username text not null,
        password blob not null,
        salt blob not null
    );

    Password(
        id integer auto increment primary key,
        url text,
        app text,
        hash blob not null,
        login text,
        phone integer,
        owner integer
    );
    """


    def __init__(self) -> None:
        self.__db = sqlite3.connect("./db.sqlite3")


    def execute(self, arg, values = None):
        if values is None:
            self.__db.execute(arg)
        else:
            self.__db.executemany(arg, values)
        self.__db.commit()
        self.__db.close()


    def search(self, arg):
        content = list(self.__db.execute(arg))
        print("sql query : ", content)
        self.__db.close()
        return content



class Encrypt:


    def __init__(self) -> None:
        pass


    def encrypt(self, arg, salt):
        arg = str(arg)
        salt = str(salt)
        arg_data = ""
        salt_data = ""
        for item in arg:
            arg_data += str(ord(item))
            arg_data += str(1111)
        for item in salt:
            salt_data += str(ord(item))
            salt_data += str(1111)
        arg = int(arg_data)
        salt = int(salt_data)
        result = arg * salt
        del arg ,salt, arg_data, salt_data
        return result


    def decrypt(self, arg, salt):
        arg = int(arg)
        salt = int(salt)
        result = str(arg/salt)
        result_list = result.split("1111")
        decrypt_list = ""
        for item in result_list:
            decrypt_list += chr(int(item))
        result = decrypt_list
        del arg, salt, result_list, decrypt_list
        return result





if __name__ == "__main__":
    Initialize()
    print("[#] Exit!")
