# Simulador de Fila de Atendimento

Exercício para a disciplina de POO, onde foi implementado um sistema de fila.

## Funcionalidades
- Adicionar clientes
- Atender próximo (priorizando fila prioritária)
- Listar filas
- Gerar relatório

## Explicação de decisões
Optei por usar a estrutura collections.deque pois é mais eficiente em operações de inserção e remoção em filas. Foram criadas duas filas: uma prioritária e uma normal, para que os clientes sejam organizados de acordo com as regras de prioridade.
Para a regra de prioridade foi usado operadores lógicos (and, or, not), assim se um cliente tiver >= 60 anos ou for gestante ou PCD ele é considerado prioritário. Essa verificação foi encapsulada em uma função, para que o código ficasse mais organizado e fosse mais fácil a manutenção.
O menu interativo permite adicionar clientes, atender o próximo (priorizando a fila prioritária), listar os clientes em espera e gerar relatórios com estatísticas de atendimento.
O relatório inclui a quantidade de atendimentos realizados, distribuição entre prioritários e normais, e o percentual de atendidos prioritários.
Também foi incluído tratamento de erros na entrada de dados, como validação de idade, para evitar que o programa seja interrompido por valores inválidos.
