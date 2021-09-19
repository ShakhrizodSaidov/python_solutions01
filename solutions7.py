# Make a list of countries you know and print the list on the console
countries = ["Uzbekistan", "Kazakhstan", "Russia", "Malaysia", "Singapore", "USA"]
print (countries)

# Output the length of the list to the console
print (countries)

# Use the #sorted () function to output the list in order to the console
print (sorted (countries))

# Use #sorted () to display the list in reverse order on the console
print (sorted (countries, reverse = True))

#Release the original list on the console
print (countries)

# Use the #reverse () method to start the list from the back
countries.reverse ()
print (countries)

# Using the #sort () method, drag the list to the console first in alphabetical order and then in reverse alphabetical order.
countries.sort ()
print (countries)
countries.sort (reverse = True)
print (countries)

# Make a list of even numbers from # 120 to 1200
numbers = list (range (120,1200))

# Calculate the sum of the numbers in the list and output it to the console
print (sum (numbers))

# Calculate the difference between the largest and smallest number in the list and output it to the console
print (max (numbers) -min (numbers))

# Count the number of items in the list
print (len (numbers))

# Output 20 values ​​from the beginning, middle, and end of the list to the console
print (numbers [: 20])
print (numbers [-20:])
print (numbers [530: 550])

# Make a list of #foods and include any 5 dishes you want
dishes = ['osh', 'somsa', 'norin', 'shashlik', 'kazankabob']

# Copy the dishes to the new list called #breakfast
breakfast = dishes [:]

#Leave only breakfast cereals on the new list, and add 2 more dishes
breakfast.remove ('norin')
breakfast.remove ('shashlik')
breakfast.remove ('kazankabob')
breakfast.append ('bread and cream')
breakfast.append ('hot bread')

#Bring both lists (dishes and breakfast) to the console
print (dishes)
print (breakfast)

# #Change the breakfast list above to an unchanging list and try setting the breakfast [0] = "cream and bread".
# breakfast = tuple (breakfast)
# breakfast [0] = "cream and bread"