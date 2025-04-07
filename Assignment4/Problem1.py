from pulp import LpMaximize, LpProblem, LpVariable

# Define the problem
model = LpProblem(name="manufacturing-optimization", sense=LpMaximize)

# Decision variables
x = LpVariable(name="X", lowBound=10, cat="Continuous")
y = LpVariable(name="Y", lowBound=0, cat="Continuous")

# Objective function (profit maximization)
model += (175*x - (20/3)*x + 290*y - (100/3)*y, "Profit")

# Constraints
model += (15*x + 20*y <= (40*60), "Machine_Time_Limit")
model += (20*x + 30*y <= (35*60), "Craftsman_Time_Limit")

# Solve the problem
model.solve()

# Print results
print(f"Optimal Production: X = {x.varValue}, Y = {y.varValue}")
print(f"Maximum Profit: £{model.objective.value()}")