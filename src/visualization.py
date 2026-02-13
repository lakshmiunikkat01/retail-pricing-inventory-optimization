import matplotlib.pyplot as plt

def plot_quantities(results_df):

    plt.figure()
    plt.bar(results_df["product"], results_df["quantity"])

    plt.title("Optimized Order Quantities")
    plt.xlabel("Product")
    plt.ylabel("Quantity")
    plt.show()

def plot_sensitivity(capacities, profits):

    plt.figure()
    plt.plot(capacities, profits)
    plt.title("Capacity vs Profit")
    plt.xlabel("Warehouse Capacity")
    plt.ylabel("Profit")
    plt.show()
