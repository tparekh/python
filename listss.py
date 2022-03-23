vegan_no_nos = ['beef','chicken','fish','milk','eggs']

pie_ingredients = ['flour', 'apples', 'sugar', 'eggs', 'salt']

for item in pie_ingredients:
    if item in vegan_no_nos:
        print(f"OH NO, CANNOT EAT {item}! IT'S NOT VEGAN!")
    else:
        print(f"YUM, I love {item}!")

        