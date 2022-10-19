import turtle

def process_turtle_commands(commands):
    """ (str) -> NoneType
    Processes the string of space-seperated commands, where each command
    can either be "up" "down" or "x,y" (where x and y
    are two integer coordinates).
    
    >>> "up 50,60 down 40,80 30,20 50,90 up 0,0 down 10,10"
    
    """
    leo = turtle.Turtle()
    
    for command in commands.split():
        if command == "up":
            leo.penup()
        elif command == "down":
            leo.pendown()
        else:
            coords = command.split(',')
            leo.goto(int(coords[0]), int(coords[1]))
    