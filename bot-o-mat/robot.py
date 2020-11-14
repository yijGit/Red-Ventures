# The functions that allow users to build/delete robots and complete tasks
# 'Robots' are simply entries in the bot_o_mat database, not actual objects

import random
import time
from database import retrieve_robots
from list_types import task_types as tt, robot_types as rt
from sqlite3 import Error

# Generate 5 random, nonrepeating tasks for the bot 
# Chosen from the list of tasks each bot type is able to do
def generate_tasks(btype) -> list:
    t = next((task for task in rt if task["type"] == btype), None)
    li_tasks = [tt[x - 1]['desc'] for x in random.sample(t['able'], 5)]
    return li_tasks

# Create row in ROBOTS table for the robot
# Create rows in TASKS table for each assigned task
# If the name is already taken, return -1
# Returns the robot_id if successful, 0 otherwise
def build_robot(conn, name, btype) -> int:
    try:
        li = retrieve_robots(conn)
        if name in li:
            return -1
        cur = conn.cursor()
        cmd1 = ''' INSERT INTO robots(name, time, tasks_completed) VALUES(?, ?, ?) '''
        cmd2 = ''' INSERT INTO tasks(robot_id, task) VALUES(?, ?) '''
        cur.execute(cmd1, (name, 0, 0))
        robot_id = cur.lastrowid
        for i in generate_tasks(btype):
            cur.execute(cmd2, (robot_id, i))
        cur.close()
        return robot_id
    except Error as e:
        print(e)
        return 0

# Deletes row in ROBOTS table for the robot
# Deletes rows in TASKS table for each assigned task
# Returns the robot_id if successful, 0 otherwise
def delete_robot(conn, name) -> int:
    try:
        cur = conn.cursor()
        cmd1 = ''' SELECT robot_id FROM robots WHERE name=? '''
        cmd2 = ''' DELETE FROM robots WHERE robot_id=? '''
        cmd3 = ''' DELETE FROM tasks WHERE robot_id=? '''
        cur.execute(cmd1, (name,))
        robot_id = cur.fetchone()
        cur.execute(cmd2, robot_id)
        cur.execute(cmd3, robot_id)
        cur.close()
        return robot_id
    except Error as e:
        print(e)
        return 0

# Remove tasks from the TASKS table
# Update num of tasks and seconds in the ROBOTS table
# Return seconds waited to complete tasks
def complete_tasks(conn, name, tasks) -> int:
    try:
        cur = conn.cursor()
        cmd1 = ''' SELECT robot_id FROM robots WHERE name=? '''
        cmd2 = ''' DELETE FROM tasks WHERE robot_id=? AND task=? '''
        cmd3 = ''' UPDATE robots SET time=time+?, tasks_completed=tasks_completed+? WHERE name=? '''
        cur.execute(cmd1, (name,))
        robot_id = cur.fetchone()[0]
        total_s = 0
        for i in tasks:
            cur.execute(cmd2, (robot_id, i))
            t = next((task for task in tt if task["desc"] == i), None)
            seconds = t['eta'] / 1000
            desc = t['desc']
            total_s += seconds
            time.sleep(seconds)
            print('Task completed: {} ({} seconds)'.format(desc, seconds))
        cur.execute(cmd3, (total_s, len(tasks), name))
        cur.close()
    except Error as e:
        print(e)
        return 0
    return total_s
