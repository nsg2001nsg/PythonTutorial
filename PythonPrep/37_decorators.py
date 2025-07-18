# Decorators

def milk_decorator(milk):
    def coffee_wrapper():  # does some extra functions on top of the base function
        steamed_milk = milk()
        coffee = " + espresso"
        return steamed_milk + coffee

    return coffee_wrapper


@milk_decorator  # does milk_decorator(make_milk) whenever we call make_milk()
def make_milk():
    return "steamed milk"


# # or
# make_latte = milk_decorator(make_milk)
# make_latte()

make_latte = make_milk()
print(make_latte)
