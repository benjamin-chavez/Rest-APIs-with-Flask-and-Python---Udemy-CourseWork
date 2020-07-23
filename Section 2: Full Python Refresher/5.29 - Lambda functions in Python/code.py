def add(x, y):
    return x + y


print(add(5, 7))

# As a Lambda function:
lambda x, y: x + y
# -or-
add = lambda x, y: x + y
######################################################

def double(x):
    return x * 2

sequence = [1, 4, 5, 9]
doubled = [double(x) for x in sequence]
doubled = map(double, sequence)

# As a Lambda function:
doubled = [(lambda x: x* 2)(x) for x in sequence]
doubled = list(map(lambda x: x * 2, sequence))