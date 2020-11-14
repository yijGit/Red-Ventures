# The different types of tasks/robots users can complete/build
# Accessed by robot.py

task_types = [
    {
        'desc': 'do the dishes',
        'eta': 1000,
    },
    {
        'desc': 'sweep the house',
        'eta': 3000,
    },
    {
        'desc': 'do the laundry',
        'eta': 10000,
    },
    {
        'desc': 'take out the recycling',
        'eta': 4000,
    },
    {
        'desc': 'make a sammich',
        'eta': 7000,
    },
    {
        'desc': 'mow the lawn',
        'eta': 20000,
    },
    {
        'desc': 'rake the leaves',
        'eta': 18000,
    },
    {
        'desc': 'give the dog a bath',
        'eta': 14500,
    },
    {
        'desc': 'bake some cookies',
        'eta': 8000,
    },
    {
        'desc': 'wash the car',
        'eta': 20000,
    }
]

robot_types = [
    {
        'type': 'Unipedal',
        'able': [1, 2, 3, 4, 5, 6, 9, 10]
    },
    {
        'type': 'Bipedal',
        'able': [1, 2, 3, 4, 5, 7, 8, 10]
    },
    {
        'type': 'Quadrupedal',
        'able': [1, 2, 3, 4, 6, 7, 8, 10]
    },
    {
        'type': 'Arachnid',
        'able': [1, 2, 3, 5, 6, 7, 8, 10]
    },
    {
        'type': 'Radial',
        'able': [1, 2, 4, 5, 6, 7, 8, 10]
    },
    {
        'type': 'Aeronautical',
        'able': [1, 3, 4, 5, 6, 7, 9, 10]
    }
]


