# This small python app shows how a value of some variable known to alice can be verified by bob 
# without ever knowing the variable 

# let's consider a scenario where alice wantes to prove bob that she knows x
# let g be a number which is known to public ( this is a simple case which can be backtracked but in a real life 
# situation it will be impossible because of elliptic curve cryptography)
x=5
g=7

# Alice sends y=g^x and also picks a random number v and sends t such that t=g^v
v=3
y=pow(g,x)
t=pow(g,v)
print(f"value of t when Alice sends it = {t}")

# Bob picks a random number c and sends that back to Alice and Alice sends back r=c-cx
c=5
r=v-c*x

# Now all tha Bob has to do is to check t=g^r*y^c ( is simplified it boils down to g^v which is essentially t)
t=pow(g,r)*pow(y,c)
print(f"value of t when Bob verifies it = {t}")