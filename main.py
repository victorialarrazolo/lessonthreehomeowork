# Victoria Larrazolo Lesson 3 Hands on
#Part One

list_of_names= ["kurt", "david", "Katherine"]
print(list_of_names)
names= []
for names in list_of_names:
    print("where is", names, "today?")

#Part Two
my_favorite_cars=["Ford", "Audi", "Dodge"]
my_favorite_flowers= ["Birds Of Paridise", "Gardenias", "Sunflowers", "Roses"]
my_favorite_animals=["cat", "dog", "Humming Bird", "Lambs", "Lions"]

my_favorite_things= my_favorite_cars + my_favorite_flowers + my_favorite_animals
print(my_favorite_things)

for thing in my_favorite_things:
    if len(thing) % 2 == 0:
        print(thing)


number_range = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for number in number_range:
    if number % 3 == 0 and number % 5 == 0:
        print('ZipZap')
    elif number % 3 == 0:
        print('Zip')
    elif number % 5 == 0:
        print('Zap')
    else:
        print(number)