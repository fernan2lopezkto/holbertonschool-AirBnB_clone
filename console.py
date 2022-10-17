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
        elif (x[0] != "BaseModel"):
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
        if not args:
            print("** class name missing **")
        elif (s[0] != "BaseModel"):
            print("** class doesn't exist **")
        elif len(s) == 1:
            print("** instance id missing **")
        else: 
            key = s[0] + "." + s[1]
            dic = storage.all()
            try:
                del dic[key]
                storage.save()
            except Exception:
                print("** no instance found **")

    def do_all(self, args):
        """prints all string representation"""
        l = []
        dic = storage.all()
        if not args:
            for k, v in dic.items():
                l.append(dic[k].to_dict())
            print(l)
        elif args == "BaseModel":
            for k, v in dic.items():
                if v.__class__.__name__ == "BaseModel":
                    l.append(dic[k].to_dict())
            print(l)
        else:
            print("** class doesn't exist **")            

    def do_update(self, args):
        """update instance atribute"""
        s = args.split(" ")
        if not args:
            print("** class name missing **")
        elif (s[0] != "BaseModel"):
            print("** class doesn't exist **")
        elif len(s) == 1:
            print("** instance id missing **")
        elif len(s) == 2:
            print("** attribute name missing **")
        elif len(s) == 3:
            print("** value missing **")
        else:
            key = s[0] + "." + s[1]
            dic = storage.all()
            try:
                inst = dic[key]
                setattr(inst, s[2], s[3])
                storage.save()
            except Exception:
                print("** no instance found **")
                return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
