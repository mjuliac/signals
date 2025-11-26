# Python Signals / Events

Este proyecto implementa un sistema de eventos en Python similar al de C#, permitiendo suscribir y desuscribir manejadores de eventos (handlers) de forma sencilla utilizando operadores.

## Características

- **Sintaxis intuitiva**: Uso de `+=` para agregar suscriptores y `-=` para removerlos.
- **Desacoplamiento**: Permite separar la lógica de disparo de eventos de la lógica de manejo.
- **Flexibilidad**: Soporta múltiples manejadores para un mismo evento.

## Estructura

- `events.py`: Contiene la implementación base del sistema de eventos (`Event`, `IEvent`, `EventHandler`).
- `main.py`: Ejemplo de uso con clases como `Button`, `Label` y `User`.

## Ejemplo de uso

```python
from events import Event

def mi_handler(mensaje):
    print(f"Evento recibido: {mensaje}")

evento = Event()
evento += mi_handler  # Suscribirse
evento.emit("Hola!")  # Disparar evento
evento -= mi_handler  # Desuscribirse
```
