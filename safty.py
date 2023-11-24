import tkinter as tk
import subprocess
import chardet

def scan_devices():
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)

    try:
        # Выполняем команду arp -a для получения списка устройств в локальной сети
        result = subprocess.check_output("arp -a", shell=True)

        # Определение кодировки
        encoding_info = chardet.detect(result)
        encoding = encoding_info['encoding']

        # Декодируем результат с учетом определенной кодировки
        result_text.insert(tk.END, result.decode(encoding))
    except Exception as e:
        result_text.insert(tk.END, f"An error occurred: {e}")

    result_text.config(state=tk.DISABLED)

# Создаем графический интерфейс
root = tk.Tk()
root.title("Wi-Fi Devices Scanner (Windows)")

scan_button = tk.Button(root, text="Scan Devices", command=scan_devices)
scan_button.pack(pady=10)

result_text = tk.Text(root, height=20, width=70, state=tk.DISABLED)
result_text.pack(pady=10)

root.mainloop()
