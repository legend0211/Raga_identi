
def string_parser(temp):
  ans=""
  for key in temp:
    val=temp[key]
    ans+=f"{key}:"
    for i in range(len(val)):
      if(i==len(val)-1): ans+=val[i]
      else: ans+=val[i]+","
    ans+="\n"
  return ans

# dict={
#   "key1":["val11","val22","val33"],
#   "key2":["Rohan","Soham"],
# }
# print(string_parser(dict))