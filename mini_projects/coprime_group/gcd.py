#22/5/2024; gcd function. Needed this to fix the coprime generator not working

def gcd(a,b):
    remainder = a%b
    running = True
    while running:
        a = b
        b = remainder
        if a%b ==  0:
            return remainder
            running = False
        else:
            remainder = a%b