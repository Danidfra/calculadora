import customtkinter
from customtkinter import *


menu = CTk()
menu.title('Calculadora')

width = 200
height = 314

# armazena o numero do mostradpr
nmr_mostrador = ["0"]
# armazena o número para realizar as operações
# nmr_para_operar = ["0"]
# armazena o resultado da operação
resultado = []
# armazena a conta da operação
conta= []
status_comma = [False]

def testaNmr(n):
    n_str = str(n)
    posi = n_str.find('.')

    if posi != -1:
        conferir = n_str[posi + 1:]
        if conferir.rstrip('0') == '':
            n_str = n_str[:posi]
    else:
        conferir = ''

    return n_str
def add_comma(status_comma, n,m):
    if not status_comma[0]:
        status_comma[0] = True
        n.append('.')
        nmr_mostrador = ''.join(n)
        m.configure(text=nmr_mostrador)

# Conferir Visor
def limpaVisor(status_comma, m, n,c,r):
    r.clear()
    c.clear()
    n.clear()
    n.append('0')
    status_comma[0] = False
    m.configure(text=n)

def formata_nmr(n):
    nmr_formatado = ''.join(n)
    return nmr_formatado

def operacao(nmr_mostrador, conta, mostrador, resultado, status_c, op):
    status_c[0] = False
    if op in '+-x÷':
        if '+' in conta or '-' in conta or 'x' in conta or '÷' in conta:

            nmr1 = conta[0]
            operador = conta[1]
            nmr2 = ''.join(nmr_mostrador)

            if operador == '+':
                resp = float(nmr1) + float(nmr2)
            elif operador == '-':
                resp = float(nmr1) - float(nmr2)
            elif operador == 'x':
                resp = float(nmr1) * float(nmr2)
            # elif operador == '÷':
            else:
                resp = float(nmr1) / float(nmr2)

            resposta = str(testaNmr(resp))
            resultado.append(resposta)
            nmr_mostrador.clear()
            nmr_mostrador.append('0')
            conta.clear()
            conta.append(resposta)
            conta.append(op)
            mostrador.configure(text=resposta)

        else:
            nmr1 = ''.join(nmr_mostrador)
            conta.append(nmr1)
            conta.append(op)

            nmr_mostrador.clear()
            nmr_mostrador.append('0')


    elif op == '=':
        try:
            # resultado.clear()
            nmr1 = conta[0]
            operador = conta[1]
            nmr2 = ''.join(nmr_mostrador)

            if operador == '+':
                resp = float(nmr1) + float(nmr2)
            elif operador == '-':
                resp = float(nmr1) - float(nmr2)
            elif operador == 'x':
                resp = float(nmr1) * float(nmr2)
            else:
                resp = float(nmr1) / float(nmr2)

            resp = str(testaNmr(resp))

            resultado.append(resp)
            mostrador.configure(text=resp)

            conta.clear()
            nmr_mostrador.clear()
            nmr_mostrador.append(resp)
        except IndexError:
            print('testando se chega aqui ou a "conta ta vazia"')

def visor(n):
    mostrador = CTkLabel(container_visor, width=190, height=60, text=n, anchor='e', font=('CTkFont', 30), bg_color='transparent')
    mostrador.pack(expand=True, padx=5)

    return mostrador

def addN(n, c, nmr_adc, mostrador):
    if c[0]:
        n.append(nmr_adc)
    else:
        if n[0] == '0':
            n[0] = nmr_adc
        else:
            n.append(nmr_adc)

    nmr = ''.join(n)

    # nmr_mostrador = testaNmr(nmr)
    mostrador.configure(text=nmr)
    n.clear()
    n.append(nmr)

def inverte_valor(nmr, mostrador):
    if nmr[0] != '0':
        if '-' not in nmr[0]:
            nmr.insert(0, "-")
            nmr_formatado = ''.join(nmr)
            nmr.clear()
            nmr.append(nmr_formatado)
        else:
            aux = list(nmr[0])
            aux.pop(0)
            nmr_formatado = ''.join(aux)
            nmr.clear()
            nmr.append(nmr_formatado)

    mostrador.configure(text=nmr)

def porcentagem(nmr, mostrador):
    aux = nmr[0]
    resp = float(aux) / 100

    resultado = testaNmr(resp)

    nmr.clear()
    nmr.append(resultado)
    mostrador.configure(text=resultado)

# nmr_mostrador_formatado = testaNmr(nmr_mostrador)
nmr_mostrador_formatado = formata_nmr(nmr_mostrador)

nmr0 = "0"
nmr1 = "1"
nmr2 = "2"
nmr3 = "3"
nmr4 = "4"
nmr5 = "5"
nmr6 = "6"
nmr7 = "7"
nmr8 = "8"
nmr9 = "9"
sim_plus = "+"
sim_minus = "-"
sim_times = "x"
sim_div = "÷"
sim_equals = "="


menu.geometry(f'{width}x{height}')

container_Principal = customtkinter.CTkFrame(menu,width=width,height=height)
container_Principal.pack(expand=True)

container_visor = customtkinter.CTkFrame(container_Principal,width=190, height=60)
container_visor.pack(expand=True)

container_nmr_sup = customtkinter.CTkFrame(container_Principal,width=200, height=50)
container_nmr_sup.pack(expand=True)

container_nmr_789 = customtkinter.CTkFrame(container_Principal,width=200, height=50)
container_nmr_789.pack(expand=True)

container_nmr_456 = customtkinter.CTkFrame(container_Principal,width=200, height=50)
container_nmr_456.pack(expand=True)

