import sqlite3

class Animal:
    def __init__(self, species):
        conn = sqlite3.connect("database.db")