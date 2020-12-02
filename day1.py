nums = open('numbers.txt').read().split()
def a1():
    for x in nums:
        for y in nums: 
            if int(x) + int(y) == 2020:
                return int(x)*int(y)
print(a1())

def a2():
    for x in nums:
        for y in nums:
            for z in nums: 
                if int(x) + int(y) + int(z) == 2020:
                    return int(x)*int(y)*int(z)
print(a2())
