# quick sort--
# real-world application/visualization - classroom: lining students up by height by:
# taking the first student's height
# comparing their height to everyone else's
# note all the heights that are less than the first student's height, place then on the left of the student (need pivot method here)
# all on the right are now taller than the first student (who is now in the middle of the line).
# Continue the process on the shorter students.
# Continue the process on the taller students.
# Once all student heights are addressed, the line is sorted


# pivot--
# real-world application/visualization - classroom: helps pivot the students by the "middle height" students of each group

def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp

def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index
    
    for i in range(pivot_index+1, end_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index

def quick_sort(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort(my_list, left, pivot_index-1)
        quick_sort(my_list, pivot_index+1, right)
    return my_list

the_list = [47, 21, 76, 18, 27, 52, 82]
print(quick_sort(the_list, 0, len(the_list)-1))
