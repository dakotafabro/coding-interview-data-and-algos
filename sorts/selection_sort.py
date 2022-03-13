# real-world application/visualization - classroom: line students up by height by 
# comparing the FIRST student with the REST of the students
# When there is a student shorter than the FIRST student, they switch spots
# then I move on to the next student and continue the process

def selection_sort(my_list):
    for i in range(0, len(my_list)):
        min_height = i
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_height]:
                min_height = j
        temp = my_list[i]
        my_list[i] = my_list[min_height]
        my_list[min_height] = temp
    return my_list

the_list = [47, 21, 76, 18, 27, 52, 82]
print(selection_sort(the_list))