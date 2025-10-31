area_square = lambda side: side * side

area_rectangle = lambda length, breadth: length * breadth

area_triangle = lambda base, height: 0.5 * base * height

print("Area of square with side 5:", area_square(5))
print("Area of rectangle with length 4 and breadth 6:", area_rectangle(4, 6))
print("Area of triangle with base 3 and height 7:", area_triangle(3, 7))
