# essentially the opposite of selection sort
# real-world application/visualization - classroom: line students up by height by 
# comparing the SECOND student to all previous students
# if the previous student is taller, switch spots
# if not, move on to the next student comparison

def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list

the_list = [47, 21, 76, 18, 27, 52, 82]
print(insertion_sort(the_list))