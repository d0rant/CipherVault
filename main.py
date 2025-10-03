from tkinter import *
from tkinter import messagebox
import base64
import os

def decrypt():
    password = code.get()

    if password == "2025":
        screen2 = Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("420x240")
        screen2.configure(bg="#1e293b")  # dark navy background

        message = text1.get(1.0, END)
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_message)
        decrypt = base64_bytes.decode("ascii")

        Label(screen2, text="🔓 Decrypted Text", font=("Segoe UI", 14, "bold"),
              fg="white", bg="#1e293b").place(x=10, y=5)
        text2 = Text(screen2, font=("Consolas", 11), bg="#f1f5f9",
                     relief=FLAT, wrap=WORD, bd=5)
        text2.place(x=10, y=40, width=400, height=180)

        text2.insert(END, decrypt)

    elif password == "":
        messagebox.showerror("Decryption", "⚠ Please enter password")
    else:
        messagebox.showerror("Decryption", "❌ Invalid Password")

def encrypt():
    password = code.get()

    if password == "2025":
        screen1 = Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("420x240")
        screen1.configure(bg="#1e293b")

        message = text1.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        Label(screen1, text="🔒 Encrypted Text", font=("Segoe UI", 14, "bold"),
              fg="white", bg="#1e293b").place(x=10, y=5)
        text2 = Text(screen1, font=("Consolas", 11), bg="#f1f5f9",
                     relief=FLAT, wrap=WORD, bd=5)
        text2.place(x=10, y=40, width=400, height=180)

        text2.insert(END, encrypt)

    elif password == "":
        messagebox.showerror("Encryption", "⚠ Please enter password")
    else:
        messagebox.showerror("Encryption", "❌ Invalid Password")


def main_screen():
    global screen
    global code
    global text1

    screen = Tk()
    screen.geometry("400x420")
    screen.configure(bg="#f8fafc")  # soft background
    screen.title("Encryption Tool")

    # Logo (if exists)
    try:
        image_icon = PhotoImage(file="images/logo.png")
        screen.iconphoto(False, image_icon)
    except:
        pass

    def reset():
        code.set("")
        text1.delete(1.0, END)

    # Title
    Label(screen, text="🔑 Text Encryption & Decryption Tool",
          fg="#0f172a", bg="#f8fafc",
          font=("Segoe UI", 13, "bold")).place(x=20, y=10)

    # Input Text Box
    text1 = Text(screen, font=("Consolas", 12), bg="#f1f5f9",
                 relief=FLAT, wrap=WORD, bd=5)
    text1.place(x=20, y=50, width=360, height=100)

    # Key Label
    Label(screen, text="Enter Secret Key:",
          fg="#334155", bg="#f8fafc",
          font=("Segoe UI", 11, "bold")).place(x=20, y=170)

    code = StringVar()
    Entry(screen, textvariable=code, width=18, bd=2,
          font=("Consolas", 16), show="*",
          relief=FLAT, bg="#e2e8f0", fg="#0f172a").place(x=20, y=200)

    # Buttons
    Button(screen, text="ENCRYPT", height=2, width=15,
           bg="#dc2626", fg="white", bd=0,
           font=("Segoe UI", 11, "bold"),
           activebackground="#b91c1c", cursor="hand2",
           command=encrypt).place(x=20, y=260)

    Button(screen, text="DECRYPT", height=2, width=15,
           bg="#16a34a", fg="white", bd=0,
           font=("Segoe UI", 11, "bold"),
           activebackground="#15803d", cursor="hand2",
           command=decrypt).place(x=210, y=260)

    Button(screen, text="RESET", height=2, width=40,
           bg="#2563eb", fg="white", bd=0,
           font=("Segoe UI", 11, "bold"),
           activebackground="#1d4ed8", cursor="hand2",
           command=reset).place(x=20, y=320)

    screen.mainloop()


main_screen()
