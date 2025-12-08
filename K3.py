import tkinter as tk

def hitung_luas():
    try:
        p = float(entry_p.get())
        l = float(entry_l.get())
        luas = p * l
        
        hasil_text.set(f"Luas: {luas} m²")
        deskripsi.config(text="Perhitungan Berhasil!", fg="green")
        
    except ValueError:
        deskripsi.config(text="Error: Masukkan angka yang valid!", fg="red")

window = tk.Tk()
window.title("Kegiatan 3 - Luas Segiempat")
window.geometry("400x350")

tk.Label(window, text="BANGUN GEOMETRI: SEGIEMPAT", font=("Arial", 14, "bold")).pack(pady=15)

deskripsi = tk.Label(window, text="Menghitung Luas = Panjang x Lebar", font=("Arial", 10, "italic"))
deskripsi.pack(pady=5)

frame_input = tk.Frame(window)
frame_input.pack(pady=10)

tk.Label(frame_input, text="Panjang :", font=("Arial", 12)).grid(row=0, column=0, sticky="e", pady=5)
entry_p = tk.Entry(frame_input, font=("Arial", 12))
entry_p.grid(row=0, column=1, padx=10)

tk.Label(frame_input, text="Lebar :", font=("Arial", 12)).grid(row=1, column=0, sticky="e", pady=5)
entry_l = tk.Entry(frame_input, font=("Arial", 12))
entry_l.grid(row=1, column=1, padx=10)

btn = tk.Button(window, text="HITUNG LUAS", font=("Arial", 12, "bold"), bg="white", command=hitung_luas)
btn.pack(pady=15)

hasil_text = tk.StringVar()
hasil_text.set("Luas: 0")
lbl_hasil = tk.Label(window, textvariable=hasil_text, font=("Arial", 18, "bold"))
lbl_hasil.pack(pady=10)

window.mainloop()