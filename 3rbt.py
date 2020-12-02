import re 
​
# list of valid command names
valid_commands = ['off', 'help', 'forward', 'back', 'right', 'left', 'sprint', 'replay']
​
# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0
# history command list
historylist = []
​
#flags for replay command
reverse_flag = False
silent_flag = False
​
​
# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100
​
#TODO: WE NEED TO DECIDE IF WE WANT TO PRE_POPULATE A SOLUTION HERE, OR GET STUDENT TO BUILD ON THEIR PREVIOUS SOLUTION.
​
def get_robot_name():
    name = input("What do you want to name your robot? ")
    while len(name) == 0:
        name = input("What do you want to name your robot? ")
    return name
​
​
def get_command(robot_name):
    """
    Asks the user for a command, and validate it as well
    Only return a valid command
    """
​
    prompt = ''+robot_name+': What must I do next? '
    command = input(prompt)
    while len(command) == 0 or not valid_command(command):
        output(robot_name, "Sorry, I did not understand '"+command+"'.")
        command = input(prompt)
​
    return command.lower()
​
​
def split_command_input(command):
    """
    Splits the string at the first space character, to get the actual command, as well as the argument(s) for the command
    :return: (command, argument)
    """
    args = command.split(' ', 1)
    if len(args) > 1:
        return args[0], args[1]
    return args[0], ''
​
​
def is_int(value):
    """
    Tests if the string value is an int or not
    :param value: a string value to test
    :return: True if it is an int
    """
    try:
        int(value)
        return True
    except ValueError:
        return False
​
​
def valid_command(command):
    """
    Returns a boolean indicating if the robot can understand the command or not
    Also checks if there is an argument to the command, and if it a valid int
    """
    global historylist
​
    (command_name, arg1) = split_command_input(command)
    '''
    if command_name.lower() == "replay" and len(arg1) == 0:
        return True
    if command_name.lower() == "replay" and arg1.lower() == "silent":
        return True
    if command_name.lower() == "replay" and arg1.lower() == "reversed":
        return True
    if command_name.lower() == "replay" and arg1.lower() == "reversed silent":
        return True
    if command_name == "replay" and arg1.isdigit():
        return True
​
    if command_name.lower() == "replay": 
        if len(arg1) == 0:
            return True
        elif arg1.lower() == "silent":
            return True
        elif arg1.lower() == "reversed":
            return True
        elif arg1.lower() == "reversed silent":
            return True
    '''
    if command_name.lower() == 'replay':
        return valid_replay_argument(arg1)
​
    if command_name.lower() == "forward" or command_name.lower() == "back" or command_name.lower() == "right" or command_name.lower() == "left" or command_name.lower() == "sprint":
        com = command_name + " " +str(arg1)
        historylist.append(com)
​
    return command_name.lower() in valid_commands and (len(arg1) == 0 or is_int(arg1))
​
​
def output(name, message):
    print(''+name+": "+message)
​
​
def do_help():
    """
    Provides help information to the user
    :return: (True, help text) to indicate robot can continue after this command was handled
    """
    return True, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replays the previous commands executed
"""
​
​
def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')
​
​
def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """
​
    return min_x <= new_x <= max_x and min_y <= new_y <= max_y
​
​
def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """
​
    global position_x, position_y
    new_x = position_x
    new_y = position_y
​
    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps
​
    if is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        return True
    return False
​
​
def do_forward(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    if update_position(steps):
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'
​
​
def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
​
    if update_position(-steps):
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'
​
​
def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index
​
    current_direction_index += 1
    if current_direction_index > 3:
        current_direction_index = 0
​
    return True, ' > '+robot_name+' turned right.'
​
​
def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    global current_direction_index
​
    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3
​
    return True, ' > '+robot_name+' turned left.'
​
​
def do_sprint(robot_name, steps):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
    :param robot_name:
    :param steps:
    :return: (True, forward output)
    """
​
    if steps == 1:
        return do_forward(robot_name, 1)
    else:
        (do_next, command_output) = do_forward(robot_name, steps)
        print(command_output)
        return do_sprint(robot_name, steps - 1)
​
​
​
def do_replay(robot_name, silent, reverse, n, m):
    count =0
    global silent_flag
    global reverse_flag
    global historylist
    
    silent_flag = silent
    reverse_flag = reverse
