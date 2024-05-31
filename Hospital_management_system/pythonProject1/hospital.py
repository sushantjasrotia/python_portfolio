from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        #=================variables=================

        self.Nameofthetablets=StringVar()
        self.Ref = StringVar()
        self.Dose = StringVar()
        self.Numberoftablets = StringVar()
        self.Lot = StringVar()
        self.Issuedate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.sideEffect = StringVar()
        self.FurtherInfo = StringVar()
        self.StorageAdvice = StringVar()
        self.DrivingUsingMachine = StringVar()
        self.medication = StringVar()
        self.PatientID = StringVar()
        self.NHSnumber = StringVar()
        self.PatientNumb = StringVar()
        self.dob = StringVar()
        self.PatientAddress = StringVar()

        lbl_title = Label(self.root, bd=20, relief=RIDGE, text = "HOSPITAL MANAGEMANT SYSTEM", fg="red", bg="grey", font=("times new roman",50,"bold"))
        lbl_title.pack(side=TOP,fill=X)

        # ===================Dataframe=========================
        Data_frame = Frame(self.root, bd=20, relief=RIDGE)
        Data_frame.place(x=0,y=130,width=1530,height=400)

        Data_frame_left = LabelFrame(Data_frame,bd=10,padx=20,relief=RIDGE,
                                     font=("arial",12,"bold"),text="Patient Information")
        Data_frame_left.place(x=0,y=5,width=980,height=350)

        Data_frame_right = LabelFrame(Data_frame, bd=10, padx=20, relief=RIDGE,
                                     font=("arial", 12, "bold"), text="Prescription")
        Data_frame_right.place(x=990, y=5, width=460, height=350)

        #====================== button - frame ==========================

        Button_frame = Frame(self.root, bd=20, relief=RIDGE)
        Button_frame.place(x=0, y=530, width=1530, height=70)

        #====================== Details Frame ============================

        Details_frame = Frame(self.root, bd=20, relief=RIDGE)
        Details_frame.place(x=0, y=600, width=1530, height=190)

        #====================Date_frame_left===============================

        lbl_name_tablet = Label(Data_frame_left,text="Name Of Tablet",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_name_tablet.grid(row=0, column=0, sticky=W)

        Com_Tablet_name = ttk.Combobox(Data_frame_left, textvariable=self.Nameofthetablets,state="readonly",
                                       font=("arial",12,"bold"),width=33)
        Com_Tablet_name['value']=("Nice", "Paracetamol", "Azithromiciene", "Zerodol-MR", "Septlin","Torex")
        Com_Tablet_name.current(0)
        Com_Tablet_name.grid(row=0, column=1)

        lbl_ref = Label(Data_frame_left,font=("arial",12,"bold"),text="Reference No:",padx=2)
        lbl_ref.grid(row=1,column=0,sticky=W)
        textref = Entry(Data_frame_left,textvariable=self.Ref,font=("arial",13,"bold"),width=35)
        textref.grid(row=1,column=1)

        lbl_dose = Label(Data_frame_left, font=("arial", 12, "bold"), text="Dose:", padx=2,pady=4)
        lbl_dose.grid(row=2, column=0, sticky=W)
        textdose = Entry(Data_frame_left,textvariable=self.Dose, font=("arial", 13, "bold"), width=35)
        textdose.grid(row=2, column=1)

        lbl_tablet_no = Label(Data_frame_left, font=("arial", 12, "bold"), text="No of Tablets:", padx=2, pady=4)
        lbl_tablet_no.grid(row=3, column=0, sticky=W)
        texttablets = Entry(Data_frame_left,textvariable=self.Numberoftablets, font=("arial", 13, "bold"), width=35)
        texttablets.grid(row=3, column=1)

        lbl_lot = Label(Data_frame_left, font=("arial", 12, "bold"), text="Lot:", padx=2, pady=6)
        lbl_lot.grid(row=4, column=0, sticky=W)
        textlot = Entry(Data_frame_left,textvariable=self.Lot, font=("arial", 13, "bold"), width=35)
        textlot.grid(row=4, column=1)

        lbl_issue_date = Label(Data_frame_left, font=("arial", 12, "bold"), text="Issue Date:", padx=2, pady=6)
        lbl_issue_date.grid(row=5, column=0, sticky=W)
        textissuedate = Entry(Data_frame_left,textvariable=self.Issuedate, font=("arial", 13, "bold"), width=35)
        textissuedate.grid(row=5, column=1)

        lbl_Expire_date = Label(Data_frame_left, font=("arial", 12, "bold"), text="Expire Date:", padx=2, pady=6)
        lbl_Expire_date.grid(row=6, column=0, sticky=W)
        textexpiredate = Entry(Data_frame_left, textvariable=self.ExpDate ,font=("arial", 13, "bold"), width=35)
        textexpiredate.grid(row=6, column=1)

        lbl_Daily_dose = Label(Data_frame_left, font=("arial", 12, "bold"), text="Daily Dose:", padx=2, pady=4)
        lbl_Daily_dose.grid(row=7, column=0, sticky=W)
        textdailydose = Entry(Data_frame_left,textvariable=self.DailyDose, font=("arial", 13, "bold"), width=35)
        textdailydose.grid(row=7, column=1)

        lbl_side_effect = Label(Data_frame_left, font=("arial", 12, "bold"), text="Side Effect:", padx=2, pady=6)
        lbl_side_effect.grid(row=8, column=0, sticky=W)
        textsideeffect = Entry(Data_frame_left,textvariable=self.sideEffect, font=("arial", 13, "bold"), width=35)
        textsideeffect.grid(row=8, column=1)

        lbl_add_info = Label(Data_frame_left, font=("arial", 12, "bold"), text="Add info:", padx=2)
        lbl_add_info.grid(row=0, column=2, sticky=W)
        textaddinfo = Entry(Data_frame_left,textvariable=self.FurtherInfo, font=("arial", 13, "bold"), width=35)
        textaddinfo.grid(row=0, column=3)

        lbl_bp = Label(Data_frame_left, font=("arial", 12, "bold"), text="BP:", padx=2, pady=6)
        lbl_bp.grid(row=1, column=2, sticky=W)
        textbp = Entry(Data_frame_left,textvariable=self.DrivingUsingMachine, font=("arial", 13, "bold"), width=35)
        textbp.grid(row=1, column=3)

        lbl_Storage = Label(Data_frame_left, font=("arial", 12, "bold"), text="Storage Advice:", padx=2, pady=6)
        lbl_Storage.grid(row=2, column=2, sticky=W)
        textstorage = Entry(Data_frame_left,textvariable=self.StorageAdvice, font=("arial", 13, "bold"), width=35)
        textstorage.grid(row=2, column=3)

        lbl_Medication = Label(Data_frame_left, font=("arial", 12, "bold"), text="Medication:", padx=2, pady=6)
        lbl_Medication.grid(row=3, column=2, sticky=W)
        text_medication = Entry(Data_frame_left, textvariable=self.medication,font=("arial", 13, "bold"), width=35)
        text_medication.grid(row=3, column=3)

        lbl_PatientId = Label(Data_frame_left, font=("arial", 12, "bold"), text="Patient ID:", padx=2, pady=6)
        lbl_PatientId.grid(row=4, column=2, sticky=W)
        text_PatientID = Entry(Data_frame_left,textvariable=self.PatientID, font=("arial", 13, "bold"), width=35)
        text_PatientID.grid(row=4, column=3)

        lbl_NHS_no = Label(Data_frame_left, font=("arial", 12, "bold"), text="NHS No.", padx=2, pady=6)
        lbl_NHS_no.grid(row=5, column=2, sticky=W)
        text_NHS_no = Entry(Data_frame_left,textvariable=self.NHSnumber, font=("arial", 13, "bold"), width=35)
        text_NHS_no.grid(row=5, column=3)

        lbl_Paitent_name = Label(Data_frame_left, font=("arial", 12, "bold"), text="Patient_Name:", padx=2, pady=6)
        lbl_Paitent_name.grid(row=6, column=2, sticky=W)
        text_patient_name = Entry(Data_frame_left, textvariable=self.PatientNumb,font=("arial", 13, "bold"), width=35)
        text_patient_name.grid(row=6, column=3)

        lbl_DOB = Label(Data_frame_left, font=("arial", 12, "bold"), text="DOB:", padx=2, pady=6)
        lbl_DOB.grid(row=7, column=2, sticky=W)
        textdob = Entry(Data_frame_left, textvariable=self.dob, font=("arial", 13, "bold"), width=35)
        textdob.grid(row=7, column=3)

        lbl_address = Label(Data_frame_left, font=("arial", 12, "bold"), text="Address", padx=2, pady=6)
        lbl_address.grid(row=8, column=2, sticky=W)
        textaddress = Entry(Data_frame_left, textvariable=self.PatientAddress, font=("arial", 13, "bold"), width=35)
        textaddress.grid(row=8, column=3)

        #===============================Dateframe_right===========================
        self.txtPrescription = Text(Data_frame_right,  font=("arial", 13, "bold"),width=45,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)

        #===============================Button_frame============================
        btn_prescription = Button(Button_frame,text="Prescription",fg="White",bg="Pink",font=("arial",16,"bold"),width=18,padx=1,pady=2,command=self.prectioption_data)
        btn_prescription.grid(row=0, column=0)

        btn_prescription_data = Button(Button_frame, text="Prescription Data", fg="White", bg="Pink",
                                       font=("arial", 16, "bold"), width=18, padx=1, pady=2,command=self.iPrescriptionDate)
        btn_prescription_data.grid(row=0, column=1)


        btn_Update = Button(Button_frame,text="Update",fg="White",bg="Pink",font=("arial",16,"bold"),width=19,padx=1,pady=2,command=self.update)
        btn_Update.grid(row=0, column=2)


        btn_delete = Button(Button_frame,text="Delete",fg="White",bg="Pink",font=("arial",16,"bold"),width=18,padx=1,pady=1,command=self.delete)
        btn_delete.grid(row=0, column=3)


        btn_Clear = Button(Button_frame,text="Clear",fg="White",bg="Pink",font=("arial",16,"bold"),width=19,padx=1,pady=2,command=self.clear)
        btn_Clear.grid(row=0, column=4)


        btn_Exit = Button(Button_frame,text="Exit",fg="White",bg="Pink",font=("arial",16,"bold"),width=18,padx=1,pady=2,command=self.Exit)
        btn_Exit.grid(row=0, column=5)

        #================================Table===========================
        #================================Scrollbar=======================
        scroll_x = ttk.Scrollbar(Details_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Details_frame, orient=VERTICAL)
        self.hospital_table = ttk.Treeview(Details_frame, column=("nameoftable", "ref", "dose","nofotablets", "lot","issuedate","expdate","dailydose","storage","nhsnumber","pname","dob","address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x = ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y = ttk.Scrollbar(command=self.hospital_table.xview)

        self.hospital_table.heading("nameoftable", text="Name of Table")
        self.hospital_table.heading("ref", text="Reference No.")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("nofotablets", text="No of Tablets")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issuedate", text="Issue Date")
        self.hospital_table.heading("expdate", text="Expire Date")
        self.hospital_table.heading("dailydose", text="Daily Dose")
        self.hospital_table.heading("storage", text="Storage")
        self.hospital_table.heading("nhsnumber", text="NHS Number")
        self.hospital_table.heading("pname", text="Patient Name")
        self.hospital_table.heading("dob", text="DOB")
        self.hospital_table.heading("address", text="Address")


        self.hospital_table["show"] = "headings"


        self.hospital_table.column("nameoftable",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nofotablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        #=========================================Functinality Declaration ====================================================

    def iPrescriptionDate(self):
        if self.Numberoftablets.get() == "" or self.Ref.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(user='root', password='Nokia?tl3',
                                               host='127.0.0.1',
                                               database='hospital_mng_sys')

                my_cursor = conn.cursor()

                # Corrected SQL query syntax
                sql_query = """INSERT INTO hospital 
                               (Name_of_tablets, Reference_nol, dose, Number_of_tablets, lot, issue_date, expire_date, daily_dose, storage, nhs_number, paitent_name, dob, patient_address)
                               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

                # Using placeholder values to prevent SQL injection
                data = (self.Nameofthetablets.get(), self.Ref.get(), self.Dose.get(), self.Numberoftablets.get(),
                        self.Lot.get(), self.Issuedate.get(), self.ExpDate.get(), self.DailyDose.get(),
                        self.StorageAdvice.get(), self.NHSnumber.get(), self.PatientNumb.get(), self.dob.get(),
                        self.PatientAddress.get())

                my_cursor.execute(sql_query, data)

                conn.commit()  # Commit changes to the database

                self.fetch_data()

                conn.close()  # Close the connection

                messagebox.showinfo("Success", "Record has been inserted")
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error occurred: {err}")

    def update(self):
        conn = mysql.connector.connect(user='root', password='Nokia?tl3',
                                       host='127.0.0.1',
                                       database='hospital_mng_sys')

        my_cursor = conn.cursor()
        sql_update_data = ("""UPDATE hospital 
                            SET Name_of_tablets=%s, dose=%s, Number_of_tablets=%s, lot=%s, issue_date=%s, 
                                expire_date=%s, daily_dose=%s, storage=%s,
                                nhs_number=%s, paitent_name=%s, dob=%s, patient_address=%s 
                            WHERE Reference_nol=%s""")

        data_2 = (self.Nameofthetablets.get(), self.Dose.get(), self.Numberoftablets.get(),
                  self.Lot.get(), self.Issuedate.get(), self.ExpDate.get(), self.DailyDose.get(),
                  self.StorageAdvice.get(), self.NHSnumber.get(), self.PatientNumb.get(), self.dob.get(),
                  self.PatientAddress.get(), self.Ref.get())

        my_cursor.execute(sql_update_data, data_2)
        self.fetch_data()
        # Commit the changes
        conn.commit()
        # Close cursor and connection
        my_cursor.close()
        conn.close()




    def fetch_data(self):
        conn = mysql.connector.connect(user='root', password='Nokia?tl3',
                                       host='127.0.0.1',
                                       database='hospital_mng_sys')

        my_cursor = conn.cursor()
        my_cursor.execute("select * from hospital")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event = ""):
        cursor_row = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        row = content["values"]
        self.Nameofthetablets.set(row[0])
        self.Ref.set(row[1])
        self.Dose.set(row[2])
        self.Numberoftablets.set(row[3])
        self.Lot.set(row[4])
        self.Issuedate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.StorageAdvice.set(row[8])
        self.NHSnumber.set(row[9])
        self.PatientNumb.set(row[10])
        self.dob.set(row[11])
        self.PatientAddress.set(row[12])

    def prectioption_data(self):
        self.txtPrescription.insert(END,"Name of Tablets:\t\t\t" + self.Numberoftablets.get() + "\n")
        self.txtPrescription.insert(END,"Reference No:\t\t\t" + self.Ref.get() + "\n")
        self.txtPrescription.insert(END,"Dose:\t\t\t" + self.Dose.get() + "\n")
        self.txtPrescription.insert(END,"Number of Tablets:\t\t\t" + self.Numberoftablets.get() + "\n")
        self.txtPrescription.insert(END,"Lot:\t\t\t" + self.Lot.get() + "\n")
        self.txtPrescription.insert(END,"Issue Date:\t\t\t" + self.Issuedate.get() + "\n")
        self.txtPrescription.insert(END,"Exp date:\t\t\t" + self.ExpDate.get() + "\n")
        self.txtPrescription.insert(END,"Daily Dose:\t\t\t" + self.DailyDose.get() + "\n")
        self.txtPrescription.insert(END,"Side Effect:\t\t\t" + self.sideEffect.get() + "\n")
        self.txtPrescription.insert(END,"Further Info:\t\t\t" + self.FurtherInfo.get() + "\n")
        self.txtPrescription.insert(END,"Storage Advice:\t\t\t" + self.StorageAdvice.get() + "\n")
        self.txtPrescription.insert(END,"Driving Using Machine:\t\t\t" + self.DrivingUsingMachine.get() + "\n")
        self.txtPrescription.insert(END,"Patient ID:\t\t\t" + self.PatientID.get() + "\n")
        self.txtPrescription.insert(END,"NHS number:\t\t\t" + self.NHSnumber.get() + "\n")
        self.txtPrescription.insert(END,"Patient Name:\t\t\t" + self.PatientNumb.get() + "\n")
        self.txtPrescription.insert(END,"Date of Birth:\t\t\t" + self.dob.get() + "\n")
        self.txtPrescription.insert(END,"PatientAddress:\t\t\t" + self.PatientAddress.get() + "\n")

    def delete(self):
        conn = mysql.connector.connect(user='root', password='Nokia?tl3',
                                       host='127.0.0.1',
                                       database='hospital_mng_sys')
        mycursor = conn.cursor()
        query = "DELETE FROM hospital WHERE Reference_nol=%s"
        value = (self.Ref.get(),)  # Corrected to properly define a tuple
        mycursor.execute(query, value)

        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete", "Patient has been deleted successfully")

    def clear(self):
        self.Numberoftablets.set("")
        self.Ref.set("")
        self.Dose.set("")
        self.Numberoftablets.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.sideEffect.set("")
        self.FurtherInfo.set("")
        self.StorageAdvice.set("")
        self.DrivingUsingMachine.set("")
        self.PatientID.set("")
        self.NHSnumber.set("")
        self.PatientNumb.set("")
        self.dob.set("")
        self.PatientAddress.set("")
        self.txtPrescription.delete("1.0",END)

    def Exit(self):
        Exit = messagebox.askyesno("hospital management system","Confirm you want to exit")
        if Exit>0:
            root.destroy()
            return















root=Tk()
ob=Hospital(root)
root.mainloop()