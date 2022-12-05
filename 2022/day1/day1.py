from helpers import utils

lines = utils.input_lines('input.txt')

sums = []
curr_sum = 0
for line in lines:
    if line == "":
        sums.append(curr_sum)
        curr_sum = 0
    else:
        curr_sum += int(line)

# curr_biggest = 0
# biggest = None
# for i, s in enumerate(sums):
#     if s > curr_biggest:
#         curr_biggest = s
#         biggest = i



# print(biggest + 1, curr_biggest)

sorted_sums = list(sorted(sums, reverse=True))
print(sum(sorted_sums[:3]))

