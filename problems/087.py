import time
import primes
import math

start_time = time.clock()

upper_bound = 50000000
lower_bound = 2 ** 2 + 2 ** 3 + 2 ** 4
# print(lower_bound)
squares_upper_bound = math.ceil(math.sqrt(upper_bound)) + 1
cubes_upper_bound = math.ceil(upper_bound ** (1 / 3)) + 1
fourths_upper_bound = math.ceil(math.sqrt(math.sqrt(upper_bound))) + 1

prime_list_squares = primes.find_primes_less_than_n(squares_upper_bound)
prime_list_cubes = primes.find_primes_less_than_n(cubes_upper_bound)
prime_list_fourths = primes.find_primes_less_than_n(fourths_upper_bound)

print(len(prime_list_squares))
print(len(prime_list_cubes))
print(len(prime_list_fourths))

prime_squares = {p: p ** 2 for p in prime_list_squares}
prime_cubes = {p: p ** 3 for p in prime_list_cubes}
prime_fourths = {p: p ** 4 for p in prime_list_fourths}

sums = set()

for square in prime_squares:
    for cube in prime_cubes:
        for fourth in prime_fourths:
            sums.add(prime_squares[square] + prime_cubes[cube] + prime_fourths[fourth])

# print(sums)

print(len([i for i in sums if i < upper_bound]))

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))
