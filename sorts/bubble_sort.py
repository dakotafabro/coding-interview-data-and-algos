# real-world application/visualization - classroom: lining students up by height
# compare student heights while they stand next to each other (j and j+1)
# start at index -1
# iterate through rest of list until a larger value is found
# swap the last index with the larger value
# goal: list sorted in ascending order

def bubble_sort(list):
    for i in range(len(list-1, 0, -1)):
        for j in range(i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list
