def one(number):
    factors = []
    for i in range(2, number):
        if number % i == 0:
            prime = True
            for j in range(2,i):
                if i % j == 0:
                    prime = False
                    break
            if prime:
                    factors.append(i)
    print('\t', f'prime factors of {number} = {factors}')

def two(n):
    second_to_last = 0
    last = 1
    i = 2
    while i < n:
        total = last + second_to_last
        second_to_last = last
        last = total
        i = i + 1
    print('\t', f'fibonacci term {n} = {last}')

def three(text1, text2):
    text1_lower = text1.lower().replace(' ', '')
    text2_lower = text2.lower().replace(' ', '')
    anagram = True
    if len(text1_lower) != len(text2_lower):
        anagram = False
    else:
        for c in text1_lower:
            count1 = 0
            count2 = 0
            for c2 in text1_lower:
                if c2 == c:
                    count1 = count1 + 1
            for c2 in text2_lower:
                if c2 == c:
                    count2 = count2 + 1
            if count1 != count2:
                anagram = False
                break
    if anagram:
        print('\t', f'"{text1}" and "{text2}" are anagrams')
    else:
        print('\t', f'"{text1}" and "{text2}" are not anagrams')

def four(first_term, difference, n):
    current = first_term
    i = 0
    while i < n:
        print(current)
        current = current + difference
        i = i + 1

def five(lst):
    lst2 = lst[:]
    for i in range(len(lst2)):
        for j in range(i + 1, len(lst2)):
            if lst2[i] > lst2[j]:
                temp = lst2[i]
                lst2[i] = lst2[j]
                lst2[j] = temp
    length = len(lst2)
    if length % 2 == 1:
        median = lst2[length // 2]
    else:
        left = lst2[(length // 2) - 1]
        right = lst2[(length // 2)]
        median = (left + right) / 2
    print('\t', f'the median is {median}')

def six(number):
    total = 0
    divisor = 1
    while divisor < number:
        if number % divisor == 0:
            total = total + divisor
        divisor = divisor + 1
    if total == number:
        print('\t', f'{number} is a perfect number')
    else:
        print('\t', f'{number} is not a perfect number')

def seven(number):
    total = 0
    for digit in str(number):
        total = total + int(digit)
    print('\t', f'sum of digits in {number} = {total}')

def eight(sentence):
    words = sentence.split()
    longest = words[0]
    i = 1
    while i < len(words):
        if len(words[i]) > len(longest):
            longest = words[i]
        i = i + 1
    print('\t', f'the longest word is {longest}')

def nine(sentence):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    sentence_lower = sentence.lower()
    panagram = True
    for letter in alphabet:
        if letter not in sentence_lower:
            panagram = False
            break
    if panagram:
        print('\t', f'the {sentence} is a panagram')
    else:
        print('\t', f'the {sentence} is not a panagram')

def ten():
    number = 2
    while number <= 1000:
        prime = True
        divisor = number - 1
        while divisor > 1:
            if number % divisor == 0:
                prime = False
                break
            divisor = divisor - 1
        if prime:
            print(number)
        number = number + 1