books = {'Maths':'130 INR', 'English':'210 INR', 'Biology':'190 INR', 'Chemistry':'140 INR', 'Physics':'100 INR', 'History':'160 INR', 'Geography':'120 INR', 'French':'250 INR', 'Spanish':'240 INR'}
books['Physics'] = '200 INR'

for i in books.keys():
    print(i, books[i])

for k, v in books.items():
    print(f'{k}:{v}')

choice = input('Enter the name of a book: ')
if choice in books:
    print(f'The cost of the {choice} book is {books[choice]}')
else:
    print(f'{choice} is not available')