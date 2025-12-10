import tkinter as tk

def close():
    window.destroy()

window = tk.Tk()
window.title("Kegiatan 1")
window.geometry("400x300")

judul = tk.Label(window, text="DATA DIRI", font=("ARIAL", 16, "bold"))
judul.pack(pady=10)

frame_data = tk.Frame(window)
frame_data.pack()

tk.Label(frame_data, text="Nama:", font=("Arial", 12)).grid(row=0, column=0, sticky="w", padx=10, pady=5)
tk.Label(frame_data, text=":", font=("Arial", 12)).grid(row=0, column=1)
tk.Label(frame_data, text="Masukkan nama mu", font=("Arial", 12, "bold")).grid(row=0, column=2, sticky="w", padx=10)

tk.Label(frame_data, text="NIM:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=10, pady=5)
tk.Label(frame_data, text=":", font=("Arial", 12)).grid(row=1, column=1)
tk.Label(frame_data, text="Masukkan NIM mu", font=("Arial", 12, "bold")).grid(row=1, column=2, sticky="w", padx=10)

tk.Label(frame_data, text="Buku Favorit:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=10, pady=5)
tk.Label(frame_data, text=":", font=("Arial", 12)).grid(row=2, column=1)
tk.Label(frame_data, text="Masukkan Buku Favorit", font=("Arial", 12, "bold")).grid(row=2, column=2, sticky="w", padx=10)

tk.Label(frame_data, text="Motto Hidup:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=10, pady=5)
tk.Label(frame_data, text=":", font=("Arial", 12)).grid(row=3, column=1)
tk.Label(frame_data, text="Masukkan Motto Hidup Mu", font=("Arial", 12, "bold")).grid(row=3, column=2, sticky="w", padx=10)

btn_close = tk.Button(window, text="Close", command=close)
btn_close.pack(pady=10)

window.mainloop()