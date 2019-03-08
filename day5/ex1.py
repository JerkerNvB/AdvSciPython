from scipy import linalg
import numpy as np

a = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 19]])

print "...a"

print a

print "...b"
b = np.array([1, 2, 3])
print b

print "...solve"
x = linalg.solve(a, b)
print x

print "...checking"
print np.dot(a, x) == b
print np.allclose(np.dot(a, x), b)

print "...random array as b"
b = np.random.rand(3,3)
print b

print "...solve"
x = linalg.solve(a, b)
print x

print "...eigenvalue of a"
x = linalg.eig(a)
print x

print "...inverse, determinant"
x = linalg.inv(a)
print x
x = linalg.det(a)
print x

print "...norm"
x = linalg.norm(a)
print x

print "...norm order=2"
x = linalg.norm(a,2)
print x


##print "circulant"
##print "---------"
##x = linalg.solve_circulant(a, b)
##print x
##print np.dot(a, x) == b
##print np.allclose(np.dot(a, x), b)
##
##print "triangular"
##print "----------"
##x = linalg.solve_triangular(a, b)
##print x
###x = linalg.solve_toeplitz(a, b)
##print np.dot(a, x) == b
##print np.allclose(np.dot(a, x), b)
##
##print "eigenvalue"
##print "----------"
##
##print linalg.eigenvalue
##
