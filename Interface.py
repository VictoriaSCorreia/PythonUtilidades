from tkinter import *
def dataentry():
    from random import randint
    window2 = Toplevel()
    window2.title('Winner')

    n = int(number_box.get())
    esc = choice_box.get().lower().strip()[0]
    pc = randint(1, 100)
    total = n + pc
    result = Label(window2, text=(f'Your move: {n}\nMy move: {pc}')) 
    if total % 2 == 0:
        PouI = Label(window2, text=f'{total} is an even number!')
        if esc in 'iío' or esc.isnumeric():
            winner = Label(window2, text='Humans... GAMEOVER.')
        else:
            winner = Label(window2, text="Did you see my code? I've... lost.")
    if total % 2 != 0:
        PouI = Label(window2, text=f'{total} is an odd number!')
        if esc in 'pe' or esc.isnumeric():
            winner = Label(window2, text='Humans... GAMEOVER.')
        else:
            winner = Label(window2, text="Did you see my code? I've... lost.")
    result.grid(column=0, row=4, padx=30, pady=10)
    PouI.grid(column=0, row=5, padx=30, pady=10)
    winner.grid(column=0, row=6, padx=30, pady=10)
    voltar = Button(window2, text=' Back ', cursor="hand2", command=window2.destroy)
    voltar.grid(column=0, row=7, padx=30, pady=20)


window = Tk()   # abrir e fechar a janela de exibição
window.title('PAR ou ÍMPAR?')
text = f'''
Choose a number from 1 to 100 and I'll choose mine\n
Guess if the sum of both is an even or odd number 
'''  
title = Label(window, text='')
title['text'] = text  # alternativa melhor quando o texto é grande
title.grid(column=0, row=0, padx=30, pady=10) 

number_label = Label(window, text='Your move:')
number_label.grid(column=0, row=1, padx=(30, 105), pady=(20, 10))
number_box = Entry(window, width=10)
number_box.grid(column=0, row=1, padx=(105, 30), pady=(20, 10))

choice_label = Label(window, text='Even or odd? ')
choice_label.grid(column=0, row=2, padx=(30, 105), pady=10)
choice_box = Entry(window, width=10)
choice_box.grid(column=0, row=2, padx=(105, 30), pady=10)
botao = Button(window, text=' result ', cursor="hand2", command=dataentry)
botao.grid(column=0, row=3, padx=30, pady=20)

window = mainloop()   # manter a janela aberta
