file = open('input.txt')

def has_vowels(string):
    vowel_count = 0
    for character in string:
        if character in 'aeiou':
            vowel_count += 1
    if vowel_count < 3:
        return False
    return True

def has_twice(string):
    last_character = None
    for character in string:
        if character == last_character:
            return True
        last_character = character
    return False

def has_illegal(string):
    if 'ab' in string or 'cd' in string or 'pq' in string or 'xy' in string:
        return True
    return False

def is_nice(string):
    if has_vowels(string) == False:
        return False
    if has_twice(string) == False:
        return False
    if has_illegal(string) == True:
        return False
    return True

nice_count = 0
for string in file:
    if is_nice(string):
        nice_count += 1

print(nice_count)

