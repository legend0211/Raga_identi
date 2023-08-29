import numpy as np
from helper.closest_array import closest_array
def find_thaat(obt_thaat):
    
    # The dataset of the various songs
    thaat = ["Bilawal", "Kalyan", "Khamaj", "Kafi", "Asavari", "Todi", "Poorvi", "Marva", "Bhairavi", "Bhairav"]
    check_thaat = [np.array(["C", "G", "D", "E", "F", "A", "B"]), 
                   np.array(["C", "G", "D", "E", "F#/Gb", "A", "B"]),
                   np.array(["C", "G", "D", "E", "F", "A", "A#/Bb"]), 
                   np.array(["C", "G", "D", "D#/Eb", "F", "A", "A#/Bb"]),
                   np.array(["C", "G", "D", "D#/Eb", "F", "G#/Ab", "A#/Bb"]), 
                   np.array(["C", "G", "C#/Db", "D#/Eb", "F#/Gb", "G#/Ab", "A#/Bb"]),
                   np.array(["C", "G", "C#/Db", "E", "F#/Gb", "G#/Ab", "B"]), 
                   np.array(["C", "G", "C#/Db", "E", "F#/Gb", "A", "B"]),
                   np.array(["C", "G", "C#/Db", "D#/Eb", "F", "G#/Ab", "A#/Bb"]), 
                   np.array(["C", "G", "C#/Db", "E", "F", "G#/Ab", "B"])]
    
    obt_thaat = np.array(obt_thaat)
    
    # Finding the closest thaat corresponding to the obtained pitch values
    closest_index = closest_array(obt_thaat, check_thaat)
    possible_thaat_list = []
    print("Thaat(s) :", end=' ')
    for i in closest_index:
        possible_thaat_list.append(thaat[i])
        print(thaat[i], end=' ')
    
    return possible_thaat_list
