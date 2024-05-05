import customtkinter
from customtkinter import *
from funcoes.funcoes import *
from variaveis.variaveis import *

menu = CTk()
menu.title('Calculadora')

width = 200
height = 314


menu.geometry(f'{width}x{height}')

container_Principal = customtkinter.CTkFrame(menu,width=width,height=height)
container_Principal.pack(expand=True)


container_visor = cria_container(container_Principal,190,60)

container_nmr_sup = cria_container(container_Principal,200,50)

container_nmr_789 = cria_container(container_Principal,200,50)

container_nmr_456 = cria_container(container_Principal,200,50)

container_nmr_123 = cria_container(container_Principal,200,50)

container_nmr_inf = cria_container(container_Principal,200,50)

# mostrador = visor(nmr_mostrador_formatado, container_visor)
mostrador = visor(nmr_mostrador, container_visor)

btn_div, btn_porc, btn_invert, btn_clear = botoes_superiores(container_nmr_sup, sim_div, porc, invert, clear, mostrador)

btn_times, btn_9, btn_8, btn_7 = botoes(container_nmr_789, sim_times, nmr9, nmr8, nmr7, mostrador)

btn_minus, btn_6, btn_5, btn_4 = botoes(container_nmr_456, sim_minus, nmr6, nmr5, nmr4, mostrador)

btn_plus, btn_3, btn_2, btn_1 = botoes(container_nmr_123, sim_plus, nmr3, nmr2, nmr1, mostrador)

btn_0,btn_comma,btn_equals = botoes_inferiores(container_nmr_inf, nmr0, comma, sim_equals, mostrador)

menu.mainloop()