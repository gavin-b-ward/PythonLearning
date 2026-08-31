etpl = ()
etpl = tuple()
brothers = tuple(("shane", "austin"))
sister = ("alexa",)
print(sister)
siblings = brothers + sister
print("Num siblings: ", len(siblings))
family_members = siblings + ("darla", "ken")
print(family_members)
*b, s, m, d  = family_members
print(b)
print(s)
print(m)
print(d)

fruits = ("apple", "banana", "orange")
vegatables = ("broccoli", "cabbage")
meats = ("chicken breast", "ribeye", "pork belly")
food_stuff_tp = fruits + vegatables + meats
food_stuff_lt = list(food_stuff_tp)
middle = food_stuff_tp[len(food_stuff_tp) // 2: len(food_stuff_tp) // 2 + 2]

print(middle)

