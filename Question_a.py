from pulp import *

# Initialize Class, Define Vars., and Objective
model = LpProblem("Glass_Manufacturing_Industries_Profits",LpMaximize)
# Define variables
A = LpVariable('A', lowBound=0)
B = LpVariable('B', lowBound=0)

# Define Objetive Function: Profit on Product A and B
model += 60 * A + 50 * B

# Constraint 1
model += 4 * A + 10 * B <= 100

# Constraint 2
model += 2 * A + 1 * B <= 22

# Constraint 3
model += 3 * A + 3 * B <= 39

# Solve Model
model.solve()

print("Model Status:{}".format(LpStatus[model.status]))
print("Objective = ", value(model.objective))

for v in model.variables():
    print(v.name,"=", v.varValue)