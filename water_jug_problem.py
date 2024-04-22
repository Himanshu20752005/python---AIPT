def display():
    print("\nSelect the rule to be applied")
    print("Rule 1: Fill the 4-gallon jug")
    print("Rule 2: Fill the 3-gallon jug")
    print("Rule 3: Pour some water out of the 4-gallon jug")
    print("Rule 4: Pour some water out of 3-gallon jug.")
    print("Rule 5: Empty the 4-gallon jug on the ground")
    print("Rule 6: Empty the 3-gallon jug on the ground")
    print("Rule 7: Pour water from the 3-gallon jug into the 4-gallon jug until the 4-gallon jug is full")
    print("Rule 8: Pour water from the 4-gallon jug into the 3-gallon jug until the 3-gallon jug is full.")
    print("Rule 9: Pour all the water from the 3-gallon jug into the 4-gallon jug.")
    print("Rule 10: Pour all the water from the 4-gallon jug into the 3-gallon jug")
    print("Rule 11: Pour the 2-gallon water from 3-gallon jug into the 4-gallon jug.")
    print("Rule 12: Empty the 2-gallon in the 4-gallon jug on the ground. \n")
def rule_applied(rule ,x,y):
    if rule == 1:
        x=4
        return x,y
    elif rule == 2:
        y=3
        return x,y
    #elif rule == 3:
    #elif rule == 4:

    elif rule == 5:
        x=0
        return x,y
    elif rule == 6:
        y=0
        return x,y
    elif rule == 7:
        y = y - (4-x)
        x = 4
        return x,y
    elif rule == 8:
        x = x-(3-y)
        y=3
        return x,y
    elif rule == 9:
        x=x+y
        y=0
        return x,y
    elif rule == 10:
        y = y+x
        x=0
        return x,y
    elif rule == 11:
        x = x+2
        y=0
        return x, y
    elif rule == 12:
        y = y+2
        x=0
        return x,y

x = y = 0
display()
while True :
    if x == 2:
        print("Goal achieved")
        break
    else:
        rule = int(input())
        x,y = rule_applied(rule ,x,y)
        print("jug_4l : ", x, "jug_3l : ", y)







