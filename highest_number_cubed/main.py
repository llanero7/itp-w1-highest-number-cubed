"""This is the entry point of the program."""


def highest_number_cubed(limit):
    prev_num = 0
    
    while (prev_num - 1) ** 3 < limit: 
        current_num = prev_num + 1
        if current_num ** 3 > limit:
            return prev_num
            
        prev_num = current_num



# 1 ^ 3 = 1 < 30? Yes
# 2 ^ 3 = 8 < 30? Yes
# 3 ^ 3 = 27 < 30? Yes
#         30
# 4 ^ 3 = 64 < 30? NO 