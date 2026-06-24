def one(lst):
    largest = lst[0]
    for number in lst:
        if number > largest:
            largest = number
    print('\t', f'the largest element is {largest}')

def two(lst):
    sum = 0
    i = 0
    while i < len(lst):
        sum = sum + lst[i]
        i = i + 1
    average = sum / len(lst)
    print('\t', f'the average is {average}')

def three(text):
    text_lower = text.lower()
    palindrome = True
    for i in range(len(text_lower) // 2):
        left = text_lower[i]
        right = text_lower[len(text_lower) - 1 - i]
        if left != right:
            palindrome = False
            break
    if palindrome:
        print('\t', f'"{text}" is a palindrome')
    else:
        print('\t', f'"{text}" is not a palindrome')

def four(first_term, ratio, n):
    current = first_term
    i = 0
    while i < n:
        print('\t', current)
        current = current * ratio
        i = i + 1

def five(lst):
    largest = lst[0]
    second_largest = None
    for number in lst:
        if number > largest:
            second_largest = largest
            largest = number
        elif second_largest is None or number > second_largest:
            if number != largest:
                second_largest = number
    print('\t', f'the second largest number is {second_largest}')

def six(number):
    sum = number
    i = number - 1
    while i > 0:
        sum = sum * i
        i = i - 1
    print('\t', f'{number} factorial = {sum}')

def seven(number):
    perfect_square = False
    for i in range(1, number + 1):
        if i * i == number:
            perfect_square = True
            break
        elif i * i > number:
            break
    if perfect_square:
        print('\t', f'{number} is a perfect square')
    else:
        print('\t', f'{number} is not a perfect square')

def eight():
    total_sum = 0
    number = 2
    while number <= 100:
        prime = True
        divisor = 2
        while divisor < number:
            if number % divisor == 0:
                prime = False
            divisor = divisor + 1
        if prime:
            total_sum = total_sum + number
        number = number + 1
    print('\t', f'the total sum of primes between 1 and 100 is {total_sum}')

def nine(sentence):
    words = sentence.split()
    count = 0
    for word in words:
        count = count + 1
    print('\t', f'word count = {count}')

def ten(lst1, lst2):
    similarities = []
    i = 0
    while i < len(lst1):
        if lst1[i] in lst2:
            similarities.append(lst1[i])
        i = i + 1
    print(similarities)

