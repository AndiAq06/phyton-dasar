def cough_dec(func):

    def func_wrapper():
        # code before function
        print(' *cough* ')
        func()
        # code after function
        print(' *cough* ')

    return func_wrapper


@cough_dec
def question():
    print('can you give me a discount on that?')


@cough_dec
def answer():
    print("it's only 50p you cheapskate")


# question = cough_dec(question)
question()
answer()


#  Dekarator biasa

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Memanggil fugsi: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Fungsi {func.__name__} selesai dipanggil.")
        return result
    return wrapper


@log_decorator
def say_hello(name):
    print(f"Hello, {name}")


say_hello("Andi")


# Dekorator dengan Parameter
def repeat(n):
    def log_decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Memanggil fugsi: {func.__name__}")
            for _ in range(n):
                func(*args, **kwargs)
            print(f"Fungsi {func.__name__} selesai dipanggil.")
        return wrapper
    return log_decorator


@repeat(3)
def greet(name):
    print(f"Hello, {name}!")


greet("Andi")
