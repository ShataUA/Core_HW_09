"""CLI_Bot"""


def input_error(func):
    """Decorator returns input error"""
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Invalid user name or user name not found"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "User name is already exists"
    return inner


@input_error
def hello_func():
    """Returns greeting"""
    return "How can I help you?"


@input_error
def add_func(users_dict, command):
    """Add a new contact"""
    _, name, phone = command.split()
    if name and phone and name not in users_dict:
        users_dict[name] = phone
        return f"Contact {name.capitalize()}: phone {phone}"
    raise IndexError if users_dict[name] else ValueError


@input_error
def change_func(users_dict, command):
    """Change a current contact"""
    _, name, phone = command.split()
    if name and phone and name in users_dict:
        users_dict[name] = phone
        return f"Phone number for {name.capitalize()} changed to {phone}"
    raise ValueError if users_dict[name] else KeyError


@input_error
def show_phone(users_dict, command):
    """Show a current contact's phone number"""
    _, name = command.split()
    if name not in users_dict:
        raise KeyError
    return f"The phone number for {name.capitalize()} is {users_dict[name]}"


def show_all(users_dict):
    """Show all contacts if it possible"""
    if not users_dict:
        return "No users available"
    result = "\n".join([f"{name.capitalize()}: {phone}" for name, phone in users_dict.items()])
    return result



def main():
    """Main function"""
    users_dict = {}
    while True:
        command = input("Enter command: ").lower().strip()
        if command in ["good bye", "close", "exit", "stop", "."]:
            print("Good bye!")
            break
        if command in ["hello", "hi"]:
            print(hello_func())
        elif command.startswith("add "):
            print(add_func(users_dict, command))
        elif command.startswith("change "):
            print(change_func(users_dict, command))
        elif command.startswith("phone "):
            print(show_phone(users_dict, command))
        elif command == "show all":
            print(show_all(users_dict))
        else:
            print("Unknown command")


if __name__ == "__main__":
    main()
