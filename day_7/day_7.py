# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print("Length of it_companies: ", it_companies)
it_companies.add("Twitter")
print("it_companies with twitter: ", it_companies)
it_companies.update(["Palantir", "Shipt", "Block"])
print("Added companies: ", it_companies)
print("Removing a random company: ", it_companies.pop())
# the difference between remove and discard is remove will throw an error if the value is not found, discard will not

print("\n\n Section 2\n\n")

C = A.union(B)
int_AB = A.intersection(B)
is_sub = A.issubset(B)
is_disjoin = A.isdisjoint(B)
sym_diff = A.symmetric_difference(B)

print("Join A and B: ", C)
print("A intersection B: ", int_AB)
print("is A subset of B: ", is_sub)
print("are A and B disjoint: ", is_disjoin)


del A
del B