container_nmr_123 = customtkinter.CTkFrame(container_Principal,width=200, height=50)
container_nmr_123.pack(expand=True)

container_nmr_inf = customtkinter.CTkFrame(container_Principal,width=200, height=50)
container_nmr_inf.pack(expand=True, side='bottom')

mostrador = visor(nmr_mostrador_formatado)

btn_div = customtkinter.CTkButton(container_nmr_sup, text=sim_div, width=50, height=50, border_width=1, border_color='white', command=lambda: operacao(nmr_mostrador, conta, mostrador, resultado, status_comma, sim_div))
btn_div.pack(side='right', anchor='e')
btn_porc = customtkinter.CTkButton(container_nmr_sup, text='%', width=50, height=50, border_width=1, border_color='white', command=lambda: porcentagem(nmr_mostrador, mostrador))
btn_porc.pack(side='right', anchor='center')
btn_invert = customtkinter.CTkButton(container_nmr_sup, text='+/-', width=50, height=50, border_width=1, border_color='white', command=lambda: inverte_valor(nmr_mostrador,mostrador))
btn_invert.pack(side='right', anchor='center')
btn_clear = customtkinter.CTkButton(container_nmr_sup, text='C', width=50, height=50, border_width=1, border_color='white', command=lambda: limpaVisor(status_comma, mostrador, nmr_mostrador,conta,resultado))
btn_clear.pack(side='left', anchor='w')

btn_times = customtkinter.CTkButton(container_nmr_789, text=sim_times, width=50, height=50, border_width=1, border_color='white', command=lambda: operacao(nmr_mostrador, conta, mostrador, resultado, status_comma, sim_times))
btn_times.pack(side='right', anchor='e')
btn_9 = customtkinter.CTkButton(container_nmr_789, text=nmr9, width=50, height=50, border_width=1, border_color='white', command=lambda: addN(nmr_mostrador, status_comma, nmr9, mostrador))
btn_9.pack(side='right', anchor='center')
btn_8 = customtkinter.CTkButton(container_nmr_789, text=nmr8, width=50, height=50, border_width=1, border_color='white', command=lambda: addN(nmr_mostrador, status_comma, nmr8, mostrador))
btn_8.pack(side='right', anchor='center')
btn_7 = customtkinter.CTkButton(container_nmr_789, text=nmr7, width=50, height=50, border_width=1, border_color='white', command=lambda: addN(nmr_mostrador, status_comma, nmr7, mostrador))
btn_7.pack(side='left', anchor='w')

btn_minus = customtkinter.CTkButton(container_nmr_456, text=sim_minus, width=50, height=50, border_width=1, border_color='white', command=lambda: operacao(nmr_mostrador, conta, mostrador, resultado, status_comma, sim_minus))
btn_minus.pack(side='right', anchor='e')
btn_6 = customtkinter.CTkButton(container_nmr_456, text=nmr6, width=50, height=50, border_width=1, border_color='white', command=lambda: addN(nmr_mostrador, status_comma, nmr6, mostrador))
btn_6.pack(side='right', anchor='center')
btn_5 = customtkinter.CTkButton(container_nmr_456, text=nmr5, width=50, height=50, border_width=1, border_color='white', command=lambda: addN(nmr_mostrador, status_comma, nmr5, mostrador))
btn_5.pack(side='right', anchor='center')
btn_4 = customtkinter.CTkButton(container_nmr_456, text=nmr4, width=50, height=50, border_width=1, border_color='white', command=lambda: addN(nmr_mostrador, status_comma, nmr4, mostrador))
btn_4.pack(side='left', anchor='w')

btn_plus = customtkinter.CTkButton(container_nmr_123, text=sim_plus, width=50, height=50, border_width=1, border_color='white', command=lambda: operacao(nmr_mostrador, conta, mostrador,resultado , status_comma, sim_plus))
btn_plus.pack(side='right', anchor='e')
btn_3 = customtkinter.CTkButton(container_nmr_123, text=nmr3, width=50, height=50, border_width=1, border_color='white', command=lambda: addN(nmr_mostrador, status_comma, nmr3, mostrador))
btn_3.pack(side='right', anchor='center')
btn_2 = customtkinter.CTkButton(container_nmr_123, text=nmr2, width=50, height=50, border_width=1, border_color='white', command=lambda: addN(nmr_mostrador, status_comma, nmr2, mostrador))
btn_2.pack(side='right', anchor='center')
btn_1 = customtkinter.CTkButton(container_nmr_123, text=nmr1, width=50, height=50, border_width=1, border_color='white', command=lambda: addN(nmr_mostrador, status_comma, nmr1, mostrador))
btn_1.pack(side='left', anchor='w')

btn_0 = customtkinter.CTkButton(container_nmr_inf, text=nmr0, width=100, height=50, border_width=1, border_color='white', command=lambda: addN(nmr_mostrador, status_comma, nmr0, mostrador))
btn_0.pack(side='left', anchor='w')
btn_comma = customtkinter.CTkButton(container_nmr_inf, text=',', width=50, height=50, border_width=1, border_color='white', command= lambda: add_comma(status_comma, nmr_mostrador, mostrador))
btn_comma.pack(side='left', anchor='w')
btn_equals = customtkinter.CTkButton(container_nmr_inf, text=sim_equals, width=50, height=50,border_width=1, border_color='white', command= lambda: operacao(nmr_mostrador, conta, mostrador, resultado, status_comma, sim_equals))
btn_equals.pack(side='left', anchor='w')

menu.mainloop()