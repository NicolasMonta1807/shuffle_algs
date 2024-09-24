from utils import rec_shuffle, mem_shuffle

def main():
  x = ['C', 'A', 'S', 'A']
  y = ['C', 'A', 'R', 'R', 'O']
  
  z = ['C', 'C', 'A', 'S', 'A', 'R', 'R', 'A', 'O']
  
  rec_res = rec_shuffle.check_shuffle(x, y, z)
  mem_res = mem_shuffle.check_shuffle(x, y, z)
  
  print(f"The shuffle is {'valid' if rec_res else 'invalid'} (Recursive)")
  print(f"The shuffle is {'valid' if rec_res else 'invalid'} (Memo)")

if __name__ == "__main__":
  main()