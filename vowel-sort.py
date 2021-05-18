vowels = ['e','a','u','i','o']

vowels.sort()
print('Sorted list:',vowels)

vowels.sort(reverse=True)
print('Sorted list (descending):',vowels)

numbers = ['like','i','coffee','black']
numbers.sort(key=len)
print(numbers)
