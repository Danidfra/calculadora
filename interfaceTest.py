import customtkinter
from customtkinter import *



menu = CTk()
menu.title('Calculadora')

width = 300
height = 500
nmr_mostrador = ["0"]
nmr_para_operar = ["0"]
resultado = []
conta= []
status_comma = [False]
def add_comma(status_comma, n,m):
    if not status_comma[0]:
        status_comma[0] = True
        n.append('.')
        m.configure(text=n)

# Conferir Visor
def limpaVisor(status_comma, m, n, pn,c,r):
    r.clear()
    c.clear()
    pn.clear()
    pn.append("0")
    n.clear()
    n.append('0')
    status_comma[0] = False
    m.configure(text=n)


def formata_nmr(n):
    nmr_formatado = ''.join(n)
    print(nmr_formatado)
    return nmr_formatado

def preparaConta(op, nmr_para_op, conta):
    conta.append(nmr_para_op[0])
    conta.append(op)
    nmr_para_op[0] = "0"
    print(conta)


def calcula(nmr_mostrador, conta, mostrador, resultado, nmr):
    resultado.clear()
    conta.append(nmr[0])
    nmr1 = conta[0]
    operador = conta[1]
    if operador == '+':
        resp = float(nmr1) + float(nmr[0])
    elif operador == '-':
        resp = float(nmr1) - float(nmr[0])
    elif operador == 'x':
        resp = float(nmr1) * float(nmr[0])
    elif operador == '÷':
        resp = float(nmr1) / float(nmr[0])

    resp = str(resp)

    resultado.append(resp)
    mostrador.configure(text=resp)
    print(resp)
    print()
    print(resultado)
    print()
    print(conta)
    print()
    conta.clear()
    nmr_mostrador.clear()
    nmr_mostrador.append(resp)
    print(nmr_mostrador)

def visor(n):
    mostrador = CTkLabel(container_visor, width=200, height=50, text=n, anchor='e', font=('CTkFont', 20))
    mostrador.pack(expand=True, padx=(0, 20))

    return mostrador

def addN(n, c, nmr_adc, mostrador, pn):
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
    pn[0] = nmr
    print(pn)



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


menu.geometry(f'{width}x{height}')

container_Principal = customtkinter.CTkFrame(menu,width=width,height=height)
container_Principal.pack(expand=True)

container_visor = customtkinter.CTkFrame(container_Principal,width=200, height=60)
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

btn_div = customtkinter.CTkButton(container_nmr_sup, text=sim_div, width=50, height=50, border_width=1, border_color='white', command= lambda: preparaConta(sim_div, nmr_para_operar, conta))
btn_div.pack(side='right', anchor='e')
btn_porc = customtkinter.CTkButton(container_nmr_sup, text='%', width=50, height=50, border_width=1, border_color='white')
btn_porc.pack(side='right', anchor='center')
btn_invert = customtkinter.CTkButton(container_nmr_sup, text='+/-', width=50, height=50, border_width=1, border_color='white')
btn_invert.pack(side='right', anchor='center')
btn_clear = customtkinter.CTkButton(container_nmr_sup, text='C', width=50, height=50, border_width=1, border_color='white', command=lambda: limpaVisor(status_comma, mostrador, nmr_mostrador, nmr_para_operar,conta,resultado))
btn_clear.pack(side='left', anchor='w')

btn_times = customtkinter.CTkButton(container_nmr_789, text=sim_times, width=50, height=50, border_width=1, border_color='white', command=lambda: preparaConta(sim_times, nmr_para_operar, conta))
btn_times.pack(side='right', anchor='e')
btn_9 = customtkinter.CTkButton(container_nmr_789, text=nmr9, width=50, height=50, border_width=1, border_color='white', command=lambda: addN(nmr_mostrador, status_comma, nmr9, mostrador, nmr_para_operar))
btn_9.pack(side='right', anchor='center')
btn_8 = customtkinter.CTkButton(container_nmr_789, text=nmr8, width=50, height=50, border_width=1, border_color='white', command=lambda: addN(nmr_mostrador, status_comma, nmr8, mostrador, nmr_para_operar))
btn_8.pack(side='right', anchor='center')
btn_7 = customtkinter.CTkButton(container_nmr_789, text=nmr7, width=50, height=50, border_width=1, border_color='white', command=lambda: addN(nmr_mostrador, status_comma, nmr7, mostrador, nmr_para_operar))
btn_7.pack(side='left', anchor='w')

btn_minus = customtkinter.CTkButton(container_nmr_456, text=sim_minus, width=50, height=50, border_width=1, border_color='white', command=lambda: preparaConta(sim_minus, nmr_para_operar, conta))
btn_minus.pack(side='right', anchor='e')
btn_6 = customtkinter.CTkButton(container_nmr_456, text=nmr6, width=50, height=50, border_width=1, border_color='white', command=lambda: addN(nmr_mostrador, status_comma, nmr6, mostrador, nmr_para_operar))
btn_6.pack(side='right', anchor='center')
btn_5 = customtkinter.CTkButton(container_nmr_456, text=nmr5, width=50, height=50, border_width=1, border_color='white', command=lambda: addN(nmr_mostrador, status_comma, nmr5, mostrador, nmr_para_operar))
btn_5.pack(side='right', anchor='center')
btn_4 = customtkinter.CTkButton(container_nmr_456, text=nmr4, width=50, height=50, border_width=1, border_color='white', command=lambda: addN(nmr_mostrador, status_comma, nmr4, mostrador, nmr_para_operar))
btn_4.pack(side='left', anchor='w')

btn_plus = customtkinter.CTkButton(container_nmr_123, text=sim_plus, width=50, height=50, border_width=1, border_color='white', command=lambda: preparaConta(sim_plus, nmr_para_operar, conta))
btn_plus.pack(side='right', anchor='e')
btn_3 = customtkinter.CTkButton(container_nmr_123, text=nmr3, width=50, height=50, border_width=1, border_color='white', command=lambda: addN(nmr_mostrador, status_comma, nmr3, mostrador, nmr_para_operar))
btn_3.pack(side='right', anchor='center')
btn_2 = customtkinter.CTkButton(container_nmr_123, text=nmr2, width=50, height=50, border_width=1, border_color='white', command=lambda: addN(nmr_mostrador, status_comma, nmr2, mostrador, nmr_para_operar))
btn_2.pack(side='right', anchor='center')
btn_1 = customtkinter.CTkButton(container_nmr_123, text=nmr1, width=50, height=50, border_width=1, border_color='white', command=lambda: addN(nmr_mostrador, status_comma, nmr1, mostrador, nmr_para_operar))
btn_1.pack(side='left', anchor='w')

btn_0 = customtkinter.CTkButton(container_nmr_inf, text=nmr0, width=100, height=50, border_width=1, border_color='white', command=lambda: addN(nmr_mostrador, status_comma, nmr0, mostrador, nmr_para_operar))
btn_0.pack(side='left', anchor='w')
btn_comma = customtkinter.CTkButton(container_nmr_inf, text=',', width=50, height=50, border_width=1, border_color='white', command= lambda: add_comma(status_comma, nmr_mostrador, mostrador))
btn_comma.pack(side='left', anchor='w')
btn_equals = customtkinter.CTkButton(container_nmr_inf, text='=', width=50, height=50,border_width=1, border_color='white', command= lambda: calcula(nmr_mostrador, conta, mostrador, resultado, nmr_para_operar))
btn_equals.pack(side='left', anchor='w')

menu.mainloop()