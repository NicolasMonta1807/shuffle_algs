def check_shuffle(x, y, z):
    if len(z) != len(x) + len(y):
        return False
    
    # Create memory with |x| * |y| size
    dp = [[None] * (len(y) + 1) for _ in range(len(x) + 1)]
    
    return check_shuffle_aux(x, y, z, len(x), len(y), dp)

def check_shuffle_aux(x, y, z, i, j, dp):
    if dp[i][j] is not None:
        return dp[i][j]
    
    if i == 0 and j == 0:
        dp[i][j] = True
        return True

    if i > 0 and z[i + j - 1] == x[i - 1]:
        if check_shuffle_aux(x, y, z, i - 1, j, dp):
            dp[i][j] = True
            return True
    
    if j > 0 and z[i + j - 1] == y[j - 1]:
        if check_shuffle_aux(x, y, z, i, j - 1, dp):
            dp[i][j] = True
            return True
    
    dp[i][j] = False
    return False