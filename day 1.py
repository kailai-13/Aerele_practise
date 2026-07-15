#squeres
a=[1,2,3,4,5,6]
squeres=[i*i for i in a]

print(squeres)

#filter

evens=[i for i in a if i%2==0]

print(evens)

#context manager

with open("students.txt") as f:
    for line in f:
        print(line.strip())
#java style

names = ["Alice", "Bob", "Charlie"]

lengths = []

for i in range(len(names)):
    lengths.append(len(names[i]))

print(lengths)

#pythonic
lens=[len(i) for i in names]

#enumerate

for i,v in enumerate(a):
    print(f"index: {i} and value: {v}")

l=[1,2,3,4,5]
r=[1,4,9,16,25]

for a,b in zip(l,r):
    print(f"{a} and {b}")
    