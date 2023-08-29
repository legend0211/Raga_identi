from helper.jaccard_similarity import jaccard_similarity
from helper.check_similarity import check_similarity

def closest_array(str_arr1, str_arr2):

    # Finding jaccard similarity of the obtained notes with the database notes
    similarities = []
    for i in range(len(str_arr2)):
        similarity = jaccard_similarity(str_arr1, str_arr2[i])
        similarities.append((similarity, i))
    similarities.sort(key=lambda x: x[0], reverse=True)
    
    ret = []
    ret.append(similarities[0][1])
    # print(len(similarities))
    for i in range(len(similarities)):
        if(i==0):
            continue
        if(similarities[i-1][0]==similarities[i][0]):
            ret.append(similarities[i][1])
        else:
            break
    
    # Now, for tie cases we calculate the similarity by taking the closest among the possible options
    similarities = []
    for i in ret:
        similarity = check_similarity(str_arr1, str_arr2[i])
        similarities.append((similarity, i))
    similarities.sort(key=lambda x: x[0], reverse=False)
    
    # Taking the thaats that have lowest difference, if we still have multiple thaats then we are printing both of them as possible
    ret = []
    print(similarities)
    ret.append(similarities[0][1])
    for i in range(len(similarities)):
        if(i==0):
            continue
        if(similarities[i-1][0]==similarities[i][0]):
            ret.append(similarities[i][1])
        else:
            break
    return ret
