
def playing_time(thaat_list):
  info={"Bilawal":["Anytime"],
        "Kalyan":["Anytime"],
        "Khamaj":["Afternoon","Evening"],
        "Kafi":["Anytime"],
        "Asavari":["Morning","Afternoon","Evening"],
        "Todi":["Morning","Evening"],
        "Poorvi":["Anytime"],
        "Marva":["Morning","Night"],
        "Bhairavi":["Anytime"],
        "Bhairav":["Morning","Afternoon"],}
  
  time=set()

  for thaat in thaat_list:
    for t in info[thaat]:
      time.add(t)

  return list(time)


#print(playing_time(["Marva","Bhairav"]))#test