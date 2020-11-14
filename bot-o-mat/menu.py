# Contains all the different prompts for the CLI

CHAR_LIMIT = 20

main = {
'type': 'list',
'name': 'function',
'message': 'What would you like to do?',
'choices': 
    ['Build Robot',
    'Complete Task',
    'Leaderboard',
    'Delete Robot',
    'Exit']
}

num_robots = {
    'type': 'input',
    'name': 'number',
    'message': 'How many would you like to create?'
}

build_robot = [
    {
        'type': 'list',
        'name': 'type',
        'message': 'Please pick a robot type:',
        'choices': ['Unipedal',
                    'Bipedal',
                    'Quadrupedal',
                    'Arachnid',
                    'Radial',
                    'Aeronautical']
    },
    {
        'type': 'input',
        'name': 'name',
        'message': 'Enter name for robot:',
        'validate': lambda answer: 'Too many characters. Char limit: 20' \
                    if len(answer) > CHAR_LIMIT else True
    }
]

list_robots = {
        'type': 'list',
        'name': 'name',
        'message': 'Please pick a robot:',
        'choices': []
}

list_tasks = {
        'type': 'checkbox',
        'name': 'task',
        'message': 'Pick as many tasks as you wish:',
        'choices': []
}

confirm = {
        'type': 'confirm',
        'message': 'Are you sure?',
        'name': 'continue',
        'default': True,
}