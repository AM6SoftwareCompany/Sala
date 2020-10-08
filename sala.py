import os
import sqlite3
import datetime
import webbrowser
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import *


# The main window
main = Tk()
main.title('Sala | الصلاة') # title
main.iconbitmap("img/am6-logo.ico") # icon
main.geometry('300x320') # area
# Make the window unresizable
main.resizable(0, 0)


# db
day = datetime.date.today()
s = 'day' + '_' + str(day.year) + '_' + str(day.month) + '_' + str(day.day)
'''
# Create db folder if not exist
if not os.path.exists('db'):
    os.makedirs('db')
    FILE_ATTRIBUTE_HIDDEN = 0x02
    ctypes.windll.kernel32.SetFileAttributesW(path, 2)
'''
with sqlite3.connect("db\sala.db") as db:
    c = db.cursor()

# Create table
c.execute("""CREATE TABLE IF NOT EXISTS %s (
    Fajr integer,
    Dhohr integer,
    Asr integer,
    Maghreb integer,
    Isha integer,
    time text
    )"""% s)

c.execute("SELECT *,oid FROM %s ORDER BY oid DESC LIMIT 1"% s)
record = c.fetchone()

# Define the checkbuttons as int
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()

if record == None:
    c.execute("INSERT INTO %s VALUES (0, 0, 0, 0, 0, 'Start')"% s)
    # Checkbuttons' values
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
else:
    # Values of the checkbuttons
    var1.set(record[0])
    var2.set(record[1])
    var3.set(record[2])
    var4.set(record[3])
    var5.set(record[4])



db.commit()



# The main frame
frame1 = LabelFrame(main,text="Prayers Table | جدول الصلوات", padx=20, pady=20)
frame1.pack(padx=30, pady=30)




# list of checkbuttons
c1 = Checkbutton(frame1,text="Fajr | الفجر", variable=var1)
c2 = Checkbutton(frame1,text="Dhohr | الظهر", variable=var2)
c3 = Checkbutton(frame1,text="Asr | العصر", variable=var3)
c4 = Checkbutton(frame1,text="Maghreb | المغرب", variable=var4)
c5 = Checkbutton(frame1,text="Isha | العشاء", variable=var5)

c1.pack()
c2.pack()
c3.pack()
c4.pack()
c5.pack()

# Progress Bar
sala_progress = ttk.Progressbar(main, orient=HORIZONTAL,length=275, mode='determinate')
sala_progress.pack()

def step():
    progress_number = int(var1.get()) + int(var2.get()) + int(var3.get()) + int(var4.get()) + int(var5.get())
    sala_progress['value'] = progress_number * 20

step()


def submit():
    now = datetime.datetime.now()

    current_time = now.strftime("%H:%M:%S")

    with sqlite3.connect("db\sala.db") as db:
        c = db.cursor()
    c.execute("INSERT INTO %s VALUES (:Fajr, :Dhohr, :Asr, :Maghreb, :Isha, :time)"% s,
        {
            'Fajr': var1.get(),
            'Dhohr': var2.get(),
            'Asr': var3.get(),
            'Maghreb': var4.get(),
            'Isha': var5.get(),
            'time': current_time
        })
    db.commit()
    step()
    messagebox.showinfo('Submit', 'تم الحفظ')

# submit button
submit = Button(frame1, text='Submit | حفظ', command=submit)
submit.pack()

