matéria=input('qual é a matéria que você quer calcular a média? ')

trimestre_1= float(input('digite sua nota de ' + matéria + ' no PRIMEIRO trimestre: '))
trimestre_2=float(input('digite sua nota de ' + matéria +  ' no SEGUNDO trimestre: '))
trimestre_3=float(input('digite sua nota de ' + matéria + ' no TERCEIRO trimestre: ') )

média=(trimestre_1 + trimestre_2 + trimestre_3) / 3
print (int(média))
mensagem= 'sua média é: ' + (int(média)) + ' em ' + matéria
print(mensagem)

if média >= 6:
    print('aprovado')
else:    print('reprovado')