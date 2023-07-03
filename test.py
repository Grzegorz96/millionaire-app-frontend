from tkinter import *


root = Tk()
root.geometry("480x480")


# frame1 = LabelFrame(root, text="siema jakis text")
# frame1.pack(pady=20)
#
#
# my_mess = Label(frame1, text="jakis teskt na testa jakis teskt na testa \njakis teskt na testa jakis teskt na testa \njakis teskt na testa jakis teskt na testa \njakis teskt na testa jakis teskt na testa")
# my_mess.pack(pady=10, padx=10)
#
# print(len(my_mess.))


question_text = Text(root, width=49, height=6, bg="#A9A9A9", font=("Arial", 12))
question_text.place(x=25, y=100)

question = "siemka siemka siemka siemka siemkasiemkasiem kasie"
new = question.split(" ")
len_string = 0
for obj in new:
    if len(obj) + len_string <= 50:
        question_text.insert("1.0", new)
        len_string += len(obj)
        print(len_string)



question_text.insert("1.0", "siemka siemka siemka siemka siemkasiemkasiem kasie")
question_text["state"] = "disabled"

print(len(question_text.get("1.0", 'end-1c')))


root.mainloop()