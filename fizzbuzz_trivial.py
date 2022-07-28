# Author: Dominic Lannutti
# Date: 31 January 2022

def main(lim: int) -> None:
    # exit function if given limit is not an integer
    if lim % 1 != 0:
        return None
   
   # exit function if given limit is less than 0
    elif lim < 0:
        return None

    # create generator loop using modulus operators to find fizziness and buzziness
    for i in range(1, lim+1):
        if i % 15 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)


if __name__ == "__main__":
    lim = 100
    main(lim)
