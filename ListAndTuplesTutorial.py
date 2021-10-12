# #+INDEX -    0       1      2
# courses = ["BSIT","BSCS","BLIS","BA","ACS","BSCS","BSIT"]
#
# #Range selection
# print(courses[1:5])
#
# #Changing index value
# courses[0] = "Accountancy"
# print(courses)
#
# #Printing the length of the list
# print(len(courses))
#
# #Printing the number of duplicates from the list
# print(courses.count("BSIT"))
#
# #Adding values from the list
# courses.append("Business")
# courses.append("PE")
# courses.append("Health")
# print(courses)
#
# #Inserting index from the list
# courses.insert(1,"Family Planning")
# print(courses)
#
# #Deleting specified item from the list
# courses.remove("Accountancy")
# print(courses)
#
# #Deleting specified index from the list
# courses.pop(0)
# print(courses)
#
# #Delete default end from the list
# courses.pop()
# print(courses)
#
# #delete the whole list
# del courses
# print(courses)
#
#
# #Clear the indexes from the list
# test = ["Math", "English"]
# test.clear()
# print(test)

# #Copy lists from another lists
# listOne = ["BSIT", "BSCS", "BLIS"]
# listOne.pop()
# listTwo = listOne.copy()
# print(listTwo)

# #Combining Lists by adding
# listOne = ["BSIT","BSCS","BLIS"]
# listTwo = ["Hatdog","CheeseDog"]
# listThree = listOne + listTwo
# print(listThree)

# #Combining Lists by adding(using extend)
# listOne = ["BSIT","BSCS","BLIS"]
# listTwo = ["Hatdog","CheeseDog"]
# listOne.extend(listTwo)
# print(listOne)

