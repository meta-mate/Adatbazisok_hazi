import tkinter as tk
from tkinter import messagebox as MessageBox
import mysql.connector as mysql

mtable = 'fejleszto'

def show(table):
    mtable = table
    con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
    cursor = con.cursor()
    cursor.execute('select * from {}'.format(table))
    rows = cursor.fetchall()
    list.delete(0, list.size())
    for row in rows:
        insertData = ''
        for ri in row:
            insertData += '{} '.format(ri)
        insertData = insertData[:-1]
        list.insert(list.size() + 1, insertData)
    con.close()

def get0():
    if e_id0.get() == "":
        MessageBox.showinfo("Info", "kotelezo adatok hianyoznak")
    else:
        e_nev0.delete(0, 'end')
        e_email0.delete(0, 'end')
        e_csatlakozas0.delete(0, 'end')
        e_szerepkorok0.delete(0, 'end')
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('select * from fejleszto where id=\'{}\''.format(e_id0.get()))
        rows = cursor.fetchmany(1)
        for row in rows:
            e_nev0.insert(0, row[0])
            e_email0.insert(0, row[3])
            e_csatlakozas0.insert(0, row[2])
            e_szerepkorok0.insert(0, row[4])
        con.close()
        show('fejleszto')

def insert0():
    if e_nev0.get() == "" or e_email0.get() == "" or e_csatlakozas0.get() == "" or e_szerepkorok0.get() == "":
        MessageBox.showinfo("Info", "hianyzo adat")
    else:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('insert into fejleszto values("{}","{}","{}","{}","{}")'.format(e_nev0.get(), e_id0.get(), e_email0.get(), e_csatlakozas0.get(), e_szerepkorok0.get()))
        cursor.execute('commit')
        e_id0.delete(0, 'end')
        e_nev0.delete(0, 'end')
        e_email0.delete(0, 'end')
        e_csatlakozas0.delete(0, 'end')
        e_szerepkorok0.delete(0, 'end')
        MessageBox.showinfo('Info', 'Sikeres beszuras')
        con.close()
        show('fejleszto')

def update0():
    if e_id0.get() == "" or e_nev0.get() == "" or e_email0.get() == "" or e_csatlakozas0.get() == "" or e_szerepkorok0.get() == "":
        MessageBox.showinfo("Info", "Minden mezo kotelezo")
    else:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('update fejleszto set nev=\'{}\', email=\'{}\', csatlakozas=\'{}\', szerepkorok=\'{}\' where id=\'{}\''.format(e_nev0.get(), e_email0.get(), e_csatlakozas0.get(), e_szerepkorok0.get(), e_id0.get()))
        cursor.execute('commit')
        e_id0.delete(0, 'end')
        e_nev0.delete(0, 'end')
        e_email0.delete(0, 'end')
        e_csatlakozas0.delete(0, 'end')
        e_szerepkorok0.delete(0, 'end')
        MessageBox.showinfo('Info', 'Sikeres frissites')
        con.close()
        show('fejleszto')

def delete0():
    if e_id0.get() == "":
        MessageBox.showinfo("Info", "hianyzo infok")
    else:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('delete from fejleszto where id=\'{}\''.format(e_id0.get()))
        cursor.execute('commit')
        e_id0.delete(0, 'end')
        e_nev0.delete(0, 'end')
        e_email0.delete(0, 'end')
        e_csatlakozas0.delete(0, 'end')
        e_szerepkorok0.delete(0, 'end')
        MessageBox.showinfo('Info', 'torles vegrehajtva')
        con.close()
        show('fejleszto')

#masodik panel

def get1():
    if e_id1.get() == "" or e_jelentesi_ido1.get() == "" or e_nev1.get() == "" or e_verzio1.get() == "":
        MessageBox.showinfo("Info", "kotelezo adatok hianyoznak")
    else:
        e_leiras1.delete(0, 'end')
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('select * from hibajelentes where id=\'{}\' AND jelentesi_ido=\'{}\' AND nev=\'{}\' AND verzio=\'{}\''.format(e_id1.get(), e_jelentesi_ido1.get(), e_nev1.get(), e_verzio1.get()))
        rows = cursor.fetchmany(1)
        for row in rows:
            e_leiras1.insert(0, row[1])
        con.close()
        show('hibajelentes')

