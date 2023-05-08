from my_classes import *

# Define break points and available commands
BREAK_POINTS = "good bye", "close", "exit"


# Decorator for handling input errors
def input_error(func):
    """Decorator that handles common input errors for command functions."""

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "No such contact!"
        except ValueError:
            return "No such phone number!"
        except TypeError:
            return 'Invalid request! To see available list of commands type "help" '

    return inner


# Command functions
@input_error
def hello(*_):
    """Greet the user."""

    return "How can I help you? Type 'help' to see list of available commands \n "


@input_error
def help(*_):
    """Show a list of available commands and their usage."""

    list_of_instructions = [
        "please not that the separator is space in this bot!" "hello = greeting",
        "add *name* *number* *additional numbers*= adding or updating a contact",
        "change *name* *number* = completely modifies an existing contact",
        "call *name* = number(s)",
        "delete *name* *number(s)* = removes the corresponding phone from the list",
        "remove *name* = removes the contact entirely" "show_all = reveal the data",
        "help = show all commands",
        f"{BREAK_POINTS} = exit the program",
    ]

    return "\n".join(list_of_instructions)


@input_error
def add(name, phone, *_):
    """Add a new contact to the data."""

    if name in DATA.data.keys():
        phone = Phone(phone)
        DATA[name].add_phone(phone)
        for i in _:
            DATA[name].add_phone(Phone(i))
        return "list of numbers is now updated"

    else:
        name = Name(name)
        phone = Phone(phone)
        extra_phones = [Phone(i) for i in _]
        record = Record(name, phone, *extra_phones)
        result = DATA.add_record(record)
        return result


@input_error
def change(name, phone, *_):
    """Change the phone number for an existing contact."""
    if name in DATA.data.keys():
        phone = Phone(phone)
        record = DATA.data[name]
        result = record.change_phone(phone)
        return result
    else:
        return "No such contact!"


@input_error
def call(name, *_):
    """Show the phone number(s) for a contact."""
    list_of_contacts = [i.value for i in DATA.data[name].phones]
    return f"{name}'s number is {', or'.join(list_of_contacts)}"


@input_error
def delete(name, *_):
    """Deletes the phone number(s) for a contact."""
    if name in DATA.data.keys() and _:
        response = [DATA.data[name].delete_phone(i) for i in _]
        return response
    else:
        return "something went wrong!"


@input_error
def remove(name, *_):
    """Deletes the contact."""
    for i in DATA.data.keys():
        if i == name:
            DATA.delete_record(DATA[i])
            return "done!"
    return "something went wrong"


@input_error
def show_all(*_):
    """Show all contacts in the data."""

    return "\n".join(
        f'{i}:{", ".join(k.value for k in j.phones)}' for i, j in DATA.data.items()
    )


# Set of command functions
_commands = {
    "hello": hello,
    "add": add,
    "change": change,
    "call": call,
    "delete": delete,
    "remove": remove,
    "show_all": show_all,
    "help": help,
}


# command parser
@input_error
def command_parser(input):
    command, *data = input.split(" ")
    return command, *data


DATA = AddressBook()


# Main loop
@input_error
def main():
    """Main function that runs the program."""
    while True:
        user_input = input("> ").lower()

        if user_input in BREAK_POINTS:
            break

        command, *data = command_parser(user_input)
        if (func := _commands.get(command)) is not None:
            print(func(*data))
        else:
            print(
                "No such command! Please repeat. To see available list of commands type 'help' "
            )

    print("Good bye!")


if __name__ == "__main__":
    main()
