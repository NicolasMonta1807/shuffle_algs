def check_shuffle_bottom_up(x, y, z):
    if len(z) != len(x) + len(y):
        return False, [], []
    
    dp = [[False] * (len(y) + 1) for _ in range(len(x) + 1)]
    
    # True if element can be matched with X. False if element can be matched with Y
    trace = [[None] * (len(y) + 1) for _ in range(len(x) + 1)]
    
    # Empty subsequence. Base case
    dp[0][0] = True
    
    for i in range(len(x) + 1):
        for j in range(len(y) + 1):
            if i > 0 and z[i + j - 1] == x[i - 1] and dp[i - 1][j]:
                dp[i][j] = True
                trace[i][j] = True
            
            if j > 0 and z[i + j - 1] == y[j - 1] and dp[i][j - 1]:
                dp[i][j] = True
                trace[i][j] = False
    
    # Nor X or Y could be matched
    if not dp[len(x)][len(y)]:
        return False, []
    
    return True, mem_analysis(trace, len(x), len(y))

def mem_analysis(trace, i, j):
   
    # Mem-analysis
    x_index = []
    y_index = []
        
    while i > 0 or j > 0:
        # Matched from X
        if trace[i][j] == True:
            x_index.append(i + j)
            i -= 1
        # Matched from Y
        else:
            y_index.append(i + j)
            j -= 1

    x_index.reverse()
    y_index.reverse()
    
    return x_index, y_index