# Edit Menu opening functions
def edit_yeasterday():
    top = Toplevel()
    top.iconbitmap("img/am6-logo.ico") # icon
    top.geometry('300x300') # area
    tdelta = datetime.timedelta(days=1)
    yeasterday_date = day - tdelta
    s = 'day' + '_' + str(yeasterday_date.year) + '_' + str(yeasterday_date.month) + '_' + str(yeasterday_date.day)
    with sqlite3.connect("db\sala.db") as db:
        c = db.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS %s (
    Fajr integer,
    Dhohr integer,
    Asr integer,
    Maghreb integer,
    Isha integer,
    time text
    )"""% s)

    c.execute("SELECT *,oid FROM %s ORDER BY oid DESC LIMIT 1"% s)
    record = c.fetchone()

    # Define the checkbuttons as int
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()

    if record == None:
        c.execute("INSERT INTO %s VALUES (0, 0, 0, 0, 0, 'Start')"% s)
        # Checkbuttons' values
        var1.set(0)
        var2.set(0)
        var3.set(0)
        var4.set(0)
        var5.set(0)
    else:
        # Values of the checkbuttons
        var1.set(record[0])
        var2.set(record[1])
        var3.set(record[2])
        var4.set(record[3])
        var5.set(record[4])



    db.commit()



    # The main frame
    frame2 = LabelFrame(top,text="Prayers Table | جدول الصلوات", padx=20, pady=20)
    frame2.pack(padx=30, pady=30)




    # list of checkbuttons
    c1 = Checkbutton(frame2,text="Fajr | الفجر", variable=var1)
    c2 = Checkbutton(frame2,text="Dhohr | الظهر", variable=var2)
    c3 = Checkbutton(frame2,text="Asr | العصر", variable=var3)
    c4 = Checkbutton(frame2,text="Maghreb | المغرب", variable=var4)
    c5 = Checkbutton(frame2,text="Isha | العشاء", variable=var5)

    c1.pack()
    c2.pack()
    c3.pack()
    c4.pack()
    c5.pack()

    def submit():
        now = datetime.datetime.now()

        current_time = now.strftime("%H:%M:%S")

        with sqlite3.connect("db\sala.db") as db:
            c = db.cursor()
        c.execute("INSERT INTO %s VALUES (:Fajr, :Dhohr, :Asr, :Maghreb, :Isha, :time)"% s,
            {
                'Fajr': var1.get(),
                'Dhohr': var2.get(),
                'Asr': var3.get(),
                'Maghreb': var4.get(),
                'Isha': var5.get(),
                'time': current_time
            })
        db.commit()
        step()
        messagebox.showinfo('Submit', 'تم الحفظ')

    # submit button
    submit = Button(frame2, text='Submit | حفظ', command=submit)
    submit.pack()

def grab_date_edit():
    top = Toplevel()
    top.iconbitmap("img/am6-logo.ico") # icon
    top.geometry('300x300') # area
    cal = Calendar(top, font="Arial 12", selectmode='day', locale='en_US', maxdate=datetime.date.today(), year=datetime.date.today().year, month=datetime.date.today().month, day=datetime.date.today().day)
    cal.pack(fill="both", expand=True)

    def grabt_date():
        top = Toplevel()
        top.iconbitmap("img/am6-logo.ico") # icon
        top.geometry('300x300') # area
        grabbed_date = cal.selection_get() #2020-10-07
        s = 'day' + '_' + str(grabbed_date.year) + '_' + str(grabbed_date.month) + '_' + str(grabbed_date.day)
        with sqlite3.connect("db\sala.db") as db:
            c = db.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS %s (
        Fajr integer,
        Dhohr integer,
        Asr integer,
        Maghreb integer,
        Isha integer,
        time text
        )"""% s)

        
        c.execute("SELECT *,oid FROM %s ORDER BY oid DESC LIMIT 1"% s)
        record = c.fetchone()

        # Define the checkbuttons as int
        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        var5 = IntVar()

        if record == None:
            c.execute("INSERT INTO %s VALUES (0, 0, 0, 0, 0, 'Start')"% s)
            # Checkbuttons' values
            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            var5.set(0)
        else:
            # Values of the checkbuttons
            var1.set(record[0])
            var2.set(record[1])
            var3.set(record[2])
            var4.set(record[3])
            var5.set(record[4])



        db.commit()



        # The main frame
        frame3 = LabelFrame(top,text="Prayers Table | جدول الصلوات", padx=20, pady=20)
        frame3.pack(padx=30, pady=30)




        # list of checkbuttons
        c1 = Checkbutton(frame3,text="Fajr | الفجر", variable=var1)
        c2 = Checkbutton(frame3,text="Dhohr | الظهر", variable=var2)
        c3 = Checkbutton(frame3,text="Asr | العصر", variable=var3)
        c4 = Checkbutton(frame3,text="Maghreb | المغرب", variable=var4)
        c5 = Checkbutton(frame3,text="Isha | العشاء", variable=var5)

        c1.pack()
        c2.pack()
        c3.pack()
        c4.pack()
        c5.pack()

        def submit():
            now = datetime.datetime.now()

            current_time = now.strftime("%H:%M:%S")

            with sqlite3.connect("db\sala.db") as db:
                c = db.cursor()
            c.execute("INSERT INTO %s VALUES (:Fajr, :Dhohr, :Asr, :Maghreb, :Isha, :time)"% s,
                {
                    'Fajr': var1.get(),
                    'Dhohr': var2.get(),
                    'Asr': var3.get(),
                    'Maghreb': var4.get(),
                    'Isha': var5.get(),
                    'time': current_time
                })
            db.commit()
            step()
            messagebox.showinfo('Submit', 'تم الحفظ')

        # submit button
        submit = Button(frame3, text='Submit | حفظ', command=submit)
        submit.pack()


    grab_date_button = Button(top, text='Get Date', command=grabt_date)
    grab_date_button.pack(pady=10)



