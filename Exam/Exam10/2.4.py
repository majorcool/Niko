def min_cost_stair(costs, nowpos, nowcost):
    if nowpos == len(costs) -1 or nowpos == len(costs) -2:
        return nowcost + costs[nowpos]
    return min(min_cost_stair(costs, nowpos+1, nowcost + costs[nowpos]), min_cost_stair(costs, nowpos+2, nowcost + costs[nowpos]))

c = 10,14,17,9,16,2,0,8,13,1,0,18,3,19,20,4
print(min(min_cost_stair(c, 0, 0), min_cost_stair(c, 1, 0)))