"""CLI_Bot"""


def input_error(func):
    """Decorator returns input error"""
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Unknown user or invalid user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Invalid command or input"
    return inner


@input_error
def hello_func():
    """Returns greeting"""
    return "How can I help you?"


@input_error
def add_func(users_dict, name, phone):
    """Add a new contact"""
    if name and phone:
        users_dict[name] = phone
        return f"Contact {name.capitalize()}: phone {phone}"
    raise ValueError


@input_error
def change_func(users_dict, name, phone):
    """Change a current contact"""
    if name and phone:
        if name not in users_dict:
            raise KeyError
        users_dict[name] = phone
        return f"Phone number for {name.capitalize()} changed to {phone}"
    raise ValueError



@input_error
def show_phone(users_dict, name):
    """Show a current contact's phone number"""
    if name not in users_dict:
        raise KeyError
    return f"The phone number for {name.capitalize()} is {users_dict[name]}"



def show_all(users_dict):
    """Show all contacts if it possible"""
    if not users_dict:
        return "No users available"
    result = "\n".join([f"{name.capitalize()}: {phone}" for name, phone in users_dict.items()])
    return result


@input_error
def input_error_raiser():
    """Returns input error"""
    raise IndexError


def main():
    """Main function"""
    users_dict = {}
    while True:
        command = input("Enter command: ").lower()
        if command in ["good bye", "close", "exit", "stop", "."]:
            print("Good bye!")
            break
        if command in ["hello", "hi"]:
            print(hello_func())
        elif command.startswith("add "):
            if len(command.split(' ')) != 3:
                print(input_error_raiser())
            else:
                _, name, phone = command.split(' ')
                print(add_func(users_dict, name, phone))
        elif command.startswith("change "):
            if len(command.split(' ')) != 3:
                print(input_error_raiser())
            else:
                _, name, phone = command.split(' ')
                print(change_func(users_dict, name, phone))
        elif command.startswith("phone "):
            if len(command.split(' ')) != 2:
                print(input_error_raiser())
            else:
                _, name = command.split(' ')
                print(show_phone(users_dict, name))
        elif command == "show all":
            print(show_all(users_dict))
        else:
            print("Unknown command")


if __name__ == "__main__":
    main()
