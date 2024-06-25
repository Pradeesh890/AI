import random

target = input("Enter the target string: ")
pop_size = 100
mut_rate = 0.01

genes = ''.join([chr(i) for i in range(32, 127)])

population = [''.join([random.choice(genes) for _ in range(len(target))]) for _ in range(pop_size)]

def calc_fitness(member):
    return sum([1 for i in range(len(target)) if member[i] == target[i]])

gen = 1

while True:
    best_member = max(population, key=calc_fitness)
    best_fitness = calc_fitness(best_member)
    print(f"Generation {gen} - Best: {best_member}, Fitness: {best_fitness}")

    if best_fitness == len(target):
        print("Target achieved!")
        break

    elite_count = int(0.1 * pop_size)
    elite = sorted(population, key=calc_fitness, reverse=True)[:elite_count]
    new_population = elite[:]

    while len(new_population) < pop_size:
        parent1, parent2 = random.choices(population, k=2)
        crossover_point = random.randint(1, len(target) - 1)
        child = parent1[:crossover_point] + parent2[crossover_point:]
        child = ''.join([char if random.random() > mut_rate else random.choice(genes) for char in child])
        new_population.append(child)
        
    population = new_population
    gen += 1