# View Menu opening functions
def view_yeasterday():
    top = Toplevel()
    top.iconbitmap("img/am6-logo.ico") # icon
    top.geometry('200x200') # area
    tdelta = datetime.timedelta(days=1)
    yeasterday_date = day - tdelta
    s = 'day' + '_' + str(yeasterday_date.year) + '_' + str(yeasterday_date.month) + '_' + str(yeasterday_date.day)
    with sqlite3.connect("db\sala.db") as db:
        c = db.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS %s (
    Fajr integer,
    Dhohr integer,
    Asr integer,
    Maghreb integer,
    Isha integer,
    time text
    )"""% s)

    c.execute("SELECT *,oid FROM %s ORDER BY oid DESC LIMIT 1"% s)
    record = c.fetchone()

    if record == None:
        c.execute("INSERT INTO %s VALUES (0, 0, 0, 0, 0, 'Start')"% s)
        db.commit()

        day_view = Label(top, text=f'Date : {str(yeasterday_date.day)}/{str(yeasterday_date.month)}/{str(yeasterday_date.year)}')
        day_view.pack()
        split_view = Label(top, text='====================')
        split_view.pack()

        f_status = 'No'

        f_views = Label(top, text=f'Fajr: {f_status}.')
        f_views.pack()

        d_status = 'No'
                
        d_views = Label(top, text=f'Dhohr: {d_status}.')
        d_views.pack()

        a_status = 'No'
                
        a_views = Label(top, text=f'Asr: {a_status}.')
        a_views.pack()

        m_status = 'No'
                
        m_views = Label(top, text=f'Maghreb: {m_status}.')
        m_views.pack()

        i_status = 'No'
                
        i_views = Label(top, text=f'Isha: {i_status}.')
        i_views.pack()

    else:
        day_view = Label(top, text=f'Date : {str(yeasterday_date.day)}/{str(yeasterday_date.month)}/{str(yeasterday_date.year)}')
        day_view.pack()

        split_view = Label(top, text='====================')
        split_view.pack()

        if record[0] == 1:
            f_status = 'Yes'
        else:
            f_status = 'No'
            
        f_views = Label(top, text=f'Fajr: {f_status}.')
        f_views.pack()

        if record[1] == 1:
            d_status = 'Yes'
        else:
            d_status = 'No'
            
        d_views = Label(top, text=f'Dhohr: {d_status}.')
        d_views.pack()

        if record[2] == 1:
            a_status = 'Yes'
        else:
            a_status = 'No'
            
        a_views = Label(top, text=f'Asr: {a_status}.')
        a_views.pack()

        if record[3] == 1:
            m_status = 'Yes'
        else:
            m_status = 'No'
            
        m_views = Label(top, text=f'Maghreb: {m_status}.')
        m_views.pack()

        if record[4] == 1:
            i_status = 'Yes'
        else:
            i_status = 'No'
            
        i_views = Label(top, text=f'Isha: {i_status}.')
        i_views.pack()



def grab_date_view():
    top = Toplevel()
    top.iconbitmap("img/am6-logo.ico") # icon
    top.geometry('300x300') # area
    cal = Calendar(top, font="Arial 12", selectmode='day', locale='en_US', maxdate=datetime.date.today(), year=datetime.date.today().year, month=datetime.date.today().month, day=datetime.date.today().day)
    cal.pack(fill="both", expand=True)
    def grab_date():
        top = Toplevel()
        top.iconbitmap("img/am6-logo.ico") # icon
        top.geometry('200x200') # area
        grabbed_date = cal.selection_get() #2020-10-07
        s = 'day' + '_' + str(grabbed_date.year) + '_' + str(grabbed_date.month) + '_' + str(grabbed_date.day)
        with sqlite3.connect("db\sala.db") as db:
            c = db.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS %s (
        Fajr integer,
        Dhohr integer,
        Asr integer,
        Maghreb integer,
        Isha integer,
        time text
        )"""% s)

        c.execute("SELECT *,oid FROM %s ORDER BY oid DESC LIMIT 1"% s)
        record = c.fetchone()

        if record == None:
            c.execute("INSERT INTO %s VALUES (0, 0, 0, 0, 0, 'Start')"% s)
            day_view = Label(top, text=f'Date : {str(grabbed_date.day)}/{str(grabbed_date.month)}/{str(grabbed_date.year)}')
            day_view.pack()

            split_view = Label(top, text='====================')
            split_view.pack()

            f_status = 'No'

            f_views = Label(top, text=f'Fajr: {f_status}.')
            f_views.pack()

            d_status = 'No'
                
            d_views = Label(top, text=f'Dhohr: {d_status}.')
            d_views.pack()

            a_status = 'No'
                
            a_views = Label(top, text=f'Asr: {a_status}.')
            a_views.pack()

            m_status = 'No'
                
            m_views = Label(top, text=f'Maghreb: {m_status}.')
            m_views.pack()

            i_status = 'No'
                
            i_views = Label(top, text=f'Isha: {i_status}.')
            i_views.pack()

            db.commit()

        else:
            day_view = Label(top, text=f'Date : {str(grabbed_date.day)}/{str(grabbed_date.month)}/{str(grabbed_date.year)}')
            day_view.pack()

            split_view = Label(top, text='====================')
            split_view.pack()

            if record[0] == 1:
                f_status = 'Yes'
            else:
                f_status = 'No'
                
            f_views = Label(top, text=f'Fajr: {f_status}.')
            f_views.pack()

            if record[1] == 1:
                d_status = 'Yes'
            else:
                d_status = 'No'
                
            d_views = Label(top, text=f'Dhohr: {d_status}.')
            d_views.pack()

            if record[2] == 1:
                a_status = 'Yes'
            else:
                a_status = 'No'
                
            a_views = Label(top, text=f'Asr: {a_status}.')
            a_views.pack()

            if record[3] == 1:
                m_status = 'Yes'
            else:
                m_status = 'No'
                
            m_views = Label(top, text=f'Maghreb: {m_status}.')
            m_views.pack()

            if record[4] == 1:
                i_status = 'Yes'
            else:
                i_status = 'No'
                
            i_views = Label(top, text=f'Isha: {i_status}.')
            i_views.pack()
        
    grab_date_button = Button(top, text='Get Date', command=grab_date)
    grab_date_button.pack(pady=10)
    




