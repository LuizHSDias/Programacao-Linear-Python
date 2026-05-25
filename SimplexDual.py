from pulp import *

# PROBLEMA DUAL
print("DUAL")

# CRIAÇÃO DO MODELO
model = LpProblem("Dual", LpMaximize)

# VARIÁVEIS
y1 = LpVariable("y1", lowBound=0)
y2 = LpVariable("y2", lowBound=0)

# FUNÇÃO OBJETIVO
model += 5*y1 + 4*y2

# RESTRIÇÕES
model += y1 + 3*y2 <= 4
model += 4*y1 + 2*y2 <= 5


# RESOLVER
model.solve(PULP_CBC_CMD(msg=True))

# RESULTADOS
print("\nSTATUS")
print(LpStatus[model.status])

print("\nVARIÁVEIS")
print(f"y1 = {y1.varValue:.2f}")
print(f"y2 = {y2.varValue:.2f}")

print("\nFUNÇÃO OBJETIVO")
print(f"W = {value(model.objective):.2f}")