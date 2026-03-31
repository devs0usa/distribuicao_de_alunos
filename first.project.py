turma = input('Para qual turma você quer utilizar esse serviço: ')
numero_total_alunos = input('Tem quantos alunos matriculados nesta turma: ')
numero_salas = input('Tem quantas salas nessa escola: ')

numero_de_alunos_por_sala = int(numero_total_alunos) // int(numero_salas)

print('Terá', numero_de_alunos_por_sala, 'alunos em cada sala')

if numero_de_alunos_por_sala < 0:
    print('A escola precisa de mais salas para acomodar os alunos')
else:    print('A escola tem salas suficientes para acomodar os alunos')
