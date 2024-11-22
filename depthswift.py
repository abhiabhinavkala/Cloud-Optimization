import random
import numpy as np
from deap import base, creator, tools, algorithms

creator.create("FitnessMulti", base.Fitness, weights=(-1.0, -1.0))  
creator.create("Individual", list, fitness=creator.FitnessMulti)

def init_individual():
    return [random.randint(2, 10) for _ in range(2)]  

def cost_function(TD, Cost_BW, C_L, p):
    total_bw_cost = TD * Cost_BW
    security_cost = C_L * np.prod(p)
    return total_bw_cost + security_cost

def depthswift_optimization(individual):

    matrix_A = np.random.rand(individual[0], individual[0])  
    matrix_B = np.random.rand(individual[1], individual[1])  

    num_secure_mult = 10
    Cost_BW = 0.2  
    C_L = 1.5  
    p = [0.8, 0.9]  

    TD = matrix_A.size + matrix_B.size  

    total_cost = cost_function(TD, Cost_BW, C_L, p)

    depth_optimization_factor = 1.2  

    optimized_cost = total_cost * depth_optimization_factor

    time_cost = 0.1  
    resource_cost = 0.1  

    return optimized_cost, resource_cost

toolbox = base.Toolbox()
toolbox.register("individual", tools.initIterate, creator.Individual, init_individual)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
toolbox.register("select", tools.selNSGA2)
toolbox.register("evaluate", depthswift_optimization)

def main():
    population = toolbox.population(n=50)  
    algorithms.eaMuPlusLambda(population, toolbox, mu=50, lambda_=100, cxpb=0.7, mutpb=0.2, ngen=100, 
                              stats=None, halloffame=None, verbose=True)

    for ind in population:
        print(ind.fitness.values)

if __name__ == "__main__":
    main()