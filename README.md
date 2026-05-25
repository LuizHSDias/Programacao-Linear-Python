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
├── SimplexPrimal.py
├── SimplexDual.py
├── PLInteira.py
├── README.md
```

---

# 1. Problema Primal

Arquivo:

```text
SimplexPrimal.py
```

O problema primal realiza a minimização da função objetivo:

O modelo também apresenta:

- análise dual;
- preços-sombra;
- folgas das restrições.

---

# 2. Problema Dual

Arquivo:

```text
SimplexDual.py
```

O problema dual foi modelado a partir do primal utilizando dualidade da Programação Linear.

---

# 3. Programação Linear Inteira (PLI)

Arquivo:

```text
PLInteira.py
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

## Instalação

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

Caso o comando `pip` não funcione no Windows:

```bash
py -m pip install -r requirements.txt
```

# Executando os Projetos

## Problema Primal

```bash
python SimplexPrimal.py
```

## Problema Dual

```bash
python SimplexDual.py
```

## PLI - Branch and Bound

```bash
python PLInteira.py
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
- João Carlos Ferreira Martins
- Luiz Henrique Dias