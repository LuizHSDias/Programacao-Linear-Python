# Programação Linear com Python

Projeto desenvolvido utilizando Python, PuLP e CBC Solver para implementação de métodos de otimização aplicados à Pesquisa Operacional.

## Objetivo

O projeto apresenta exemplos práticos de:

- Programação Linear (PL)
- Problema Primal e Dual
- Simplex Dual
- Programação Linear Inteira (PLI)
- Branch and Bound
- Análise Dual
- Problema de Transporte

---

# Tecnologias Utilizadas

- Python 3
- PuLP
- CBC Solver

---

# Estrutura do Projeto

```text
Programacao-Linear-Python/
│
├── primal.py
├── dual.py
├── pli_branch_bound.py
├── README.md
└── requirements.txt
```

---

# 1. Problema Primal

Arquivo:

```text
primal.py
```

O problema primal realiza a minimização da função objetivo:

\[
Z = 4x_1 + 5x_2
\]

Sujeito às restrições:

\[
x_1 + 4x_2 \ge 5
\]

\[
3x_1 + 2x_2 \ge 4
\]

O modelo também apresenta:

- análise dual;
- preços-sombra;
- folgas das restrições.

---

# 2. Problema Dual

Arquivo:

```text
dual.py
```

O problema dual foi modelado a partir do primal utilizando dualidade da Programação Linear.

Função objetivo:

\[
W = 5y_1 + 4y_2
\]

Sujeito às restrições:

\[
y_1 + 3y_2 \le 4
\]

\[
4y_1 + 2y_2 \le 5
\]

---

# 3. Programação Linear Inteira (PLI)

Arquivo:

```text
pli_branch_bound.py
```

O problema de transporte da companhia aérea foi modelado utilizando:

- variáveis inteiras;
- minimização de custos;
- restrições de oferta e demanda.

O solver CBC utiliza automaticamente o algoritmo:

# Branch and Bound

para encontrar a solução inteira ótima.

---

# Solver CBC

O projeto utiliza o solver CBC (Coin-or Branch and Cut), responsável pela resolução dos problemas de otimização linear e inteira.

O CBC pode utilizar algoritmos como:

- Simplex
- Dual Simplex
- Branch and Bound
- Branch and Cut

---

# Instalação

Clone o repositório:

```bash
git clone https://github.com/LuizHSDias/Programacao-Linear-Python.git
```

Acesse a pasta:

```bash
cd Programacao-Linear-Python
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

# Executando os Projetos

## Problema Primal

```bash
python primal.py
```

## Problema Dual

```bash
python dual.py
```

## PLI - Branch and Bound

```bash
python pli_branch_bound.py
```

---

# Conceitos Aplicados

- Pesquisa Operacional
- Programação Linear
- Dualidade
- Simplex Dual
- Otimização
- Programação Linear Inteira
- Branch and Bound
- Solver CBC

---

# Autor

Luiz Henrique Dias