

def healing_therapies(thaat_list):
    info={'Bilawal': ['Gives healthy mind and body', 'Control sound and sonorous sleep'], 
          'Kalyan': ['Reduce mental tension', 'Relief from headache', 
                     'Relief from cough and cold', 'Relief from problems of high blood pressure', 
                     'Can cure Rheumatic Arthritis'], 
          'Khamaj': ['Control sound and sonorous sleep', 'Reduce mental tension', 
                     'Relief from asthma', 'Prevents hysteria'], 
          'Kafi': ['Gives healthy mind and body', 'Brings joy', 'Mitigate insomina', 
                   'Reduces anxiety', 'Reduces hypertension'], 
          'Asavari': ['Reduce mental tension', 'Reduces hypertension', 
                      'Brings Creativity and Happiness', 'Cure low blood pressure', 
                      'Control psychological hazards and builds confidence', 'Used for constipation'],  
          'Todi': ['Reduce mental tension', 'Relief from headache', 'Relief from cough and cold', 
                   'Prevents hysteria', 'Reduces anxiety', 'Brings serenity'], 
          'Poorvi': ['Reduce mental tension', 'Mitigate insomina'],  
          'Marva': ['Gives healthy mind and body', 'Prevents hysteria', 
                    'Enhances compassion and patience'], 
          'Bhairavi': ['Relief from headache', 'Brings Creativity and Happiness', 
                       'Enhances compassion and patience', 'Relief from High fever', 
                       'Relief from phlegm, toothache, intestinal gas, sinusitis'], 
          'Bhairav': ['Relief from headache', 'Relief from cough and cold', 'Brings serenity', 
                      'It can be used for Emotional strength, Devotion and Peace, Restful Sleep, Tranquility, Relaxation & Rest'],
          'Mixed Thhat':['Not Applicable'],}
    
    
    therapy_number = set()
    
    for thaat in thaat_list:
        for t in info[thaat]:
            therapy_number.add(t)
    
   
    return list(therapy_number)

#print(healing_therapies(["Bilawal","Poorvi","Marva","Asavari"]))#test