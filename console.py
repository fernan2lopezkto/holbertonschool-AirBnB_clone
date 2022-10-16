#!/usr/bin/python3
"""interprete"""

from models.base_model import BaseModel
from models import storage
import cmd


class HBNBCommand(cmd.Cmd):
    """class HBNB interpreter"""
    prompt = "(hbnb)"

    """task 6
    """

    def do_quit(self, arg):
        """func to quit"""
        return True

    def do_EOF(self,):
        """end of a file function"""
        return True

    def emptyline(self):
        """empty line"""
        pass

    """task 7
    """

    def do_create(self, base_name):
        """create Base MOdel instance"""
        if base_name:
            if base_name == "BaseModel":
                created = BaseModel()
                print(created.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self,):
        print("helo")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
