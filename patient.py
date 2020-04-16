class Patient: 
    def __init__(self, social_security_number, dob, health_insurance_num, first_name, last_name, address): 
        self.__social_security_number = social_security_number
        self.__dob = dob
        self.__health_insurance_num = health_insurance_num
        self.__first_name = first_name
        self.__last_name = last_name
        self.__full_name = ""
        self.__address = address
    #first and last name should not be exposed as properties, only through full_name
    @property 
    def social_security_number(self): 
            return {self.__social_security_number}
    @property
    def full_name(self): 
        return f"{self.__first_name} {self.__last_name}"
    #address should have a getter and setter 
    @property 
    def address(self): 
        return self.__address
    @address.setter
    def address(self, new_address): 
        self.__address = new_address
    