def insert1():
    if e_id1.get() == "" or e_leiras1.get() == "" or e_jelentesi_ido1.get() == "" or e_nev1.get() == "" or e_verzio1.get() == "":
        MessageBox.showinfo("Info", "hianyzo adat")
    else:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('insert into hibajelentes values("{}","{}","{}","{}","{}")'.format(e_jelentesi_ido1.get(), e_leiras1.get(), e_id1.get(), e_nev1.get(), e_verzio1.get()))
        cursor.execute('commit')
        e_id1.delete(0, 'end')
        e_leiras1.delete(0, 'end')
        e_jelentesi_ido1.delete(0, 'end')
        e_nev1.delete(0, 'end')
        e_verzio1.delete(0, 'end')
        MessageBox.showinfo('Info', 'Sikeres beszuras')
        con.close()
        show('hibajelentes')

def update1():
    if e_id1.get() == "" or e_leiras1.get() == "" or e_jelentesi_ido1.get() == "" or e_nev1.get() == "" or e_verzio1.get() == "":
        MessageBox.showinfo("Info", "Minden mezo kotelezo")
    else:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('update hibajelentes set leiras="{}" where jelentesi_ido=\'{}\' AND id=\'{}\' AND nev=\'{}\' AND verzio=\'{}\''.format(e_leiras1.get(), e_jelentesi_ido1.get(), e_id1.get(), e_nev1.get(), e_verzio1.get()))
        cursor.execute('commit')
        e_id1.delete(0, 'end')
        e_leiras1.delete(0, 'end')
        e_jelentesi_ido1.delete(0, 'end')
        e_nev1.delete(0, 'end')
        e_verzio1.delete(0, 'end')
        MessageBox.showinfo('Info', 'Sikeres frissites')
        con.close()
        show('hibajelentes')

def delete1():
    if e_id1.get() == "" or e_jelentesi_ido1.get() == "" or e_nev1.get() == "" or e_verzio1.get() == "":
        MessageBox.showinfo("Info", "hianyzo infok")
    else:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('delete from hibajelentes where id1=\'{}\' AND jelentesi_ido1=\'{}\' AND nev1=\'{}\' AND verzio1=\'{}\''.format(e_id1.get(), e_jelentesi_ido1.get(), e_nev1.get(), e_verzio1.get()))
        cursor.execute('commit')
        e_id1.delete(0, 'end')
        e_leiras1.delete(0, 'end')
        e_jelentesi_ido1.delete(0, 'end')
        e_nev1.delete(0, 'end')
        e_verzio1.delete(0, 'end')
        MessageBox.showinfo('Info', 'torles vegrehajtva')
        con.close()
        show('hibajelentes')

#harmadik panel

def get2():
    if e_bejelento_id2.get() == ""  or e_jelentesi_ido2.get() == "" or e_nev2.get() == "" or e_verzio2.get() == "" or e_javito_id2.get() == "":
        MessageBox.showinfo("Info", "kotelezo adatok hianyoznak")
    else:
        e_leiras2.delete(0, 'end')
        e_changelog2.delete(0, 'end')
        e_javitasi_ido2.delete(0, 'end')
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('select * from javitas where bejelento_id=\'{}\' AND jelentesi_ido=\'{}\' AND nev=\'{}\' AND verzio=\'{}\' AND javito_id=\'{}\''.format(e_bejelento_id2.get(), e_jelentesi_ido2.get(), e_nev2.get(), e_verzio2.get(), e_javito_id2.get()))
        rows = cursor.fetchmany(1)
        for row in rows:
            e_changelog2.insert(0, row[0])
            e_javitasi_ido2.insert(0, row[1])
            e_leiras2.insert(0, row[2])
        con.close()
        show('javitas')

