
respostas = []

respostas.append(input('Falou com a vítima no dia do crime? s/n:  '))
respostas.append(input('Esteve no local do crime? s/n:  '))
respostas.append(input('Mora perto da vítima? s/n:  '))
respostas.append(input('Devia dinheiro para a vítima? s/n:  '))
respostas.append(input('Já trabalhou com a vítima? s/n:  '))

def resp_sim(respostas):
    while 'n' in respostas:
        respostas.remove('n')
    return respostas

def acusacao(sim):
    if sim == 2:
        print('suspeita.')
    if sim == 3 or sim == 4:
        print('Cúmplice.')
    if sim == 5:
        print('Assassina!')
    if sim == 1:
        print('Inocente.')

if __name__ == "__main__":
    sim = len(resp_sim(respostas))
    acusacao(sim)