import tkinter as tk
from tkinter import messagebox
import hashlib
import time

'''a gui python cracker programmed in python'''
def crack_me():
    hash_to_crack = str(entry.get())
    with open("passlist.txt", "r") as files:
        result = files.readlines()
        for line in result:
            hash_obj = hashlib.md5(line.strip().encode())
            hash_word = hash_obj.hexdigest()
            if hash_to_crack == hash_word:
                messagebox.showinfo(title="cracked", message=f"found md5 password to be: {line}")
                #exit()
                break
                text.delete(1.0, tk.END)
                text.insert(tk.END, output)
#########################Body configuration####################   
root = tk.Tk()
root.title("Password Hash Cracker")
root.geometry("500x500")
root.configure(bg="indigo")
############################################Input and widget configuration################################
label = tk.Label(text="Enter the password hash to decrypt", fg="blue", bg="white", font=("arial", 15))
label.pack(pady=20)
entry = tk.Entry(root, font=("arial", 15))
entry.pack()
check_state1 = tk.IntVar()
check_state2 = tk.IntVar()

######################################Button configuration############
checkframe = tk.Frame(root)
checkframe.columnconfigure(0, weight=1)
checkframe.columnconfigure(1, weight=1)
check1 = tk.Checkbutton(checkframe, text="MD5 Hash", font=("arial", 12))
check2 = tk.Checkbutton(checkframe, text="SHA1 Hash", font=("arial", 12))
check1.grid(row=0, column=0, sticky=tk.E + tk.W)
check2.grid(row=0, column=1, sticky=tk.E + tk.W)

btn1 = tk.Button(checkframe, text="Start MD5 Cracking", command=crack_me, font=("arial", 15))
btn2 = tk.Button(checkframe, text="Start SHA1 Cracking", font=("arial", 15))
btn1.grid(row=1, column=0, sticky=tk.E + tk.W)
btn2.grid(row=1, column=1, sticky=tk.E + tk.W)
checkframe.pack(pady=10, fill="x")


text = tk.Text(root, height=20, font=("arial", 12))
text.pack(pady=10, padx=30)




root.mainloop()   
