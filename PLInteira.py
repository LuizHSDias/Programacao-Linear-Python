from pulp import *

# PROGRAMAÇÃO LINEAR INTEIRA
print("PLI - BRANCH AND BOUND")

# AEROPORTOS
airports = [
    'Aeroporto_A',
    'Aeroporto_B',
    'Aeroporto_C'
]

supply = {
    'Aeroporto_A': 300,
    'Aeroporto_B': 400,
    'Aeroporto_C': 200
}

# DESTINOS
destinations = [
    'Destino_1',
    'Destino_2',
    'Destino_3',
    'Destino_4'
]

demand = {
    'Destino_1': 200,
    'Destino_2': 150,
    'Destino_3': 250,
    'Destino_4': 200
}


# CUSTOS
costs = {

    ('Aeroporto_A', 'Destino_1'): 8,
    ('Aeroporto_A', 'Destino_2'): 6,
    ('Aeroporto_A', 'Destino_3'): 10,
    ('Aeroporto_A', 'Destino_4'): 7,

    ('Aeroporto_B', 'Destino_1'): 9,
    ('Aeroporto_B', 'Destino_2'): 12,
    ('Aeroporto_B', 'Destino_3'): 8,
    ('Aeroporto_B', 'Destino_4'): 11,

    ('Aeroporto_C', 'Destino_1'): 14,
    ('Aeroporto_C', 'Destino_2'): 7,
    ('Aeroporto_C', 'Destino_3'): 10,
    ('Aeroporto_C', 'Destino_4'): 12,
}


# MODELO
model = LpProblem("PLI_Branch_And_Bound", LpMinimize)

# ROTAS
routes = [
    (a, d)
    for a in airports
    for d in destinations
]

# VARIÁVEIS INTEIRAS
shipments = LpVariable.dicts("Enviar", routes, lowBound=0, cat='Integer')

# FUNÇÃO OBJETIVO
model += lpSum(
    costs[a, d] * shipments[a, d]
    for (a, d) in routes
)


# RESTRIÇÕES DE OFERTA
for a in airports:
    model += (
        lpSum(
            shipments[a, d]
            for d in destinations
        )
        <= supply[a]
    )

# RESTRIÇÕES DE DEMANDA
for d in destinations:
    model += (
        lpSum(
            shipments[a, d]
            for a in airports
        )
        >= demand[d]
    )


# RESOLVER
solver = PULP_CBC_CMD(msg=False)
model.solve(solver)

# STATUS
print("\nSTATUS")
print("----------------------")
print(LpStatus[model.status])

# RESULTADOS
if LpStatus[model.status] == "Optimal":

    print("\nROTAS")
    print("----------------------")

    for (a, d) in routes:

        if shipments[a, d].varValue > 0:

            print(
                f"{a} -> {d}: "
                f"{shipments[a, d].varValue}"
            )

    print("\nFUNÇÃO OBJETIVO")
    print("----------------------")

    print(
        f"Custo mínimo = "
        f"${value(model.objective):,.2f}"
    )

    print("\nOBSERVAÇÃO")
    print("----------------------")

    print(
        "O solver CBC utilizou "
        "Branch and Bound "
        "para encontrar a solução inteira ótima."
    )

else:

    print("\nNão existe solução viável para o problema.")

    print(
        "\nA demanda total excede "
        "a capacidade disponível dos aeroportos.")