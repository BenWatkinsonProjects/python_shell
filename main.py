import sys
from pathlib import Path
import os

p = Path.cwd()
valid_commands = ['echo', 'type', 'exit']
p = os.path.dirname(sys.executable)
p = p.split("\\")


def cmd_exit(args):
    exit()

def cmd_echo(args):
    print(args)

def cmd_type(args):
    if args in valid_commands:
        print(args + " is a shell builtin")
    else:    
        print(args + ": not found")

commands = {
    "exit" : cmd_exit,
    "echo" : cmd_echo,
    "type" : cmd_type
}

def user_input():
    raw_inp = input("$ ")
    if not raw_inp:
        return

    parts = raw_inp.strip().split(" ", 1)
    name = parts[0]
    args = parts[1] if len(parts) > 1 else ""

    if name in commands:
        commands[name](args)
    else: 
        print(name + ": command not found")

while True:
    if __name__ == "__main__":
        user_input()

 
