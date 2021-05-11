import tkinter as tk
#from tkinter import ttk
#from tkinter.messagebox import showinfo


rootWindow = tk.Tk()
rootWindow.geometry('860x860')
top_frame = tk.Frame(rootWindow)

# 將元件分為 top/bottom 兩群並加入主視窗

topTxt = tk.Label(top_frame,text='請依照下方指示輸入數值',font=('Arial',24))
topTxt.pack()
top_frame.pack()

bottom_frame = tk.Frame(rootWindow)
bottom_frame.pack(side=tk.BOTTOM)

# 以下為 top 群組
left_button = tk.Button(top_frame, text='Red', fg='red')
# 讓系統自動擺放元件，預設為由上而下（靠左）
left_button.pack(side=tk.LEFT)

# 運行主程式
rootWindow.mainloop()