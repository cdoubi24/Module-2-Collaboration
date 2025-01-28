# 4.1 Conditional Tests

# Assigning values to variables
secret = 7  # Choose a number between 1 and 10
guess = 5   # Choose another number between 1 and 10

# Conditional tests
if guess < secret:
    print('too low')
elif guess > secret:
    print('too high')
else:
    print('just right')
