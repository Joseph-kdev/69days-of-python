def decorator_function(function):
    def wrapper_function(function):
        function()
        function()
        
    return wrapper_function

@decorator_function
def say_hello():
    print("Hello")