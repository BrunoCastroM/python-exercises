# Questão: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor
# literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
def voto(ano):
    from datetime import date
    data_atual = date.today().year
    idade = data_atual - ano
    if 18 <= idade <= 60:
        return f'Com {idade} anos: Voto obrigatório!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: Voto facultativo!'
    else:
        return f'Com {idade} anos: Não vota!'


nascimento = int(input('Em que ano você nasceu? '))
print(voto(nascimento))