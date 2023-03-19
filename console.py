#!/usr/bin/python3

"""Module implements command line interface for manipulating objects"""

from models.base_model import BaseModel
from models.user import User
from models.ingredient import Ingredient
from models.meal import Meal
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DB_Storage
import cmd
import models
from colorama import init, Fore, Back, Style
import random

classes = {"User": User, "Ingredient": Ingredient, "Meal": Meal}

class DietBUDCommand(cmd.Cmd):
    """ DietBUD console """
    prompt = f"{Style.BRIGHT}{Fore.LIGHTYELLOW_EX}DietBUD{Fore.LIGHTYELLOW_EX}[$]{Style.RESET_ALL} "

    def do_quit(self, args):
        """Exits cmd interface"""
        print(random.choice([
            "Remember, breakfast is the most important meal of the day!",
            "Drink plenty of water to stay hydrated throughout the day!",
            "Don't forget to eat your fruits and veggies!",
            "Protein is essential for building and repairing muscles!",
            "A balanced diet is key to maintaining good health!"]))
        return True

        print("See You Later")
        print("DIET_BUDDY 'SAVOUR EVERY MOMENT'")
        quit()

    def do_help(self, args):
        """renders help to user"""

    def preloop(self):
        print(Fore.LIGHTBLUE_EX + "\nHello! Welcome to DietBUD V_1.0\n" +
              Style.RESET_ALL )

    def emptyline(self):
        """Continue to next prompt"""
        pass

    def do_all(self, args):
        """returns all objects in storage"""
        try:
            if len(args) == 0:
                all_objects = []
                for key, value in models.storage.all().items():
                    all_objects.append(str(value))
                print(all_objects)
                return
            arguments = args.split(" ")
            if len(arguments) == 1:
                class_objects = []
                if arguments[0] in classes:
                    for value in models.storage.all(arguments[0]).values():
                        class_objects.append(str(value))
                    print(class_objects)
                else:
                    print(Fore.RED + "Please enter a valid class"
                          + Style.RESET_ALL)
        except Exception:
            pass

    def do_create(self, args):
        """creates objects and saves them to storage"""
        try:
            if len(args) == 0:
                print("Please enter Class Name to create Object")
                return
            arguments = args.split(" ")

            if arguments[0] not in classes:
                print("**Invalid Class**")
                return

            if len(arguments) == 1:
                obj = eval(arguments[0])()
                obj.save()
                print(Fore.MAGENTA +
                      f"Successfully created {obj.__class__.__name__}"
                      +
                      f" object: id --  {obj.id}" + Style.RESET_ALL)
                return
            if len(arguments) > 1:
                new_dict = {}
                for entry in arguments[1:len(arguments)]:
                    key = entry.split("=")[0]
                    key = str(key)
                    key = key.replace('"', "")
                    key = key.replace("'", "")
                    attr = entry.split("=")[1]

                    if attr == "True" or attr == "False":
                        attr = bool(attr)
                    elif (attr[0] == '"'
                          and attr[len(attr) - 1] == '"' or
                          attr[0] == "'" and attr[len(attr) - 1] == "'"):
                        attr = str(attr)
                        attr = attr.replace('"', "")
                        attr = attr.replace("'", "")
                        attr = attr.replace("_", " ")
                    else:
                        try:
                            attr = int(attr)
                        except TypeError:
                            print("Not an integer")
                    new_dict.update({key: attr})
                obj = eval(arguments[0])(**new_dict)
                obj.save()
                print(f"Successfully Created {obj.__class__.__name__} object: "
                      + Fore.LIGHTGREEN_EX
                      + f" DietBUD_id --  {obj.id}"
                      + Style.RESET_ALL)
        except Exception:
            pass

    def do_delete(self, args):
        """Deletes object from storage"""
        try:
            arguments = args.split(" ")
            if len(arguments) == 1:
                cid = args
                for key, value in models.storage.all().items():
                    obj_id = key.split(".")[1]
                    if cid == obj_id:
                        models.storage.delete(value)
                        print(Fore.RED + "Deleted" + Style.RESET_ALL)
        except Exception:
            pass

    def do_update(self, args):
        """Updates object"""
        try:
            arguments = args.split(" ")
            if len(arguments) > 1:
                new_dict = {}
                for entry in arguments[1:len(arguments)]:
                    key = entry.split("=")[0]
                    key = str(key)
                    key = key.replace('"', "")
                    key = key.replace("'", "")
                    attr = entry.split("=")[1]

                    if attr == "True" or attr == "False":
                        attr = bool(attr)
                    elif (attr[0] == '"' and attr[len(attr) - 1] == '"'
                          or attr[0] == "'" and attr[len(attr) - 1] == "'"):
                        attr = str(attr)
                        attr = attr.replace('"', "")
                        attr = attr.replace("'", "")
                        attr = attr.replace("_", " ")
                    else:
                        try:
                            attr = int(attr)
                        except TypeError:
                            print("Not an integer")
                    new_dict.update({key: attr})
                cid = arguments[0]
                for key in models.storage.all().keys():
                    obj_id = key.split(".")[1]
                    if cid == obj_id:
                        models.storage.update(key, **new_dict)
                        print(Fore.LIGHTMAGENTA_EX + "Instance Updated"
                              + Style.RESET_ALL)
        except Exception:
            pass

    def do_count(self, args):
        """Counts all objects"""
        try:
            if len(args) == 0:
                print("The total number of objects in Storage is {}".
                      format(len(models.storage.all())))
                return
            arguments = args.split(" ")
            if len(arguments) == 1:
                if arguments[0] in classes:
                    obj_count = len(models.storage.all(arguments[0]))
                    print("The total number of {}s".
                          format(arguments[0]) + Fore.LIGHTGREEN_EX
                          + "{}".format(obj_count)
                          + Style.RESET_ALL)
                    return
                else:
                    print(Fore.RED + "Please enter a valid class" +
                          Style.RESET_ALL)
        except Exception:
            pass

    def do_show(self, args):
        """Prints object based id"""
        arguments = args.split(" ")
        try:
            if len(arguments) == 1:
                for key, value in models.storage.all().items():
                    obj_id = key.split(".")[1]
                    if arguments[0] == obj_id:
                        print(models.storage.get(key))
        except Exception:
            pass


if __name__ == "__main__":
     DietBUDCommand().cmdloop()
