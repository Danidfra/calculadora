import customtkinter
from customtkinter import *
from variaveis.variaveis import *
def add_n(n, c, nmr_adc, mostrador):
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
def limpaVisor(status_comma, m, n,c,r,sr):
    print(status_comma)
    print(sr)
    print(r)
    print(c)
    print(n)

    r.clear()
    c.clear()
    n.clear()
    n.append('0')
    status_comma[0] = False
    sr[0] = False
    m.configure(text=n)

    print(status_comma)
    print(sr)
    print(r)
    print(c)
    print(n)

def formata_nmr(n):
    nmr_formatado = ''.join(n)
    return nmr_formatado

def operacao(nmr_mostrador, conta, mostrador, resultado, status_c, op):
    if op in '+-x÷':
        status_c[0] = False
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
            status_resultado.append(True)
        except IndexError:
            print('testando se chega aqui ou a "conta ta vazia"')

def visor(n, container_visor):
    mostrador = CTkLabel(container_visor, width=190, height=60, text=n, anchor='e', font=('CTkFont', 30), bg_color='transparent')
    mostrador.pack(expand=True, padx=5)

    return mostrador

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

def cria_container(master, width, height):
    container = customtkinter.CTkFrame(master, width=width, height=height)
    container.pack(expand=True)

    return container


def botoes_superiores(master, var_btn1, var_btn2, var_btn3, var_btn4, mostrador):
    btn_div = customtkinter.CTkButton(master, text=var_btn1, width=50, height=50, border_width=1, border_color='white', command=lambda: operacao(nmr_mostrador, conta, mostrador, resultado, status_comma, var_btn1))
    btn_div.pack(side='right', anchor='e')

    btn_porc = customtkinter.CTkButton(master, text=var_btn2, width=50, height=50, border_width=1, border_color='white', command=lambda: porcentagem(nmr_mostrador, mostrador))
    btn_porc.pack(side='right', anchor='center')

    btn_invert = customtkinter.CTkButton(master, text=var_btn3, width=50, height=50, border_width=1, border_color='white', command=lambda: inverte_valor(nmr_mostrador, mostrador))
    btn_invert.pack(side='right', anchor='center')

    btn_clear = customtkinter.CTkButton(master, text=var_btn4, width=50, height=50, border_width=1, border_color='white', command=lambda: limpaVisor(status_comma, mostrador, nmr_mostrador, conta, resultado, status_resultado))
    btn_clear.pack(side='left', anchor='w')

    return btn_div, btn_porc, btn_invert, btn_clear

def botoes(master, var_btn1, var_btn2, var_btn3, var_btn4, mostrador):

    btn_op = customtkinter.CTkButton(master, text=var_btn1, width=50, height=50, border_width=1, border_color='white', command=lambda: operacao(nmr_mostrador, conta, mostrador, resultado, status_comma, var_btn1))
    btn_op.pack(side='right', anchor='e')

    btn_1 = customtkinter.CTkButton(master, text=var_btn2, width=50, height=50, border_width=1, border_color='white', command=lambda: add_n(nmr_mostrador, status_comma, var_btn2, mostrador))
    btn_1.pack(side='right', anchor='center')

    btn_2 = customtkinter.CTkButton(master, text=var_btn3, width=50, height=50, border_width=1, border_color='white', command=lambda: add_n(nmr_mostrador, status_comma, var_btn3, mostrador))
    btn_2.pack(side='right', anchor='center')

    btn_3 = customtkinter.CTkButton(master, text=var_btn4, width=50, height=50, border_width=1, border_color='white', command=lambda: add_n(nmr_mostrador, status_comma, var_btn4, mostrador))
    btn_3.pack(side='left', anchor='w')


    return btn_op, btn_1, btn_2, btn_3

def botoes_inferiores(master, text_btn1, text_btn2, text_btn3,mostrador):
    btn_0 = customtkinter.CTkButton(master, text=text_btn1, width=100, height=50, border_width=1, border_color='white', command=lambda: add_n(nmr_mostrador, status_comma, nmr0, mostrador))
    btn_0.pack(side='left', anchor='w')
    btn_comma = customtkinter.CTkButton(master, text=text_btn2, width=50, height=50, border_width=1, border_color='white', command= lambda: add_comma(status_comma, nmr_mostrador, mostrador))
    btn_comma.pack(side='left', anchor='w')
    btn_equals = customtkinter.CTkButton(master, text=text_btn3, width=50, height=50,border_width=1, border_color='white', command= lambda: operacao(nmr_mostrador, conta, mostrador, resultado, status_comma, sim_equals))
    btn_equals.pack(side='left', anchor='w')

    return btn_0, btn_comma, btn_equals