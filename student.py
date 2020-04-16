class Student: 
    def __init__(self): 
        # Initializing with private properties
        self.__first_name = ""
        self.__last_name = "" 
        self.__age = 0
        self.__cohort = 0
        self.__full_name = ""

    @property #getter 
    def first_name(self): # acts as a public property, is actually a function
        return self.__first_name
    @first_name.setter #setter
    def first_name(self, new_first_name):
        if type(new_first_name) is str:
            self.__first_name = new_first_name
        else:
            raise TypeError('Please provide a string')
    @property
    def last_name(self): 
        return self.__last_name
    @last_name.setter 
    def last_name(self, new_last_name): 
        if type(new_last_name) is str: 
            self.__last_name = new_last_name
        else: 
            raise TypeError('Please provide a string')
    @property 
    def age(self): 
        return self.__age
    @age.setter 
    def age(self, new_age): 
        if type(new_age) is int: 
            self.__age = new_age
        else: 
            raise TypeError('Please provide an integer')
    @property 
    def cohort(self): 
        return self.__cohort
    @cohort.setter 
    def cohort(self, new_cohort):
        if type(new_cohort) is int: 
            self.__cohort = new_cohort 
        else: 
            raise TypeError('Please provide an integer')
    @property
    def full_name(self): 
        return (f"{self.first_name} {self.last_name}")

    def __str__(self):
        return f"{self.full_name} is {self.age} years old and is in cohort {self.cohort}"

#Mike Ellis is 35 years old and is in cohort 39


