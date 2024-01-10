import args

#Decorators: başka fonksiyonları parametre olarak kabul edip onları değiştirme özelliğine sahiptir
def print_fun():
    print("hey")

def decorator_func(func):
    def wrapper_func():
        return func()
    return wrapper_func()

decorated_print = decorator_func(print_fun)

#aynı şeyin laciverti
@decorator_func
def print_func():
    print("hey")

def decorator_func(func):
    def wrapper_func():
        print(f"the of the funciton is {func.__name__}")
        return func(*args)
    return wrapper_func

#aliye sor output neden böyle geldi