def jaccard_similarity(str_arr1, str_arr2):

    # Making two sets of the arrays and finding the arrays with the most similarities
    set1 = set(str_arr1)
    set2 = set(str_arr2)
    intersection = set1.intersection(set2)
    return len(intersection)