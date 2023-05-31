"""
1. Make a list containing of only strings. Now ask user for any string and re-arrange the list in the decending order of occurance of that string.

for example:
list1 = ['no bun', 'bug bun bug bun bug bug', 'bunny bug', 'buggy bug bug buggy']
input string = 'bug'
output list = ['bug bun bug bun bug bug', 'buggy bug bug buggy', 'bunny bug', 'no bun']
"""
list1 = ['no bun', 'bug bun bug bun bug bug', 'bunny bug', 'buggy bug bug buggy']
input_string = 'bug'
list2 = []
for string in list1:
    count = string.count(input_string)
    list2.append(str(count) + "_" + string)
list2.sort()
list2.reverse()
print(list2)