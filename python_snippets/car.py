# Lets start working with classes and instances

class Car:
    ''' A simple car excercise'''
    def __init__(self, make, model, year):
        ''' initialize attributes for the car'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # defuine a default value for the odometer reading
    def read_odometer(self):
        ''' print the current odometer reading'''
        print(f"This car has {self.odometer_reading} miles on it.")

    def get_description(self):
        ''' return a neatly formatted descriptive name'''
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
### Modifying attributes by creating method
    def update_odometer(self, mileage):
        '''This method updates the odometer reading  it is the second way to modify the value of an attribute'''
        ''' set the odometer reading to the given value'''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        '''This method increments the odometer reading by a given amount'''
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")

###  Adding this method to witness overriding a method in the child
    def fill_gas_tank(self):
        '''This method simulates filling the gas tank'''
        print("The gas tank is now full.")


##### Adding the battery class to the car class
# This is a class that will be used as an attribute in the ElectricCar class.
# Moved this above the class definition to avoid confusion and allow the class to be defined first

class Battery:
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 240
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go approximately {range} miles on a full charge.")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        # Call the parent class's __init__ method  super() allows us to call the parent class's methods and attributes
        # In this case, we are initializing the make, model, and year attributes from the parent class
        # The super() function returns a temporary object of the superclass that allows us to call its methods and access its attributes
        
        super().__init__(make, model, year)  # initialize the parent class attributes
        self.battery = Battery()  # Create an instance of the Battery class as an attribute of ElectricCar

    # Here we comment out our original method and override it    
    # def describe_battery(self):
    #    """Print a statement describing the battery size."""
    #     print(f"This car has a {self.battery_size}-kWh battery.")
    def fill_gas_tank(self):
        """Override the fill_gas_tank method to indicate that electric cars don't have gas tanks."""
        print("This car doesn't have a gas tank!")