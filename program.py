import math
import sys

class Program:
    commands = (
        { 'command': 'commands', 'desc': 'List al available commands' },
        { 'command': 'list', 'desc': 'List al available programs' },
        { 'command': 'run', 'desc': 'Starts given program, syntax: run program-name' },
        { 'command': 'exit', 'desc': 'Exit program' },
    )
    name = ''
    programs = ()
    running = True

    def __init__(self, name, programs):
        self.name = name
        self.programs = programs

    # prints a list of the comamnds
    def printCommands(self):
        print('-----------------------------------------------------')
        print('------------------- Commands ------------------------')
        for i in self.commands:
            print(i['command'] + ':', i['desc'])
        print('-----------------------------------------------------')

    # prints a list of the runnable programs
    def printPrograms(self):
        print('-----------------------------------------------------')
        print('------------------- Programs ------------------------')
        for i in self.programs:
            print(i['name'] + ':', i['desc'])
        print('-----------------------------------------------------')

    def run(self, params):
        programString = params[0]
        # check if there is a program in the dictionary tuple
        program = next((i for i in self.programs if i['name'] == programString), None)
        while not program:
            programString = input('Program not found, enter program: ').lower()
            program = next((i for i in self.programs if i['name'] == programString), None)

        # import the program file
        __import__(program['file'])
        del sys.modules[program['file']]


    def start(self):
        # Print entry message
        length = 100 # TODO: use this for commands, list prints too

        nameLength = len(self.name)
        nameString = '-' * (math.floor((length - nameLength) / 2) - 1) + ' ' + self.name + ' ' + '-' * (math.floor((length - nameLength) / 2) - 1)
        if len(nameString) % 2 == 1: nameString += '-'

        commandsString = 'Use `Commands` for all available commands'
        commandsLength = len(commandsString)
        commandsString = '-' * (math.floor((length - commandsLength) / 2) - 1) + ' ' + commandsString + ' ' + '-' * (math.floor((length - commandsLength) / 2) - 1) + '-'

        print()
        print('-' * length)
        print(nameString)
        print('-' * length)
        print()
        print('-' * length)
        print(commandsString)
        print('-' * length)
        print()

        # Program loop
        while self.running:
            # Ask for a command
            commandList = input('Command: ').lower().split(' ')
            commandString = commandList[0]
            commandParameters = commandList[1:]

            # check if there is a command in the dictionary tuple
            while not any(i['command'] == commandString for i in self.commands):
                print('Command not found!')
                commandList = input('Command: ').lower().split(' ')
                commandString = commandList[0]
                commandParameters = commandList[1:]

            # Python has no switch
            # define the function blocks
            if commandString == 'run':
                self.run(commandParameters)

            # Display list with all programs
            elif commandString == 'commands':
                self.printCommands()

            # Display list with all programs
            elif commandString == 'list':
                self.printPrograms()

            # Exit the program
            elif commandString == 'exit':
                self.running = False

            print()

        # Print exit message
        print('Exit:', self.name)
