from utils import rec_shuffle, mem_shuffle, bottom_up_shuffle

def main():
  cases = [
    (['A', 'B', 'C'], ['D', 'E', 'F'], ['A', 'B', 'C', 'D', 'E', 'F']),
    (['A', 'B'], ['1', '2'], ['A', '1', 'B', '2']),
    (['A', 'A', 'B'], ['A', 'B'], ['A', 'A', 'A', 'B', 'B']),
    (['A', 'B'], ['1', '2'], ['A', '2', '1', 'B']),
    (['A', 'B'], ['1', '2'], ['A', '1', 'B']),
    (['C', 'A', 'T'], ['D', 'O', 'G'], ['C', 'D', 'A', 'O', 'T', 'G']),
    (['A', 'B', 'C'], ['X', 'Y', 'Z'], ['A', 'X', 'B', 'C', 'Y']),
    (['A', 'A', 'A'], ['A', 'A', 'A'], ['A', 'A', 'A', 'A', 'A', 'A']),
    (['A', 'B', 'C'], ['X', 'Y', 'Z'], ['A', 'X', 'B', 'Y', 'C', 'Z']),
    (['1', '2'], ['3', '4'], ['1', '2', '3', '4', '5']),
  ]

  for i, (x, y, z) in enumerate(cases):
      print(f"\nEjemplo {i+1}: X = {x}, Y = {y}, Z = {z}")
      
      rec_res = rec_shuffle.check_shuffle(x, y, z)
      mem_res = mem_shuffle.check_shuffle(x, y, z)
      bot_res, index = bottom_up_shuffle.check_shuffle_bottom_up(x, y, z)
      
      print(f"Recursive result: {rec_res}")
      print(f"Memoized result: {mem_res}")
      print(f"Bottom up result: {bot_res}")
      if bot_res:
        print(f"\tMatched with: X{index[0]} + Y{index[1]}")

if __name__ == "__main__":
  main()
