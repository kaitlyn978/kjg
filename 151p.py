from tkinter import*
root=Tk()
root.geometry("700x700")
root.title("Sales Application")
m=Label(root)
p=Label(root)
maxa=Label(root)
mina=Label(root)
months=("january","febuary","march","april","may","june","july","august","september","october","november","december")
profits=(65000,43000,19000,597000,870000,58000,92000,83000,37000,74000,12000,64000)
m["text"]="Months: "+str(months)
p["text"]="Profits: "+str(profits)

def maxprofits():
     max_profits=max(profits)
     mpi=profits.index(max_profits)
     max_month=months[mpi]
     maxa["text"]="The max profit of "+str(max_profits)+" has been recorded in the month of "+str(max_month)+"."
     
def minprofits():
     min_profits=min(profits)
     mmpi=profits.index(min_profits)
     min_month=months[mmpi]
     mina["text"]="The min profit of "+str(min_profits)+" has been recorded in the month of "+str(min_month)+"."

m.place(relx=0.5,rely=0.3,anchor=CENTER)

p.place(relx=0.5,rely=0.4,anchor=CENTER)

max1=Button(root,text="Show Me Max Profits",command=maxprofits)
max1.place(relx=0.5,rely=0.5,anchor=CENTER)
maxa.place(relx=0.5,rely=0.6,anchor=CENTER)
min1=Button(root,text="Show Me Min Profits",command=minprofits)
min1.place(relx=0.5,rely=0.7,anchor=CENTER)
mina.place(relx=0.5,rely=0.8,anchor=CENTER)
root.mainloop()

