# --------------
# Code starts here
def sep():
    print('='*30)
# Create the lists 
class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']
# Concatenate both the strings
new_class = class_1+class_2
# Append the list
print(new_class)
sep()
new_class.append('Peter Warden')

# Print updated list
print(new_class)
sep()
# Remove the element from the list
new_class.remove('Carla Gentry')

# Print the list
print(new_class)
sep()
# Create the Dictionary

courses = {'Math': 65,'English' : 70,'History': 80,'French': 70,'Science': 60}


# Slice the dict and stores  the all subjects marks in variable

print(courses)
sep()
# Store the all the subject in one variable `Total`
total = sum(courses.values())

# Print the total
print(total)
sep()
# Insert percentage formula
percentage = (total / 500) * 100
# Print the percentage

print(percentage)
sep()


# Create the Dictionary
mathematics = {'Geoffrey Hinton' :78 , 'Andrew Ng':98, 'Sebastian Raschka':65, 
               'Yoshua Bengio':50, 'Hilary Mason':70, 'Corinna Cortes':66, 'Peter Warden':75}
print(mathematics) 
sep()


# Given string


# Create variable first_name 

# Create variable Last_name and store last two element in the list
topper = max(mathematics,key= mathematics.get)

# Concatenate the string
first_name, last_name = topper.split(' ')

# print the full_name
full_name = (last_name+' '+first_name)
# print the name in upper case
certificate_name = full_name.upper()
print(certificate_name)
# Code ends here


