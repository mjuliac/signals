from abc import ABCMeta, abstractmethod



class EventHandler:
    def __init__(self, callback):
        self._callback = callback
    
    def handle(self, *args, **kwargs):
        self._callback(*args, **kwargs)


class IEvent(metaclass=ABCMeta):
    @abstractmethod
    def add_handler(self, handler: EventHandler):
        pass
    
    @abstractmethod
    def remove_handler(self, handler: EventHandler):
        pass
    
    @abstractmethod
    def emit(self, *args, **kwargs):
        pass 

    def __iadd__(self, handler: EventHandler):
        self.add_handler(handler)
        return self

    def __isub__(self, handler: EventHandler):
        self.remove_handler(handler)
        return self


class Event(IEvent):
    def __init__(self):
        self._handlers = {}
    
    def add_handler(self, handler):
        self._handlers[handler] = EventHandler(handler)
    
    def remove_handler(self, handler):
        if handler in self._handlers:
            self._handlers.pop(handler)
    
    def emit(self, *args, **kwargs):
        for handler in self._handlers.values():
            handler.handle(*args, **kwargs)
    @property
    def handlers(self):
        return self._handlers
