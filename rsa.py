
# Extended Euclidean Algorithm (from stack overflow) 
def modinv(e, phi):
    d_old = 0; r_old = phi
    d_new = 1; r_new = e
    while r_new > 0:
        a = r_old // r_new
        (d_old, d_new) = (d_new, d_old - a * d_new)
        (r_old, r_new) = (r_new, r_old - a * r_new)
    return d_old % phi if r_old == 1 else None

# 2 prime numbers
p, q = 13, 7

n = p*q
phi = (p-1)*(q-1)

# public key
e = 5

# private key
d = modinv(e, phi)

#--------Lets encrypt the data now-----------

class Rsa:

    def __init__(self, data):
        self.data = data
    
    def encrypt(self):
        temp = self.data*self.data
        count = 2
        while count < e:
            temp = temp*self.data
            if temp > n:
                temp = temp%n
            count = count + 1
        return temp
    
    def decrypt(self, edata):
        temp = edata*edata
        count = 2
        while count < d:
            temp = temp*edata
            if temp > n:
                temp = temp%n
            count = count + 1
        return temp

a = Rsa(67)

print(f"Encrypted value is {a.encrypt()}")
print(f"Decrypted value is {a.decrypt(a.encrypt())}")