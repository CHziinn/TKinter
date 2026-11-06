import tkinter as tk

janela = tk.Tk()

janela.title("Minha Janela")
janela.geometry("1200x600")

janela.config(bg="white")

texto = tk.Label(janela, text='Minha Janela', font=('Arial', 20), fg='black', bg='white')
texto.pack(pady=20)

texto.place(relx = 0.5, rely = 0.5, anchor = 'center')

janela.mainloop()