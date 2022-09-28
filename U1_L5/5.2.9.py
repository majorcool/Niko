def plunge_scr(ratings,difficulty):
    if len(ratings) != 7:
        return False
    ratings_list = list(ratings) # tuple?
    ratings_list.sort()
    ratings_list.pop(0)
    ratings_list.pop(0)
    ratings_list.pop()
    ratings_list.pop()
    return ((ratings_list[0]+ratings_list[1]+ratings_list[2])*difficulty)

print(plunge_scr([1,2,3,4,5,6,7],3.1415926))