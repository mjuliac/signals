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
        self.click = Event()

class Label(Event):
    def __init__(self):
        self.text_changed = Event()
        

class UserDAO:
    def __init__(self):
        self._create = Event()
        self._remove = Event()
        
    def add(self, user: User):
        self.user = user
        self._create += self.create_user
        self._create.emit()

    def create_user(self):
        print("User created:", self.user)

    def remove(self, user: User):
        self.user = user
        self._remove += self.remove_user
        self._remove.emit()

    def remove_user(self):
        print("User removed:", self.user)


def main():
    button = Button()
    button.click += print_click
    button.click.emit(50, 20)
    button.click -= print_click
    button.click.emit(510, 20)
    
    label = Label()
    label.text_changed += print_label
    label.text_changed.emit("Hola mundo")
    label.text_changed.emit("Adios mundo")
    label.text_changed -= print_label
    label.text_changed.emit("No se imprimira")
    
    user = User("John", 30, "john@example.com")
    user_dao = UserDAO()
    user_dao.add(user)
    user_dao.remove(user)


if __name__ == "__main__":
    main()
