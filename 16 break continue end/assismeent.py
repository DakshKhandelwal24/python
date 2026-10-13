# # Q1. Stop Before Printing 5

# for i in range(1, 8):
#     if i == 5:
#         break
#     print(i)
# print("Finished")

# # Output:
# # 1
# # 2
# # 3
# # 4
# # Finished


# # Q2. Stop at the First Vowel

# word = "skyline"

# for ch in word:
#     if ch in "aeiou":
#         break
#     print(ch)

# # Output:
# # s
# # k
# # y


# # Q3. break in a while Loop

# n = 2

# while n <= 10:
#     print(n)
#     if n == 6:
#         break
#     n += 2

# # Output:
# # 2
# # 4
# # 6


# # Q4. Stop at a Target Number

# limit = int(input("Enter limit: "))

# for i in range(1, limit + 1):
#     if i == 7:
#         break
#     print(i, end=" ")

# # Input: 10
# # Output:
# # 1 2 3 4 5 6


# # Q5. Find the First Matching Character

# word = input("Enter string: ")
# target = input("Enter target character: ")

# for ch in word:
#     print(ch)
#     if ch == target:
#         break

# # Input:
# # computer
# # p
# # Output:
# # c
# # o
# # m
# # p


# # Q6. Stop at a Negative Number

# numbers = list(map(int, input("Enter numbers: ").split()))

# for num in numbers:
#     if num < 0:
#         break
#     print(num, end=" ")

# # Input: 4 8 2 -3 9
# # Output:
# # 4 8 2


# # Q7. break Only Exits the Inner Loop

# for row in range(1, 4):
#     for col in range(1, 5):
#         if col == 3:
#             break
#         print(row, col)

# # Output:
# # 1 1
# # 1 2
# # 2 1
# # 2 2
# # 3 1
# # 3 2

# # Explanation:
# # break exits only the inner loop.
# # The outer loop continues with the next row.


# # Q8. Search a Word

# sentence = input("Enter sentence: ")
# target = input("Enter target word: ")

# for word in sentence.split():
#     if word == target:
#         print("Found")
#         break
# else:
#     print("Not found")

# # Input:
# # python makes coding fun
# # coding
# # Output:
# # Found


# # Q9. Skip Number 4

# for i in range(1, 7):
#     if i == 4:
#         continue
#     print(i)

# # Output:
# # 1
# # 2
# # 3
# # 5
# # 6


# # Q10. Skip Vowels

# for ch in "education":
#     if ch in "aeiou":
#         continue
#     print(ch, end="")

# # Output:
# # dctn


# # Q11. continue in a while Loop

# n = 0

# while n < 5:
#     n += 1
#     if n == 3:
#         continue
#     print(n)

# # Output:
# # 1
# # 2
# # 4
# # 5


# # Q12. Print Numbers That Are Not Multiples of 3

# n = int(input("Enter n: "))

# for i in range(1, n + 1):
#     if i % 3 == 0:
#         continue
#     print(i, end=" ")

# # Input: 8
# # Output:
# # 1 2 4 5 7 8


# # Q13. Remove a Chosen Character from Display

# word = input("Enter string: ")
# target = input("Enter character: ")

# for ch in word:
#     if ch == target:
#         continue
#     print(ch, end="")

# # Input:
# # mississippi
# # s
# # Output:
# # miippi


# # Q14. Print Only Passing Marks

# marks = list(map(int, input("Enter marks: ").split()))

# for mark in marks:
#     if mark < 40:
#         continue
#     print(mark, end=" ")

# # Input: 25 40 75 32 90
# # Output:
# # 40 75 90


# # Q15. continue Does Not Skip the Whole Loop

# for i in range(1, 5):
#     if i == 2:
#         continue
#     print("A", i)
#     print("B", i)

# # Output:
# # A 1
# # B 1
# # A 3
# # B 3
# # A 4
# # B 4


# # Q16. Fix the Infinite Loop

# n = 0

# while n < 5:
#     n += 1
#     if n == 3:
#         continue
#     print(n)

# # Output:
# # 1
# # 2
# # 4
# # 5


# # Q17. Count Non-Vowel Characters

# word = input("Enter word: ")
# count = 0

# for ch in word:
#     if ch in "aeiou":
#         continue
#     count += 1

# print(count)

# # Input: education
# # Output:
# # 4


# # Q18. Normal Completion

# for i in range(1, 4):
#     print(i)
# else:
#     print("Done")

# # Output:
# # 1
# # 2
# # 3
# # Done


# # Q19. Completion After continue

# for i in range(1, 5):
#     if i == 2:
#         continue
#     print(i)
# else:
#     print("Completed")

# # Output:
# # 1
# # 3
# # 4
# # Completed


# # Q20. Completion After break

# for i in range(1, 5):
#     if i == 3:
#         break
#     print(i)
# else:
#     print("Completed")

# print("Outside loop")

# # Output:
# # 1
# # 2
# # Outside loop


# # Q21. Empty Iterable

# for item in []:
#     print("Inside")
# else:
#     print("Else block")

# # Output:
# # Else block


# # Q22. Search for a Number

# numbers = list(map(int, input("Enter numbers: ").split()))
# target = int(input("Enter target: "))

# for num in numbers:
#     if num == target:
#         print("Found")
#         break
# else:
#     print("Not found")

# # Input:
# # 4 8 12 16
# # 12
# # Output:
# # Found


# # Q23. Check Whether a Character Exists

# word = input("Enter string: ")
# target = input("Enter character: ")

# for ch in word:
#     if ch == target:
#         print("Character exists")
#         break
# else:
#     print("Character missing")

# # Input:
# # programming
# # g
# # Output:
# # Character exists


# # Q24. Find the First Divisor

