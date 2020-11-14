import menu as m
from database import create_db, retrieve_robots, retrieve_tasks, leaderboard
from sqlite3 import Error
from robot import build_robot, complete_tasks, delete_robot
from PyInquirer import prompt

# The CLI allows users to do 4 things:
# 1) Build robot(s)
# 2) Complete tasks for a specific robot
# 3) Display the leaderboard with all robots
# 4) Delete robot
# 5) Exit the program
def main(conn):
    answer = prompt(m.main)['function']

    if answer == 'Build Robot':
        n = int(prompt(m.num_robots)['number'])
        for i in range(n):
            bot_info = prompt(m.build_robot)
            name = bot_info['name']
            btype = bot_info['type']
            result = build_robot(conn, name, btype)
            if result == -1:
                print('Name already taken.')
            elif result == 0:
                print('Error. Sorry, try again.')
            else:
                conn.commit()

    elif answer == 'Complete Task':
        li = retrieve_robots(conn)
        if li:
            m.list_robots['choices']=li
            robot = prompt(m.list_robots)['name']
            li = [{'name':task} for task in retrieve_tasks(conn, robot)]
            if li:
                m.list_tasks['choices']=li
                tasks = prompt(m.list_tasks)['task']
                if complete_tasks(conn, robot, tasks):
                    conn.commit()
            else:
                print('Tasks all completed!')
        else:
            print('No robots have been created yet!')

    elif answer == 'Leaderboard':
        rows = sorted(leaderboard(conn), key=lambda elem: (-elem[1], -elem[2], elem[0]))
        heading1 = 'Name'.center(m.CHAR_LIMIT)
        heading2 = 'Time (s)'.center(m.CHAR_LIMIT)
        heading3 = '# of Tasks Done'.center(m.CHAR_LIMIT)
        fill_in = '{} | {} | {}'
        separator = '---' * (m.CHAR_LIMIT + 2)
        print(fill_in.format(heading1, heading2, heading3))
        print(separator)
        for i in rows:
            entry1 = i[0].center(m.CHAR_LIMIT)
            entry2 = str(i[1]).center(m.CHAR_LIMIT)
            entry3 = str(i[2]).center(m.CHAR_LIMIT)
            print(fill_in.format(entry1, entry2, entry3))
            print(separator)

    elif answer == 'Delete Robot':
        li = retrieve_robots(conn)
        if li:
            m.list_robots['choices']=li
            robot = prompt(m.list_robots)['name']
            confirm = prompt(m.confirm)['continue']
            if confirm and delete_robot(conn, robot):
                conn.commit()
        else:
            print('No robots have been created yet!')

    elif answer == 'Exit':
        return
    
    main(conn)

if __name__ == "__main__":
    try:
        conn = create_db()
        main(conn)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()