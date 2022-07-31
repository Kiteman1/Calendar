from time import strftime
from tkinter import * 
from datetime import datetime, date
from tkcalendar import Calendar
    

class Calendar__(Frame):
    """Sub-Class of Frame class, also the datetime module; it is not coded in, though"""
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.label = Label(text="", fg="black", font=("Times New Roman", 18), background="pink")
        self.label.place(x=50, y=120) 
        self.today()
        self._current_year = datetime.now().year
        self._current_month = datetime.now().month
        self._current_day = datetime.now().day
        self.label2 = Label(text="", fg="black", font=("Times New Roman", 18), background="pink")
        self.label2.place(x=60, y=190)
        self.calendar()
    def today(self):
        current = date.today()
        self.label.configure(text=current, background="pink") 
    def calendar(self):
        cal = Calendar(self.master, selectmode = 'day',
               year = self._current_year, month = self._current_month,
               day = self._current_day)
        cal.pack(pady = 50)
        cal.date
        date = Label(self.master, text = "")
        date.pack(pady = 50)    


class Clock(Frame):
    """Also sub-class of the Frame class, used for the clock"""    
    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.master = master
        self.label = Label(text="", fg="black", background="pink", font=("Times New Roman", 18))
        self.label.place(x=50,y=80)
        self.update_clock()
        
    def update_clock(self):
        now = strftime("%I:%M:%S %p")
        self.label.configure(text=now, background="pink")
        self.after(1000, self.update_clock)

    
root = Tk()
root.wm_title("Calendar")
root.geometry("700x290")
root.configure(background="pink")

app=Clock(root)
root.resizable(False, False)
root.after(1000, app.update_clock)
appe = Calendar__(root)


root.mainloop() 
       
