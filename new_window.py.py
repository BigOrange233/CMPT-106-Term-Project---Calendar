import tkinter as tk
from tkcalendar import Calendar, DateEntry
from datetime import datetime

class MyCalendar(tk.Tk):
    
    #Creates a new window called "Another window"
    def create_window(self):
        
        self.newwin = tk.Toplevel()
        self.newwin.title('Another window')  

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        #Creates button to add event
        self.B = tk.Button(self, text="Click to Add Event", background='blue', foreground='white', command=self.create_window)
        self.B.pack(side="top")

        #Create calendar
        self.cal = Calendar(self, font="Arial 14", selectmode='day', tooltipforeground='black', tooltipbackground='pink',
            tooltipalpha='1', tooltipdelay='0')
        date = self.cal.datetime.today()

        #Add in events
        self.cal.c1 = self.cal.calevent_create(date + self.cal.timedelta(days=5), "Fuck me in the ass", 'message')
        self.cal.calevent_create(date, 'Bake cookies at 3am', 'reminder')
        self.cal.calevent_create(date + self.cal.timedelta(days=-2), 'Date at McDonalds', 'reminder')
        self.cal.calevent_create(date + self.cal.timedelta(days=3), 'Mine Diamonds with Jimothy', 'message')

        #Set calendar and adjust colours
        self.cal.tag_config('reminder', background='red', foreground='yellow')
        self.cal.pack(fill="both", expand=True)

        #Set status/tool tip bar
        self.l2 = tk.Label(self, text="Click on a date to check for events!", width=40)
        self.l2.pack(side="bottom")

        #Executes "set_date" when a day is clicked
        self.cal.bind("<<CalendarSelected>>", self.set_date)

    def set_date(self, event):
        
        #Get the date clicked
        self.date = self.cal.get_date()

        #Convert date from string format to datetime object format
        self.DTObject = datetime.strptime(self.date, '%m/%d/%y')

        #Get tuple of events on the date clicked
        self.eventslist = self.cal.get_calevents(self.DTObject)

        #If there >0 events, display first event on status/tool tip bar
        if len(self.eventslist) > 0:
            self.l2.configure(text=self.cal.calevents[self.eventslist[0]]["text"])

        #Display no events
        else:
            self.l2.configure(text="No events for " + self.date)


#Running loop
root = MyCalendar()
root.mainloop()