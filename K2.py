import tkinter as tk

def hitung(operasi):
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        hasil = 0
        
        if operasi == '+':
            hasil = a + b
        elif operasi == '-':
            hasil = a - b
        elif operasi == 'x':
            hasil = a * b
        elif operasi == ':':
            if b != 0:
                hasil = a / b
            else:
                hasil = "Tak Terhingga"
        
        label_hasil.config(text=str(hasil))
        
    except ValueError:
        label_hasil.config(text="Input Angka Dulu!")

window = tk.Tk()
window.title("Simple Calculator")
window.geometry("400x300")

frame1 = tk.Frame(window)
frame1.pack(pady=10)
tk.Label(frame1, text="Angka 1: ", font=("Arial", 12)).pack(side="left")
entry1 = tk.Entry(frame1, font=("Arial", 12))
entry1.pack(side="left")

frame2 = tk.Frame(window)
frame2.pack(pady=5)
tk.Label(frame2, text="Angka 2: ", font=("Arial", 12)).pack(side="left")
entry2 = tk.Entry(frame2, font=("Arial", 12))
entry2.pack(side="left")

frame_tombol = tk.Frame(window)
frame_tombol.pack(pady=15)

tk.Button(frame_tombol, text="+", width=5, font=("Arial", 12), command=lambda: hitung('+')).grid(row=0, column=0, padx=5)
tk.Button(frame_tombol, text="-", width=5, font=("Arial", 12), command=lambda: hitung('-')).grid(row=0, column=1, padx=5)
tk.Button(frame_tombol, text="x", width=5, font=("Arial", 12), command=lambda: hitung('x')).grid(row=0, column=2, padx=5)
tk.Button(frame_tombol, text=":", width=5, font=("Arial", 12), command=lambda: hitung(':')).grid(row=0, column=3, padx=5)

label_hasil = tk.Label(window, text="Hasil: 0", font=("Arial", 16, "bold"))
label_hasil.pack(pady=20)

window.mainloop()