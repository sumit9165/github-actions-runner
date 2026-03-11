def add(a, b):
    return a + b

# simple test
if add(2, 2) != 4:
    raise Exception("Math test failed")

print("All tests passed")
add(2, 3)