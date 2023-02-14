def say_hello(sep='|', name='friend'):
    print('hello', name, sep=sep)
    print('how are you today?')
    print('it was nice to meet you', name, sep=sep)


people = ['noah', 'eric', 'justin', 'jordan', 'gene']

for person in people:
    say_hello('*', person)
