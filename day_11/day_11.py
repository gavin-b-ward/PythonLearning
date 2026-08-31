from enum import Enum
from math import pi
from typing import List
from typing import Any


def add_two_numbers(x: int, y: int) -> int:
    return x + y


def area_of_circle(radious: float) -> float:
    return pi * (radious**2)


def add_all_nums(*nums: int) -> int:
    total = 0
    for num in nums:
        total += num
    return total


print(add_all_nums(1, 2, 3, 4, 5, 6))


def convert_celsius_to_fahrenheit(c: float):
    return (9 / 5) * c + 32


print(convert_celsius_to_fahrenheit(1.0))


def check_season(month: str) -> str:
    if month == "march" or month == "april" or month == "may":
        return "spring"
    if month == "june" or month == "july" or month == "august":
        return "summer"
    if month == "september" or month == "october" or month == "novemeber":
        return "autumn"
    if month == "december" or month == "january" or month == "february":
        return "winter"

    return "invalid month"


print(check_season("december"))
print(check_season("pizza"))


def print_list(l: list[Any]):
    for item in l:
        print(item)


print(print_list([1, 2, 3, 4, 5]))
print(print_list(["A", "B", "C"]))


def reverse_list(l: list[Any]) -> list[Any]:
    reversed_list = []
    for i in range(len(l) - 1, -1, -1):
        reversed_list.append(l[i])
    return reversed_list


print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))
