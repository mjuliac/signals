from events import Event
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    mail: str
    
class Button:
    def __init__(self):        
        self.clicked = Event()

    def click(self, x, y):
        self.clicked.emit(x, y)

class Label(Event):
    def __init__(self):
        self.text_changed = Event()

    def set_text(self, text):
        self.text = text
        self.text_changed.emit(self.text)
        

class UserDAO:
    def __init__(self):
        self.user_created = Event()
        self.user_deleted = Event()
        
    def add(self, user: User):
        print("Adding user: ", user)
        self.user_created.emit(user)
    
    def remove(self, user: User):
        print("Deleting user: ", user)
        self.user_deleted.emit(user)

    def __del__(self):
        for event in self.__dict__.values():
            for handler in list(event.handlers):
                event -= handler

        
       

def print_click(x, y):
    print("Button clicked at", x, y)

def print_label(text):
    print("Label printed:", text)

def user_created(user):
    print("User created:", user)

def finally_user_created(user):
    print("Finally user created:", user)

def user_deleted(user):
    print("User deleted:", user)


def main():
    button = Button()
    button.clicked += print_click
    button.click(50, 20)
    button.clicked -= print_click
    button.click(510, 20)
    
    label = Label()
    label.text_changed += print_label
    label.set_text("Hola mundo")
    label.set_text("Adios mundo")
    label.text_changed -= print_label
    label.set_text("No se imprimira")
    
    user = User("John", 30, "john@example.com")
    user_dao = UserDAO()
    user_dao.user_created += user_created
    user_dao.user_created += finally_user_created
    user_dao.user_deleted += user_deleted
    user_dao.add(user)
    user_dao.remove(user)
    del user_dao
    

if __name__ == "__main__":
    main()
