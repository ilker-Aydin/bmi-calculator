from tkinter import *

window = Tk()
window.title("BMI Calculator")

weight=Label(text="enter your weight(kg) :")
weight.grid(row=0,column=0)
weight_entry= Entry()
weight_entry.grid(row=0,column=2)

height = Label(text="enter your height(cm): ")
height.grid(row=1,column=0)
height_entry= Entry()
height_entry.grid(row=1,column=2)

result=Label(text="enter")
result.grid(row=3, column=1)
def calculate_bmı():

    h=height_entry.get()
    w=weight_entry.get()

    if h == "" or w == "":
        global result
        result.config(text="enter your height correctly like height = 173,weight=79")


    else:
         try:
            y = float(h) * float(h)
            z = float(w)
            bmı_value = (z / y) * 10000
            if bmı_value <= 18.4:
                result.config(text="bmı result: under weight")


            elif 18.4 < bmı_value <= 24.9:
                result.config(text="bmı result: normal")

            elif 25 <= bmı_value <= 39.9:
                result.config(text="bmı result: over weight")

            elif 40.0 <= bmı_value:
                result.config(text="bmı result: obese")
         except:
             result.config(text="enter numbers corretly")










calculate_button=Button(text="calculate your BMI value",command=calculate_bmı)
calculate_button.grid(row=2,column=1)


window.mainloop()