def insert2():
    if e_changelog2.get()== "" or e_javitasi_ido2.get()== "" or e_leiras2.get()== "" or e_bejelento_id2.get() == "" or e_bejelento_id2.get() == "" or e_jelentesi_ido2.get() == "" or e_nev2.get() == "" or e_verzio2.get() == "" or e_javito_id2== "":
        MessageBox.showinfo("Info", "hianyzo adat")
    else:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('insert into javitas values("{}","{}","{}","{}","{}","{}","{}","{}")'.format(e_changelog2.get(), e_javitasi_ido2.get(), e_leiras2.get(), e_bejelento_id2.get(), e_jelentesi_ido2.get(), e_nev2.get(), e_verzio2.get(), e_javito_id2.get()))
        cursor.execute('commit')
        e_bejelento_id2.delete(0, 'end')
        e_leiras2.delete(0, 'end')
        e_jelentesi_ido2.delete(0, 'end')
        e_nev2.delete(0, 'end')
        e_verzio2.delete(0, 'end')
        e_javito_id2.delete(0, 'end')
        e_changelog2.delete(0, 'end')
        e_javitasi_ido2.delete(0, 'end')
        
        MessageBox.showinfo('Info', 'Sikeres beszuras')
        con.close()
        show('javitas')

def update2():
    if e_changelog2.get()== "" or e_javitasi_ido2.get()== "" or e_leiras2.get()== "" or e_bejelento_id2.get() == "" or e_bejelento_id2.get() == "" or e_jelentesi_ido2.get() == "" or e_nev2.get() == "" or e_verzio2.get() == "" or e_javito_id2.get() == "":
        MessageBox.showinfo("Info", "Minden mezo kotelezo")
    else:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('update javitas set changelog=\'{}\', javitasi_ido=\'{}\', leiras=\'{}\' where bejelento_id=\'{}\' AND jelentesi_ido=\'{}\' AND nev=\'{}\' AND verzio=\'{}\' AND javito_id=\'{}\''.format(e_changelog2.get(), e_javitasi_ido2.get(), e_leiras2.get(), e_bejelento_id2.get(), e_jelentesi_ido2.get(), e_nev2.get(), e_verzio2.get(), e_javito_id2.get()))
        cursor.execute('commit')
        e_bejelento_id2.delete(0, 'end')
        e_leiras2.delete(0, 'end')
        e_jelentesi_ido2.delete(0, 'end')
        e_nev2.delete(0, 'end')
        e_verzio2.delete(0, 'end')
        e_javito_id2.delete(0, 'end')
        e_changelog2.delete(0, 'end')
        e_javitasi_ido2.delete(0, 'end')
        MessageBox.showinfo('Info', 'Sikeres frissites')
        con.close()
        show('javitas')

def delete2():
    if e_bejelento_id2.get() == "" or e_jelentesi_ido2.get() == "" or e_nev2.get() == "" or e_verzio2.get() == "" or e_javito_id2== "":
        MessageBox.showinfo("Info", "hianyzo infok")
    else:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('delete from javitas where bejelento_id=\'{}\' AND jelentesi_ido=\'{}\' AND nev=\'{}\' AND verzio=\'{}\' AND javito_id=\'{}\''.format(e_bejelento_id2.get(), e_jelentesi_ido2.get(), e_nev2.get(), e_verzio2.get(), e_javito_id2.get()))
        cursor.execute('commit')
        e_bejelento_id2.delete(0, 'end')
        e_leiras2.delete(0, 'end')
        e_jelentesi_ido2.delete(0, 'end')
        e_nev2.delete(0, 'end')
        e_verzio2.delete(0, 'end')
        e_javito_id2.delete(0, 'end')
        e_changelog2.delete(0, 'end')
        e_javitasi_ido2.delete(0, 'end')
        MessageBox.showinfo('Info', 'torles vegrehajtva')
        con.close()
        show('javitas')

#negyedik panel

def get3():
    if e_nev3.get() == "" or e_verzio3.get() == "":
        MessageBox.showinfo("Info", "kotelezo adatok hianyoznak")
    else:
        e_leiras3.delete(0, 'end')
        e_changelog3.delete(0, 'end')
        e_elozo_verzio3.delete(0, 'end')
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('select * from szoftver where nev=\'{}\' AND verzio=\'{}\''.format(e_nev3.get(), e_verzio3.get()))
        rows = cursor.fetchmany(1)
        for row in rows:
            e_leiras3.insert(0, row[2])
            e_changelog3.insert(0, row[3])
            e_elozo_verzio3.insert(0, row[4])
        con.close()
        show('szoftver')

