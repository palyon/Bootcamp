def chosenShape(user_shape):
    if user_shape == 1:
        height = int(raw_input("What is the height of the triangle? "))
        triangle(height)
    if user_shape == 2:
        width = int(raw_input("Width? "))
        height = int(raw_input("Height? "))
        square(width, height)
    if user_shape == 3:
        diameter = int(raw_input("What is the diameter? "))
        kindaCircle(diameter)

def triangle(height):
    design = '*'
    true_height = height * 2
    for iterations in range(1, true_height, 2):
        print(' ' * (height - 1) + design * iterations)
        height = height - 1

def square(height, width):
    design = '*'
    true_height = (design + (width - 2)*' ' + design)
    print design * width
    for iterations in range(height):
        print true_height
    print design * width

def kindaCircle(diameter):
    for idx in range(diameter - 1):
        print((diameter - idx) * ' ' + (2 * idx + 1) * '*')
    for idx in range(diameter - 1, -1, -1):
        print((diameter - idx) * ' ' + (2 * idx +1) * '*')

print("What shape do you wish to print?")
print("""
1 for Triangle
2 for Square
3 for "Circle"
    """)
user_shape = int(raw_input("Choose? "))

chosenShape(user_shape)

print("Bye!")
