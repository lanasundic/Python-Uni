def my_fun(x):
    return x % 5

nums = [14, 31, 27, 70, 53]
nums.sort(key = my_fun)
print(nums)     #stampa - [70, 31, 27, 53, 14]