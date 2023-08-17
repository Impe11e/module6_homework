from tkinter import*

root = Tk()
root.geometry("600x600")

canvas = Canvas(bg = "white", width = 600, height = 600)

canvas.pack()

xStart = 50
yStart = 40
widthStaff = 10
heightStaff = 100
widthFlag = 80
heightFlag = heightStaff//2



shift = 120


canvas.create_rectangle(xStart, yStart, xStart + widthStaff, yStart + heightStaff, fill='black')
canvas.create_rectangle(xStart + widthStaff, yStart, xStart + widthFlag + widthStaff, yStart + heightFlag, fill='white')

canvas.create_text(100,250, font="Arial 20", text = 'JAPAN')

for i in range(3):
    

root.mainloop()

