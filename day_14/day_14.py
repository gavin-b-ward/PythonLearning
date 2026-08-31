from functools import reduce

countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
names = ["Asabeneh", "Lidiya", "Ermias", "Abraham"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map applies a change to each value in a list; One example is squaring all numbers in a list

# filter reduces the amount of values in a list based on some filter criteria

# reduce reduces all values in a list down to a single value by doing someoperation, like squaring all values then adding them together.

# a higher order functions mean functions can take functions as params be returned as values, be modified, and can be assigned as a variable

# closures are when a function returns a function as a result that can be called to update a value within the outer function


# a decorator is a wrapper function that does some action before the inner function is executed.
def print_list(l):
    for i in l:
        print(i)


c = map(lambda country: country.upper(), countries)


n = map(lambda num: num**2, numbers)


c = filter(lambda country: "land" not in country, countries)
c = filter(lambda country: len(country) != 6, countries)
c = filter(lambda country: country[0] != "E", countries)
n = reduce(lambda x, y: x + y, numbers)


def make_sentence(x, y) -> str:
    return f"{x}, {y}"


cv = f"{reduce(make_sentence, countries)} are north european countries"


print_list(c)
print(n)
print(cv)
