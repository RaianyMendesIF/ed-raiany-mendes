# ed-fila-raiany-mendes

Implemente um simulador do algoritmo escalonador de processos Round-Robin. O algoritmo deve utilizar o conceito de FILAs implementada com listas simplesmente encadeadas, conforme exemplo da aula.

## Algoritmo Round-Robin

Uma aplicação clássica de filas na Ciência da Computação é o escalonamento de processos em sistemas operacionais, particularmente no algoritmo Round-Robin. Podemos compreender esse mecanismo por meio de uma analogia com o jogo infantil Batata Quente. Em vez de crianças formando uma roda, temos um conjunto de processos prontos para execução. Em vez de uma batata, temos um token de execução, que concede ao processo o direito de utilizar a CPU.
Considere um conjunto de K processos prontos para execução, organizados em uma fila Q. O processo na frente da fila é aquele que atualmente possui o token e pode executar por um intervalo fixo de tempo (quantum).

## O funcionamento é o seguinte:

- O processo no início da fila executa por um tempo máximo pré-definido MAX (quantum).
- Após esse período, se o processo ainda não terminou, ele é removido do início da fila e reinserido no final (operação dequeue seguida de enqueue).
- O próximo processo assume o início da fila e recebe o token.
- Se um processo termina sua execução durante seu quantum, ele é removido definitivamente da fila.

## O ciclo continua até que todos finalizem, dependendo do modelo adotado. Nesse contexto:

- A fila modela a lista de processos prontos.
- O token representa o direito exclusivo de acesso à CPU.
- A rotação da fila simula a política de justiça do escalonador.