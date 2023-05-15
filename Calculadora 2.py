import tkinter as tk

def btn_click(valor):
    current = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(tk.END, current + str(valor))

def btn_clear():
    entrada.delete(0, tk.END)

def btn_calcular():
    expressao = entrada.get()
    resultado = eval(expressao)
    entrada.delete(0, tk.END)
    entrada.insert(tk.END, str(resultado))

# Configuração da janela principal
janela = tk.Tk()
janela.title("Calculadora")

# Entrada
entrada = tk.Entry(janela, width=20, font=("Arial", 14))
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Botões numéricos
btn_numeros = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

for valor, linha, coluna in btn_numeros:
    btn = tk.Button(janela, text=valor, width=5, height=2,
                    command=lambda valor=valor: btn_click(valor))
    btn.grid(row=linha, column=coluna, padx=5, pady=5)

# Botão de Limpar
btn_limpar = tk.Button(janela, text="C", width=11, height=2, command=btn_clear)
btn_limpar.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Botão de Calcular
btn_calcular = tk.Button(janela, text="Calcular", width=11, height=2, command=btn_calcular)
btn_calcular.grid(row=5, column=2, columnspan=2, padx=5, pady=5)

janela.mainloop()
