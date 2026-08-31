from random import randint
import string


def random_user_id() -> str:
    id: str = ""
    for _ in range(6):
        if randint(0, 1) == 0:
            idx = randint(0, 51)
            id += string.ascii_letters[idx]
        else:
            idx = randint(0, 9)
            id += string.digits[idx]
    return id


def user_id_gen_by_user():
    l = input("ID length: ")
    c = input("ID count: ")

    for _ in range(int(c)):
        id: str = ""
        for _ in range(int(l)):
            if randint(0, 1) == 0:
                idx = randint(0, 51)
                id += string.ascii_letters[idx]
            else:
                idx = randint(0, 9)
                id += string.digits[idx]
        print(id)


def print_rgb_number():
    c1 = randint(0, 255)
    c2 = randint(0, 255)
    c3 = randint(0, 255)
    print(f"rgb({c1},{c2},{c3})")


def list_of_hexa_colors(r: int):
    color_list = []
    for i in range(r):
        id: str = "#"
        for _ in range(6):
            if randint(0, 1) == 0:
                idx = randint(0, 5)
                id += string.ascii_letters[idx]
            else:
                idx = randint(0, 9)
                id += string.digits[idx]
        color_list.append(id)
    print(color_list)


def list_of_rgb_colors(r: int):
    color_list = []
    for i in range(r):
        c1 = randint(0, 255)
        c2 = randint(0, 255)
        c3 = randint(0, 255)
        color_list.append(f"rgb({c1},{c2},{c3})")
    print(color_list)


def generate_colors(color_type: str, r: int):
    color_list = []
    if color_type == "hexa":
        for i in range(r):
            id: str = "#"
            for _ in range(6):
                if randint(0, 1) == 0:
                    idx = randint(0, 5)
                    id += string.ascii_letters[idx]
                else:
                    idx = randint(0, 9)
                    id += string.digits[idx]
            color_list.append(id)
    elif color_type == "rgb":
        for i in range(r):
            c1 = randint(0, 255)
            c2 = randint(0, 255)
            c3 = randint(0, 255)
            color_list.append(f"rgb({c1},{c2},{c3})")
    print(color_list)


def return_unique_nums():
    num_list = []
    while len(num_list) < 7:
        idx = randint(0, 9)
        number = string.digits[idx]
        if number not in num_list:
            num_list.append(number)
    print(num_list)


def shuffle_list(l):
    for i in range(len(l)):
        idx = randint(0, len(l) - 1)
        temp = l[i]
        l[i] = l[idx]
        l[idx] = temp
    print(l)


shuffle_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
