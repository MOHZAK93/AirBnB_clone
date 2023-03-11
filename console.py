#!/usr/bin/python3

import cmd, sys


class HBNBCommand(cmd.Cmd):
    """"""
    prompt = '(hbnb) '
    file = None

    def do_EOF(self, arg):
        'End of file'
        EOF(*parse(arg))
    def do_quit(self, arg):
        'Quit command to exit the program\n'
        self.close()
        return True
    def precmd(self, line):
        line = line.lower()
        if self.file and 'playback' not in line:
            print(line, file=self.file)
        return line
    def emptyline(self):
        """Called when an empty line is entered in response to prompt"""
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')
    def close(self):
        if self.file:
            self.file.close()
            self.file = None

if __name__ == '__main__':
    HBNBCommand().cmdloop()
