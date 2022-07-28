# Author: Dominic Lannutti
# Date: 31 January 2022

def main(lim: int) -> int:
    # exit function if given limit is not an integer
    if lim % 1 != 0:
        return False
   
   # exit function if given limit is less than 0
    elif lim < 0:
        return False

    # create generator loop using modulus operators to find fizziness and buzziness
    for i in range(1, lim+1):
        if i % 15 == 0:
            yield "fizzbuzz"
        elif i % 3 == 0:
            yield "fizz"
        elif i % 5 == 0:
            yield "buzz"
        else:
            yield i


if __name__ == "__main__":
    lim = 100
    for n in main(lim):
        print(n)
