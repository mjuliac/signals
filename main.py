from events import Event
from dataclasses import dataclass

def print_click(x, y):
    print("Button clicked at", x, y)

def print_label(text):
    print("Label printed:", text)

def print_user_created(user):
    print("User created:", user)

@dataclass
class User:
    name: str
    age: int
    mail: str
    
class Button:
    def __init__(self):
        # super(Button, self).__init__()
        # Add the global click function as a handler
        self.click = Event()
        self.click += print_click

class Label(Event):
    def __init__(self):
        super(Label, self).__init__()
        self += print_label

class CreateUser(Event):
    def __init__(self, user: User):
        super(CreateUser, self).__init__()
        self.user = user
        self.create = Event()
        
    def add(self):
        self.create += print_user_created
        self.create.emit(self.user)

    def remove(self):
        self.create -= print_user_created
        self.create.emit(self.user)


def main():
    button = Button()
    button.click.emit(50, 20)
    # Remove the global click function handler
    button.click -= print_click
    button.click.emit(510, 20)
    
    label = Label()
    label.emit("Hola mundo")
    label -= print_label
    label.emit("Adios mundo")
    
    user = User("John", 30, "john@example.com")
    create_user = CreateUser(user)
    create_user.add()

    create_user.remove()


if __name__ == "__main__":
    main()
