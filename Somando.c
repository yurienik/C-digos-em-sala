//Bliblioteca
#include <stdio.h>
//Função para executar o código
int main ()
{
    //reservar uma varíavel
    int n1;
    //Mostrar mensagem na tela
    printf("Insira o primeiro número\n");
    //Informar o valor entregue do usuário para a variável livre
    scanf("%d", &n1);
    //reserva de variável
    int n2;
    //Mostrar mensagem na tela
    printf("Insira o segundo número\n");
    //Informar o valor entregue do usuário para a variável livre
    scanf("%d", &n2);
    //variável que armazena o resulatado das somas dadas
    int n3 = n1 + n2;
    //Demonstra na tela o resultado completo, mesclando mensagem e variáveis qualquer
    printf("A partir do primeiro número %d e do segundo número sendo %d, a soma dos dois é %d", n1, n2, n3);
    //fechamento de código
    return 0;
}