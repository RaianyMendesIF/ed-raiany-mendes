# Atividade: Estrutura de Dados - Pilhas (Stacks)

Este repositório contém a resolução de dois problemas clássicos de lógica de programação utilizando a estrutura de dados **Pilha (Stack)**, baseada no princípio **LIFO** (*Last In, First Out*).

---

## 📋 Exercícios

### 1. Inversão de String
O objetivo é inverter uma palavra utilizando o comportamento natural de uma pilha.

* **Lógica:**
    1. Percorrer a palavra caractere por caractere.
    2. **Empilhar (push)** cada caractere na pilha.
    3. **Desempilhar (pop)** todos os caracteres até que a pilha esteja vazia, concatenando-os na saída.
* **Exemplo:**
    - **Entrada:** `ALGORITMO`
    - **Saída:** `OMTIROGLA`

---

### 2. Verificação de Parênteses
Implementação de um algoritmo que valida se os parênteses em uma expressão matemática estão devidamente balanceados.

* **Lógica:**
    1. Ao encontrar um parêntese de abertura `(`, ele deve ser **empilhado**.
    2. Ao encontrar um parêntese de fechamento `)`:
        - Se a pilha estiver vazia, a expressão é **inválida** (fechamento sem abertura).
        - Se não estiver vazia, remove-se o topo da pilha (**pop**).
    3. Ao final da leitura, se a pilha estiver vazia, a expressão é **válida**. Se sobrar algo na pilha, é **inválida**.

#### Casos de Teste:

| Expressão | Status |
| :--- | :--- |
| `((A+B) * C)` | ✅ Válido |
| `(A+B))` | ❌ Inválido (Sobra fechamento) |
| `((A+B)` | ❌ Inválido (Sobra abertura) |

---

## 🛠️ Tecnologias Utilizadas
* Linguagem: [Inserir Linguagem Ex: Python/C++/Java]
* Estrutura: Pilha Dinâmica ou Estática

---
*Repositório criado para fins acadêmicos.*