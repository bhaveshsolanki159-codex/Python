nums = [1, 2, 3, 4, 5]
doubles = []
for num in nums:
    if num * 2 > 5:
        doubles.append(num * 2)



nums = [1, 2, 3, 4, 5]
doubles = [double for num in nums if (double := num * 2) > 5]


nums = [10, 15, 20, 25]
half = []
for num in nums:
    if num % 5 == 0:
        half.append(num // 2)


half = [h for num in nums if (h := num // 2) % 5 == 0]
