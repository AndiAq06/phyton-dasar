# FUNCTION

def greet():
    print('Hello, Wolrd')


greet()

# Parameters


def greet(name='ryu', time="morning"):
    print(f'Good {time} {name}, hope you are well?')


greet("Andi", "morning")
greet(name='Niki')


# Something more useful
def factorial(num):
    ans = num
    i = 1
    while i < num:
        ans = ans * (num - i)
        i += 1
    print(ans)


number = int(input('Calculate factorial of: '))
factorial(number)

#  Return Statement


def areaCirc(radius):
    return 3.142 * radius * radius


def volCyl(area, length):
    return area * length


rad = int(input('Enter a circle radius (m): '))
len = int(input('Enter a cylinder length (m): '))
vol = volCyl(areaCirc(rad), len)


print(f'The volume of the cylinder is {vol} cubed metres')
