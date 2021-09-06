def get_hello_message():
    return 'Hello, World'


def say_hello():
    message = get_hello_message()
    print(message)


def get_hello_message():
    name = input("What`s your name? ")
    if not name:
        name = "World"
    return f'Hello, {name}!'


def get_user_name():
    entered_name = input("What`s your name? ")
    return entered_name.capitalize()


def say_helo():
    user_name = get_user_name()
    message = get_hello_message(user_name)
    print(message)


say_hello()