def insert3():
    if e_nev3.get() == "" or e_verzio3.get() == "":
        MessageBox.showinfo("Info", "hianyzo adat")
    else:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('insert into szoftver values("{}","{}","{}","{}","{}")'.format(e_nev3.get(), e_verzio3.get(), e_leiras3.get(), e_changelog3.get(), e_elozo_verzio3.get()))
        cursor.execute('commit')
        e_leiras3.delete(0, 'end')
        e_nev3.delete(0, 'end')
        e_verzio3.delete(0, 'end')
        e_changelog3.delete(0, 'end')
        e_elozo_verzio3.delete(0, 'end')
        MessageBox.showinfo('Info', 'Sikeres beszuras')
        con.close()
        show('szoftver')

def update3():
    if e_nev3.get() == "" or e_verzio3.get() == "" or e_leiras3.get() == "" or e_changelog3.get() == "" or e_elozo_verzio3.get() == "":
        MessageBox.showinfo("Info", "Minden mezo kotelezo")
    else:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('update szoftver set leiras="{}", changelog="{}", elozo_verzio="{}" where nev=\'{}\' AND verzio=\'{}\''.format(e_leiras3.get(), e_changelog3.get(), e_elozo_verzio3.get(), e_jelentesi_ido1.get(), e_id3.get(), e_nev3.get(), e_verzio3.get()))
        cursor.execute('commit')
        e_leiras3.delete(0, 'end')
        e_nev3.delete(0, 'end')
        e_verzio3.delete(0, 'end')
        e_changelog3.delete(0, 'end')
        e_elozo_verzio3.delete(0, 'end')
        MessageBox.showinfo('Info', 'Sikeres frissites')
        con.close()
        show('szoftver')

def delete3():
    if e_nev3.get() == "" or e_verzio3.get() == "":
        MessageBox.showinfo("Info", "hianyzo infok")
    else:
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('delete from szoftver where nev=\'{}\' AND verzio=\'{}\''.format(e_nev3.get(), e_verzio3.get()))
        cursor.execute('commit')
        e_leiras3.delete(0, 'end')
        e_nev3.delete(0, 'end')
        e_verzio3.delete(0, 'end')
        e_changelog3.delete(0, 'end')
        e_elozo_verzio3.delete(0, 'end')
        MessageBox.showinfo('Info', 'torles vegrehajtva')
        con.close()
        show('szoftver')

if __name__ == '__main__':
    dbhost = 'localhost'
    dbuser = 'bugzilla'
    dbpass = 'mys3cr3t'
    dbname = 'bugzilla'

    root = tk.Tk()
    root.geometry("600x600")
    root.title("SQL bugzilla")

    list = tk.Listbox(root, width=45, height=10)
    list.place(x=300, y=420)

    px = 0
    py = 0
    
    px1 = 300
    py1 = 0

    px2 = 0
    py2 = 200

    px3 = 300 #+195
    py3 = 200 #+180

