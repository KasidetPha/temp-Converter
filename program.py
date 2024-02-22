from tkinter import *
from tkinter import ttk

root = Tk()
root.iconbitmap("icon/tempicon.ico")
root.title("temp converter")
root.resizable(0,0)

def result():

    output_txt.delete(0,END)

    c = float(input_txt.get())
    unit = unit_combo.get()

    if unit == "เคลวิน":
        k = c + 274.15
        output_txt.insert(0,k)
    else:
        f = c * 1.8 + 32
        output_txt.insert(0,f)

font = ("Arial", 15)
color = "orange"

def reset():
    input_txt.delete(0,END)
    unit_combo.set("เคลวิน")
    output_txt.delete(0,END)


# input
input_label = Label(root, text=("อุณหภูมิ (C)"), font=font)
input_txt = Entry(root, font=font)

input_label.grid(row=0,column=0, sticky=W)
input_txt.grid(row=0,column=1)

# combobox
unit_label = Label(root, text="เลือกหน่วย", font=font)
unit = ["เคลวิน", "ฟาเรนไฮน์์"]
unit_combo = ttk.Combobox(root, value=unit, font=font, width=18)
unit_combo.set("เคลวิน")

unit_label.grid(row=1,column=0, sticky=W)
unit_combo.grid(row=1,column=1)

# output
output_label = Label(root, text="ผลลัพธ์", font=font)
output_txt = Entry(root, font=font)

output_label.grid(row=2, column=0, sticky=W)
output_txt.grid(row=2, column=1)

# btn
btn_result = Button(root, text="แปลง", font=font, bg=color, width=8, command=result)
btn_result.grid(row=3, column=1, sticky=W, padx=5, pady=5)

btn_cls = Button(root, text="ล้าง", font=font, bg=color, width=8, command=reset)
btn_cls.grid(row=3, column=1, sticky=E, padx=5, pady=5)


root.mainloop()