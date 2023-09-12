
def playing_time(thaat_list):
  thaat = ["Bilawal", "Kalyan", "Khamaj", "Kafi", "Asavari", "Todi", "Poorvi", "Marva", "Bhairavi", "Bhairav"]

  playing_time=["Anytime","Morining","Afternoon","Evening","Night"]

  possible_choice=[[0],[0],[3,4],[1],[1,2,3],[1,3],[1],[1,4],[0],[1,2]]

  time=set()

  for i in range(len(thaat)):
    if thaat[i] in thaat_list:
      for j in possible_choice[i]:
        time.add(playing_time[j])

  return list(time)


print(playing_time(["Bhairavi","Kalyan"]))