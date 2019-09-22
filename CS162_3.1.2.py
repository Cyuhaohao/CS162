def liskov_substitution_principle(x):
    x = x % x
    x = x * 2
    print(x)

liskov_substitution_principle(True)
