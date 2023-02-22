katz_deli = []

def line(list):
    if len(list) == 0: 
        print("The line is currently empty.")
    else:
        string = "The line is currently:"
        for index, name in enumerate(list):
            string += f" {index + 1}. {name}"
        print(string)

def take_a_number(list, name):
    list.append(name)
    print(f"Welcome, {name}. You are number {len(list)} in line.")


def now_serving(list):
    if len(list) == 0:
        print("There is nobody waiting to be served!")
    else: 
        print(f"Currently serving {list[0]}.")
        list.pop(0)
