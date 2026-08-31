empty = []
l = list((1, 2, 3, 4, 5))
print(len(l))
print(f"{l[0]}, {l[2]}, {l[-1]}")
mixed_data_types = list(("gavin", 21, 6.4, "unmarried", "145 silk leaf dr")) 

it_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(", ")
print(it_companies)

print(f"Num Companies: {len(it_companies)}")
print(f"First {it_companies[0]}, Middle {it_companies[len(it_companies)//2]} , Last {it_companies[-1]}")
it_companies[0] = "palantir_inshallah"
print(it_companies)
print("#; ".join(it_companies))
print(it_companies[0:3])
print(it_companies[-3:])
it_companies.pop(len(it_companies) // 2)
print(it_companies)


