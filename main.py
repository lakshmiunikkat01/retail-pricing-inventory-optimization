from data.generate_data import generate_data
from src.model import solve_milp
from src.heuristic import heuristic_solution
from src.sensitivity import capacity_sensitivity
from src.visualization import plot_quantities, plot_sensitivity

data = generate_data(n=5)

warehouse_capacity = 600
budget = 50000

results, optimal_profit = solve_milp(data, warehouse_capacity, budget)

print("Optimal Solution")
print(results)
print("Optimal Profit:", optimal_profit)

heuristic_profit = heuristic_solution(data)

print("Heuristic Profit:", heuristic_profit)

improvement = ((optimal_profit - heuristic_profit) / heuristic_profit) * 100
print("Improvement %:", improvement)

capacities = [400, 500, 600, 700, 800]
profits = capacity_sensitivity(data, capacities, budget)

plot_quantities(results)
plot_sensitivity(capacities, profits)

results.to_csv("results/output.csv", index=False)
