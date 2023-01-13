from tkinter import *

def entradadedados():
    """
    Calcular a soma do número escolhido pelo usuário com um gerado aleatoriamente
    e se ele acertou se ela é par ou ímpar.
    """
    from random import randint
    window2 = Toplevel()
    window2.title('VENCEDOR')

    n = int(caixa_numero.get())
    esc = caixa_escolha.get().lower().strip()[0]
    maquina = randint(1, 100)
    total = n + maquina

    resultado = Label(window2, text=(f'Você jogou {n} e minha jogada foi {maquina}')) 
    if total % 2 == 0:
        PouI = Label(window2, text=f'{total} é PAR!')
        if esc in 'ií':
            vencedor = Label(window2, text='Humanos... GAMEOVER.')
        else:
            vencedor = Label(window2, text='Você leu o meu código? Eu... perdi.')
    if total % 2 != 0:
        PouI = Label(window2, text=f'{total} é ÍMPAR!')
        if esc == 'p':
            vencedor = Label(window2, text='Humanos... GAMEOVER.')
        else:
            vencedor = Label(window2, text='Você leu o meu código? Eu... perdi.')
    resultado.grid(column=0, row=4, padx=30, pady=10)
    PouI.grid(column=0, row=5, padx=30, pady=10)
    vencedor.grid(column=0, row=6, padx=30, pady=10)

    voltar = Button(window2, text=' Voltar ', cursor="hand2", command=window2.destroy)
    voltar.grid(column=0, row=7, padx=30, pady=20)


window = Tk()   # abrir e fechar a janela de exibição
window.title('PAR ou ÍMPAR?')
texto = f'''
Escolha um número de 1 a 100 e eu escolherei o meu\n
Adivinhe se a soma
dos dois será PAR ou ÍMPAR
'''  # alternativa melhor quando o texto é grande
titulo = Label(window, text='')
titulo['text'] = texto
titulo.grid(column=0, row=0, padx=30, pady=10) 

label_numero = Label(window, text='Sua jogada:')
label_numero.grid(column=0, row=1, padx=(30, 105), pady=(20, 10))
caixa_numero = Entry(window, width=10)
caixa_numero.grid(column=0, row=1, padx=(105, 30), pady=(20, 10))

label_escolha = Label(window, text='PAR ou ÍMPAR? ')
label_escolha.grid(column=0, row=2, padx=(30, 105), pady=10)
caixa_escolha = Entry(window, width=10)
caixa_escolha.grid(column=0, row=2, padx=(105, 30), pady=10)
botao = Button(window, text=' Resultado ', cursor="hand2", command=entradadedados)
botao.grid(column=0, row=3, padx=30, pady=20)

window = mainloop()   # manter a janela aberta
