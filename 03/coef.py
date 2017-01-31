 C(n, k) = C(n-1, k-1) + C(n-1, k)
 C(n, 0) = C(n, n) = 1



 def binomialCoeff(n , k):
 	if k==0 or k ==n :
    	return 1
    # Recursive Call
    return binomialCoeff(n-1 , k-1) + binomialCoeff(n-1 , k)

n = 5
k = 2
print ("Value of C(%d,%d) is (%d)" %(n , k , binomialCoeff(n , k)))
 



         C(5, 2)
                    /                      \
           C(4, 1)                           C(4, 2)
            /   \                          /           \
       C(3, 0)   C(3, 1)             C(3, 1)               C(3, 2)
                /    \               /     \               /     \
         C(2, 0)    C(2, 1)      C(2, 0) C(2, 1)          C(2, 1)  C(2, 2)
                   /        \              /   \            /    \
               C(1, 0)  C(1, 1)      C(1, 0)  C(1, 1)   C(1, 0)  C(1, 1)