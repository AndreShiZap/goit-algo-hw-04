# Початковий бот-асистент (без обробки помилок та збереження у файл): 
# зберігає ім'я та номер телефону (у пам’яті), 
# знаходить номер телефону за ім'ям, 
# змінює записаний номер телефону, 
# виводить в консоль всі записи, які збереженні


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return "Contact already exists"
    else:
        contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
    else:
        return "Contact not found"
    return "Contact updated."

def phone_show(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found"

def main():
    print("Welcome to the assistant bot!")
    contacts = {}
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case ("close" | "exit"):
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, contacts))
            case "change":
                print(change_contact(args, contacts))
            case "phone":
                print(phone_show(args, contacts))
            case "all":
                print(contacts)
            case _:
                print("Invalid command.")


if __name__ == "__main__":
    main()
