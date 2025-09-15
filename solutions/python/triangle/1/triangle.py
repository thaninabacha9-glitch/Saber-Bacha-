def equilateral(sides):
    a, b, c = sides
    if not is_valid_triangle(sides):
        return False
    return a == b == c

def isosceles(sides):
    a, b, c = sides
    if not is_valid_triangle(sides):
        return False
    return a == b or a == c or b == c

def scalene(sides):
    a, b, c = sides
    if not is_valid_triangle(sides):
        return False
    return a != b and a != c and b != c

def is_valid_triangle(sides):
    a, b, c = sides
    # All sides must be positive
    if a <= 0 or b <= 0 or c <= 0:
        return False
    # Triangle inequality theorem
    return (a + b > c) and (a + c > b) and (b + c > a)
