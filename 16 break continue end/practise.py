# section - A

for i in range(1, 5):
    if i == 1:
        break
    print(i)

print("End")

#output
    #END

for i in range(1, 7):
    print(i)
    if i == 4:
        break
print("Finished")

#output
    #1
    #2
    #3
    #Finished

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

#output
    #1
    #2
    #4
    #5


for i in range(1, 5):
    if i == 2:
        pass
    print(i)

#output
    #1
    #2
    #3
    #4
    #5

for i in range(3):
    print("Python")
else:
    print("Done")

#output
    #python
    #python
    #python
    #done

for i in range(1, 5):
    print("A", i)
    if i == 3:
        break
    print("B", i)

#output
    # A 1
    # B 1
    # A 2
    # B 2
    # A 3

for i in range(1, 5):
    if i == 2:
        continue
    print("Value:", i)
    print("Next line")

#output
    # Value: 1
    # Next line
    # Value: 3
    # Next line
    # Value: 4
    # Next line

for i in range(1, 4):
    if i == 2:
        pass
        print("Inside if")
    print("Outside if", i)

#output
    # Outside if 1
    # Inside if
    # Outside if 2
    # Outside if 3

for i in range(2, 8, 2):
    print(i)
    if i == 4:
        break
    print("Hello")

print("After loop")

#output
    # 2
    # Hello
    # 4
    # After loop

for i in range(1, 5):
    print("Start", i)
    if i == 3:
        continue
    print("End", i)

#output
    # Start 1
    # End 1
    # Start 2
    # End 2
    # Start 3
    # Start 4
    # End 4

for i in range(2, 5):
    print(i)
else:
    print("Loop completed")

#output
    # 2
    # 3
    # 4
    # Loop completed

for i in range(1, 6):
    if i == 4:
        break
    print(i)
else:
    print("Completed")
print("Program end")

#output
    # 1
    # 2
    # 3
    # Program end


for i in range(1, 5):
    if i % 2 == 0:
        continue
    print(i)
else:
    print("Completed")

#output
    # 1
    # 3
    # Completed

for i in range(5, 5):
    print(i)
else:
    print("Else executed")

#output
    # Else executed

for letter in "CODE":
    print(letter)
    if letter == "D":
        break
else:
    print("All letters checked")

#output
    # C
    # O
    # D

for i in range(1, 4):
    if i == 2:
        pass
    print(i)
else:
    print("Finished normally")

#output
    # 1
    # 2
    # 3
    # Finished normally

word = "banana"

for ch in word:
    if ch == "n":
        print("Found")
        break
else:
    print("Not found")

#output
    #Found

word = "apple"

for ch in word:
    if ch == "z":
        print("Found")
        break
else:
    print("Not found")
    
#output
    #Not found

for ch in "education":
    if ch in "aeiou":
        continue
    print(ch, end="")
print()

#output
    #dctn

for ch in "programming":
    if ch == "g":
        break
    print(ch, end="-")

#output 
    #p-r-o-
    
for ch in "computer":
    if ch == "o":
        continue
    if ch == "t":
        break
    print(ch, end="")

#output
    #cmpu

for ch in "cat":
    if ch == "a":
        pass
    print(ch.upper(), end=" ")

#output
    #C A T

n = 1

while n <= 5:
    print(n)
    if n == 3:
        break
    n += 1

print("Stopped")

#output
    # 1
    # 2
    # 3
    # Stopped

n = 0

while n < 5:
    n += 1
    if n == 3:
        continue
    print(n)

#output
    # 1
    # 2
    # 4
    # 5

n = 1

while n <= 5:
    if n == 2:
        n += 1
        continue
    print(n)
    n += 1

#output
    # 1
    # 3
    # 4
    # 5

n = 1

while n <= 4:
    if n == 3:
        break
    print(n)
    n += 1

print(n)

#output
    # 1
    # 2
    # 3

for row in range(1, 4):
    for col in range(1, 5):
        if col == 3:
            break
        print(row, col)
    
#output
    # 1 1
    # 1 2
    # 2 1
    # 2 2
    # 3 1
    # 3 2

for row in range(1, 3):
    for col in range(1, 4):
        if col == 2:
            continue
        print(row, col)

#output
    # 1 1
    # 1 3
    # 2 1
    # 2 3

for i in range(1, 4):
    print("Outer", i)
    for j in range(1, 4):
        if j == 2:
            break
        print("Inner", j)

#output
    # Outer 1
    # Inner 1
    # Outer 2
    # Inner 1
    # Outer 3
    # Inner 1

for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            break
        print(i, j)
    else:
        print("Inner else", i)

#output
    # 1 1
    # 2 1
    # 3 1

for i in range(1, 3):
    for j in range(1, 4):
        if j == 2:
            continue
        print(i, j)
    else:
        print("Inner loop complete")

#output
    # 1 1
    # 1 3
    # Inner loop complete
    # 2 1
    # 2 3
    # Inner loop complete

for i in range(1, 7):
    if i == 2:
        continue
    if i == 5:
        break
    print(i)
else:
    print("Loop else")
print("End")

#output
    # 1
    # 3
    # 4
    # End

for i in range(1, 5):
    if i == 3:
        pass
    else:
        print("Else block", i)
    print("Number", i)

#output
    # Else block 1
    # Number 1
    # Else block 2
    # Number 2
    # Number 3
    # Else block 4
    # Number 4

for i in range(1, 5):
    print("X", end="")
    if i == 2:
        continue
    print("Y", end="")
print("Z")

#output
    # XYXXYXYZ

for i in range(1, 5):
    if i == 2:
        pass
    elif i == 3:
        continue
    elif i == 4:
        break
    print(i)
else:
    print("Completed")
print("Outside")

#output
    # 1
    # 2
    # Outside