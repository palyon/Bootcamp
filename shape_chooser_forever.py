def paint():
    print("What shape do you wish to print?")
    print("""
    1 for Triangle
    2 for Square
    3 for "Circle"
        """)
    user_shape = int(raw_input("Choose? "))
    chosenShape(user_shape)


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
    design = "*"
    for idx in range(diameter - 1):
        print((diameter - idx) * ' ' + (2 * idx + 1) * design)
    for idx in range(diameter - 1, -1, -1):
        print((diameter - idx) * ' ' + (2 * idx +1) * design)

def paintAgain():
    while True:
        paint_again = raw_input("Paint again (yes / no)? ")
        if paint_again == "yes":
            paint()
        if paint_again == "no":
            print "Bye!"
            break
        else:
            whatWasThat()

def whatWasThat():
    while True:
        paint_again = raw_input("What was that? Paint again (yes / no)? ")
        if paint_again == "yes":
            paint()
        if paint_again == "no":
            print "Bye!"
            break
        else:
            whatWasThat()

paint()
paintAgain()

#def whatWasThat():
    #paint_again = raw_input("Paint again (yes / no)? ")
    # paint_again = paint_again.lower()
    # if paint_again == "yes":
    #     paint_again = True
    # elif paint_again == "no":
    #     paint_again = False
    #     print("Bye!")
    # else:
    #     paint_again != "yes" or paint_again != "no"
    #     paint_again = raw_input("I'm sorry, what? Do you want to paint again (yes / no)? ")

#def play_again():
#     whatWasThat()
#     if paint_again == True:
#         (paint)
#
# paint()
# paint_again = raw_input("Paint again (yes / no)? ")
# #whatWasThat(paint_again)
# play_again()
# # paint_again = True
#
# while paint_again == True:
#     paint()
#
# whatWasThat(paint_again)
#
# if paint_again == "yes":
#     paint_again = True
# if paint_again == "no":
#     paint_again = False
#     print("Bye!")
