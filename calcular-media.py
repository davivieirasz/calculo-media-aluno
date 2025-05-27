def calcular_media():
    n1 = float(input('Informe a primeira nota: '))
    n2 = float(input('Informe a segunda nota: '))
    n3 = float(input('Informe a terceira nota: '))
    resultado = ((n1 + n2 + n3) / 3)
    resultadoformatado = round(resultado, 1)
    print('Sua média é de:', resultadoformatado)

    if(resultado < 7 ):
        print('Você está REPROVADO!')
    else:
        print('Você está APROVADO!')



while True:
    calcular_media()

    repetir = input('Deseja calcular outra média? (S/N): ').lower()
    if repetir != 's':
        break

input('Pressione ENTER para fechar o programa...')