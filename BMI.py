import tkinter as tk
import math


window = tk.Tk()
window.title('BMI App')
window.geometry('450x200')
window.configure(background='black')

header_label = tk.Label(window, text='BMI 計算器' , fg='blue' , font='微軟正黑體 16' , bg='black')
header_label.pack(side='top')

#體重輸入
height_frame = tk.Frame(window)
height_frame.config(background='black')
height_frame.pack()

labelKg = tk.Label(height_frame , text = '輸入體重' , fg='red' , font='微軟正黑體 16' , bg='black')
labelKg.pack(side='left')

enKg = tk.Entry(height_frame)
enKg.pack(side='right')

#身高輸入
weight_frame = tk.Frame(window)
weight_frame.config(background='black')
weight_frame.pack()

labelM2 = tk.Label(weight_frame , text = '輸入身高' , fg='red' , font='微軟正黑體 16' , bg='black')
labelM2.pack(side='left')

enM2 = tk.Entry(weight_frame)
enM2.pack(side='right')

result_label = tk.Label(window)
result_label.pack()



def application():
    height = float(enM2.get())
    weight = float(enKg.get())
    result = round( weight / math.pow(height, 2), 2)
    result_label.config(text='你的BMI指數為'+str(result))



sureButton = tk.Button(window , text='確認' , fg='black' , font='微軟正黑體 16' , bg='green' , command=application)
sureButton.pack(side='bottom')



# 運行主程式
window.mainloop()