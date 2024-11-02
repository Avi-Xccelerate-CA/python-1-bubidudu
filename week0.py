# week 0 problem 1
# create a function that returns a list of (vitamins,injections) tuples for each attribute that they need.
# Complete problem statement in README.mds


# your input type should be a list,
# output should also be a list containing tuples
# Example:
# input: [250, 0, 250, 0, 0, 0]
# expected output: [(25,0),(0,0),(25,0),(0,0),(0,0),(0,0)]
# input: [500, 1, 2, 3, 4, 5]
#expected output: "No medicine given"
# HINT: using % operator to find remainder may be helpful
    #YOUR SOLUTION STARTS HERE
# your input type should be a list,
# output should also be a list containing tuples
# Example:
# input: [250, 0, 250, 0, 0, 0]
# expected output: [(25,0),(0,0),(25,0),(0,0),(0,0),(0,0)]
# input: [500, 1, 2, 3, 4, 5]
# expected output: "No medicine given"
# HINT: using % operator to find remainder may be helpful
# YOUR SOLUTION STARTS HERE
def dose(needs):
    # Check if any attribute exceeds 250 or if the total points exceed 500
    if any(attr >= 250 for attr in needs) or sum(needs) > 500:
        return "No medicine given"
    
    result = []
    for attr in needs:
        # Calculate the number of vitamins needed (each vitamin increases by 10)
        vitamins = attr // 10
        # Calculate the number of injections needed (remainder)
        injections = attr % 10
        result.append((vitamins, injections))
    
    return result
    #YOUR SOLUTION ENDS HERE

