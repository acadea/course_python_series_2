
# map - transform elements of an iterable into something else

fruits = ['apple', 'orange', 'grape', 'kiwi', 'durian']


def to_upper(word: str):
    return word.upper()

# uppercase = map(to_upper, fruits)


# using lambda function is shorter and cleaner
uppercase = map(lambda word: word.upper(), fruits)


# we can pass in multiple iterables to the map function
map(lambda word, index: print(index, word), fruits, range(0, len(fruits)))


# filter - filter out elements based on a condition
filtered = filter(lambda word: len(word) > 4, fruits)
print(filtered)

