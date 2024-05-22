#3/10/2024; a mini-project to help me with abstract algerbra
from gcd import gcd

def coprime_group_generator(modulus):
    """returns the set of integers relatively prime to the specified modulus"""
    coprime_set = []
    index = 1

    # loop through nums up to congruence class to decide if index belongs in set
    while index < modulus:
        """if the index and modulus are coprime, add them to the set."""
        if gcd(index, modulus) == 1:
            coprime_set.append(index)
            index += 1
        else:
            index += 1

    return(coprime_set)

print(coprime_group_generator(15)) 