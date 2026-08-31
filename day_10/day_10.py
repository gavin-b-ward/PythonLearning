for i in range(11):
    print(i)

print("\n\n")

i = 0 
while i < 11 :
    print(i)
    i += 1

print("\n\n")

for i in range(1, 8, 1):
    print("#" * i)

for i in range(16):
    for j in range(16): 
        if i % 2 and j % 2:
            print("#", end="")
        else:
            print(" ", end="")
    print("\n", end="")
