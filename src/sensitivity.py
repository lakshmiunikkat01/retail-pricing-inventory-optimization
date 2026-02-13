from src.model import solve_milp

def capacity_sensitivity(data, capacities, budget):

    profits = []

    for cap in capacities:
        _, profit = solve_milp(data, cap, budget)
        profits.append(profit)

    return profits
