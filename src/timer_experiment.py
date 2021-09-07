import bitarray
from math import log
import time

s1 = '11100011100011100011100001110100011010100000011111'
s2 = '11100001100011100111110101010101010001010100111110'
array = s1 + s2
mask = s2 + s1

for length in [1, 10, 100, 1000, 10000]:
    barray = bitarray.bitarray(length * array)
    bmask = bitarray.bitarray(length * mask)
    start = time.perf_counter()
    total_len = length * len(array)
    log_len = log(total_len)
    for _ in range(10000000):
        barray ^ bmask
    print(f"Length: {total_len} Time: {time.perf_counter() - start} Time/Ln(Length): {(time.perf_counter() - start)/log_len}")
