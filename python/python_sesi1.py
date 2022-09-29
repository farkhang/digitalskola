## sequential
x = 10
y = 20
r = x*y
print(r)

## conditional 1
z = 1235
if z % 2 == 0:
    print("z habis dibagi 2")
elif z % 3 == 0:
    print("z habis dibagi 3")
else:
    print("z ga habis dibagi 2 dam 3")

## conditional 2
name = "DOnGO"
species = "dog"

if species == "dog":
    print(name.lower(), "barks")
elif species == "cat":
    print(name.lower(), "meow")
elif species == "duck":
    print(name.lower(), "quack")
else:
    print("I don't know")