# n = int(input("Enter number: "))

# for i in range(2, n):
#     if n % i == 0:
#         print("Not prime")
#         break
# else:
#     print("Prime")

# # Input: 7
# # Output:
# # Prime

# # Input: 12
# # Output:
# # Not prime

# # Input: 2
# # Output:
# # Prime


# # Q25. Trace the else

# values = [2, 4, 6, 8]

# for value in values:
#     if value % 2 != 0:
#         print("Odd found")
#         break
# else:
#     print("All are even")

# # Output:
# # All are even


# # Q26. Does else Run?

# # Case A

# for x in range(3):
#     continue
# else:
#     print("A")

# # Output:
# # A
# # Explanation: continue does not stop the loop.


# # Case B

# for x in range(3):
#     break
# else:
#     print("B")

# # Output:
# # No output
# # Explanation: break prevents the else block.


# # Case C

# for x in range(0):
#     print(x)
# else:
#     print("C")

# # Output:
# # C
# # Explanation: An empty iterable completes normally.


# # Q27. Find the First Repeated Character

# word = input("Enter string: ")

# for i in range(len(word)):
#     count = 0

#     for ch in word:
#         if ch == word[i]:
#             count += 1

#     if count >= 2:
#         print(word[i])
#         break
# else:
#     print("No repeated character")

# # Input: lamp
# # Output:
# # No repeated character

# # Input: level
# # Output:
# # l

# # Input: abcded
# # Output:
# # d


# # Q28. pass Inside a Loop

# for i in range(1, 4):
#     if i == 2:
#         pass
#     print(i)

# # Output:
# # 1
# # 2
# # 3


# # Q29. Empty if Block

# x = 10

# if x > 5:
#     pass

# print("Finished")

# # Output:
# # Finished


# # Q30. pass in a Loop Body

# for letter in "cat":
#     pass

# print("Loop ended")

# # Output:
# # Loop ended


# # Q31. Create a Placeholder for Future Work

# for i in range(1, 6):
#     if i % 2 == 0:
#         pass
#     print(i)

# # Output:
# # 1
# # 2
# # 3
# # 4
# # 5

# # Explanation:
# # pass does nothing, so even numbers are still printed.


# # Q32. Incomplete Menu Option

# choice = int(input("Enter choice: "))

# if choice == 1:
#     print("Option 1 selected")
# elif choice == 2:
#     pass
# else:
#     print("Unknown option")

# print("Program closed")

# # Input: 1
# # Output:
# # Option 1 selected
# # Program closed

# # Input: 2
# # Output:
# # Program closed

# # Input: 9
# # Output:
# # Unknown option
# # Program closed


# # Q33. Compare pass and continue

# # Program A

# for i in range(1, 5):
#     if i == 3:
#         pass
#     print(i)

# # Output:
# # 1
# # 2
# # 3
# # 4


# # Program B

# for i in range(1, 5):
#     if i == 3:
#         continue
#     print(i)

# # Output:
# # 1
# # 2
# # 4

# # Explanation:
# # pass does nothing.
# # continue skips the current iteration.


# # Q34. Complete the Skeleton

# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)

# # Output:
# # 1
# # 2
# # 4
# # 5

# # Explanation:
# # break stops the entire loop.
# # pass does not skip printing.
# # continue skips printing 3.


# # Q35. Output Prediction

# for i in range(1, 6):
#     if i == 2:
#         continue
#     if i == 4:
#         break
#     print(i)
# else:
#     print("Finished")

# # Output:
# # 1
# # 3

# # Explanation:
# # continue skips 2.
# # break stops at 4.
# # Therefore, else does not run.


# # Q36. Search and Report

# numbers = list(map(int, input("Enter numbers: ").split()))
# target = int(input("Enter target: "))

# for num in numbers:
#     if num < 0:
#         continue

#     if num == target:
#         print("Target found")
#         break
# else:
#     print("Target not found")

# # Input:
# # -2 4 7 9
# # 7
# # Output:
# # Target found

# # Input:
# # -5 -1 3 6 8
# # 7
# # Output:
# # Target not found

# # Input:
# # 2 4 6
# # 2
# # Output:
# # Target found


# # Q37. Skip, Stop, or Complete?

# numbers = list(map(int, input("Enter numbers: ").split()))

# for num in numbers:
#     if num == 0:
#         continue

#     if num == -1:
#         break

#     print(num)
# else:
#     print("All values processed")

# # Input: 2 0 4 -1 8
# # Output:
# # 2
# # 4

# # Input: 0 3 5
# # Output:
# # 3
# # 5
# # All values processed

# # Input: -1 2 3
# # Output:
# # No numbers printed
# # No completion message


# # Q38. Understand Nested Loops

# for row in range(1, 4):
#     for col in range(1, 4):
#         if col == 2:
#             continue
#         if row == 3:
#             break
#         print(row, col)
#     else:
#         print("Inner loop completed")

# # Output:
# # 1 1
# # 1 3
# # Inner loop completed
# # 2 1
# # 2 3
# # Inner loop completed

# # Explanation:
# # Row 1: inner loop completes without break.
# # Row 2: inner loop completes without break.
# # Row 3: break stops the inner loop.
# # Therefore, the inner else does not run for row 3.


# # Q39. Find the First Number Divisible by Both 4 and 6

# numbers = list(map(int, input("Enter numbers: ").split()))

# for num in numbers:
#     if num < 0:
#         continue

#     if num % 4 == 0 and num % 6 == 0:
#         print("Found:", num)
#         break
# else:
#     print("No matching number")

# # Input: -3 8 12 24
# # Output:
# # Found: 12

# # Input: 5 7 10 14
# # Output:
# # No matching number

# # Input: -12 6 18
# # Output:
# # No matching number