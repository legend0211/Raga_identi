from helper.find_closest import find_closest
from helper.find_thaat import find_thaat


def octave_table(most_prominent_note):
    
    # Intialising the notes and the octave values of the notes
    note = ["C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B"]
    octave2 = [65.41, 69.30, 73.42, 77.78, 82.41, 87.31, 92.50, 98.00, 103.83, 110.00, 116.54, 123.47]
    octave3 = [130.81, 138.59, 146.83, 155.56, 164.81, 174.61, 185.00, 196.00, 207.65, 220.00, 233.08, 246.94]
    octave4 = [261.63, 277.18, 293.66, 311.13, 329.63, 349.23, 369.99, 392.00, 415.30, 440.00, 466.16, 493.88]
    
    octave2_ll = [64.72855, 68.70765, 72.7327, 77.1305, 81.8172, 86.722, 91.7842, 97.03175, 102.94515, 109.19075, 115.5236, 122.10605]
    octave3_ll = [129.4471, 137.4053, 145.4554, 154.261, 163.6244, 173.434, 183.5684, 194.0635, 205.8803, 218.3815, 231.0472, 244.2121]
    octave4_ll = [258.9042, 274.8106, 290.9108, 308.532, 327.2588, 346.878, 367.1268, 388.127, 411.7606, 436.763, 462.0944, 488.4242]
    
    octave2_hl = [66.09145, 69.89235, 74.1073, 78.4295, 83.0028, 87.898, 93.2158, 98.96825, 104.71485, 110.80925, 117.5564, 124.83395]
    octave3_hl = [132.1729, 139.7747, 148.2046, 156.859, 165.9956, 175.786, 186.4316, 197.9365, 209.4197, 221.6185, 235.1128, 249.6679]
    octave4_hl = [264.3558, 279.5494, 296.4092, 313.728, 332.0012, 351.582, 372.8532, 395.873, 418.8394, 443.237, 470.2256, 499.3358]   
    
    octave_to_be_used_ll = []
    octave_to_be_used_hl = []
    octave_to_be_used = []
    
    # Finding under which note the most prominent note will fall
    if(most_prominent_note < 127.14):
        octave_to_be_used = octave2
        octave_to_be_used_ll = octave2_ll
        octave_to_be_used_hl = octave2_hl
        
    elif(most_prominent_note < 254.286):
        octave_to_be_used = octave3
        octave_to_be_used_ll = octave3_ll
        octave_to_be_used_hl = octave3_hl
    else:
        octave_to_be_used = octave4
        octave_to_be_used_ll = octave4_ll
        octave_to_be_used_hl = octave4_hl
    
    # Finding the note of the most prominent note
    closest = find_closest(octave_to_be_used, octave_to_be_used_ll, octave_to_be_used_hl, most_prominent_note)
    
    final = []
    final.append(most_prominent_note)
    
    # Finding the other pitch values of the notes of the octave
    for i in range(closest):
        number = (octave_to_be_used[closest-i-1]/octave_to_be_used[closest-i]) * final[0]
        final.insert(0,number)
    
    for i in range(closest,(len(octave_to_be_used)-1)):
        number = (octave_to_be_used[i+1]/octave_to_be_used[i]) * final[i]
        final.append(number)
    
    # Calculatng errors of formulated pitch and actual pitch
    for i in range(len(final)):
        final[i] = abs(octave_to_be_used[i]-final[i])/octave_to_be_used[i]
        
    # Sorting according to the least errors
    for i in range(len(final)):
        for j in range(len(final)):
            if(final[i]<final[j]):
                temp = final[i]
                final[i] = final[j]
                final[j] = temp
                
                temp = note[i]
                note[i] = note[j]
                note[j] = temp

    # Appending the corresponding notes       
    thaat = []
    thaat.append(note[closest])
    c = 0
    for i in range(len(final)):
        if(note[closest]==note[i]):
            continue
        thaat.append(note[i])
        c = c+1
        
    print(thaat)
    obtained_thaat = find_thaat(thaat[0:7])
    return obtained_thaat
