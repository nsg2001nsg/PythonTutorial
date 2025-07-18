# closures
# A record storing a function together with an environment
# A mapping associating each free variable of the func with the value
# A function carrying some memory with it

def outer_instruction():
    secret = "chocolate chips"

    def inner_recipe():  # closure function
        print("Using", secret)

    return inner_recipe


cook = outer_instruction()
cook()

# It lets you make customized functions that remember things without needing global variables or classes.
# A closure closes over the free variables in its environment