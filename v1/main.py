import sqlite3
import uuid
import openai

CLIENT = openai.OpenAI()

class Animal:
    def __init__(self, species):
        conn = sqlite3.connect("database.db")
        table_name = f"talbe_{uuid.uuid4().hex}"
        conn.execute(f"DROP TABLE IF EXISTS {table_name}")

