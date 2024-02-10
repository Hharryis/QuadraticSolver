# taking values for the quadratic equation
ax = int(input("Enter the coefficient of x^2: "))
bx = int(input("Enter the coefficient of x: "))
c = int(input("Enter the constant: "))

# a discriminant determines how many solutions there are to the given quadratic equation
# a positive discriminant indicates that the quadratic has two distinct real number solutions.
# a discriminant of zero indicates that the quadratic has a repeated real number solution.
# a negative discriminant indicates that neither of the solutions are real numbers.
# d is the discriminant

d = bx**2 - 4*ax*c

# checking for solution(s)
if d > 0 :
    x_one = (-bx + d**0.5)/(2*ax)
    x_two = (-bx - d**0.5)/(2*ax)
    print("Here are your two solutions: ", x_one, x_two)
elif d == 0:
    xnew = -bx/(2*ax)
    print("Here is the value of x: ", xnew)
else:
    print("NO SOLUTION(S)")

#check parabola opens up or down
if ax > 0: 
    print("Parabola opens up")
else:
    print("Parabola opens down")

# calculating vertex x and y (-b/2a) according to google for vertex x
    
vertex_x = -bx/(2*ax)

# vertex y formula ax^2 +bx +c

vertex_y = ax*vertex_x**2 +bx*vertex_x +c

print("Vertex x: ", vertex_x, "and", "Vertex y: ", vertex_y)

# In a parabola, x stays zero and using the ax^2 + bx + c so y will be c

yintercept = c

print("the interception is: (0,", yintercept,")")





