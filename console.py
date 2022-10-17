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
                created.save()
                print(created.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, args):
        """show obj"""
        x = args.split(" ")
        if len(x) == 0:
            print("** class name missing **")
        elif (x[0] =! "BaseModel"):
            print("** class doesn't exist **")
        elif len(x) == 1:
            print("** instance id missing **")
        else:
            key = x[0] + "." + x[1]
            dic = storage.all()
            try:
                print(dic[key])
            except Exception:
                print("** no instance found **")

    def do_destroy(self, args):
        """destroy obj"""
        s = args.split(" ")
        if len(s) == 0:
            print("** class name missing **")
        elif (s[0] =! "BaseModel"):
            print("** class doesn't exist **")
        elif len(s) == 1:
            print("** instance id missing **")
        else: 
            key = x[0] + "." + x[1]
            dic = storage.all()
        try:
            print(dic[key])
        except Exception:
            print("** no instance found **")

    def do_all(self, args)
        """prints all string representation"""
        l = []
        dic = storage.all()
        if args is None:
            for k, v in dic.items():
                l.append(dic[k])
            print(l)
        if (m[0] =! "BaseModel"):
            print("** class doesn't exist **")
