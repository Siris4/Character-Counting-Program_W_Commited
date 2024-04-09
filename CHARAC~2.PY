
user_input = input("Please type a common phrase or sentence: ")
# messageVariable = 'It was a bright cold day in April, and all the clocks were striking thirteen.'
count = {}  # assume r is the key, and 12 is the value IF it appears 12 times.

print(f"\nThis is how many times each character showed up:")

for eachCharacter in user_input:
    if eachCharacter in count:
        count[eachCharacter] += 1
    else:
        count[eachCharacter] = 1

print(count)
