# 6.1 Use a for loop to print the values of the list [3, 2, 1, 0]
for value in [3, 2, 1, 0]:
    print(value)

# 6.2 While loop to compare number with guess_me
guess_me = 7
number = 1

while True:
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it!")
        break
    else:
        print("oops")
        break
    number += 1

# 6.3 For loop with guess_me and range(10)
guess_me = 5

for number in range(10):
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it!")
        break
    else:
        print("oops")
        break
