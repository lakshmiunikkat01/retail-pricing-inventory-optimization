# Retail Pricing & Inventory Optimization using MILP

## Problem Statement

Retailers must decide:

- How much inventory to order per product  
- Which price level to select  
- While respecting warehouse capacity and budget constraints  

The goal is to maximize total profit using Mixed Integer Linear Programming (MILP).

---

## Approach

This project models retail pricing and inventory decisions as a MILP problem using:

- Integer quantity decision variables  
- Binary price level selection  
- Elastic demand modeling  
- Warehouse capacity constraints  
- Budget constraints  

The problem is solved using the CBC solver via PuLP.

---

## Mathematical Formulation

### Decision Variables

- z_ik: Quantity sold for product i at price level k (Integer)  
- y_ik: Binary variable indicating selected price level  

### Objective Function

Maximize:

Sum over (Price_ik − Holding_i − Ordering_i) × z_ik

### Constraints

- Only one price level selected per product  
- Demand limit based on price level  
- Warehouse capacity constraint  
- Budget constraint  
- Non-negativity and integrality conditions  

---

## Results

- The optimizer reallocates storage toward high-margin products  
- Low profitability SKUs are automatically deprioritized  
- Solver converges in under 0.1 seconds  
- Demonstrates realistic retail trade-off behavior  

---

## Tech Stack

- Python  
- PuLP (MILP modeling)  
- CBC Solver  
- Pandas  
- NumPy  
- Matplotlib  

---

## How to Run

1.Clone the repository:
git clone <your-repo-link>
cd retail-pricing-inventory-optimization

2.Install dependencies:
pip install -r requirements.txt

3.Run:
python main.py

