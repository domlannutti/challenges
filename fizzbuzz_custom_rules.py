def main(lim):
    # exit function if limit is less than zero
    if lim < 0:
        return False
    # exit function if limit is not an integer
    elif lim % 1 != 0:
        return False

    # create dictionary containing game rules
    rules = {
            3: "Fizz",
            5: "Buzz",
            7: "Bazz"
            }

    # run through integers n over 1<=n<=lim
    for n in range(1, lim+1):
        s = ""
        for k, v in rules.items():
            if n % k == 0:
                s += v
        if len(s) > 0:
            yield s
        else:
            yield n


if __name__ == "__main__":
    lim = 200
    for ans in main(lim):
        print(ans)
