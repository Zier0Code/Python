n = int(input("insert a number from 1-10: "))

if n < 10:
    for i in range(n):
        print(i)
        # hello

names = []
for i in range(2):
    name = input(f"Add a Name")
    print(f"{name} is no. {i + 1} name on the list. ")
    names.append(name)

print("List of Names: ")

for name in names:
    print(name)