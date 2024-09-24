def check_shuffle(x, y, z):
  if len(z) != len(x) + len(y):
    return False
  
  return check_shuffle_aux(x, y, z, 0, 0, 0)

def check_shuffle_aux(x, y, z, i, j, k):
  if k == len(z):
    return i == len(x) and j == len(y)
  
  if i < len(x) and z[k] == x[i]:
    if check_shuffle_aux(x, y, z, i + 1, j, k + 1):
      return True
  
  if j < len(y) and z[k] == y[j]:
    if check_shuffle_aux(x, y, z, i, j + 1, k + 1):
      return True
  
  return False
