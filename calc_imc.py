import tkinter as tk
from tkinter import messagebox

def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())

        imc = peso / (altura * altura)

        resultado_texto.set(f"Seu IMC é: {imc:.2f}")

        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            classificacao = "Peso normal"
        elif 25 <= imc < 29.9:
            classificacao = "Sobrepeso"
        elif 30 <= imc < 34.9:
            classificacao = "Obesidade Grau 1"
        elif 35 <= imc < 39.9:
            classificacao = "Obesidade Grau 2"
        else:
            classificacao = "Obesidade Grau 3"

        messagebox.showinfo("Classificação IMC", f"{classificacao}")

    except ValueError:  
        messagebox.showerror("Erro", "Por favor, insira valores válidos para peso e altura.")

janela = tk.Tk()  
janela.title("Calculadora de IMC")  

tk.Label(janela, text="Peso (kg):").grid(row=0, column=0, padx=10, pady=10)
entry_peso = tk.Entry(janela)
entry_peso.grid(row=0, column=1, padx=10, pady=10)

tk.Label(janela, text="Altura (m):").grid(row=1, column=0, padx=10, pady=10)
entry_altura = tk.Entry(janela)
entry_altura.grid(row=1, column=1, padx=10, pady=10)

resultado_texto = tk.StringVar()

label_resultado = tk.Label(janela, textvariable=resultado_texto)
label_resultado.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

btn_calcular = tk.Button(janela, text="Calcular IMC", command=calcular_imc)
btn_calcular.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

janela.mainloop()