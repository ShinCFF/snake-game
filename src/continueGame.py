import numpy as np
def checkContinue():
    with open('data/check.txt', 'r') as file:
        data = file.read()
        ok = int(data)
        return ok

def colorHead():
    with open('data/colorHead.txt', 'r') as file:
        data = file.read()
        color = eval(data)
        return color

def colorBody():
    with open('data/colorBody.txt', 'r') as file:
        data = file.read()
        color = eval(data)
        return color

def snakeArray():
    with open('data/snake.txt', 'r') as file:
        lines = file.readlines()
        processed_lines = [line.replace('[', '').replace(']', '') for line in lines]
    return np.loadtxt(processed_lines)

def foodArray():
    with open('data/fruit.txt', 'r') as file:
        lines = file.readlines()
        processed_lines = [line.replace('[', '').replace(']', '') for line in lines]
    return np.loadtxt(processed_lines)

def snakeDir():
    with open('data/direction.txt', 'r') as file:
        data = file.read()
        dir = int(data)
        return dir
    
def levelGame():
    with open('data/level.txt', 'r') as file:
        data = file.read()
        level = int(data)
        return level
