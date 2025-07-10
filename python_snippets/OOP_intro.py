# Class names are typically written in CamelCase, with the first letter of each
# word capitalized and no underscores. # This is a convention in Python to 
# distinguish class names from variable and function names, which are typically
# written in snake_case.


class Dog:
    """A simple dog class."""  # This is a docstring that describes the class.

# Methods in a class are defined using the def keyword, just like functions.
# __init__ is a special method called a constructor, which is called when an
# instance of the class is created. It initializes the attributes of the class.

    def __init__(self, name, age):):
# every method in a class takes at least one parameter, which is usually named
# self. This parameter refers to the instance of the class itself, allowing you 
# to access its attributes and methods. The self parameter is not explicitly
# passed when you call the method; Python automatically provides it.

#any variable that is prefixed with self. is an instance variable, which means
# it is tied to a specific instance of the class. In this case, name and age
# are instance variables that store the name and age of the dog.

# instance variables are also known as attributes or properties of the class.

"""Initialize the dog with a name and age."""
        self.name = name
        self.age = age
    def sit(self):
        """Make the dog sit."""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """Make the dog roll over."""
        print(f"{self.name} rolled over!")



# Let's create an instance of the Dog class and call its methods.
my_dog = Dog("Buddy", 3)
print(f"My dog's name is {my_dog.name} and he is {my_dog.age} years old.")
my_dog.roll_over()  # Output: Buddy rolled over!
# The instance variable name is accessed using self.name, and the instance
# variable age is accessed using self.age. This allows you to store and retrieve
# information specific to each instance of the class.
# The print statement uses an f-string to format the output, which is a convenient
my_dog.sit()  # Output: Buddy is now sitting.