# The functions that build a database, a connection to it, and its tables
# Also has functions to retrieve data from the database

import sqlite3
import pathlib
from sys import argv
from sqlite3 import Error

# Opens a connection to the bot_o_mat.db database
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

# Helper function that creates tables for the database
# Create_str is a sqlite3 CREATE TABLE command 
def create_table(conn, create_str):
    try:
        c = conn.cursor()
        c.execute(create_str)
    except Error as e:
        print(e)

# Creates the bot_o_mat.db file if it doesn't exist
# Otherwise returns a connection to the database
# Initalizes two tables: ROBOTS and TASKS
def create_db():
    database = pathlib.Path(__file__).parent.absolute().joinpath('bot_o_mat.db')
 
    create_robot_table = """CREATE TABLE IF NOT EXISTS robots (
                                    robot_id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    time integer NOT NULL,
                                    tasks_completed integer NOT NULL
                                    );"""
 
    create_task_table = """CREATE TABLE IF NOT EXISTS tasks (
                                    robot_id integer NOT NULL,
                                    task text NOT NULL,
                                    FOREIGN KEY (robot_id) REFERENCES robots (robot_id)
                                    );"""

    conn = create_connection(database)
    if conn is not None:
        create_table(conn, create_robot_table)
        create_table(conn, create_task_table)
    else:
        print('Error! cannot create the database connection.')

    return conn

# Query all robots from ROBOTS table
# Returns list of robots if successful, empty otherwise
def retrieve_robots(conn) -> list:
    try:
        cur = conn.cursor()
        cmd1 = ''' SELECT * FROM robots '''
        cur.execute(cmd1)
        li_robots = [name[1] for name in cur.fetchall()]
        cur.close()
        return li_robots
    except Error as e:
        print(e)

# Query tasks by the robot_id from TASKS table
# Returns list of task if successful, empty otherwise
def retrieve_tasks(conn, name) -> list:
    try:
        cur = conn.cursor()
        cmd1 = ''' SELECT robot_id FROM robots WHERE name=? '''
        cmd2 = ''' SELECT task FROM tasks WHERE robot_id=? '''
        cur.execute(cmd1, (name,))
        robot_id = cur.fetchone()
        cur.execute(cmd2, robot_id)
        li_tasks = [task[0] for task in cur.fetchall()]
        cur.close()
        return li_tasks
    except Error as e:
        print(e)

# Query all robots from ROBOTS table
# Returns list of robots if successful, empty otherwise
def leaderboard(conn) -> list:
    try:
        cur = conn.cursor()
        cmd1 = ''' SELECT * FROM robots '''
        cur.execute(cmd1)
        rows = [[row[1], row[2], row[3]] for row in cur.fetchall()]
        cur.close()
        return rows
    except Error as e:
        print(e)

if __name__ == "__main__":
    create_db()