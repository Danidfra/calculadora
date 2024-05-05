import customtkinter
from customtkinter import *
from funcoes.funcoes import *

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

# nmr_mostrador_formatado = testaNmr(nmr_mostrador)
# nmr_mostrador_formatado = formata_nmr(nmr_mostrador)

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

def cria_container(master, width, height):
    container = customtkinter.CTkFrame(master, width=width, height=height)
    container.pack(expand=True)

    return container



container_visor = cria_container(container_Principal,190,60)

container_nmr_sup = cria_container(container_Principal,200,50)

container_nmr_789 = cria_container(container_Principal,200,50)

container_nmr_456 = cria_container(container_Principal,200,50)

container_nmr_123 = cria_container(container_Principal,200,50)

container_nmr_inf = cria_container(container_Principal,200,50)

# mostrador = visor(nmr_mostrador_formatado, container_visor)
mostrador = visor(nmr_mostrador, container_visor)

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
btn_9 = customtkinter.CTkButton(container_nmr_789, text=nmr9, width=50, height=50, border_width=1, border_color='white', command=lambda: add_n(nmr_mostrador, status_comma, nmr9, mostrador))
btn_9.pack(side='right', anchor='center')
btn_8 = customtkinter.CTkButton(container_nmr_789, text=nmr8, width=50, height=50, border_width=1, border_color='white', command=lambda: add_n(nmr_mostrador, status_comma, nmr8, mostrador))
btn_8.pack(side='right', anchor='center')
btn_7 = customtkinter.CTkButton(container_nmr_789, text=nmr7, width=50, height=50, border_width=1, border_color='white', command=lambda: add_n(nmr_mostrador, status_comma, nmr7, mostrador))
btn_7.pack(side='left', anchor='w')

btn_minus = customtkinter.CTkButton(container_nmr_456, text=sim_minus, width=50, height=50, border_width=1, border_color='white', command=lambda: operacao(nmr_mostrador, conta, mostrador, resultado, status_comma, sim_minus))
btn_minus.pack(side='right', anchor='e')
btn_6 = customtkinter.CTkButton(container_nmr_456, text=nmr6, width=50, height=50, border_width=1, border_color='white', command=lambda: add_n(nmr_mostrador, status_comma, nmr6, mostrador))
btn_6.pack(side='right', anchor='center')
btn_5 = customtkinter.CTkButton(container_nmr_456, text=nmr5, width=50, height=50, border_width=1, border_color='white', command=lambda: add_n(nmr_mostrador, status_comma, nmr5, mostrador))
btn_5.pack(side='right', anchor='center')
btn_4 = customtkinter.CTkButton(container_nmr_456, text=nmr4, width=50, height=50, border_width=1, border_color='white', command=lambda: add_n(nmr_mostrador, status_comma, nmr4, mostrador))
btn_4.pack(side='left', anchor='w')

btn_plus = customtkinter.CTkButton(container_nmr_123, text=sim_plus, width=50, height=50, border_width=1, border_color='white', command=lambda: operacao(nmr_mostrador, conta, mostrador,resultado , status_comma, sim_plus))
btn_plus.pack(side='right', anchor='e')
btn_3 = customtkinter.CTkButton(container_nmr_123, text=nmr3, width=50, height=50, border_width=1, border_color='white', command=lambda: add_n(nmr_mostrador, status_comma, nmr3, mostrador))
btn_3.pack(side='right', anchor='center')
btn_2 = customtkinter.CTkButton(container_nmr_123, text=nmr2, width=50, height=50, border_width=1, border_color='white', command=lambda: add_n(nmr_mostrador, status_comma, nmr2, mostrador))
btn_2.pack(side='right', anchor='center')
btn_1 = customtkinter.CTkButton(container_nmr_123, text=nmr1, width=50, height=50, border_width=1, border_color='white', command=lambda: add_n(nmr_mostrador, status_comma, nmr1, mostrador))
btn_1.pack(side='left', anchor='w')

btn_0 = customtkinter.CTkButton(container_nmr_inf, text=nmr0, width=100, height=50, border_width=1, border_color='white', command=lambda: add_n(nmr_mostrador, status_comma, nmr0, mostrador))
btn_0.pack(side='left', anchor='w')
btn_comma = customtkinter.CTkButton(container_nmr_inf, text=',', width=50, height=50, border_width=1, border_color='white', command= lambda: add_comma(status_comma, nmr_mostrador, mostrador))
btn_comma.pack(side='left', anchor='w')
btn_equals = customtkinter.CTkButton(container_nmr_inf, text=sim_equals, width=50, height=50,border_width=1, border_color='white', command= lambda: operacao(nmr_mostrador, conta, mostrador, resultado, status_comma, sim_equals))
btn_equals.pack(side='left', anchor='w')

menu.mainloop()