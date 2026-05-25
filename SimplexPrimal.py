from pulp import *

print("PRIMAL")

model = LpProblem("Primal", LpMinimize)

x1 = LpVariable("x1", lowBound=0)
x2 = LpVariable("x2", lowBound=0)

model += 4*x1 + 5*x2

model += x1 + 4*x2 >= 5, "Restricao_1"
model += 3*x1 + 2*x2 >= 4, "Restricao_2"

model.solve(PULP_CBC_CMD(msg=False))

print("\nSTATUS")
print(LpStatus[model.status])

print("\nVARIÁVEIS")
print(f"x1 = {x1.varValue:.2f}")
print(f"x2 = {x2.varValue:.2f}")

print("\nFUNÇÃO OBJETIVO")
print(f"Z = {value(model.objective):.2f}")

# ANÁLISE DUAL
print("\nANÁLISE DUAL")

for nome, restricao in model.constraints.items():
    print(f"\n{nome}")
    print(f"Preço-sombra = {restricao.pi:.2f}")
    print(f"Folga = {restricao.slack:.2f}")