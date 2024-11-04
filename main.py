a = int(input("Enter a number:"))
b = int(input("Enter another number:"))

def hcf(a,b):
    if a == 0:
        return b
    return hcf(b % a, a)
def lcm(a,b):
    return (a // hcf(a,b))* b

print('LCM of', a, 'and', b, 'is', lcm(a, b))