from utils import rec_shuffle, mem_shuffle, bottom_up_shuffle

def main():
  examples = [
    (['a', 'b'], ['x', 'y'], ['a', 'x', 'b', 'y']),  
    (['a', 'b'], ['x', 'y'], ['a', 'b', 'x', 'y']),  
    (['a', 'b'], ['x', 'y'], ['a', 'x', 'y', 'b']),  
    (['a', 'b'], ['x', 'y'], ['x', 'a', 'b', 'y']),  
    (['a', 'b'], ['x', 'y'], ['x', 'y', 'a', 'b']),  
    (['a', 'b'], ['x', 'y'], ['a', 'y', 'b', 'x']),
  ]

  for i, (x, y, z) in enumerate(examples):
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
