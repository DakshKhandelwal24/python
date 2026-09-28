# for i in range (1,6) :
#     name = input(f"Enter username - {i} :") 
#     count1 = count2 = 0  
#     for j in name :
#         if  j.isdigit() :
#             count1 += 1
#         if j == chr(95) :
#             count2 += 1
#     if chr(33) <= j <= chr(47) or chr(58) <= j <= chr(64) or chr(91) <= j <= chr(96) :
#         print("Invalid")
#     elif count1 > 0 and count2 > 0 :
#         print("Needs to improvement.")
#     else :
#         print("Valid")
#     print(f"Length of name is : {len(name)}")
#     print(f"First letter of name is : {name[0]}")
#     print(f"Total digits is/are : {count1}")
#     print(f"Total underscores used : {count2}")


# ## Question = 12
# count1 = count2 = 0
# sentence = input("Enter a sentence :").lower()
# print(f"Vowel frequency of (a) - {sentence.count("a")}")
# print(f"Vowel frequency of (e) - {sentence.count("e")}")
# print(f"Vowel frequency of (i) - {sentence.count("i")}")
# print(f"Vowel frequency of (o) - {sentence.count("o")}")
# print(f"Vowel frequency of (u) - {sentence.count("u")}")
# for i in sentence :
#     for j in i :
#         if j in "aeiou":
#             count1 += 1
#         if j in "bcdfghjklmnpqrstvwxyz":
#             count2 += 1
# if count1 > count2 :
#     print(f"Vowel Wins .")
# elif count2 > count1 :
#     print(f"Consonants wins .")
# else :
#     print(f"Draw !!")


# ## Question = 13
# bill1 = bill2 = bill3 = bill4 = 0
# for i in range (1,7) :

#     unit = int(input("Enter unit usage by costomer-{i} :"))
#     if unit <= 100 :
#         bill1 = unit*5
#         print(f"Bill is- {bill1}")
#     elif 100 < unit <= 200 :
#         bill1 = 100*5
#         bill2 = (unit - 100)*7
#         print(f"Bill is- {bill1 + bill2}")
#     elif 200 < unit <= 400 :
#         bill1 = 100*5
#         bill2 = 100*7
#         bill3 = (unit - 200)*10
#         print(f"Bill is- {bill1 + bill2 + bill3}")
#     else :
#         bill1 = 100*5
#         bill2 = 100*7
#         bill3 = 200*10
#         bill4 = (unit - 400)*15
#         print(f"Bill is- {bill1 + bill2 + bill3 + bill4}")









# ## Question = 16
# password = input("Enter a password :")
# count1 = count2 = count3 = count4 = 0
# for i in password :
#     if i.islower() :
#         count1 += 1
#     elif i.isupper() :
#         count2 += 1
#     elif i.isdigit() :
#         count3 += 1
#     else :
#         count4 += 1
# a = len(password)
# print(f"The percentage of lower is - {(count1 / (a))*100}%")
# print(f"The percentage of upper is - {(count2 / (a))*100}%")
# print(f"The percentage of digit is - {(count3 / (a))*100}%")
# print(f"The percentage of special characters is - {(count4 / (a))*100}%")

# if count1 > 1 and count2 > 1 and count3 > 1 and count4 > 1 :
#     print("Strong password.")
# elif count1 > 1 and count2 > 1 and count3 < 1 and count4 < 1 :
#     print("Weak password.")
# else :
#     print("Medium password.")

# ## Question = 17
# for i in range (1,6):
#     name = (input(f"Enter name of student-{i} : ")).lower()
#     marks = int(input(f"Enter marks of students-{i} :"))
#     if 75 < marks <= 100 :
#         print("A")
#     elif 50 <= marks <= 75 :
#         print("B")
#     else:
#         print("fail")
#     count = count1 = 0
#     for j in name :
#         if j in "aeiou" :
#             count += 1
#         elif j in "bcdfghjklmnpqrstvwxyz" :
#             count1 += 1
#     print(f"Vowels in name is/are - :{count}"  )
#     print(f"Total characters in name are - :{len(name)}")
#     if count > count1 :
#         print(f"Vowels are more than consonents in this name ")
#     elif count1 > count :
#         print(f"consonents are more than vowel in this name ")
#     else :
#         print(f"vowel and consonents are equal :")
#################################### maximum mark of student ##################################################


## Question = 18
# for i in range (1,8):
#     print()
 