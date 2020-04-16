from student import Student
from patient import Patient

sofia = Student()

sofia.first_name = "Sofia"
sofia.last_name = "Candiani"
sofia.age = 21
sofia.cohort = 38

print(sofia)

#patient 

cashew = Patient(
    "097-23-1003", "08/13/92", "7001294103",
    "Daniela", "Agnoletti", "500 Infinity Way")

 # This should not change the state of the object
# cashew.social_security_number = "838-31-2256"

# Neither should this
cashew.date_of_birth = "01-30-90"

# But printing either of them should work
print(cashew.social_security_number)   # "097-23-1003"

# These two statements should output nothing
# print(cashew.first_name)
# print(cashew.last_name)

# But this should output the full name
print(cashew.full_name)   # "Daniela Agnoletti"

