# Exercise 4
## Objective: create a function dog(); when run, this function should return "poodle" 

def dog(type):
    if type.lower() == "poodle":
        return type
    else:
        return None

print(dog("poodle"))