#elso panel: nev nev csatlakozas email szerepkorok

    nev0 = tk.Label(root, text='nev', font=('bold', 10))
    nev0.place(x= px + 20, y= py + 30)

    id0 = tk.Label(root, text='id', font=('bold', 10))
    id0.place(x= px + 20, y= py + 60)

    email0 = tk.Label(root, text='email', font=('bold', 10))
    email0.place(x= px + 20, y= py + 90)

    csatlakozas0 = tk.Label(root, text='csatlakozas', font=('bold', 10))
    csatlakozas0.place(x= px + 20, y= py + 120)

    szerepkorok0 = tk.Label(root, text='szerepkorok', font=('bold', 10))
    szerepkorok0.place(x= px + 20, y= py + 150)

    e_nev0 = tk.Entry()
    e_nev0.place(x= px + 150, y= py + 30)

    e_id0 = tk.Entry()
    e_id0.place(x= px + 150, y= py + 60)

    e_email0 = tk.Entry()
    e_email0.place(x= px + 150, y= py + 90)

    e_csatlakozas0 = tk.Entry()
    e_csatlakozas0.place(x= px + 150, y= py + 120)

    e_szerepkorok0 = tk.Entry()
    e_szerepkorok0.place(x= px + 150, y= py + 150)

    insert_button0 = tk.Button(root, text="beszuras", font=('italic', 10), bg="white", command=insert0)
    insert_button0.place(x= px + 20, y= py + 180)

    update_button0 = tk.Button(root, text="frissit", font=('italic', 10), bg="white", command=update0)
    update_button0.place(x= px + 90, y= py + 180)

    delete_button0 = tk.Button(root, text="torles", font=('italic', 10), bg="white", command=delete0)
    delete_button0.place(x= px + 135, y= py + 180)

    get_button0 = tk.Button(root, text="lekeres", font=('italic', 10), bg="white", command=get0)
    get_button0.place(x= px + 195, y= py + 180)


#masodik panel

    leiras1 = tk.Label(root, text='leiras', font=('bold', 10))
    leiras1.place(x= px1 + 20, y= py1 + 30)

    id1 = tk.Label(root, text='id', font=('bold', 10))
    id1.place(x= px1 + 20, y= py1 + 60)

    jelentesi_ido1 = tk.Label(root, text='jelentesi_ido', font=('bold', 10))
    jelentesi_ido1.place(x= px1 + 20, y= py1 + 90)

    nev1 = tk.Label(root, text='nev', font=('bold', 10))
    nev1.place(x= px1 + 20, y= py1 + 120)

    verzio1 = tk.Label(root, text='verzio', font=('bold', 10))
    verzio1.place(x= px1 + 20, y= py1 + 150)

    e_leiras1 = tk.Entry()
    e_leiras1.place(x= px1 + 150, y= py1 + 30)

    e_id1 = tk.Entry()
    e_id1.place(x= px1 + 150, y= py1 + 60)

    e_jelentesi_ido1 = tk.Entry()
    e_jelentesi_ido1.place(x= px1 + 150, y= py1 + 90)

    e_nev1 = tk.Entry()
    e_nev1.place(x= px1 + 150, y= py1 + 120)

    e_verzio1 = tk.Entry()
    e_verzio1.place(x= px1 + 150, y= py1 + 150)

    insert_button1 = tk.Button(root, text="beszuras", font=('italic', 10), bg="white", command=insert1)
    insert_button1.place(x= px1 + 20, y= py1 + 180)

    update_button1 = tk.Button(root, text="frissit", font=('italic', 10), bg="white", command=update1)
    update_button1.place(x= px1 + 90, y= py1 + 180)

    delete_button1 = tk.Button(root, text="torles", font=('italic', 10), bg="white", command=delete1)
    delete_button1.place(x= px1 + 135, y= py1 + 180)

    get_button1 = tk.Button(root, text="lekeres", font=('italic', 10), bg="white", command=get1)
    get_button1.place(x= px1 + 195, y= py1 + 180)


