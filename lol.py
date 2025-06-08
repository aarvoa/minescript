# modify these names to be snake_case
shoe_size = 5
my_age = 13
def get_my_age():
    print("i am working")
    return my_age

def get_my_age1():
    print("i am 1")
    return my_age

def get_my_age2():
    print("i am 2")
    name = "aarav"

    return my_age

def get_things():
    print("egg,milk and cornflakes")

def special():
    print("naan and butter chicken")

def starters():
    print("mango lassi")

print('welcome to aaravs cafe')
menu = input("what would you like?")

if menu == "special":
    special()
elif menu == "starters":
    starters()
else:
    get_things()


