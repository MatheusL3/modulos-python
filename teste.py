from moeda.banco import bdopcoes
from moeda.numeros import calcular
from moeda.formatacoes import formatacao

def ciclo(valor,aumentar=0,diminuir=0):
    funcao = bdopcoes.asopcoes()
    print("Agora selecione a função que desejas, sendo: ")
    funcao_escolhida = int(input(print(funcao)))

    status = True if ((str(input(print("Deseja que este numero venha formatado?[S/N]"))).lower()) == "s") else False

    def opcao1():
        return calcular.aumentar(valor,aumentar)

    def opcao2():
        return calcular.diminuir(valor,diminuir)

    def opcao3():
        return calcular.dobrar(valor)

    def opcao4():
        return calcular.metade(valor)

    opcoes = {1: opcao1, 2: opcao2, 3: opcao3,4: opcao4}

    result = opcoes.get(funcao_escolhida)()

    print(f'''{"="*20}
Resultado: {formatacao.moeda(result,status)}
{"="*20}''')
    if (str(input(print("Deseja fazer novamente?[S/N]"))).lower()) == "s":
        print('\n' * 100)
        valor = float(input(print("Digite um valor: ")))
        ciclo(valor,80,30)

