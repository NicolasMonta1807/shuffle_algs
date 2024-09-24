def check_shuffle(x, y, z):
    if len(z) != len(x) + len(y):
        return False
    
    memo = {}
    
    return check_shuffle_aux(x, y, z, 0, 0, 0, memo)

def check_shuffle_aux(x, y, z, i, j, k, memo):
    if k == len(z):
        return i == len(x) and j == len(y)
    
    if (i, j, k) in memo:
        return memo[(i, j, k)]
    
    is_valid = False
    
    if i < len(x) and z[k] == x[i]:
        is_valid = check_shuffle_aux(x, y, z, i + 1, j, k + 1, memo)
    
    if not is_valid and j < len(y) and z[k] == y[j]:
        is_valid = check_shuffle_aux(x, y, z, i, j + 1, k + 1, memo)
    
    memo[(i, j, k)] = is_valid
    
    return is_valid
