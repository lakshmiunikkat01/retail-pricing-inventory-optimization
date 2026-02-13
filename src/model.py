import pulp
import pandas as pd
import numpy as np


def solve_milp(data, warehouse_capacity, budget):

    price_levels = 3

    model = pulp.LpProblem("Retail_Pricing_Optimization", pulp.LpMaximize)

    z = {}
    y = {}

    for i in data.index:
        base_price = data.loc[i, "min_price"]

        for k in range(price_levels):
            price = base_price + k * 5
            demand = max(50, data.loc[i, "demand"] - k * 30)

            z[(i, k)] = pulp.LpVariable(f"z_{i}_{k}", lowBound=0, cat='Integer')
            y[(i, k)] = pulp.LpVariable(f"y_{i}_{k}", cat='Binary')

    model += pulp.lpSum(
        (data.loc[i, "min_price"] + k * 5
         - data.loc[i, "holding_cost"]
         - data.loc[i, "ordering_cost"]) * z[(i, k)]
        for i in data.index
        for k in range(price_levels)
    )

    for i in data.index:
        model += pulp.lpSum(y[(i, k)] for k in range(price_levels)) == 1

    for i in data.index:
        for k in range(price_levels):
            demand = max(50, data.loc[i, "demand"] - k * 30)
            model += z[(i, k)] <= demand * y[(i, k)]

    model += pulp.lpSum(
        data.loc[i, "storage"] * z[(i, k)]
        for i in data.index
        for k in range(price_levels)
    ) <= warehouse_capacity

    model += pulp.lpSum(
        data.loc[i, "ordering_cost"] * z[(i, k)]
        for i in data.index
        for k in range(price_levels)
    ) <= budget

    model.solve(pulp.PULP_CBC_CMD(msg=False))

    results = []

    for i in data.index:
        for k in range(price_levels):
            if y[(i, k)].varValue == 1:
                results.append({
                    "product": data.loc[i, "product"],
                    "chosen_price": data.loc[i, "min_price"] + k * 5,
                    "quantity": z[(i, k)].varValue
                })

    total_profit = pulp.value(model.objective)

    return pd.DataFrame(results), total_profit
