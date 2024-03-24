from scipy.optimize import linprog
c = [-1, 4]
A = [[-3, 1], [1, 2]]
b = [6, 4]
x0_bounds = (None, None)
x1_bounds = (-3, None)
res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds])
res.fun
# -22.0
res.x
# array([10., -3.])
res.message
# 'Optimization terminated successfully. (HiGHS Status 7: Optimal)'
res.ineqlin
eps = 0.05
b[1] += eps
linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds]).fun
b = [6, 4]  # reset to original values
b[0] -= 39
linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds]).fun