db.close()


# Contact Us Menu opening functions
def opening_fb():
    webbrowser.open_new('facebook.com/AM6Page')

def opening_website():
    webbrowser.open_new('http://am6.tech/')

def opening_whatsapp():
    webbrowser.open_new('https://web.WhatsApp.com/send?phone=201553057088')

def opening_telegram():
    webbrowser.open_new('https://t.me/AM6SoftwareCom')

def calling_us():
    webbrowser.open_new('tel:+201553057088')


# Menu
sala_menu = Menu(main)
main.config(menu=sala_menu)

# File Menu
file_menu = Menu(sala_menu, tearoff=False)
sala_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label="Exit", command=main.quit)

# Edit Menu
edit_menu = Menu(sala_menu, tearoff=False)
sala_menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Yeasterday', command=edit_yeasterday)
edit_menu.add_command(label='Pick a day', command=grab_date_edit)

# View Menu
view_menu = Menu(sala_menu, tearoff=False)
sala_menu.add_cascade(label='View', menu=view_menu)
view_menu.add_command(label='Yeasterday', command=view_yeasterday)
view_menu.add_command(label='Pick a day', command=grab_date_view)

'''
# Week View SubMenu
week_menu = Menu(view_menu, tearoff=False)
view_menu.add_separator()
view_menu.add_command(label='Current Week', command=None)
view_menu.add_cascade(label='ALL Weeks', menu=week_menu)
# Month View SubMenu
month_menu = Menu(view_menu, tearoff=False)
view_menu.add_separator()
view_menu.add_command(label='Current Month', command=None)
view_menu.add_cascade(label='ALL Months', menu=month_menu)
# Year View SubMenu
year_menu = Menu(view_menu, tearoff=False)
view_menu.add_separator()
view_menu.add_command(label='Current Year', command=None)
view_menu.add_cascade(label='ALL Years', menu=year_menu)


# Voice Menu
voice_menu = Menu(sala_menu, tearoff=False)
sala_menu.add_cascade(label='Voice', menu=voice_menu)
'''

# Contact Us Menu
contact_menu = Menu(sala_menu, tearoff=False)
sala_menu.add_cascade(label='Contact Us', menu=contact_menu)
contact_menu.add_command(label='Email', command=None, state='disabled')
contact_menu.add_command(label='info@am6.tech', command=None)
contact_menu.add_separator()
contact_menu.add_command(label='Website', command=opening_website, state='disabled')
contact_menu.add_command(label='am6.tech', command=opening_website)
contact_menu.add_separator()
contact_menu.add_command(label='Facbook Page', command=opening_fb, state='disabled')
contact_menu.add_command(label='facebook.com/AM6Page', command=opening_fb)
contact_menu.add_separator()
contact_menu.add_command(label='Phone Number', command=None, state='disabled')
contact_menu.add_command(label='+20 155 305 7088', command=None)
contact_menu.add_command(label='Whatsapp', command=opening_whatsapp)
contact_menu.add_command(label='Telegram', command=opening_telegram)
contact_menu.add_command(label='Call Us', command=calling_us)

# maitianing the app open
main.mainloop()