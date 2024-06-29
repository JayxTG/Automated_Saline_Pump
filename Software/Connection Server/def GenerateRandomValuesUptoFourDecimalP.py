#generate 11 random values upto 4 decimal places from 1.5 to 2.5
def GenerateRandomValuesUptoFourDecimalP():
    import random
    randomlist = []
    for i in range(0,11):
        n = random.uniform(1.5,2.5)
        n = round(n,4)
        randomlist.append(n)
    return randomlist
print(GenerateRandomValuesUptoFourDecimalP())