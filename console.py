#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage
import re
import json


class HBNBCommand(cmd.Cmd):

    """ cmd """

    prompt = "(hbnb) "

    def default(self, line):
        """ cmd matching """
        self.cmd_parse(line)

    def cmd_parse(self, line):
        """ regex for parsing cmd """
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match:
            return line
        classname = match.group(1)
        method = match.group(2)
        args = match.group(3)
        match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_uid_and_args:
            uid = match_uid_and_args.group(1)
            attr_or_dict = match_uid_and_args.group(2)
        else:
            uid = args
            attr_or_dict = False

        attr_and_value = ""
        if method == "update" and attr_or_dict:
            match_dict = re.search('^({.*})$', attr_or_dict)
            if match_dict:
                self.update_dict(classname, uid, match_dict.group(1))
                return ""
            match_attr_and_value = re.search(
                '^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict)
            if match_attr_and_value:
                attr_and_value = (match_attr_and_value.group(
                    1) or "") + " " + (match_attr_and_value.group(2) or "")
        command = method + " " + classname + " " + uid + " " + attr_and_value
        self.onecmd(command)
        return command

    def dict_updt(self, class_name, uid, s_dict):
        """ Updates dict """
        x = s_dict.replace("'", '"')
        y = json.loads(s)
        if not class_name:
            print("Missing class name!")
        elif class_name not in storage.classes():
            print("Class does not exist!")
        elif uid is None:
            print("Instance UID missing!")
        else:
            key = "{}.{}".format(class_name, uid)
            if key not in storage.all():
                print("Instance/s missing!")
            else:
                attributes = storage.attributes()[class_name]
                for attribute, value in y.items():
                    if attribute in attributes:
                        value = attributes[attribute](value)
                    setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

    def do_EOF(self, line):
        """ Terminates active shell """
        print()
        return True

    def do_quit(self, line):
        """ Terminates active shell """
        return True

    def emptyline(self):
        """ Stays on prompt when enter key is pushed """
        pass

    def do_create(self, line):
        """ Will create an instance. """
        if line == "" or line is None:
            print("Missing class name!")
        elif line not in storage.classes():
            print("Class does not exist!")
        else:
            z = storage.classes()[line]()
            z.save()
            print(z.id)

    def do_show(self, line):
        """ Prints str rep of obj. """
        if line == "" or line is None:
            print("Missing class name!")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("Class does not exist!")
            elif len(words) < 2:
                print("Missing inst/obj instance id.")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("Instance missing.")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes instance based on the class name and id. """
        if line == "" or line is None:
            print("Missing class name!")
        else:
            syntax = line.split(' ')
            if syntax[0] not in storage.classes():
                print("Class does not exist!")
            elif len(syntax) < 2:
                print("Missing inst/obj instance id.")
            else:
                key = "{}.{}".format(syntax[0], syntax[1])
                if key not in storage.all():
                    print("Instance missing.")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances."""
        if line != "":
            syntax = line.split(' ')
            if syntax[0] not in storage.classes():
                print("Class does not exist!")
            else:
                nl = [str(obj) for key, obj in storage.all().items()
                      if type(obj).__name__ == syntax[0]]
                print(nl)
        else:
            new_list = [str(obj) for key, obj in storage.all().items()]
            print(new_list)

    def do_count(self, line):
        """Counts the instances of a class."""
        syntax = line.split(' ')
        if not syntax[0]:
            print("Missing class name!")
        elif syntax[0] not in storage.classes():
            print("Class does not exist!")
        else:
            matches = [
                k for k in storage.all() if k.startswith(
                    syntax[0] + '.')]
            print(len(matches))

    def do_update(self, line):
        """Updates an instance by adding or updating attribute."""
        if line == "" or line is None:
            print("Missing class name!")
            return

        regex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        regex_match = re.search(regex, line)
        class_name = regex_match.group(1)
        uid = regex_match.group(2)
        attribute = regex_match.group(3)
        value = regex_matchmatch.group(4)
        if not regex_match:
            print("Missing class name!")
        elif class_name not in storage.classes():
            print("Missing class name!")
        elif uid is None:
            print("Missing inst id.")
        else:
            key = "{}.{}".format(class_name, uid)
            if key not in storage.all():
                print("Inst/obj not found.")
            elif not attribute:
                print("Missing attribute name")
            elif not value:
                print("Missing value.")
            else:
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                attributes = storage.attributes()[class_name]
                if attribute in attributes:
                    value = attributes[attribute](value)
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass
                setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
