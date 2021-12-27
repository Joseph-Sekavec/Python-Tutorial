# Here we show how to make a class and instantiate an object

# For classes we use a constructor by using __init__ (self, ...) where self is an implicit keyword like "this" in c++
# __init__ is the name of our constructor, much like the class name in c++. All variables after "self" are values that
# we pass upon intantation ex: var_vame = class_name(parameter, parameter1, parameter2,...,parameter_n).

class student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
    # __init__(self,...) defines/initializes attributes student has
