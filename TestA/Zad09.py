def my_fun(x):
    return x % 10

nums = [12, 31, 23, 50, 35, 47, 38]
nums.sort(key = my_fun) #sortiraj od najmanjeg do najveceg po key - my_fun
print(nums) #stampa - [0, 1, 2, 3, 5, 7, 8]