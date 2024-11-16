prizes = [5, 10, 50, 100, 1000]

dbl_prizes = []
for prize in prizes:
    dbl_prizes.append(prize * 2)
print(dbl_prizes)

# the comperhension way
dbl_prizes = [prize*2 for prize in prizes]
print(dbl_prizes)


# squaring numbers
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_even_nums = []

for num in nums:
    if (num ** 2) % 2 == 0:
        squared_even_nums.append(num ** 2)
print(squared_even_nums)


# the comperhension way
squared_even_nums = [num ** 2 for num in nums if (num ** 2) % 2 == 0]
print(squared_even_nums)

# List Comperhension
even_number = [x for x in range(10) if x % 2 == 0]
print(even_number)

# Set Comprehension
squared_numbers = {x**2 for x in range(10)}
print(squared_numbers)


# Dictionary comprehension
squared_dict = {x: x**2 for x in range(10)}
print(squared_dict)
