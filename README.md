# BOT-O-MAT
Use any language to complete this challenge. The implementation is up to you: it can be a command-line application or have a graphical interface.

A housecleaning service wants to automate their process using robots and needs your help to create robots that can complete a variety of tasks.

Your application should collect a name and robot type from the types we list below. For each, it should create a Robot of the type the user chooses, e.g. Larry, Bipedal.

Given the list of tasks below, your application should then assign the Robot a set of five tasks, all of which complete after a duration that we show in milliseconds.



- Collect a name and robot type from user.
- Instantiate a Robot of the type provided by the user with the name provided by the user
  - for example: Bipedal, Larry
- Set up methods on Robot to complete tasks from the provided list

## How to Run bot-o-mat (for MacOS and Linux)
1. Download and open the Red-Ventures zip file from GitHub onto Desktop
2. In terminal, change working directory to Red-Ventures-Main folder
  ```cd /path/to/Red-Ventures-Main```
3. Setup Python3 virtual environment and activate it (assuming that venv is already installed)
  ```python3 -m venv env
     source env/bin/activate
  ```
4. Install the required libraries
  ```pip install -r requirements.txt```
5. Change working directory to bot-o-mat file
  ```cd bot-o-mate```
6. Run cli.py file
  ```python cli.py```

## Robot
Robot completes tasks and removes them from the list when they are done (i.e. enough time has passed since starting the task).

## Tasks
Tasks have a description and an estimated time to complete.

```
[
  {
    description: 'do the dishes',
    eta: 1000,
  },{
    description: 'sweep the house',
    eta: 3000,
  },{
    description: 'do the laundry',
    eta: 10000,
  },{
    description: 'take out the recycling',
    eta: 4000,
  },{
    description: 'make a sammich',
    eta: 7000,
  },{
    description: 'mow the lawn',
    eta: 20000,
  },{
    description: 'rake the leaves',
    eta: 18000,
  },{
    description: 'give the dog a bath',
    eta: 14500,
  },{
    description: 'bake some cookies',
    eta: 8000,
  },{
    description: 'wash the car',
    eta: 20000,
  },
]
```

## Types
```
{
  UNIPEDAL: 'Unipedal',
  BIPEDAL: 'Bipedal',
  QUADRUPEDAL: 'Quadrupedal',
  ARACHNID: 'Arachnid',
  RADIAL: 'Radial',
  AERONAUTICAL: 'Aeronautical'
}
```

## Features to add once the core functionality is complete 
Be creative and have fun! Use this list or create your own features.
- Allow users to create multiple robots at one time :heavy_check_mark:
- Create a leaderboard for tasks completed by each Robot **first by time, then by # of task** :heavy_check_mark:
- Create tasks specific for each robot type :heavy_check_mark:, ~~this could work in conjunction with the leaderboard~. For e.g. robots that are assigned tasks that their type can’t perform won’t get “credit” for finishing the task.~~ 
-~~Add persistance for tasks, bots and leaderboard stats~~
-~~Some customers want your robots to accomplish tasks that are not on your list, so they'd like for you to add the ability for users to create new kinds of tasks and have the robots complete them~~
- **Added option to delete bots**

## Authors
- Scott Hoffman <https://github.com/scottshane>
- Olivia Osby <https://github.com/oosby>
