import math

lst = [678, 137, 123, 101, 901, 567, 131, 234, 432, 113]

# 1
print([n + 1 for n in lst])

# 2
print([n * 2 for n in lst])

# 3 
print([n ** 2 for n in lst])

# 4
print([round(math.sqrt(n), 2) for n in lst if n > -1]) 

# 5
print([round(math.cos(n), 3) for n in lst])

# 6
print([n for n in lst if n % 2 == 0])

# 7 
print([n for n in lst if n % 2 == 1])

# 8 
print([n for n in lst if n > 500])

# 9
print([n for n in lst if n > 500 and n % 2 == 0])

# 10
print([n for n in lst if n % 2 == 0 and n % 3 == 0])

# 11
print([(n, n * 2) for n in lst])

# 12
print([(n, n ** 2) for n in lst])

# 13
print([(n, round(math.sqrt(n), 2)) for n in lst if n > -1])

# 14
print([(n, round(math.sin(n), 2)) for n in lst if n % 2 == 0])

# 15
print([(n, round(math.tan(n), 2), sum(ord(d) for d in str(n))) for n in lst])

# 16
print(sum(1 for n in lst if n % 2 == 0))

# 17
print(sum(n for n in lst if n % 2 == 1))

# 18
print(sum(lst[i] for i in range(0, len(lst), 2)))

# 19
print(sum(len(str(n)) for n in lst))

# 20
print(sum(len(str(n)) for n in lst if str(n)[0] in "123"))

# 21
print(sum(sum(int(d) for d in str(n)) for n in lst))

# 22
print(sum(sum(int(d) for d in str(n)) for n in lst if n % 2 == 0))

# 23
print(sum(sum(int(d) for d in str(n)) for n in lst if n % 2 == 1))

# 24
print([n for n in lst if all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1)) and n > 1])

# 25
print(sum(len(str(n)) for n in lst if all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1)) and n > 1))