
import tkinter as tk

def converter_cm_para_m():
    valor_cm = float(entry_cm.get())
    valor_m = valor_cm/100
    resultado_label.config(text=f"Resultado: {valor_m} metros")

janela = tk.Tk()

valor_var = tk.StringVar(janela)

janela.title("Conversor de Medidas")
tk.Label(janela, text="Digite o valor em centímetros:").pack(pady=10)
\
entry_cm = tk.Entry(janela)
entry_cm.pack(pady=10)

btn_converter = tk.Button(janela, text="Converter", command=converter_cm_para_m)
btn_converter.pack(pady=10)

resultado_label = tk.Label(janela, text="Resultado:")
resultado_label.pack(pady=10)

janela.mainloop()

