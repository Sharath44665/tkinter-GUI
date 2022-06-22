def add(n1, n2):
    return n1 + n2


def add_numbers(*args):
    sum = 0
    for n in args:  # if you do type check of args, then it will return tuple
        sum += n
    return sum


result = add(2, 4)
print(result)
result = add_numbers(3, 4, 5)
print(result)


# ----------------------

def calculate(n, **kwargs):
    # kwargs = keyword arguments
    print(kwargs)
    n += kwargs["add"]
    print(n)
    n *= kwargs["multiply"]
    print(n)


calculate(n=2, add=3, multiply=2)


class Car:
    def __init__(self, **kwargs):
        # self.model = kwargs["model"]
        # self.make = kwargs["make"]
        self.model=kwargs.get("model") # if you dont have model then return none
        self.make=kwargs.get("make")
        self.color=kwargs.get("color")


my_car = Car(make="Hyndai")


print(my_car.model)
