def standout_ideas(idea_cat):
    idea_sum_li = []
    best_idea = None
    for idea_li in idea_cat.values():
        idea_sum_li.append(sum(idea_li))
    idea_sum_li.sort(reverse=True)
    idea_sum_li = idea_sum_li[0:3]
    #print(idea_sum_li)

    idea_li = []
    for i in idea_sum_li:
        for j in idea_cat:
            if sum(idea_cat[j]) == i:
                idea_li.append(j)
                del idea_cat[j]
                break

    return(idea_li)

        

idea_cat = {
    "id1" : [2, 1, 2, 3],
    "id2" : [1, 3, 3, 1],
    "id3" : [2, 2, 1, 4], 
    "id4" : [2, 1, 1, 1]
    }

idea_li = standout_ideas(idea_cat)

for idea in idea_li:
    print(idea)
