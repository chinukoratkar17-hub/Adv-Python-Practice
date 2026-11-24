# Generators in Python

def count_numbers():
    for i in range(1, 6):
        yield i

for number in count_numbers():
    print(number)
