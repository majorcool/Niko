def largest_altitude(gain: list[int]) -> int:
    alt = [0]
    for i in range(1, len(gain)+1):
        alt.append(alt[i-1] + gain[i-1])
    return max(alt)

print(largest_altitude([-4,-3,-2,-1,4,3,2]))