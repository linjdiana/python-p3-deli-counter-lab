katz_deli = []

def line(names):
    if len(names) == 0:
        string = "The line is currently empty."
    else:
        string = "The line is currently:"
        i = 0
        for name in names:
            i += 1
            string += f" {i}. {name}"
    print(string) 

line(["A", "Brad"])

def take_a_number(names, name):
    names.append(name)
    print(f"Welcome, {name}. You are number {len(names)} in line.")

# take_a_number(["Ada", "Grace"], "Ada")

def now_serving(names):
    if len(names) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {names[0]}.")
        names.pop(0)
    