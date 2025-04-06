from pulp import LpMaximize, LpProblem, LpVariable

# Define the problem
model = LpProblem(name="manufacturing-optimization", sense=LpMaximize)

# Decision variables
x = LpVariable(name="X", lowBound=10, cat="Integer")
y = LpVariable(name="Y", lowBound=0, cat="Integer")

# Objective function (profit maximization)
model += (240*x + 160*x , "Profit")

# Constraints
model += (15*x + 20*y <= 2400, "Machine_Time_Limit")
model += (20*x + 30*y <= 2100, "Craftsman_Time_Limit")

# Solve the problem
model.solve()

# Print results
print(f"Optimal Production: X = {x.varValue}, Y = {y.varValue}")
print(f"Maximum Profit: £{model.objective.value()}")