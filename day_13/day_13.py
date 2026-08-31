numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

f_num = [i for i in numbers if i <= 0]
print(f_num)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flattened = [i for row in list_of_lists for i in row]
print(flattened)

tuple_list = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]

print(tuple_list)

countries = [[("Finland", "Helsinki")], [("Sweden", "Stockholm")], [("Norway", "Oslo")]]

country_dict = [{key, val} for i in countries for key, val in i]

names = [
    [("Asabeneh", "Yetayeh")],
    [("David", "Smith")],
    [("Donald", "Trump")],
    [("Bill", "Gates")],
]

str_name = [f"{key} {val}" for row in names for key, val in row]
print(str_name)
