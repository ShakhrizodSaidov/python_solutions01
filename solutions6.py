names = ['Ali', 'Vali', 'Hasan', 'Husan', "G'ani"]
print ("Hello" + names [0] + "How are you?")
print ( f"{names [2]} and {names [3]} twins")
print (names [-1] + "rolled the wheel")

numbers = [22, -58.2, 34.0, 67, 1983, 123_456_678_000, 112.4]
print (numbers)

numbers [0] = numbers [0] + numbers [-1]
numbers [1] = -67.8
numbers [4] = numbers [4] + 37
del numbers [5]
print (numbers)

t_shaxslar = ['Amir Temur', 'Imam Bukhari', 'Napoleon']
z_shaxslar = ['Bill Gates', 'Elon Musk', 'Doasnald Trump']

print (f"\ nI'm from historical figures {t_shaxslar.pop (1)}, \ n \
and modern ones with {z_shaxslar.pop (0)} \ n \
I would like to chat \ n ")

friends = []
friends.append ('John')
friends.append ('Alex')
friends.append ('Danny')
friends.append ('Sobirjon')
friends.append ('Vanya')
print (friends)

friends.remove ('John')
friends.remove ('Alex')
print (friends)

friends.append ('Hasan')
friends.insert (0, 'Husan')
friends.insert (2, 'Ivan')
print (friends)

guests = []
guests.append (friends.pop (3))
guests.append (friends.pop (-1))
guests.append (friends.pop (0))
print ("\ nGuests:", guests)