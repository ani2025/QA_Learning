#!/usr/bin/env python3 

import random

lottery_nums = []

while len(lottery_nums) != 6:
    random_num = random.randrange(1,50)
    if random_num not in lottery_nums:
        lottery_nums.append(random_num)
        
print("Lottery numbers are")
lottery_nums.sort()
for num in lottery_nums:
    print(num, end = " ")