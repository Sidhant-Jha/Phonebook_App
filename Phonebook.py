from tkinter import *
from tkinter.scrolledtext import *
from tkinter.messagebox import *
import re
from mysql.connector import *


def close_splash_screen():
    splash_screen.destroy()
    create_main_window()

def create_main_window():

    root = Tk()
    root.title("Phone Book App")
    root.geometry("590x540+154+155")


    f = ("Comic Sans MS", 18, "bold")
    f2 = ("Comic Sans MS", 15, "bold")

    root.configure(background= "DarkSeaGreen2")


    def confirm_close():
        result = askyesno("Confirmation", "Do you really want to close the application?")
        if result:
            root.destroy()


    root.protocol("WM_DELETE_WINDOW", confirm_close)        
                


    def f1():
        addemp.deiconify()
        root.withdraw()

    def f2():
        root.deiconify()
        addemp.withdraw()

    def f3():
        updemp.deiconify()
        root.withdraw()

    def f4():
        root.deiconify()
        updemp.withdraw()

    def f5():
        dltemp.deiconify()
        root.withdraw()

    def f6():
        root.deiconify()
        dltemp.withdraw()    

    def f7():
        viwemp.deiconify()
        root.withdraw()
        vwdata.delete(1.0, END)
        con = None
        try:
            con = connect(host = "localhost", user = "root", password = "abc456", database = "App")
            print(con)
            cursor = con.cursor()
            sql = "SELECT * FROM People ORDER BY phone_number ASC"
            cursor.execute(sql)
            data = cursor.fetchall()
            info = ""
            for d in data:
                info = info + " Mobile No. = " + str(d[0]) + "| Name = " + str(d[1]) + "| Email_id = " + str(d[2])   +  "| Address = " + str(d[3]) + "\n"
            vwdata.insert(INSERT, info)
        except Exception as e:
            showerror("issue ", e)
        finally:
            if con is not None:
                con.close()

    def f8():
        root.deiconify()
        viwemp.withdraw()    



    def add():
        con = None 
        try:
            con = connect(host = "localhost", user = "root", password = "abc456", database = "App")
            cursor = con.cursor()
            sql = "insert into People values('%s', '%s', '%s', '%s')"
            id = id_entry.get()
            name = name_entry.get()
            emaila = email_id_entry.get()
            addres = address_entry.get()


            idi = id.strip()
            namen = name.strip()
            emailas = emaila.strip()
            address = addres.strip()


            if idi == "":
                showerror("Error", "Name cannot be empty")
                con.rollback()
                id_entry.delete(0, END)
                id_entry.focus()
                return
            

            if any(not char.isalnum() and char != ' ' for char in idi):
                showerror("Error", "Name cannot contain special character")
                con.rollback()
                id_entry.delete(0, END)
                id_entry.focus()
                return
            

            if not all(char.isalpha() or char.isspace() for char in idi):
                showerror("Error", "Name cannot contain numeric value")
                con.rollback()
                id_entry.delete(0, END)
                id_entry.focus()
                return

            if not namen:
                showerror("Error", "Entered number cannot be empty.")
                name_entry.delete(0, END)
                name_entry.focus()
                return


            
            try:
                namen_float = float(namen)
            except ValueError:
                showerror("Error", "Entered number cannot be text or special characters")
                con.rollback()
                name_entry.delete(0, END)
                id_entry.focus()
                return

            
            if namen_float < 0:
                showerror("Error", "Entered number cannot be negative.")
                con.rollback()
                name_entry.delete(0, END)
                name_entry.focus()
                return

            if namen_float == 0:
                showerror("Error", "Entered number should be greater than 0")
                con.rollback()
                name_entry.delete(0, END)
                name_entry.focus()
                return
            
            if namen_float > 10000000000 or namen_float < 1000000000:
                showerror("Error", "Entered number should be a 10 digit number")
                con.rollback()
                name_entry.delete(0, END)
                name_entry.focus()
                return
            
            if any(not char.isalnum() for char in namen):
                showerror("Error", "Entered number cannot contain special characters.")
                con.rollback()
                name_entry.delete(0, END)
                name_entry.focus()
                return

            

            if emailas == "":
                showerror("Error", "Email cannot be empty")
                con.rollback()
                email_id_entry.delete(0, END)
                email_id_entry.focus()
                return
            
            if not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', emailas):
                showerror("Error", "Email type not valid")
                con.rollback()
                email_id_entry.delete(0, END)
                email_id_entry.focus()
                return
            

            if addres == "":
                showerror("Error", "Address cannot be empty")
                con.rollback()
                address_entry.delete(0, END)
                address_entry.focus()
                return
            


            


            cursor.execute(sql % (name, id, emaila, address))
            con.commit()
            showinfo("Success", "record created")
            id_entry.delete(0, END)
            name_entry.delete(0, END)
            email_id_entry.delete(0, END)
            address_entry.delete(0, END)
            id_entry.focus()

        finally:
            if con is not None:
                con.close()




    def update(update_name, update_num, update_email, update_address):
        con = None
        try:
            con = connect(host = "localhost", user = "root", password = "abc456", database = "App")
            cursor = con.cursor()
            check_sql = "SELECT phone_number FROM People WHERE phone_number = %s"
            id = update_num
            name = update_name
            email = update_email
            addres = update_address


            idi = id.strip()
            namen = name.strip()
            emails = email.strip()
            address = addres.strip()


            if namen == "":
                showerror("Error", "Name cannot be empty")
                con.rollback()
                uname_entry.delete(0, END)
                uname_entry.focus()
                return


            if any(not char.isalnum() and char != ' ' for char in namen):
                showerror("Error", "Name cannot contain special character")
                con.rollback()
                uname_entry.delete(0, END)
                uname_entry.focus()
                return

            if not all(char.isalpha() or char.isspace() for char in namen):
                showerror("Error", "Name cannot contain numeric values")
                con.rollback()
                uname_entry.delete(0, END)
                uname_entry.focus()
                return



            if not idi:
                showerror("Error", "Entered number cannot be empty.")
                id_entry.delete(0, END)
                id_entry.focus()
                return

            
            try:
                idi_float = float(idi)
            except ValueError:
                showerror("Error", "Entered number cannot be text or special character")
                con.rollback()
                uid_entry.delete(0, END)
                uid_entry.focus()
                return


            if idi_float < 0:
                showerror("Error", "Entered number cannot be negative.")
                con.rollback()
                uid_entry.delete(0, END)
                uid_entry.focus()
                return

            if idi_float == 0:
                showerror("Error", "Entered number should be greater than 0")
                con.rollback()
                uid_entry.delete(0, END)
                uid_entry.focus()
                return
            
            if idi_float > 10000000000 and idi_float < 1000000000:
                showerror("Error", "Entered number should be a 10 digit number")
                con.rollback()
                uid_entry.delete(0, END)
                uid_entry.focus()
                return
            
            if any(not char.isalnum() for char in idi):
                showerror("Error", "Entered number cannot contain special characters.")
                con.rollback()
                uid_entry.delete(0, END)
                uid_entry.focus()
                return
            

        

            if emails == "":
                showerror("Error", "Email cannot be empty")
                con.rollback()
                usalary_entry.delete(0, END)
                usalary_entry.focus()
                return
            
            if not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', emails):
                showerror("Error", "Email type not valid")
                con.rollback()
                usalary_entry.delete(0, END)
                usalary_entry.focus()
                return
            

            if address == "":
                showerror("Error", "Address cannot be empty")
                con.rollback()
                uaddress_entry.delete(0, END)
                uaddress_entry.focus()
                return
            


            
            cursor.execute(check_sql, (int(id),))
            if cursor.fetchone() is None:
                showerror("Error", "Contact number not found")
                uid_entry.delete(0, END)
                uname_entry.delete(0, END)
                usalary_entry.delete(0, END)
                uaddress_entry.delete(0, END)
                uid_entry.focus()
                return

            print("hello")

            # Update the record
            update_sql = "UPDATE People SET name= %s, email_id= %s, Address = %s WHERE phone_number = %s"
            cursor.execute(update_sql, (name, email, addres, id))
            con.commit()
            showinfo("Success", "Record updated")
            uid_entry.delete(0, END)
            uname_entry.delete(0, END)
            usalary_entry.delete(0, END)
            uaddress_entry.delete(0, END)
            uid_entry.focus()
        except Exception as e:
            con.rollback()
            showerror("Issue", e)
        finally:
            if con is not None:
                con.close()






    def delete(emp_id):
        con = None
        try:
            con = connect(host = "localhost", user = "root", password = "abc456", database = "App")
            print(con)
            cursor = con.cursor()

            # Check if the contact number exists
            check_sql = "Select * from People where phone_number = %s"
            id = emp_id
            idi = id.strip()

            if not idi:
                showerror("Error", "Entered number cannot be empty.")
                did_entry.delete(0, END)
                did_entry.focus()
                return

            
            try:
                idi_float = float(idi)
            except ValueError:
                showerror("Error", "Entered number cannot be text or special character")
                con.rollback()
                did_entry.delete(0, END)
                did_entry.focus()
                return

            
            if idi_float < 0:
                showerror("Error", "Entered number cannot be negative.")
                con.rollback()
                did_entry.delete(0, END)
                did_entry.focus()
                return

            if idi_float == 0:
                showerror("Error", "Entered number should be greater than 0")
                con.rollback()
                did_entry.delete(0, END)
                did_entry.focus()
                return
            
            if idi_float > 10000000000 and idi_float < 1000000000:
                showerror("Error", "Entered number should be a 10 digit number")
                con.rollback()
                did_entry.delete(0, END)
                did_entry.focus()
                return
            
            if any(not char.isalnum() for char in idi):
                showerror("Error", "Entered number cannot contain special characters.")
                con.rollback()
                did_entry.delete(0, END)
                did_entry.focus()
                return
            

            cursor.execute(check_sql, (emp_id,))
            if cursor.fetchone() is None:
                showerror("Error", "Contact number not found")
                did_entry.delete(0, END)
                did_entry.focus()
                return

            # Delete the record
            delete_sql = "DELETE FROM People WHERE phone_number = %s"
            cursor.execute(delete_sql, (emp_id,))
            con.commit()
            showinfo("Success", "Record deleted")
            did_entry.delete(0, END)
            did_entry.focus()
        except Exception as e:
            con.rollback()
            showerror("Issue", e)
        finally:
            if con is not None:
                con.close()






    ################################################    ADD Contact ############################################################

    # Create a black frame
    frame = Frame(root, bg="black", bd=0.5, relief=SUNKEN)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    addbtn = Button(frame, font=f, text="Add", bg="white", bd=0,width = 6,  highlightthickness=0, command = f1)
    viewbtn = Button(frame, font=f, text="View", bg="white", bd=0, width = 6,  highlightthickness=0, command = f7)
    updatebtn = Button(frame, font=f, text="Update", bg="white", bd=0, highlightthickness=0, command = f3)
    deletebtn = Button(frame, font=f, text="Delete", bg="white", bd=0, highlightthickness=0, command = f5)

    addbtn.grid(row=0, column=0, padx=10, pady=10)
    viewbtn.grid(row=0, column=1, padx=10, pady=10)
    updatebtn.grid(row=1, column=0, padx=10, pady=10)
    deletebtn.grid(row=1, column=1, padx=10, pady=10)

    label1 = Label(root, text="Phone Book App", font=f, bg="DarkSeaGreen2")
    label1.place(x=200, y=10)

    canvas = Canvas(root, width=200, height=2, bg="black", highlightthickness=0)
    canvas.create_line(0, 2, 200, 2, fill="black")
    canvas.place(x=190, y=45)



    addemp = Toplevel(root)
    addemp.title("Add Contact")
    addemp.geometry("590x540+154+155")
    addemp.configure(background= "lightsteelblue")

    label1 = Label(addemp, text="Register Contact", font = f, bg="lightsteelblue")
    labid = Label(addemp, font = f, text = "Name", bg = "lightsteelblue")
    id_entry = Entry(addemp, font = f, highlightthickness=2, highlightbackground="steelblue")
    labname = Label(addemp, font =f, text = "Mobile No", bg = "lightsteelblue")
    name_entry = Entry(addemp, font = f, highlightthickness=2, highlightbackground="steelblue")
    labsalary = Label(addemp, font = f, text = "Email_Id", bg = "lightsteelblue")
    labaddres = Label(addemp, text="Address ", bg="lightsteelblue", font=f)
    address_entry = Entry(addemp, font=f, highlightthickness=2, highlightbackground="steelblue")
    email_id_entry = Entry(addemp, font = f, highlightthickness=2, highlightbackground="steelblue") 

    btnsave = Button(addemp, font = f2, text = "Save", width = 7, command = add)
    btnback = Button(addemp, font = f2, text = "Back", width = 7, command = f2)


    label1.place(x = 200 , y = 10)
    labid.place(x = 10, y = 100)
    id_entry.place(x = 160, y = 100)
    labname.place(x = 10, y = 160)
    name_entry.place(x = 160 , y = 160)
    labsalary.place(x = 10 , y = 220)
    email_id_entry.place(x = 160, y = 220)
    labaddres.place(x = 10, y= 280)
    address_entry.place(x = 160, y = 280)

    btnsave.place(x = 240, y = 390)
    btnback.place(x = 240, y = 450) 

    addemp.withdraw()

    ############################################## UPDATE Contact #############################################


    updemp = Toplevel(root)
    updemp.title("Update Contact")
    updemp.geometry("590x540+154+155")
    updemp.configure(background= "peachpuff")

    ulabel1 = Label(updemp, text="Update Contact", font = f, bg = "peachpuff")
    uid_entry = Entry(updemp, font = f, highlightthickness=2, highlightbackground="steelblue")
    ulabid = Label(updemp, font = f, text = "Name", bg = "peachpuff")
    ulabname = Label(updemp, font =f, text = "Mobile No", bg = "peachpuff")
    uname_entry = Entry(updemp, font = f, highlightthickness=2, highlightbackground="steelblue")
    ulabsalary = Label(updemp, font = f, text = "Email_Id", bg = "peachpuff")
    ulabaddres = Label(updemp, text="Address ", font=f, bg = "peachpuff")
    uaddress_entry = Entry(updemp, font=f, highlightthickness=2, highlightbackground="steelblue")
    usalary_entry = Entry(updemp, font = f, highlightthickness=2, highlightbackground="steelblue") 

    ubtnsave = Button(updemp, font = f2, text = "Save", width = 7, command=lambda: update(uid_entry.get(), uname_entry.get(), usalary_entry.get(), uaddress_entry.get()))
    ubtnback = Button(updemp, font = f2, text = "Back", width = 7, height = 0, command = f4)


    ulabel1.place(x = 200 , y = 10)
    ulabid.place(x = 10, y = 100)
    uid_entry.place(x = 160, y = 100)
    ulabname.place(x = 10, y = 160)
    uname_entry.place(x = 160 , y = 160)
    ulabsalary.place(x = 10 , y = 220)
    usalary_entry.place(x = 160, y = 220)
    ulabaddres.place(x = 10, y= 280)
    uaddress_entry.place(x = 160, y = 280)

    ubtnsave.place(x = 240, y = 380)
    ubtnback.place(x = 240, y = 450) 

    updemp.withdraw()


    ################################################# DELETE Contact  #################################################

    dltemp = Toplevel(root)
    dltemp.title("Delete Employee")
    dltemp.geometry("590x540+154+155")
    dltemp.configure(background= "lightsteelblue")

    dlabel1 = Label(dltemp, text="Delete Contact", font = f, bg = "lightsteelblue")
    dlabid = Label(dltemp, font = f, text = "Mobile No", bg = "lightsteelblue")
    did_entry = Entry(dltemp, font = f, highlightthickness=2, highlightbackground="steelblue")

    dbtnsave = Button(dltemp, font=f2, text="Delete" , command=lambda: delete(did_entry.get()))
    dbtnback = Button(dltemp, font = f2, text = "Back" , command = f6)

    dlabel1.place(x = 200 , y = 10)
    dlabid.place(x = 10, y = 100)
    did_entry.place(x = 160, y = 100)

    dbtnsave.place(x = 240, y = 300)
    dbtnback.place(x = 245, y = 370)
    dltemp.withdraw()

    ############################################################## View Contacts ######################################################

    viwemp = Toplevel(root)
    viwemp.title("View Contacts")
    viwemp.geometry("590x540+154+155")
    viwemp.configure(background= "palegoldenrod")

    vw_scrollbar_x = Scrollbar(viwemp, orient=HORIZONTAL)
    vwdata = ScrolledText(viwemp, width=36, height=12, font=f, wrap="none", xscrollcommand=vw_scrollbar_x.set,  )

    vw_scrollbar_x.config(command=vwdata.xview)
    vwdata.pack(pady=10)
    vw_scrollbar_x.pack(fill=X, pady=10)


    vbtnback = Button(viwemp, font = f2, text = "Back", width = 9, command = f8)
    vwdata.pack(pady = 10)
    vbtnback.pack(pady = 5)
    viwemp.withdraw()


    root.mainloop()


splash_screen = Tk()
splash_screen.overrideredirect(True)  # Remove the window decorations
splash_screen_label = Label(splash_screen, text="Phone Book App", font=("Comic Sans MS", 24, "bold"))
splash_screen_label.pack(pady=100)

# Center the splash screen
splash_screen.update_idletasks()
width = splash_screen.winfo_width()
height = splash_screen.winfo_height()
x = (splash_screen.winfo_screenwidth() // 2) - (width // 2)
y = (splash_screen.winfo_screenheight() // 2) - (height // 2)
splash_screen.geometry(f"{width}x{height}+{x}+{y}")

# Close the splash screen after 3 seconds
splash_screen.after(3000, close_splash_screen)

splash_screen.mainloop()