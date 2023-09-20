for fizzbuzz in range(100):
    if fizzbuzz % 6 == 0 and fizzbuzz % 10 == 0:
        print("FIZZBUZZ")
        continue
    elif fizzbuzz % 6 == 0:
        print("FIZZ")
        continue
    elif fizzbuzz % 10 == 0:
        print("BUZZ")
        continue
    print(fizzbuzz)
