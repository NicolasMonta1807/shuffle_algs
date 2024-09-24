import random
import string
import time
import matplotlib.pyplot as plt

from utils import rec_shuffle, mem_shuffle, bottom_up_shuffle

# Generate random sequences
def generate_random_sequence(length):
    return ''.join(random.choices(string.ascii_uppercase, k=length))

# Datos de prueba
test_cases = [
    (10, 3),
    (20, 5),
    (50, 10),
    (100, 15),
    (1000, 3)
]

# Resultados para la gráfica
recursion_times = []
memoization_times = []
bottom_up_times = []

for z_size, num_experiments in test_cases:
    total_recursion_time = 0
    total_memoization_time = 0
    total_bottom_up_time = 0
    
    for _ in range(num_experiments):
        x_length = random.randint(1, z_size // 2)
        y_length = z_size - x_length
        
        x = generate_random_sequence(x_length)
        y = generate_random_sequence(y_length)
        
        # Generate a random shuffle sequence
        z = ''.join(random.sample(x + y, z_size))
        
        # Recursive
        start_time = time.perf_counter_ns()
        rec_shuffle.check_shuffle(x, y, z)
        total_recursion_time += (time.perf_counter_ns() - start_time)
        
        # Memoized
        start_time = time.perf_counter_ns()
        mem_shuffle.check_shuffle(x, y, z)
        total_memoization_time += (time.perf_counter_ns() - start_time)
        
        # Bottom up
        start_time = time.perf_counter_ns()
        bottom_up_shuffle.check_shuffle_bottom_up(x, y, z)
        total_bottom_up_time += (time.perf_counter_ns() - start_time)
    
    recursion_times.append(total_recursion_time / num_experiments)
    memoization_times.append(total_memoization_time / num_experiments)
    bottom_up_times.append(total_bottom_up_time / num_experiments)

# Graphic plotter
plt.figure(figsize=(10, 6))
plt.plot([z_size for z_size, _ in test_cases], recursion_times, marker='o', label='Recursivo')
plt.plot([z_size for z_size, _ in test_cases], memoization_times, marker='o', label='Memoizado')
plt.plot([z_size for z_size, _ in test_cases], bottom_up_times, marker='o', label='Bottom-Up')
plt.title('Tiempo de ejecución promedio de los algoritmos de check_shuffle')
plt.xlabel('|Z| (Tamaño de la secuencia Z)')
plt.ylabel('Tiempo promedio (nanosegundos)')
plt.legend()
plt.grid()
plt.show()

print("Times: ")
print(f"Rec: {recursion_times}")
print(f"Mem: {memoization_times}")
print(f"Bottom: {bottom_up_times}")
