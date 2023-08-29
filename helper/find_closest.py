
def find_closest(list, list1, list2, target):

    closest_index = 0
    for i in range(len(list1)):
        if abs(list1[i] - target) < abs(list2[closest_index] - target):
            closest_index = i
    
    for i in range(len(list2)):
        if abs(list2[i] - target) < abs(list2[closest_index] - target):
            closest_index = i
    
    for i in range(len(list)):
        if abs(list[i] - target) < abs(list[closest_index] - target):
            closest_index = i
    
    return closest_index
