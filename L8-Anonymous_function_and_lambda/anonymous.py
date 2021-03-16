
# anonymous function are function without a name
# a one-liner function


def add(x, y):
    return x + y

# we use the 'lambda' keyword to create anonymous function
add2 = lambda x, y: x + y




# how is this useful? Useful in callback
def for_each(iterable, operation):
    for item in iterable:
        operation(item)

if __name__ == '__main__':
    print(add(1, 5))
    print(add2(1, 5))

    fruits = ['apple', 'orange', 'grapes']
    # nice and clean, we don't need to create a new function for this
    for_each(fruits, lambda fruit: print(fruit.upper()))