#harmadik panel
    leiras2 = tk.Label(root, text='leiras', font=('bold', 10))
    leiras2.place(x= px2 + 20, y= py2 + 30)

    bejelento_id2 = tk.Label(root, text='bejelento_id', font=('bold', 10))
    bejelento_id2.place(x= px2 + 20, y= py2 + 60)

    jelentesi_ido2 = tk.Label(root, text='jelentesi_ido', font=('bold', 10))
    jelentesi_ido2.place(x= px2 + 20, y= py2 + 90)

    nev2 = tk.Label(root, text='nev', font=('bold', 10))
    nev2.place(x= px2 + 20, y= py2 + 120)

    verzio2 = tk.Label(root, text='verzio', font=('bold', 10))
    verzio2.place(x= px2 + 20, y= py2 + 150)

    javito_id2 = tk.Label(root, text='javito_id', font=('bold', 10))
    javito_id2.place(x= px2 + 20, y= py2 + 180)

    changelog2 = tk.Label(root, text='changelog', font=('bold', 10))
    changelog2.place(x= px2 + 20, y= py2 + 210)

    javitasi_ido2 = tk.Label(root, text='javitasi_ido', font=('bold', 10))
    javitasi_ido2.place(x= px2 + 20, y= py2 + 240)

    e_leiras2 = tk.Entry()
    e_leiras2.place(x= px2 + 150, y= py2 + 30)

    e_bejelento_id2 = tk.Entry()
    e_bejelento_id2.place(x= px2 + 150, y= py2 + 60)

    e_jelentesi_ido2 = tk.Entry()
    e_jelentesi_ido2.place(x= px2 + 150, y= py2 + 90)

    e_nev2 = tk.Entry()
    e_nev2.place(x= px2 + 150, y= py2 + 120)

    e_verzio2 = tk.Entry()
    e_verzio2.place(x= px2 + 150, y= py2 + 150)

    e_javito_id2 = tk.Entry()
    e_javito_id2.place(x= px2 + 150, y= py2 + 180)

    e_changelog2 = tk.Entry()
    e_changelog2.place(x= px2 + 150, y= py2 + 210)

    e_javitasi_ido2 = tk.Entry()
    e_javitasi_ido2.place(x= px2 + 150, y= py2 + 240)

    insert_button2 = tk.Button(root, text="beszuras", font=('italic', 10), bg="white", command=insert2)
    insert_button2.place(x= px2 + 20, y= py2 + 270)

    update_button2 = tk.Button(root, text="frissit", font=('italic', 10), bg="white", command=update2)
    update_button2.place(x= px2 + 90, y= py2 + 270)

    delete_button2 = tk.Button(root, text="torles", font=('italic', 10), bg="white", command=delete2)
    delete_button2.place(x= px2 + 135, y= py2 + 270)

    get_button2 = tk.Button(root, text="lekeres", font=('italic', 10), bg="white", command=get2)
    get_button2.place(x= px2 + 195, y= py2 + 270)

#negyedik panel

    nev3 = tk.Label(root, text='nev', font=('bold', 10))
    nev3.place(x= px3 + 20, y= py3 + 30)

    verzio3 = tk.Label(root, text='verzio', font=('bold', 10))
    verzio3.place(x= px3 + 20, y= py3 + 60)

    leiras3 = tk.Label(root, text='leiras', font=('bold', 10))
    leiras3.place(x= px3 + 20, y= py3 + 90)

    changelog3 = tk.Label(root, text='changelog', font=('bold', 10))
    changelog3.place(x= px3 + 20, y= py3 + 120)

    elozo_verzio3 = tk.Label(root, text='elozo verzio', font=('bold', 10))
    elozo_verzio3.place(x= px3 + 20, y= py3 + 150)

    e_nev3 = tk.Entry()
    e_nev3.place(x= px3 + 150, y= py3 + 30)

    e_verzio3 = tk.Entry()
    e_verzio3.place(x= px3 + 150, y= py3 + 60)

    e_leiras3 = tk.Entry()
    e_leiras3.place(x= px3 + 150, y= py3 + 90)

    e_changelog3 = tk.Entry()
    e_changelog3.place(x= px3 + 150, y= py3 + 120)

    e_elozo_verzio3 = tk.Entry()
    e_elozo_verzio3.place(x= px3 + 150, y= py3 + 150)

    insert_button3 = tk.Button(root, text="beszuras", font=('italic', 10), bg="white", command=insert3)
    insert_button3.place(x= px3 + 20, y= py3 + 180)

    update_button3 = tk.Button(root, text="frissit", font=('italic', 10), bg="white", command=update3)
    update_button3.place(x= px3 + 90, y= py3 + 180)

    delete_button3 = tk.Button(root, text="torles", font=('italic', 10), bg="white", command=delete3)
    delete_button3.place(x= px3 + 135, y= py3 + 180)

    get_button3 = tk.Button(root, text="lekeres", font=('italic', 10), bg="white", command=get3)
    get_button3.place(x= px3 + 195, y= py3 + 180)
    
    show(mtable)
    root.mainloop()