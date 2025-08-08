from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before function runs")
        func()
        print("After fucntion runs")
    return wrapper

@my_decorator
def greet():
    print("Hello, Im Rabi!")
    
greet()
print(greet.__name__)