​
    '''
    if reverse == True:
        for command in reversed(historylist):
            handle_command(robot_name, command)
            count += 1
            com = str(count)
    else:
        for command in historylist:
            handle_command(robot_name, command)
            count += 1
            com = str(count)
    '''
    if reverse_flag == True or (silent == True and reverse == True):
        historylist = historylist[::-1]
    
    for command in historylist[n:m]:
        handle_command(robot_name, command)
        count +=1
    
    silent_flag = False
    reverse_flag = False
​
    if silent == True and reverse == True:
        return True, ' > '+robot_name+ ' replayed '+str(count)+ ' commands in reverse silently.'        
    if silent == True:
        return True, ' > '+robot_name+ ' replayed '+str(count)+ ' commands silently.'
    if reverse == True:
        return True, ' > '+robot_name+ ' replayed '+str(count)+ ' commands in reverse.'
    
​
    return True,' > '+robot_name+ ' replayed ' + str(count) + ' commands.'
​
#Step 6
def limit_range(command):
    parameter = re.findall("\d-\d", command)
    return parameter  
​
#Step 6
def handle_replay(arg):
    global historylist
    silent = False
    reverse = False
    parameter = limit_range(arg)
    n = 0
    m = len(historylist)
​
    if not arg:
        return silent, reverse, n, m
    
    if 'silent' in arg.split():
        silent = True
    if 'reversed' in arg.split():
        reverse = True
    
    if is_int(arg.split()[0]) == True:
        n = len(historylist) - int(arg.split()[0])
    
    if parameter:
        n = len(historylist) - int(parameter[0].split('-')[0])
        m = len(historylist) - int(parameter[0].split('-')[1])
​
    return silent, reverse, n, m
​
​
def valid_replay_argument(arg):
    valid = True
    arg = arg.lower()
    arglist = arg.split()
​
    if len(arg) ==0:
        return True
    
    for x in range(0, len(arglist)):
        if arglist[x] != 'silent' and arglist[x] != 'reversed':
            if not is_int(arglist[x]):
                if len(arglist[x].split('-')) != 2:
                    valid = False
    
    return valid
​
​
def handle_command(robot_name, command):
    """
    Handles a command by asking different functions to handle each command.
    :param robot_name: the name given to robot
    :param command: the command entered by user
    :return: `True` if the robot must continue after the command, or else `False` if robot must shutdown
    """
    #global reverse_flag
    global silent_flag
    silent = False
    reverse = False
​
    (command_name, arg) = split_command_input(command)
​
    if command_name == 'off':
        return False
    elif command_name == 'help':
        (do_next, command_output) = do_help()
    elif command_name == 'forward':
        (do_next, command_output) = do_forward(robot_name, int(arg))
    elif command_name == 'back':
        (do_next, command_output) = do_back(robot_name, int(arg))
    elif command_name == 'right':
        (do_next, command_output) = do_right_turn(robot_name)
    elif command_name == 'left':
        (do_next, command_output) = do_left_turn(robot_name)
    elif command_name == 'sprint':
        (do_next, command_output) = do_sprint(robot_name, int(arg))
    elif command_name == 'replay':
        (silent, reverse, n, m) = handle_replay(arg)
        (do_next, command_output) = do_replay(robot_name, silent, reverse, n, m)
        '''
        if arg == 'silent':
            silent_flag = True
        elif arg == 'reversed':
            reverse_flag = True
        elif arg == 'reversed silent':
            silent_flag = True
            reverse_flag = True
            
        (do_next, command_output) = do_replay(robot_name, silent_flag, reverse_flag, n, m)
        silent_flag = False
        '''
​
    if silent_flag == False:
        print(command_output)
        show_position(robot_name)
​
    return do_next
​
​
def robot_start():
    """This is the entry point for starting my robot"""
​
    global position_x, position_y, current_direction_index
    global historylist
    
    robot_name = get_robot_name()
    output(robot_name, "Hello kiddo!")
    global reverse_flag
    global silent_flag
    reverse_flag = False
    silent_flag = False
    historylist = []
    position_x = 0
    position_y = 0
    current_direction_index = 0
​
    command = get_command(robot_name)
    while handle_command(robot_name, command):
        command = get_command(robot_name)
    output(robot_name, "Shutting down..")
​
​
if __name__ == "__main__":
    robot_start()




