import customtkinter
from customtkinter import *



menu = CTk()
menu.title('Calculadora')

width = 300
height = 500
nmr_mostrador = 123

# Conferir Visor
def limpaVisor(n):
    global nmr
    nmr = 0
    n.configure(text='0')
    print(nmr)

def visor(n):
    mostrador = CTkLabel(container_visor, width=200, height=50, text=n, anchor='e', font=('CTkFont', 20))
    mostrador.pack(expand=True, padx=(0, 20))

    return mostrador, n

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

def addN(nmr_adc, mostrador):
    global nmr
    nmr = str(nmr)
    nmr += str(nmr_adc)
    nmr = float(nmr)
    nmr_mostrador = testaNmr(nmr)
    mostrador.configure(text=nmr_mostrador)


nmr_mostrador_formatado = testaNmr(nmr_mostrador)
nmr0 = 0
nmr1 = 1
nmr2 = 2
nmr3 = 3
nmr4 = 4
nmr5 = 5
nmr6 = 6
nmr7 = 7
nmr8 = 8
nmr9 = 9

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

mostrador, nmr = visor(nmr_mostrador_formatado)

btn_div = customtkinter.CTkButton(container_nmr_sup, text='÷', width=50, height=50, border_width=1, border_color='white')
btn_div.pack(side='right', anchor='e')
btn_porc = customtkinter.CTkButton(container_nmr_sup, text='%', width=50, height=50, border_width=1, border_color='white')
btn_porc.pack(side='right', anchor='center')
btn_invert = customtkinter.CTkButton(container_nmr_sup, text='+/-', width=50, height=50, border_width=1, border_color='white')
btn_invert.pack(side='right', anchor='center')
btn_clear = customtkinter.CTkButton(container_nmr_sup, text='C', width=50, height=50, border_width=1, border_color='white', command=lambda: limpaVisor(mostrador))
btn_clear.pack(side='left', anchor='w')

btn_times = customtkinter.CTkButton(container_nmr_789, text='x', width=50, height=50, border_width=1, border_color='white')
btn_times.pack(side='right', anchor='e')
btn_9 = customtkinter.CTkButton(container_nmr_789, text=nmr9, width=50, height=50, border_width=1, border_color='white', command=lambda: addN(nmr9, mostrador))
btn_9.pack(side='right', anchor='center')
btn_8 = customtkinter.CTkButton(container_nmr_789, text=nmr8, width=50, height=50, border_width=1, border_color='white', command=lambda: addN(nmr8, mostrador))
btn_8.pack(side='right', anchor='center')
btn_7 = customtkinter.CTkButton(container_nmr_789, text=nmr7, width=50, height=50, border_width=1, border_color='white', command=lambda: addN(nmr7, mostrador))
btn_7.pack(side='left', anchor='w')

btn_minus = customtkinter.CTkButton(container_nmr_456, text='-', width=50, height=50, border_width=1, border_color='white')
btn_minus.pack(side='right', anchor='e')
btn_6 = customtkinter.CTkButton(container_nmr_456, text=nmr6, width=50, height=50, border_width=1, border_color='white', command=lambda: addN(nmr6, mostrador))
btn_6.pack(side='right', anchor='center')
btn_5 = customtkinter.CTkButton(container_nmr_456, text=nmr5, width=50, height=50, border_width=1, border_color='white', command=lambda: addN(nmr5, mostrador))
btn_5.pack(side='right', anchor='center')
btn_4 = customtkinter.CTkButton(container_nmr_456, text=nmr4, width=50, height=50, border_width=1, border_color='white', command=lambda: addN(nmr4, mostrador))
btn_4.pack(side='left', anchor='w')

btn_plus = customtkinter.CTkButton(container_nmr_123, text='+', width=50, height=50, border_width=1, border_color='white')
btn_plus.pack(side='right', anchor='e')
btn_3 = customtkinter.CTkButton(container_nmr_123, text=nmr3, width=50, height=50, border_width=1, border_color='white', command=lambda: addN(nmr3, mostrador))
btn_3.pack(side='right', anchor='center')
btn_2 = customtkinter.CTkButton(container_nmr_123, text=nmr2, width=50, height=50, border_width=1, border_color='white', command=lambda: addN(nmr2, mostrador))
btn_2.pack(side='right', anchor='center')
btn_1 = customtkinter.CTkButton(container_nmr_123, text=nmr1, width=50, height=50, border_width=1, border_color='white', command=lambda: addN(nmr1, mostrador))
btn_1.pack(side='left', anchor='w')

btn_0 = customtkinter.CTkButton(container_nmr_inf, text='0', width=100, height=50, border_width=1, border_color='white', command=lambda: addN(nmr0, mostrador))
btn_0.pack(side='left', anchor='w')
btn_comma = customtkinter.CTkButton(container_nmr_inf, text=',', width=50, height=50, border_width=1, border_color='white')
btn_comma.pack(side='left', anchor='w')
btn_equals = customtkinter.CTkButton(container_nmr_inf, text='=', width=50, height=50,border_width=1, border_color='white')
btn_equals.pack(side='left', anchor='w')

menu.mainloop()