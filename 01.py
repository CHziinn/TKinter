import tkinter as tk

janela = tk.Tk()

janela.title("Minha Janela")
janela.geometry("1200x600")

janela.config(bg="white")

logo = tk.PhotoImage(file='image 1.png')
label_logo = tk.Label(janela, image=logo, bg='white')
label_logo.pack(side='top')

email = tk.Label(janela, text='Email:', font=('Arial', 20), fg='white', bg='gray')
email.pack(pady=20)

email.place(relx = 0.5, rely = 0.4, anchor = 'center')

senha = tk.Label(janela, text='Senha:', font=('Arial', 20), fg='white', bg='gray')
senha.pack(pady=20)

senha.place(relx = 0.5, rely = 0.5, anchor = 'center')

janela.mainloop()