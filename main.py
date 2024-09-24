from utils import rec_shuffle

def main():
  x = ['C', 'A', 'S', 'A']
  y = ['C', 'A', 'R', 'R', 'O']
  
  z = ['C', 'C', 'A', 'S', 'A', 'R', 'R', 'A', 'O']
  
  resultado = rec_shuffle.check_shuffle(x, y, z)
  
  print(f"The shuffle is {'valid' if resultado else 'invalid'}")

if __name__ == "__main__":
  main()