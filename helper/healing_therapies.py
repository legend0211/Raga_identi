

def healing_therapies(thaat_list):
    thaat = ["Bilawal", "Kalyan", "Khamaj", "Kafi", "Asavari", "Todi", "Poorvi", "Marva", "Bhairavi", "Bhairav"]
    
    therapy = ["Gives healthy mind and body",
               "Control sound and sonorous sleep",
               "Reduce mental tension",
               "Relief from headache",
               "Relief from cough and cold",
               "Relief from problems of high blood pressure",
               "Can cure Rheumatic Arthritis",
               "Relief from asthma",
               "Prevents hysteria",
               "Brings joy",
               "Mitigate insomina",
               "Reduces anxiety",
               "Reduces hypertension",
               "Brings Creativity and Happiness",
               "Cure low blood pressure",
               "Control psychological hazards and builds confidence",
               "Used for constipation",
               "Brings serenity",
               "Enhances compassion and patience",
               "Relief from High fever",
               "Relief from phlegm, toothache, intestinal gas, sinusitis",
               "It can be used for Emotional strength, Devotion and Peace, Restful Sleep, Tranquility, Relaxation & Rest",
               "Peace Integration"]
    
    therapy_choice = [[1,2],
                      [3,4,5,6,7],
                      [2,3,8,9],
                      [1,10,11,12,13],
                      [3,13,14,15,16,17],
                      [3,4,5,9,12,18],
                      [3,11],
                      [0,9,19],
                      [4,14,19,20,21],
                      [4,5,18,22]]
    
    therapy_number = set()
    for i in range(len(thaat)):
        if(thaat[i] in thaat_list):
            for j in therapy_choice[i]:
                    therapy_number.add(therapy[j])
    
   
    return list(therapy_number)

print(healing_therapies(["Bilawal"]))