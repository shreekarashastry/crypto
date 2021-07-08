#This is the implementation of https://arxiv.org/pdf/1906.07221.pdf paper
#This has one of the best and easily digestible explanations to understand sk-snarks

#This is a polynomial helper function where you can evaluate value of a polynomial at any point
#This implementation is for a polynomial of the form (cn)x^n+(cn-1)x^n-1+......+(c1)x+c
#using horners method to decrease the complexity 
list = [1,2,-2] # x^2+2*x-2
def polynomial(list, point):
    order = len(list) - 1 
    result = list[0]
    for i in range(1,order):
        result = result*point + list[i]
    return result

print(polynomial(list,2))

# section 3.2 states an encryption function E(v)=g^v (mod n)
def ecrypt(v):
    g = 5
    n = 12
    return pow(g, v)%n

