import os
import sqlite3
import datetime
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
c1 = Checkbutton(frame1,text="Fajr | الفجر", variable=var1).pack()
c2 = Checkbutton(frame1,text="Dhohr | الظهر", variable=var2).pack()
c3 = Checkbutton(frame1,text="Asr | العصر", variable=var3).pack()
c4 = Checkbutton(frame1,text="Maghreb | المغرب", variable=var4).pack()
c5 = Checkbutton(frame1,text="Isha | العشاء", variable=var5).pack()


def submit():
    now = datetime.datetime.now()

    current_time = now.strftime("%H:%M:%S")

    with sqlite3.connect("db/sala.db") as db:
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
submit = Button(frame1, text='Submit | حفظ', command=submit).pack()


db.close()
# maitianing the app open
main.mainloop()