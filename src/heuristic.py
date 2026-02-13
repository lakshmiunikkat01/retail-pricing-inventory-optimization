def heuristic_solution(data):

    profit = 0

    for i in data.index:
        quantity = data.loc[i, "demand"]
        price = data.loc[i, "min_price"]
        unit_profit = price - data.loc[i, "holding_cost"] - data.loc[i, "ordering_cost"]
        profit += unit_profit * quantity

    return profit
