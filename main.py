# Welcome to my city generator

import random

exit = False

vowels = ["A", "E", "I", "O", "U"]
cons = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "R", "S", "QU", "T", "V", "Y", "Z"]
titles = ["Baron", "Viscount", "Earl", "Marquess"]


while exit == False:

    city_size = input("Please, choose a size for your town: big, medium, small or exit. ")
    if city_size == "exit":
        print("Goodbye!")
        exit = True

    if city_size == "big" or city_size == "medium" or city_size == "small":
        def city_nom():
            random_number = random.randint(2, 4)
            name=""
            for x in range(random_number):
                random_vowel = random.choice(vowels)
                random_cons = random.choice(cons)
                name = name + random_cons + random_vowel
            return name

    # Number of habitants

        def city_population():
            if city_size == "big":
                random_pop = random.randint(6001, 25000)
                name_pop="This city has " + str(random_pop) + " Habitants"
            elif city_size == "medium":
                random_pop = random.randint(1001, 6000)
                name_pop="This town has " + str(random_pop) + " Habitants"
            elif city_size == "small":
                random_pop = random.randint(100, 1000)
                name_pop="This village has " + str(random_pop) + " Habitants"
            return name_pop

        def city_govern():
            if city_size == "big":
                random_gov = random.choice(titles)
                name_gov="This city is under the jusrisdiction of the " + random_gov + " of " + str.capitalize(city_nom())
            elif city_size == "medium":
                random_gov = random.choice(titles)
                name_gov="This town is under the jusrisdiction of the " + random_gov + " of " + str.capitalize(city_nom())
            elif city_size == "small":
                random_gov = random.choice(titles)
                name_gov="This village is under the jusrisdiction of the " + random_gov + " of " + str.capitalize(city_nom())
            return name_gov


        print (city_nom())
        print(city_population())
        print(city_govern())

    elif city_size != "big" or city_size != "medium" or city_size != "small" or city_size != "exit":
        print("Try again and choose a size")




