import random

# -------------------------------
# Generate a random knapsack problem
# -------------------------------
def generate_problem(num_items=6):
    # Each item is represented as a tuple: (weight, value)
    items = []
    for i in range(num_items):
        weight = random.randint(1, 20)   # Random weight between 1 and 20 kg
        value = random.randint(10, 100)    # Random price/value between 10 and 100
        items.append((weight, value))
    capacity = random.randint(20, 100)      # Random maximum capacity for the knapsack
    return items, capacity

# -------------------------------
# 1. 0-1 Knapsack: Dynamic Programming Solution
# -------------------------------
def knapsack_01(items, capacity):
    n = len(items)
    # DP table where dp[i][w] is the max value for first i items and capacity w.
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Fill the DP table step-by-step.
    for i in range(1, n + 1):
        wt, val = items[i-1]
        for w in range(1, capacity + 1):
            if wt > w:
                dp[i][w] = dp[i-1][w]  # Cannot include item i-1
            else:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-wt] + val)
    
    # Traceback to determine which items are included.
    w = capacity
    chosen_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            chosen_items.append(i-1)
            w -= items[i-1][0]

    chosen_items.reverse()  # To display in original order
    max_value = dp[n][capacity]
    return max_value, chosen_items, dp

# -------------------------------
# 2. Fractional Knapsack: Greedy Algorithm Solution
# -------------------------------
def knapsack_fractional(items, capacity):
    # Compute value/weight ratio for each item along with original index.
    items_with_ratio = []
    for idx, (wt, val) in enumerate(items):
        ratio = val / wt
        items_with_ratio.append((ratio, wt, val, idx))
    
    # Sort items based on the ratio in descending order.
    items_with_ratio.sort(key=lambda x: x[0], reverse=True)
    
    current_capacity = capacity
    total_value = 0
    fractions = []  # List to record (index, fraction taken, weight, value)
    
    for ratio, wt, val, idx in items_with_ratio:
        if current_capacity == 0:
            break
        if wt <= current_capacity:
            # Take whole item.
            fractions.append((idx, 1, wt, val))
            current_capacity -= wt
            total_value += val
        else:
            # Take fraction of the item.
            fraction = current_capacity / wt
            fractions.append((idx, fraction, current_capacity, val * fraction))
            total_value += val * fraction
            current_capacity = 0

    return total_value, fractions

def main():
    # Generate a random problem
    items, capacity = generate_problem()
    
    print("Generated Knapsack Problem:")
    print(f"Knapsack Capacity: {capacity}")
    print("Items (index: weight, value):")
    for i, (wt, val) in enumerate(items):
        print(f"  Item {i}: {wt} kg, ${val}")
    print("\n---------------------------------------------------------------------------------------------\n")
    
    # Solve 0-1 Knapsack
    print("Solving 0-1 Knapsack using Dynamic Programming...")
    max_value_01, chosen_items, dp_table = knapsack_01(items, capacity)
    print(f"Maximum Value (0-1 Knapsack): {max_value_01}")
    print("Items chosen (by index):", chosen_items)
    
    # Display DP table
    print("\nDP Table:")
    for row in dp_table:
        print(row)
    
    print("\n---------------------------------------------------------------------------------------------\n")
    
    # Solve Fractional Knapsack
    print("Solving Fractional Knapsack using Greedy Algorithm...")
    total_value_frac, fractions = knapsack_fractional(items, capacity)
    print(f"Maximum Value (Fractional Knapsack): {total_value_frac:.2f}")
    print("Items taken (by index with fraction taken):")
    for idx, fraction, wt_taken, value_taken in fractions:
        print(f"  Item {idx}: {fraction*100:.1f}% taken, Weight = {wt_taken}, Value = {value_taken:.2f}, Value/weight = {value_taken/ wt_taken:.1f}")

if __name__ == "__main__":
    main()
