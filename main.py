#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import sys
import sqlite3
from getopt import getopt

import tkinter
import customtkinter as ctk
from customtkinter import CTk, CTkButton, CTkEntry, CTkFont, CTkLabel



class Initialize:

    __Password = "$2y$19$NAT0VRqZ251lcHN3yKQpbuShyN3JO/xml98LXbRMvA6H9grtz4yVS"
    __Help = """
-h, --h . . . . . . . . . . call help message
-d, --desktop . . . . . . . start initialize desktop app
-t, --terminal. . . . . . . start initialize terminal app
    """


    def __init__(self):
        self.welcome()


    def welcome(self):
        content = sys.argv[1:];
        if type(content) == None:
            self.welcome()
            exit(1)
        else:
            o, a = getopt(content, "hdt", ["help", "desktop", "terminal"])
            for k, v in o:
                if k in ("-h", "--help"):
                    exit(0)
                elif k in ("-d", "--desktop"):
                    Initialize_Desktop_App()
                elif k in ("-t", "--terminal"):
                    Initialize_Terminal_App()
                else:
                    exit(1)






class Initialize_Desktop_App(CTk):


    def __init__(self) -> None:
        super().__init__()
        self.run_app()


    def run_app(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.geometry("800x600")
        self.title("\u00a9 PassSecurity")
        self.password = CTkEntry(self, placeholder_text="input password...", placeholder_text_color="gray", bg_color="white", border_color="green")
        self.password.pack()
        self.button = CTkButton(master=self, command=self.clicked, corner_radius=0, border_color="green", hover_color="green", text_color="white")
        self.button.pack()
        self.cp = "I don't know"
        self.mainloop()


    def clicked(self):
        password_content = self.password.get()
        if password_content == self.cp:
            label = CTkLabel(self, text="Correct password!")
            label.pack()
        else:
            label = CTkLabel(self, text="Incorrect password!")
            label.pack()


class Initialize_Terminal_App:


    def __init__(self) -> None:
        pass


class SqliteAPI:


    def __init__(self) -> None:
        self.__db = sqlite3.connect("./db.sqlite3")


    def execute(self, arg = None, values = None):
        if arg is None:
            return -1
        else:
            if values is None:
                self.__db.execute(arg)
            else:
                self.__db.executemany(arg, values)
            self.__db.commit()
            self.__db.close()


    def search(self, arg = None):
        if arg is None:
            return -1
        else:
            content = list(self.__db.execute(arg))
            return content



if __name__ == "__main__":
    Initialize()
    print("[#] Exit!")
