

# Mathematical functions
from math import *


# 9.2.1   Number-theoretic & reprsetnation funcs

# ceil(x) - ceiling of x as float,  smallest inteer value >= x
ceil(1.2)
ceil(-1.2)

#copysign(x,y) - return x with sign of y.  (pyver>=2.6)
copysign(2.0, - 1.5)
copysign(1.5, -0.0)   # some platform know -0.0)

#fabs(x) - return the absolute value of x  - float
fabs(-1)
fabs(-1.5)

# factorial(x) - x factorial or ValueError if x is not inegral or is neagtie
factorial(3)
factorial(0)
#factorial(-1)
#factorial(1.2)



#floor(x) - return floor of x as a float,  largest value <= x
floor(1.5)
floor(-1.5)

#fmod (x,y) -  x % y but more accurate ,  fmod for float, x%y for integer
fmod(2, 8)


#frexp(x) -   (m,e)  so that x == m* 2**e
frexp(2)
frexp(7)


#fsum(iterable)
fsum([1.5, 3.0, 5.4])

#isinf(x)  - is infiity - check if the float x is postive or negative infinity
isinf(-1)
isinf(1.0e+19934343434)

# isnan(x)  -  is nan (not a number)  - @see IEEE754 std


# ldexp(x, i) - x * (2**i)   -   inverse of function frexp
ldexp(1, 3)

# modf(x) -  (fractional-part, integral-part)
modf(1.33)

# trunc(x)
trunc(1.333)
trunc(-1.333)


# 9.2.2 Power and logarithmic functions

#exp(x) - e**x
exp(1.2)

# expm1(x) - e**x -1 
expm1(1.2)

#log(x[, base])
log(e)
log(64, 2)
log(1000, 10)

# log1p(x) - natural logarithm of 1+x (base 3)
log1p(e-1)

#log10(x)  - more accurate than log(x, 10)
log10(1000)

#pow(x, y)
pow(2, 3)
#pow(100000, 1000000)

#sqrt(x) - square root of x
sqrt(2)

# 9.2.3  Trigonometric functions
acos(1)
asin(1)
atan(1)
atan2(1,2)
cos(1)
hypot(1,2)
sin(1)
tan(1)

# 9.2.4  Anular conversions
degrees(pi)
radians(180)

# 9.2.5  Hyperbolic functions
acosh(2)
asinh(3)
atanh(0.1)

cosh(3)
sinh(3)
tanh(3)

# 9.2.6  Special functions

#erf(x) - return error function at x
erf(1.2)

#erfc(x)  - complementary error function at x
erfc(1.0)

# gamma(x) - return the gamma function at x
gamma(0.333)

# lgamma(x)  - return the natural logarithm of the absolute value of the Gamma function at x
lgamma(1333)

# 9.2.7  Constants

pi

e

