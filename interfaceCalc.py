import customtkinter
from customtkinter import *



menu = CTk()
menu.title('Calculadora')

width = 300
height = 500
nmr_mostrador = 123


# Conferir Visor
def limpaVisor(n):
    nmr_mostrador = '0'


# Conferir amanha
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

nmr_mostrador_formatado = testaNmr(nmr_mostrador)

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


mostrador = CTkLabel(container_visor,width=200,height=50,text=nmr_mostrador_formatado, anchor='e', font=('CTkFont',20))
mostrador.pack(expand=True, padx=(0, 20))

btn_clear = customtkinter.CTkButton(container_nmr_sup, text='÷', width=50, height=50, border_width=1, border_color='white', command=(lambda: limpaVisor(nmr_mostrador_formatado)))
btn_clear.pack(side='right', anchor='e')
btn_invert = customtkinter.CTkButton(container_nmr_sup, text='%', width=50, height=50, border_width=1, border_color='white')
btn_invert.pack(side='right', anchor='center')
btn_8 = customtkinter.CTkButton(container_nmr_sup, text='+/-', width=50, height=50, border_width=1, border_color='white')
btn_8.pack(side='right', anchor='center')
btn_7 = customtkinter.CTkButton(container_nmr_sup, text='C', width=50, height=50, border_width=1, border_color='white')
btn_7.pack(side='left', anchor='w')

btn_times = customtkinter.CTkButton(container_nmr_789, text='x', width=50, height=50, border_width=1, border_color='white')
btn_times.pack(side='right', anchor='e')
btn_9 = customtkinter.CTkButton(container_nmr_789, text='9', width=50, height=50, border_width=1, border_color='white')
btn_9.pack(side='right', anchor='center')
btn_8 = customtkinter.CTkButton(container_nmr_789, text='8', width=50, height=50, border_width=1, border_color='white')
btn_8.pack(side='right', anchor='center')
btn_7 = customtkinter.CTkButton(container_nmr_789, text='7', width=50, height=50, border_width=1, border_color='white')
btn_7.pack(side='left', anchor='w')

btn_minus = customtkinter.CTkButton(container_nmr_456, text='-', width=50, height=50, border_width=1, border_color='white')
btn_minus.pack(side='right', anchor='e')
btn_6 = customtkinter.CTkButton(container_nmr_456, text='6', width=50, height=50, border_width=1, border_color='white')
btn_6.pack(side='right', anchor='center')
btn_5 = customtkinter.CTkButton(container_nmr_456, text='5', width=50, height=50, border_width=1, border_color='white')
btn_5.pack(side='right', anchor='center')
btn_4 = customtkinter.CTkButton(container_nmr_456, text='4', width=50, height=50, border_width=1, border_color='white')
btn_4.pack(side='left', anchor='w')

btn_plus = customtkinter.CTkButton(container_nmr_123, text='+', width=50, height=50, border_width=1, border_color='white')
btn_plus.pack(side='right', anchor='e')
btn_3 = customtkinter.CTkButton(container_nmr_123, text='3', width=50, height=50, border_width=1, border_color='white')
btn_3.pack(side='right', anchor='center')
btn_2 = customtkinter.CTkButton(container_nmr_123, text='2', width=50, height=50, border_width=1, border_color='white')
btn_2.pack(side='right', anchor='center')
btn_1 = customtkinter.CTkButton(container_nmr_123, text='1', width=50, height=50, border_width=1, border_color='white')
btn_1.pack(side='left', anchor='w')

btn_0 = customtkinter.CTkButton(container_nmr_inf, text='0', width=100, height=50, border_width=1, border_color='white')
btn_0.pack(side='left', anchor='w')
btn_0 = customtkinter.CTkButton(container_nmr_inf, text=',', width=50, height=50, border_width=1, border_color='white')
btn_0.pack(side='left', anchor='w')
btn_equals = customtkinter.CTkButton(container_nmr_inf, text='=', width=50, height=50,border_width=1, border_color='white')
btn_equals.pack(side='left', anchor='w')

menu.mainloop()