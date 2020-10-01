import os
import sqlite3
import datetime
import webbrowser
from tkinter import *
from tkinter import messagebox

if not os.path.isfile('am6-logo.ico'):
    import requests
    response = requests.get("https://am6.tech/assets/img/am6-logo.ico")

    file = open("am6-logo.ico", "wb")
    file.write(response.content)
    file.close()

# The main window
main = Tk()
main.title('Sala | الصلاة') # title
main.iconbitmap("am6-logo.ico") # icon
main.geometry('300x300') # area
# Make the window unresizable
main.resizable(0, 0)

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
edit_menu.add_command(label='Yeasterday', command=None)
edit_menu.add_command(label='Pick a day', command=None)

# View Menu
view_menu = Menu(sala_menu, tearoff=False)
sala_menu.add_cascade(label='View', menu=view_menu)
view_menu.add_command(label='Yeasterday', command=None)
view_menu.add_command(label='Pick a day', command=None)
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
with sqlite3.connect("sala.db") as db:
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

def submit():
    now = datetime.datetime.now()

    current_time = now.strftime("%H:%M:%S")

    with sqlite3.connect("sala.db") as db:
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
    messagebox.showinfo('Submit', 'تم الحفظ')

# submit button
submit = Button(frame1, text='Submit | حفظ', command=submit)
submit.pack()

db.close()
# maitianing the app open
main.mainloop()