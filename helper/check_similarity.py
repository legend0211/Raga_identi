

def check_similarity(str_arr1, str_arr2):

    # Finding the non-matching notes
    note = ["C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B"]
    num_note = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    set1 = set(str_arr1)
    set2 = set(str_arr2)
    intersection = set1.intersection(set2)
    set1 = set1-intersection
    set2 = set2-intersection
    
    set1 = list(set1)
    set2 = list(set2)
    
    # Calculating distance of the closest notes in the array
    sum_dist = 0
    for i in range(len(set1)):
        for j in range(len(note)):
            if set1[i]==note[j]:
                sum_dist += num_note[j]
                set1[i] = num_note[j]
    
    for i in range(len(set2)):
        for j in range(len(note)):
            if set2[i]==note[j]:
                sum_dist -= num_note[j]
                set2[i] = num_note[j]
                
    return abs(sum_dist)
