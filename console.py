#!/usr/bin/python3
"""interprete"""

import cmd

class HBNBCommand(cmd.Cmd):
    """class HBNB interpreter"""
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """func to quit"""
        return True

    def do_EOF(self,):
        """end of a file function"""
        return True

    def emptyline(self):
        """empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

    def do_create(self, args)
        """func that creates new instaance"""
        if args == "BaseModel":
            new_base = BaseModel()
            new_base.save()
            print(new_base.id)

        if class name 
