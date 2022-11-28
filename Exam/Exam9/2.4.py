def calculate_tax(brackets: list[list[int]], income: int) -> float:
    upperbound_bracket_index = 0
    for i in range(len(brackets)):
        if income > brackets[i][0]:
            upperbound_bracket_index = i
    upperbound_bracket_index += 1
    #print("upper bound",upperbound_bracket_index)
    total_tax = 0
    if income < brackets[0][0]:
        #print("too poor," , income * brackets[0][1])
        return income * brackets[0][1]
    total_tax += brackets[0][0] * brackets[0][1]
    #print("first stage", brackets[0][0] * brackets[0][1])
    for i in range(1, upperbound_bracket_index ):
        total_tax += (brackets[i][0] - brackets[i-1][0]) * brackets[i][1]
        #print("stage index= ", i, "tax +=" ,(brackets[i][0] - brackets[i-1][0]) * brackets[i][1])
    total_tax += (income - brackets[upperbound_bracket_index - 1][0]) * brackets[upperbound_bracket_index][1]
    #print("last stage, amount = ", income - brackets[upperbound_bracket_index - 1][0], "rate = ",brackets[upperbound_bracket_index][1])
    return total_tax


print( calculate_tax([[3,50],[7,10],[12,25]], 7))