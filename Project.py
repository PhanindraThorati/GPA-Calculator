from tkinter import *
root=Tk()

def group_click():
    global groups;
    group_ans=group_entry.get()
    if group_ans=="ECE":
        groups="ECE"
    elif group_ans=="CSE":
        groups="CSE"
    elif group_ans=="IT":
        groups="IT"
    elif group_ans=="EEE":
        groups="EEE"
    elif group_ans=="EIE":
        groups="EIE"
    elif group_ans=="MECH":
        groups="MECH"
    elif group_ans=="CIVIL":
        groups="CIVIL"
    elif group_ans=="AERO":
        groups="AERO"
    else:
        groups=0

def year_click():
    global years;
    year_ans=year_entry.get()
    if year_ans=="1":
        years=1
    elif year_ans=="2":
        years=2
    elif year_ans=="3":
        years=3
    elif year_ans=="4":
        years=4
    else:
        years=0

def sem_click():
    global sems;
    sem_ans=sem_entry.get()
    if sem_ans=="1":
        sems=1
    elif sem_ans=="2":
        sems=2
    else:
        sems=0
    subject_display();

def subject_display():
    if groups=="ECE" and years==1 and sems==1:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(6):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[4,4,4,3,1.5,1.5]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/18
            result1=str(result)
            names=entrys.get()
            label7=Label(root,text=names+" your CGPA is "+result1)
            label7.grid(row=15)
            label7.after(5000,label7.destroy)
            
        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            name.destroy()
            label6.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()
                    
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="Mathematics 1")
        label2=Label(root,text="Applied Physics")
        label3=Label(root,text="PPS")
        label4=Label(root,text="EG")
        label5=Label(root,text="Applied Physics Lab")
        label6=Label(root,text="PPS Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        button1.grid(row=14,column=2)
        button2.grid(row=14,column=1)
    elif groups=="ECE" and years==1 and sems==2:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(8):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[4,4,3,2,2.5,1,1,1.5]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/19
            result1=str(result)
            names=entrys.get()
            label9=Label(root,text=names+" your CGPA is "+result1)
            label9.grid(row=17)
            label9.after(5000,label9.destroy)

        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            entry8.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()

        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="Mathematics 2")
        label2=Label(root,text="Chemistry")
        label3=Label(root,text="BEE")
        label4=Label(root,text="English")
        label5=Label(root,text="Engineering Workshop")
        label6=Label(root,text="ELCS Lab")
        label7=Label(root,text="BEE Lab")
        label8=Label(root,text="Chemistry Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entry8=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        label8.grid(row=15,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        entry8.grid(row=15,column=1)
        button1.grid(row=16,column=2)
        button2.grid(row=16,column=1)
    elif groups=="ECE" and years==2 and sems==1:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(8):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[4,3,4,4,3,1,1,1]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/21
            result1=str(result)
            names=entrys.get()
            label9=Label(root,text=names+" your CGPA is "+result1)
            label9.grid(row=17)
            label9.after(5000,label9.destroy)

        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            entry8.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()   
            
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="EDC")
        label2=Label(root,text="NATL")
        label3=Label(root,text="DSD")
        label4=Label(root,text="SS")
        label5=Label(root,text="PTSP")
        label6=Label(root,text="EDC Lab")
        label7=Label(root,text="DSD Lab")
        label8=Label(root,text="BS Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entry8=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        label8.grid(row=15,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        entry8.grid(row=15,column=1)
        button1.grid(row=16,column=2)
        button2.grid(row=16,column=1)
    elif groups=="ECE" and years==2 and sems==2:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(8):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[4,3,4,3,3,1.5,1.5,1]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/21
            result1=str(result)
            names=entrys.get()
            label9=Label(root,text=names+" your CGPA is "+result1)
            label9.grid(row=17)
            label9.after(5000,label9.destroy)

        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            entry8.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()    
            
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="LTNMCV")
        label2=Label(root,text="EMFW")
        label3=Label(root,text="ADC")
        label4=Label(root,text="LICA")
        label5=Label(root,text="ECA")
        label6=Label(root,text="ADC Lab")
        label7=Label(root,text="IC Lab")
        label8=Label(root,text="ECA Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entry8=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        label8.grid(row=15,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        entry8.grid(row=15,column=1)
        button1.grid(row=16,column=2)
        button2.grid(row=16,column=1)
    elif groups=="ECE" and years==3 and sems==1:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(8):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[4,4,4,3,3,1.5,1.5,1]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/22
            result1=str(result)
            names=entrys.get()
            label9=Label(root,text=names+" your CGPA is "+result1)
            label9.grid(row=17)
            label9.after(5000,label9.destroy)

        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            entry8.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()    
            
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="MP & MC")
        label2=Label(root,text="DC & Networks")
        label3=Label(root,text="CS")
        label4=Label(root,text="BEFA")
        label5=Label(root,text="PE - 1")
        label6=Label(root,text="MP & MC Lab")
        label7=Label(root,text="DC & Networks Lab")
        label8=Label(root,text="ACS Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entry8=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        label8.grid(row=15,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        entry8.grid(row=15,column=1)
        button1.grid(row=16,column=2)
        button2.grid(row=16,column=1)
    elif groups=="ECE" and years==3 and sems==2:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(8):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[4,4,4,3,3,1.5,1.5,1]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/22
            result1=str(result)
            names=entrys.get()
            label9=Label(root,text=names+" your CGPA is "+result1)
            label9.grid(row=17)
            label9.after(5000,label9.destroy)

        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            entry8.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()       
            
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="AP")
        label2=Label(root,text="DSP")
        label3=Label(root,text="VLSI Design")
        label4=Label(root,text="PE - 2")
        label5=Label(root,text="OE - 1")
        label6=Label(root,text="DSP Lab")
        label7=Label(root,text="e-CAD Lab")
        label8=Label(root,text="Scripting Languages Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entry8=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        label8.grid(row=15,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        entry8.grid(row=15,column=1)
        button1.grid(row=16,column=2)
        button2.grid(row=16,column=1)
    elif groups=="ECE" and years==4 and sems==1:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get(),entry9.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(9):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[3,3,3,3,2,1,2,1,3]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/21
            result1=str(result)
            names=entrys.get()
            label10=Label(root,text=names+" your CGPA is "+result1)
            label10.grid(row=18)
            label10.after(5000,label10.destroy)

        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            label9.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            entry8.destroy()
            entry9.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()    
            
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="MOC")
        label2=Label(root,text="PE - 3")
        label3=Label(root,text="PE - 4")
        label4=Label(root,text="OE - 2")
        label5=Label(root,text="PPLE")
        label6=Label(root,text="MOC Lab")
        label7=Label(root,text="Mini Project / Summer Internship")
        label8=Label(root,text="Seminar")
        label9=Label(root,text="Project Stage-1")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entry8=Entry(root,width=10,borderwidth=5)
        entry9=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        label8.grid(row=15,column=0)
        label9.grid(row=16,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        entry8.grid(row=15,column=1)
        entry9.grid(row=16,column=1)
        button1.grid(row=17,column=2)
        button2.grid(row=17,column=1)
    elif groups=="ECE" and years==4 and sems==2:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(4):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[3,3,3,7]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/16
            result1=str(result)
            names=entrys.get()
            label5=Label(root,text=names+" your CGPA is "+result1)
            label5.grid(row=13)
            label5.after(5000,label5.destroy)

        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            name.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()    
            
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="PE - 5")
        label2=Label(root,text="PE - 6")
        label3=Label(root,text="OE - 3")
        label4=Label(root,text="Project Stage - 2")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        button1.grid(row=12,column=2)
        button2.grid(row=12,column=1)
    elif groups=="CSE" and years==1 and sems==1:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(8):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[4,4,3,2,2.5,1,1,1.5]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/19
            result1=str(result)
            names=entrys.get()
            label9=Label(root,text=names+" your CGPA is "+result1)
            label9.grid(row=17)
            label9.after(5000,label9.destroy)
        
        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            entry8.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()
        
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="Mathematics 1")
        label2=Label(root,text="Chemistry")
        label3=Label(root,text="BEE")
        label4=Label(root,text="English")
        label5=Label(root,text="Engineering Workshop")
        label6=Label(root,text="ELCS Lab")
        label7=Label(root,text="BEE Lab")
        label8=Label(root,text="Chemistry Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entry8=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        label8.grid(row=15,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        entry8.grid(row=15,column=1)
        button1.grid(row=16,column=2)
        button2.grid(row=16,column=1)
    elif groups=="CSE" and years==1 and sems==2:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(6):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[4,4,4,3,1.5,1.5]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/18
            result1=str(result)
            names=entrys.get()
            label7=Label(root,text=names+" your CGPA is "+result1)
            label7.grid(row=15)
            label7.after(5000,label7.destroy)
            
        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            name.destroy()
            label6.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()
            
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="Mathematics 2")
        label2=Label(root,text="Applied Physics")
        label3=Label(root,text="PPS")
        label4=Label(root,text="EG")
        label5=Label(root,text="Applied Physics Lab")
        label6=Label(root,text="PPS Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        button1.grid(row=14,column=2)
        button2.grid(row=14,column=1)
    elif groups=="CSE" and years==2 and sems==1:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get(),entry9.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(9):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[3,4,4,3,2,1,1.5,1.5,1]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/21
            result1=str(result)
            names=entrys.get()
            label10=Label(root,text=names+" your CGPA is "+result1)
            label10.grid(row=18)
            label10.after(5000,label10.destroy)
        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            label9.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            entry8.destroy()
            entry9.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()

        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="ADE")
        label2=Label(root,text="DS")
        label3=Label(root,text="COSM")
        label4=Label(root,text="COA")
        label5=Label(root,text="OOP using C++")
        label6=Label(root,text="ADE Lab")
        label7=Label(root,text="DS Lab")
        label8=Label(root,text="IT workshop Lab")
        label9=Label(root,text="C++ Programming Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entry8=Entry(root,width=10,borderwidth=5)
        entry9=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        label8.grid(row=15,column=0)
        label9.grid(row=16,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        entry8.grid(row=15,column=1)
        entry9.grid(row=16,column=1)
        button1.grid(row=17,column=2)
        button2.grid(row=17,column=1)
    elif groups=="CSE" and years==2 and sems==2:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(8):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[3,3,3,4,4,1.5,1.5,1]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/21
            result1=str(result)
            names=entrys.get()
            label9=Label(root,text=names+" your CGPA is "+result1)
            label9.grid(row=17)
            label9.after(5000,label9.destroy)
        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            entry8.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="Discrete Mathematics")
        label2=Label(root,text="BEFA")
        label3=Label(root,text="OS")
        label4=Label(root,text="DBMS")
        label5=Label(root,text="Java Programming")
        label6=Label(root,text="OS Lab")
        label7=Label(root,text="DBMS Lab")
        label8=Label(root,text="Java Programming Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entry8=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        label8.grid(row=15,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        entry8.grid(row=15,column=1)
        button1.grid(row=16,column=2)
        button2.grid(row=16,column=1)
    elif groups=="CSE" and years==3 and sems==1:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get(),entry9.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(9):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[3,3,3,3,3,3,1.5,1.5,1]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/22
            result1=str(result)
            names=entrys.get()
            label10=Label(root,text=names+" your CGPA is "+result1)
            label10.grid(row=18)
            label10.after(5000,label10.destroy)
        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            label9.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            entry8.destroy()
            entry9.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="FLAT")
        label2=Label(root,text="Software Engineering")
        label3=Label(root,text="Computer Networks")
        label4=Label(root,text="Web Technologies")
        label5=Label(root,text="PE - 1")
        label6=Label(root,text="PE - 2")
        label7=Label(root,text="Software Engineering Lab")
        label8=Label(root,text="CNWT Lab")
        label9=Label(root,text="ACS Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entry8=Entry(root,width=10,borderwidth=5)
        entry9=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        label8.grid(row=15,column=0)
        label9.grid(row=16,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        entry8.grid(row=15,column=1)
        entry9.grid(row=16,column=1)
        button1.grid(row=17,column=2)
        button2.grid(row=17,column=1)
    elif groups=="CSE" and years==3 and sems==2:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(8):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[4,4,4,3,3,1.5,1.5,1]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/22
            result1=str(result)
            names=entrys.get()
            label9=Label(root,text=names+" your CGPA is "+result1)
            label9.grid(row=17)
            label9.after(5000,label9.destroy)
        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            entry8.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="ML")
        label2=Label(root,text="Compiler Design")
        label3=Label(root,text="DAA")
        label4=Label(root,text="PE - 3")
        label5=Label(root,text="OE - 1")
        label6=Label(root,text="ML Lab")
        label7=Label(root,text="Compiler Design Lab")
        label8=Label(root,text="PE - 3 Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entry8=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        label8.grid(row=15,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        entry8.grid(row=15,column=1)
        button1.grid(row=16,column=2)
        button2.grid(row=16,column=1)
    elif groups=="CSE" and years==4 and sems==1:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get(),entry9.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(9):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[3,2,3,3,3,1,2,1,3]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/21
            result1=str(result)
            names=entrys.get()
            label10=Label(root,text=names+" your CGPA is "+result1)
            label10.grid(row=18)
            label10.after(5000,label10.destroy)
        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            label9.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            entry8.destroy()
            entry9.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="CNS")
        label2=Label(root,text="Data Mining")
        label3=Label(root,text="PE - 4")
        label4=Label(root,text="PE - 5")
        label5=Label(root,text="OE - 2")
        label6=Label(root,text="CNS Lab")
        label7=Label(root,text="Mini Project/Summer Internship")
        label8=Label(root,text="Seminar")
        label9=Label(root,text="Project Stage - 1")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entry8=Entry(root,width=10,borderwidth=5)
        entry9=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        label8.grid(row=15,column=0)
        label9.grid(row=16,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        entry8.grid(row=15,column=1)
        entry9.grid(row=16,column=1)
        button1.grid(row=17,column=2)
        button2.grid(row=17,column=1)
    elif groups=="CSE" and years==4 and sems==2:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(4):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[3,3,3,7]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/16
            result1=str(result)
            names=entrys.get()
            label5=Label(root,text=names+" your CGPA is "+result1)
            label5.grid(row=13)
            label5.after(5000,label5.destroy)

        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            name.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="Organizational Behaviour")
        label2=Label(root,text="PE - 6")
        label3=Label(root,text="OE - 3")
        label4=Label(root,text="Project Stage - 2")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        button1.grid(row=12,column=2)
        button2.grid(row=12,column=1)
    elif groups=="IT" and years==1 and sems==1:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(8):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[4,4,3,2,2.5,1,1,1.5]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/19
            result1=str(result)
            names=entrys.get()
            label9=Label(root,text=names+" your CGPA is "+result1)
            label9.grid(row=17)
            label9.after(5000,label9.destroy)
        
        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            entry8.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()
        
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="Mathematics 1")
        label2=Label(root,text="Chemistry")
        label3=Label(root,text="BEE")
        label4=Label(root,text="English")
        label5=Label(root,text="Engineering Workshop")
        label6=Label(root,text="ELCS Lab")
        label7=Label(root,text="BEE Lab")
        label8=Label(root,text="Chemistry Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entry8=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        label8.grid(row=15,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        entry8.grid(row=15,column=1)
        button1.grid(row=16,column=2)
        button2.grid(row=16,column=1)
    elif groups=="IT" and years==1 and sems==2:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(6):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[4,4,4,3,1.5,1.5]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/18
            result1=str(result)
            names=entrys.get()
            label7=Label(root,text=names+" your CGPA is "+result1)
            label7.grid(row=15)
            label7.after(5000,label7.destroy)
            
        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            name.destroy()
            label6.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()
            
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="Mathematics 2")
        label2=Label(root,text="Applied Physics")
        label3=Label(root,text="PPS")
        label4=Label(root,text="EG")
        label5=Label(root,text="Applied Physics Lab")
        label6=Label(root,text="PPS Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        button1.grid(row=14,column=2)
        button2.grid(row=14,column=1)
    elif groups=="IT" and years==2 and sems==1:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get(),entry9.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(9):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[3,4,4,3,2,1,1.5,1.5,1]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/21
            result1=str(result)
            names=entrys.get()
            label10=Label(root,text=names+" your CGPA is "+result1)
            label10.grid(row=18)
            label10.after(5000,label10.destroy)
        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            label9.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            entry8.destroy()
            entry9.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()

        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="ADE")
        label2=Label(root,text="DS")
        label3=Label(root,text="COSM")
        label4=Label(root,text="COMP")
        label5=Label(root,text="OOP using C++")
        label6=Label(root,text="ADE Lab")
        label7=Label(root,text="DS Lab")
        label8=Label(root,text="IT workshop and MP Lab")
        label9=Label(root,text="C++ Programming Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entry8=Entry(root,width=10,borderwidth=5)
        entry9=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        label8.grid(row=15,column=0)
        label9.grid(row=16,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        entry8.grid(row=15,column=1)
        entry9.grid(row=16,column=1)
        button1.grid(row=17,column=2)
        button2.grid(row=17,column=1)
    elif groups=="IT" and years==2 and sems==2:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(8):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[3,3,3,4,4,1.5,1.5,1]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/21
            result1=str(result)
            names=entrys.get()
            label9=Label(root,text=names+" your CGPA is "+result1)
            label9.grid(row=17)
            label9.after(5000,label9.destroy)
        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            entry8.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="Discrete Mathematics")
        label2=Label(root,text="BEFA")
        label3=Label(root,text="OS")
        label4=Label(root,text="DBMS")
        label5=Label(root,text="Java Programming")
        label6=Label(root,text="OS Lab")
        label7=Label(root,text="DBMS Lab")
        label8=Label(root,text="Java Programming Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entry8=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        label8.grid(row=15,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        entry8.grid(row=15,column=1)
        button1.grid(row=16,column=2)
        button2.grid(row=16,column=1)
    elif groups=="IT" and years==3 and sems==1:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get(),entry9.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(9):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[3,3,4,2,3,3,1.5,1.5,1]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/22
            result1=str(result)
            names=entrys.get()
            label10=Label(root,text=names+" your CGPA is "+result1)
            label10.grid(row=18)
            label10.after(5000,label10.destroy)
        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            label9.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            entry8.destroy()
            entry9.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="FLAT")
        label2=Label(root,text="Software Engineering")
        label3=Label(root,text="DC and Computer Networks")
        label4=Label(root,text="Web Programming")
        label5=Label(root,text="PE - 1")
        label6=Label(root,text="PE - 2")
        label7=Label(root,text="Software Engineering Lab")
        label8=Label(root,text="CN and WP Lab")
        label9=Label(root,text="ACS Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entry8=Entry(root,width=10,borderwidth=5)
        entry9=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        label8.grid(row=15,column=0)
        label9.grid(row=16,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        entry8.grid(row=15,column=1)
        entry9.grid(row=16,column=1)
        button1.grid(row=17,column=2)
        button2.grid(row=17,column=1)
    elif groups=="IT" and years==3 and sems==2:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get(),entry9.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(9):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[3,3,3,3,3,3,1.5,1.5,1]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/22
            result1=str(result)
            names=entrys.get()
            label10=Label(root,text=names+" your CGPA is "+result1)
            label10.grid(row=18)
            label10.after(5000,label10.destroy)
        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            label9.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            entry8.destroy()
            entry9.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="Intro to ES")
        label2=Label(root,text="Principles of CC")
        label3=Label(root,text="ADM")
        label4=Label(root,text="IOT")
        label5=Label(root,text="PE - 3")
        label6=Label(root,text="OE - 1")
        label7=Label(root,text="Embedded Systems and IOT Lab")
        label8=Label(root,text="CC Lab")
        label9=Label(root,text="PE - 3 Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entry8=Entry(root,width=10,borderwidth=5)
        entry9=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        label8.grid(row=15,column=0)
        label9.grid(row=16,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        entry8.grid(row=15,column=1)
        entry9.grid(row=16,column=1)
        button1.grid(row=17,column=2)
        button2.grid(row=17,column=1)
    elif groups=="IT" and years==4 and sems==1:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get(),entry9.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(9):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[3,2,3,3,3,1,2,1,3]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/21
            result1=str(result)
            names=entrys.get()
            label10=Label(root,text=names+" your CGPA is "+result1)
            label10.grid(row=18)
            label10.after(5000,label10.destroy)
        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            label9.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            entry8.destroy()
            entry9.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="Information Security")
        label2=Label(root,text="Data Mining")
        label3=Label(root,text="PE - 4")
        label4=Label(root,text="PE - 5")
        label5=Label(root,text="OE - 2")
        label6=Label(root,text="IS Lab")
        label7=Label(root,text="Mini Project/Summer Internship")
        label8=Label(root,text="Seminar")
        label9=Label(root,text="Project Stage - 1")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entry8=Entry(root,width=10,borderwidth=5)
        entry9=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        label8.grid(row=15,column=0)
        label9.grid(row=16,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        entry8.grid(row=15,column=1)
        entry9.grid(row=16,column=1)
        button1.grid(row=17,column=2)
        button2.grid(row=17,column=1)
    elif groups=="IT" and years==4 and sems==2:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(4):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[3,3,3,7]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/16
            result1=str(result)
            names=entrys.get()
            label5=Label(root,text=names+" your CGPA is "+result1)
            label5.grid(row=13)
            label5.after(5000,label5.destroy)

        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            name.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="Organizational Behaviour")
        label2=Label(root,text="PE - 6")
        label3=Label(root,text="OE - 3")
        label4=Label(root,text="Project Stage - 2")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        button1.grid(row=12,column=2)
        button2.grid(row=12,column=1)
    elif groups=="EEE" and years==1 and sems==1:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(8):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[4,4,3,2,2.5,1,1,1.5]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/19
            result1=str(result)
            names=entrys.get()
            label9=Label(root,text=names+" your CGPA is "+result1)
            label9.grid(row=17)
            label9.after(5000,label9.destroy)
        
        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            entry8.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()
        
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="Mathematics 1")
        label2=Label(root,text="Chemistry")
        label3=Label(root,text="BEE")
        label4=Label(root,text="English")
        label5=Label(root,text="Engineering Workshop")
        label6=Label(root,text="ELCS Lab")
        label7=Label(root,text="BEE Lab")
        label8=Label(root,text="Chemistry Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entry8=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        label8.grid(row=15,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        entry8.grid(row=15,column=1)
        button1.grid(row=16,column=2)
        button2.grid(row=16,column=1)
    elif groups=="EEE" and years==1 and sems==2:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(6):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[4,4,4,3,1.5,1.5]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/18
            result1=str(result)
            names=entrys.get()
            label7=Label(root,text=names+" your CGPA is "+result1)
            label7.grid(row=15)
            label7.after(5000,label7.destroy)
            
        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            name.destroy()
            label6.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()
            
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="Mathematics 2")
        label2=Label(root,text="Applied Physics")
        label3=Label(root,text="PPS")
        label4=Label(root,text="EG")
        label5=Label(root,text="Applied Physics Lab")
        label6=Label(root,text="PPS Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        button1.grid(row=14,column=2)
        button2.grid(row=14,column=1)
    elif groups=="EEE" and years==2 and sems==1:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(8):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[4,4,3,4,3,1,1,1]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/21
            result1=str(result)
            names=entrys.get()
            label9=Label(root,text=names+" your CGPA is "+result1)
            label9.grid(row=17)
            label9.after(5000,label9.destroy)
        
        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            entry8.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()
        
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="EM")
        label2=Label(root,text="ECA")
        label3=Label(root,text="AE")
        label4=Label(root,text="EM - 1")
        label5=Label(root,text="EMF")
        label6=Label(root,text="EM Lab - 1")
        label7=Label(root,text="AE Lab")
        label8=Label(root,text="EC Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entry8=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        label8.grid(row=15,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        entry8.grid(row=15,column=1)
        button1.grid(row=16,column=2)
        button2.grid(row=16,column=1)
    elif groups=="EEE" and years==2 and sems==2:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(8):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[4,4,3,4,3,1,1,1]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/21
            result1=str(result)
            names=entrys.get()
            label9=Label(root,text=names+" your CGPA is "+result1)
            label9.grid(row=17)
            label9.after(5000,label9.destroy)
        
        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            entry8.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()
        
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="LTNMCV")
        label2=Label(root,text="EM - 2")
        label3=Label(root,text="DE")
        label4=Label(root,text="CS")
        label5=Label(root,text="PS - 1")
        label6=Label(root,text="DE Lab")
        label7=Label(root,text="EM Lab - 2")
        label8=Label(root,text="CS Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entry8=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        label8.grid(row=15,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        entry8.grid(row=15,column=1)
        button1.grid(row=16,column=2)
        button2.grid(row=16,column=1)
    elif groups=="EEE" and years==3 and sems==1:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get(),entry9.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(9):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[4,4,4,3,3,1,1,1,1]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/22
            result1=str(result)
            names=entrys.get()
            label10=Label(root,text=names+" your CGPA is "+result1)
            label10.grid(row=18)
            label10.after(5000,label10.destroy)
        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            label9.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            entry8.destroy()
            entry9.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="PE")
        label2=Label(root,text="PS - 2")
        label3=Label(root,text="MI")
        label4=Label(root,text="PE - 1")
        label5=Label(root,text="BEFA")
        label6=Label(root,text="PSS Lab")
        label7=Label(root,text="PE Lab")
        label8=Label(root,text="MI Lab")
        label9=Label(root,text="ACS Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entry8=Entry(root,width=10,borderwidth=5)
        entry9=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        label8.grid(row=15,column=0)
        label9.grid(row=16,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        entry8.grid(row=15,column=1)
        entry9.grid(row=16,column=1)
        button1.grid(row=17,column=2)
        button2.grid(row=17,column=1)
    elif groups=="EEE" and years==3 and sems==2:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get(),entry9.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(9):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[3,3,3,3,4,3,1,1,1]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/22
            result1=str(result)
            names=entrys.get()
            label10=Label(root,text=names+" your CGPA is "+result1)
            label10.grid(row=18)
            label10.after(5000,label10.destroy)
        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            label9.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            entry8.destroy()
            entry9.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="OE - 1")
        label2=Label(root,text="PE - 2")
        label3=Label(root,text="SS")
        label4=Label(root,text="MP & MC")
        label5=Label(root,text="PSP")
        label6=Label(root,text="PSOC")
        label7=Label(root,text="PS Lab")
        label8=Label(root,text="MP & MC Lab")
        label9=Label(root,text="SS Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entry8=Entry(root,width=10,borderwidth=5)
        entry9=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        label8.grid(row=15,column=0)
        label9.grid(row=16,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        entry8.grid(row=15,column=1)
        entry9.grid(row=16,column=1)
        button1.grid(row=17,column=2)
        button2.grid(row=17,column=1)
    elif groups=="EEE" and years==4 and sems==1:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(8):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[3,3,3,3,3,2,1,3]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/21
            result1=str(result)
            names=entrys.get()
            label9=Label(root,text=names+" your CGPA is "+result1)
            label9.grid(row=17)
            label9.after(5000,label9.destroy)
        
        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            entry8.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()
        
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="OE - 2")
        label2=Label(root,text="PE - 3")
        label3=Label(root,text="PE - 4")
        label4=Label(root,text="FME")
        label5=Label(root,text="EED Lab")
        label6=Label(root,text="Mini Project / Summer Internship")
        label7=Label(root,text="Seminar")
        label8=Label(root,text="Project Stage - 1")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entry8=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        label8.grid(row=15,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        entry8.grid(row=15,column=1)
        button1.grid(row=16,column=2)
        button2.grid(row=16,column=1)
    elif groups=="EEE" and years==4 and sems==2:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(4):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[3,3,3,7]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/16
            result1=str(result)
            names=entrys.get()
            label5=Label(root,text=names+" your CGPA is "+result1)
            label5.grid(row=13)
            label5.after(5000,label5.destroy)

        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            name.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="OE - 3")
        label2=Label(root,text="PE - 5")
        label3=Label(root,text="PE - 6")
        label4=Label(root,text="Project Stage - 2")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        button1.grid(row=12,column=2)
        button2.grid(row=12,column=1)
    elif groups=="EIE" and years==1 and sems==1:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(6):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[4,4,4,3,1.5,1.5]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/18
            result1=str(result)
            names=entrys.get()
            label7=Label(root,text=names+" your CGPA is "+result1)
            label7.grid(row=15)
            label7.after(5000,label7.destroy)
            
        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            name.destroy()
            label6.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()
                    
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="Mathematics 1")
        label2=Label(root,text="Applied Physics")
        label3=Label(root,text="PPS")
        label4=Label(root,text="EG")
        label5=Label(root,text="Applied Physics Lab")
        label6=Label(root,text="PPS Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        button1.grid(row=14,column=2)
        button2.grid(row=14,column=1)
    elif groups=="EIE" and years==1 and sems==2:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(8):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[4,4,3,2,2.5,1,1,1.5]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/19
            result1=str(result)
            names=entrys.get()
            label9=Label(root,text=names+" your CGPA is "+result1)
            label9.grid(row=17)
            label9.after(5000,label9.destroy)

        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            entry8.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()

        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="Mathematics 2")
        label2=Label(root,text="Chemistry")
        label3=Label(root,text="BEE")
        label4=Label(root,text="English")
        label5=Label(root,text="Engineering Workshop")
        label6=Label(root,text="ELCS Lab")
        label7=Label(root,text="BEE Lab")
        label8=Label(root,text="Chemistry Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entry8=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        label8.grid(row=15,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        entry8.grid(row=15,column=1)
        button1.grid(row=16,column=2)
        button2.grid(row=16,column=1)
    elif groups=="EIE" and years==2 and sems==1:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(8):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[4,3,4,3,4,1,1,1]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/21
            result1=str(result)
            names=entrys.get()
            label9=Label(root,text=names+" your CGPA is "+result1)
            label9.grid(row=17)
            label9.after(5000,label9.destroy)

        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            entry8.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()   
            
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="EDC")
        label2=Label(root,text="Network Theory")
        label3=Label(root,text="TE")
        label4=Label(root,text="EM")
        label5=Label(root,text="SS")
        label6=Label(root,text="EDC Lab")
        label7=Label(root,text="BS Lab")
        label8=Label(root,text="TM Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entry8=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        label8.grid(row=15,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        entry8.grid(row=15,column=1)
        button1.grid(row=16,column=2)
        button2.grid(row=16,column=1)
    elif groups=="EIE" and years==2 and sems==2:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(8):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[4,3,3,3,4,1.5,1.5,1]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/21
            result1=str(result)
            names=entrys.get()
            label9=Label(root,text=names+" your CGPA is "+result1)
            label9.grid(row=17)
            label9.after(5000,label9.destroy)

        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            entry8.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()    
            
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="LTNMCV")
        label2=Label(root,text="II")
        label3=Label(root,text="LICA")
        label4=Label(root,text="ECA")
        label5=Label(root,text="DSD")
        label6=Label(root,text="IC Lab")
        label7=Label(root,text="II Lab")
        label8=Label(root,text="ECA Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entry8=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        label8.grid(row=15,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        entry8.grid(row=15,column=1)
        button1.grid(row=16,column=2)
        button2.grid(row=16,column=1)
    elif groups=="EIE" and years==3 and sems==1:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(8):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[4,4,4,3,3,1.5,1.5,1]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/22
            result1=str(result)
            names=entrys.get()
            label9=Label(root,text=names+" your CGPA is "+result1)
            label9.grid(row=17)
            label9.after(5000,label9.destroy)

        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            entry8.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()    
            
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="MP & MC")
        label2=Label(root,text="PDC")
        label3=Label(root,text="CS")
        label4=Label(root,text="BEFA")
        label5=Label(root,text="PE - 1")
        label6=Label(root,text="MP & MC Lab")
        label7=Label(root,text="PC Lab")
        label8=Label(root,text="ACS Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entry8=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        label8.grid(row=15,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        entry8.grid(row=15,column=1)
        button1.grid(row=16,column=2)
        button2.grid(row=16,column=1)
    elif groups=="EIE" and years==3 and sems==2:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(8):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[4,4,4,3,3,1.5,1.5,1]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/22
            result1=str(result)
            names=entrys.get()
            label9=Label(root,text=names+" your CGPA is "+result1)
            label9.grid(row=17)
            label9.after(5000,label9.destroy)

        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            entry8.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()       
            
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="IA")
        label2=Label(root,text="DSP")
        label3=Label(root,text="OOP through Java")
        label4=Label(root,text="PE - 2")
        label5=Label(root,text="OE - 1")
        label6=Label(root,text="DSP Lab")
        label7=Label(root,text="IA Lab")
        label8=Label(root,text="OOP through Java Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entry8=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        label8.grid(row=15,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        entry8.grid(row=15,column=1)
        button1.grid(row=16,column=2)
        button2.grid(row=16,column=1)
    elif groups=="EIE" and years==4 and sems==1:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get(),entry9.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(9):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[3,3,3,3,2,1,2,1,3]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/21
            result1=str(result)
            names=entrys.get()
            label10=Label(root,text=names+" your CGPA is "+result1)
            label10.grid(row=18)
            label10.after(5000,label10.destroy)

        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            label9.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            entry8.destroy()
            entry9.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()    
            
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="AI")
        label2=Label(root,text="PE - 3")
        label3=Label(root,text="PE - 4")
        label4=Label(root,text="OE - 2")
        label5=Label(root,text="PPLE")
        label6=Label(root,text="AI Lab")
        label7=Label(root,text="Mini Project / Summer Internship")
        label8=Label(root,text="Seminar")
        label9=Label(root,text="Project Stage-1")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entry8=Entry(root,width=10,borderwidth=5)
        entry9=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        label8.grid(row=15,column=0)
        label9.grid(row=16,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        entry8.grid(row=15,column=1)
        entry9.grid(row=16,column=1)
        button1.grid(row=17,column=2)
        button2.grid(row=17,column=1)
    elif groups=="EIE" and years==4 and sems==2:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(4):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[3,3,3,7]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/16
            result1=str(result)
            names=entrys.get()
            label5=Label(root,text=names+" your CGPA is "+result1)
            label5.grid(row=13)
            label5.after(5000,label5.destroy)

        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            name.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()    
            
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="PE - 5")
        label2=Label(root,text="PE - 6")
        label3=Label(root,text="OE - 3")
        label4=Label(root,text="Project Stage - 2")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        button1.grid(row=12,column=2)
        button2.grid(row=12,column=1)
    elif groups=="MECH" and years==1 and sems==1:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(6):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[4,4,4,3,1.5,1.5]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/18
            result1=str(result)
            names=entrys.get()
            label7=Label(root,text=names+" your CGPA is "+result1)
            label7.grid(row=15)
            label7.after(5000,label7.destroy)
            
        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            name.destroy()
            label6.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()
                    
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="Mathematics 1")
        label2=Label(root,text="Engineering Physics")
        label3=Label(root,text="PPS")
        label4=Label(root,text="EG")
        label5=Label(root,text="Engineering Physics Lab")
        label6=Label(root,text="PPS Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        button1.grid(row=14,column=2)
        button2.grid(row=14,column=1)
    elif groups=="MECH" and years==1 and sems==2:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(7):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[4,4,4,2.5,2,1.5,1]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/19
            result1=str(result)
            names=entrys.get()
            label8=Label(root,text=names+" your CGPA is "+result1)
            label8.grid(row=16)
            label8.after(5000,label8.destroy)

        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()

        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="Mathematics 2")
        label2=Label(root,text="Chemistry")
        label3=Label(root,text="EM")
        label4=Label(root,text="Engineering Workshop")
        label5=Label(root,text="English")
        label6=Label(root,text="Chemistry Lab")
        label7=Label(root,text="ELCS Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        button1.grid(row=15,column=2)
        button2.grid(row=15,column=1)
    elif groups=="MECH" and years==2 and sems==1:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(8):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[4,4,3,3,4,1,1,1]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/21
            result1=str(result)
            names=entrys.get()
            label9=Label(root,text=names+" your CGPA is "+result1)
            label9.grid(row=17)
            label9.after(5000,label9.destroy)

        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            entry8.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()       
            
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="PSCV")
        label2=Label(root,text="MS")
        label3=Label(root,text="MSM")
        label4=Label(root,text="PT")
        label5=Label(root,text="Thermodynamics")
        label6=Label(root,text="PT Lab")
        label7=Label(root,text="Machine Drawing Practice")
        label8=Label(root,text="MSMS Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entry8=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        label8.grid(row=15,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        entry8.grid(row=15,column=1)
        button1.grid(row=16,column=2)
        button2.grid(row=16,column=1)
    elif groups=="MECH" and years==2 and sems==2:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(8):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[3,4,4,4,3,1,1,1]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/21
            result1=str(result)
            names=entrys.get()
            label9=Label(root,text=names+" your CGPA is "+result1)
            label9.grid(row=17)
            label9.after(5000,label9.destroy)

        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            entry8.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()       
            
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="BEEE")
        label2=Label(root,text="KM")
        label3=Label(root,text="TE - 1")
        label4=Label(root,text="FMHM")
        label5=Label(root,text="ICS")
        label6=Label(root,text="BEEE Lab")
        label7=Label(root,text="FMHM Lab")
        label8=Label(root,text="ICS Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entry8=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        label8.grid(row=15,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        entry8.grid(row=15,column=1)
        button1.grid(row=16,column=2)
        button2.grid(row=16,column=1)
    elif groups=="MECH" and years==3 and sems==1:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get(),entry9.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(9):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[4,3,3,3,3,3,1,1,1]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/22
            result1=str(result)
            names=entrys.get()
            label10=Label(root,text=names+" your CGPA is "+result1)
            label10.grid(row=18)
            label10.after(5000,label10.destroy)

        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            label9.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            entry8.destroy()
            entry9.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()    
            
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="DM")
        label2=Label(root,text="DMM - 1")
        label3=Label(root,text="MM Tools")
        label4=Label(root,text="BEFA")
        label5=Label(root,text="TE - 2")
        label6=Label(root,text="OR")
        label7=Label(root,text="TE Lab")
        label8=Label(root,text="MM Tools Lab")
        label9=Label(root,text="KD Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entry8=Entry(root,width=10,borderwidth=5)
        entry9=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        label8.grid(row=15,column=0)
        label9.grid(row=16,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        entry8.grid(row=15,column=1)
        entry9.grid(row=16,column=1)
        button1.grid(row=17,column=2)
        button2.grid(row=17,column=1)
    elif groups=="MECH" and years==3 and sems==2:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get(),entry9.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(9):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[3,4,3,3,3,3,1,1,1]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/22
            result1=str(result)
            names=entrys.get()
            label10=Label(root,text=names+" your CGPA is "+result1)
            label10.grid(row=18)
            label10.after(5000,label10.destroy)

        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            label9.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            entry8.destroy()
            entry9.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()    
            
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="DMM - 2")
        label2=Label(root,text="HT")
        label3=Label(root,text="CAD & CAM")
        label4=Label(root,text="PE - 1")
        label5=Label(root,text="OE - 1")
        label6=Label(root,text="FEM")
        label7=Label(root,text="HT Lab")
        label8=Label(root,text="CAD & CAM Lab")
        label9=Label(root,text="ACS Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entry8=Entry(root,width=10,borderwidth=5)
        entry9=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        label8.grid(row=15,column=0)
        label9.grid(row=16,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        entry8.grid(row=15,column=1)
        entry9.grid(row=16,column=1)
        button1.grid(row=17,column=2)
        button2.grid(row=17,column=1)
    elif groups=="MECH" and years==4 and sems==1:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(8):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[3,3,3,3,3,2,1,3]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/21
            result1=str(result)
            names=entrys.get()
            label9=Label(root,text=names+" your CGPA is "+result1)
            label9.grid(row=17)
            label9.after(5000,label9.destroy)

        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            entry8.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()       
            
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="RAC")
        label2=Label(root,text="PE - 2")
        label3=Label(root,text="PE - 3")
        label4=Label(root,text="PE - 4")
        label5=Label(root,text="OE - 2")
        label6=Label(root,text="Mini Project/Summer Internship")
        label7=Label(root,text="Seminar")
        label8=Label(root,text="Project Stage-1")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entry8=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        label8.grid(row=15,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        entry8.grid(row=15,column=1)
        button1.grid(row=16,column=2)
        button2.grid(row=16,column=1)
    elif groups=="MECH" and years==4 and sems==2:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(4):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[3,3,3,7]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/16
            result1=str(result)
            names=entrys.get()
            label5=Label(root,text=names+" your CGPA is "+result1)
            label5.grid(row=13)
            label5.after(5000,label5.destroy)

        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            name.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()    
            
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="PE - 5")
        label2=Label(root,text="PE - 6")
        label3=Label(root,text="OE - 3")
        label4=Label(root,text="Project Stage - 2")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        button1.grid(row=12,column=2)
        button2.grid(row=12,column=1)
    elif groups=="CIVIL" and years==1 and sems==1:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(6):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[4,4,4,3,1.5,1.5]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/18
            result1=str(result)
            names=entrys.get()
            label7=Label(root,text=names+" your CGPA is "+result1)
            label7.grid(row=15)
            label7.after(5000,label7.destroy)
            
        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            name.destroy()
            label6.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()
                    
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="Mathematics 1")
        label2=Label(root,text="Engineering Physics")
        label3=Label(root,text="PPS")
        label4=Label(root,text="EG")
        label5=Label(root,text="Engineering Physics Lab")
        label6=Label(root,text="PPS Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        button1.grid(row=14,column=2)
        button2.grid(row=14,column=1)
    elif groups=="CIVIL" and years==1 and sems==2:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(7):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[4,4,4,2.5,2,1.5,1]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/19
            result1=str(result)
            names=entrys.get()
            label8=Label(root,text=names+" your CGPA is "+result1)
            label8.grid(row=16)
            label8.after(5000,label8.destroy)

        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()

        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="Mathematics 2")
        label2=Label(root,text="Chemistry")
        label3=Label(root,text="EM")
        label4=Label(root,text="Engineering Workshop")
        label5=Label(root,text="English")
        label6=Label(root,text="Chemistry Lab")
        label7=Label(root,text="ELCS Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        button1.grid(row=15,column=2)
        button2.grid(row=15,column=1)
    elif groups=="CIVIL" and years==2 and sems==1:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(8):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[3,2,4,4,4,1.5,1.5,1]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/21
            result1=str(result)
            names=entrys.get()
            label9=Label(root,text=names+" your CGPA is "+result1)
            label9.grid(row=17)
            label9.after(5000,label9.destroy)

        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            entry8.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()       
            
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="SG")
        label2=Label(root,text="EG")
        label3=Label(root,text="SM - 1")
        label4=Label(root,text="PS")
        label5=Label(root,text="FM")
        label6=Label(root,text="Surveying Lab")
        label7=Label(root,text="SM Lab")
        label8=Label(root,text="EG Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entry8=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        label8.grid(row=15,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        entry8.grid(row=15,column=1)
        button1.grid(row=16,column=2)
        button2.grid(row=16,column=1)
    elif groups=="CIVIL" and years==2 and sems==2:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get(),entry9.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(9):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[3,2,3,3,3,3,1.5,1.5,1]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/21
            result1=str(result)
            names=entrys.get()
            label10=Label(root,text=names+" your CGPA is "+result1)
            label10.grid(row=18)
            label10.after(5000,label10.destroy)

        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            label9.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            entry8.destroy()
            entry9.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()    
            
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="BEEE")
        label2=Label(root,text="BME for CE")
        label3=Label(root,text="BMCP")
        label4=Label(root,text="SM - 2")
        label5=Label(root,text="HHM")
        label6=Label(root,text="SA - 1")
        label7=Label(root,text="Computer Aided CE Drawing")
        label8=Label(root,text="HHM Lab")
        label9=Label(root,text="BEEE Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entry8=Entry(root,width=10,borderwidth=5)
        entry9=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        label8.grid(row=15,column=0)
        label9.grid(row=16,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        entry8.grid(row=15,column=1)
        entry9.grid(row=16,column=1)
        button1.grid(row=17,column=2)
        button2.grid(row=17,column=1)
    elif groups=="CIVIL" and years==3 and sems==1:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get(),entry9.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(9):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[3,3,4,3,3,2,1.5,1.5,1]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/22
            result1=str(result)
            names=entrys.get()
            label10=Label(root,text=names+" your CGPA is "+result1)
            label10.grid(row=18)
            label10.after(5000,label10.destroy)

        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            label9.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            entry8.destroy()
            entry9.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()    
            
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="SA - 2")
        label2=Label(root,text="GE")
        label3=Label(root,text="SE - 1")
        label4=Label(root,text="TE")
        label5=Label(root,text="PE - 1")
        label6=Label(root,text="EEA")
        label7=Label(root,text="HECT Lab")
        label8=Label(root,text="GE Lab")
        label9=Label(root,text="ACS Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entry8=Entry(root,width=10,borderwidth=5)
        entry9=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        label8.grid(row=15,column=0)
        label9.grid(row=16,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        entry8.grid(row=15,column=1)
        entry9.grid(row=16,column=1)
        button1.grid(row=17,column=2)
        button2.grid(row=17,column=1)
    elif groups=="CIVIL" and years==3 and sems==2:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(8):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[4,3,3,4,3,3,1,1]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/22
            result1=str(result)
            names=entrys.get()
            label9=Label(root,text=names+" your CGPA is "+result1)
            label9.grid(row=17)
            label9.after(5000,label9.destroy)

        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            entry8.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()       
            
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="HWRE")
        label2=Label(root,text="EE")
        label3=Label(root,text="FE")
        label4=Label(root,text="SE - 2")
        label5=Label(root,text="PE - 2")
        label6=Label(root,text="OE - 1")
        label7=Label(root,text="EE Lab")
        label8=Label(root,text="CAD Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entry8=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        label8.grid(row=15,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        entry8.grid(row=15,column=1)
        button1.grid(row=16,column=2)
        button2.grid(row=16,column=1)
    elif groups=="CIVIL" and years==4 and sems==1:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(8):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[4,3,3,3,2,2,1,3]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/21
            result1=str(result)
            names=entrys.get()
            label9=Label(root,text=names+" your CGPA is "+result1)
            label9.grid(row=17)
            label9.after(5000,label9.destroy)

        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            entry8.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()       
            
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="ECPM")
        label2=Label(root,text="PE - 3")
        label3=Label(root,text="PE - 4")
        label4=Label(root,text="OE - 2")
        label5=Label(root,text="PPLE")
        label6=Label(root,text="Mini Project/Summer Internship")
        label7=Label(root,text="Seminar")
        label8=Label(root,text="Project Stage - 1")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entry8=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        label8.grid(row=15,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        entry8.grid(row=15,column=1)
        button1.grid(row=16,column=2)
        button2.grid(row=16,column=1)
    elif groups=="CIVIL" and years==4 and sems==2:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(4):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[3,3,3,7]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/16
            result1=str(result)
            names=entrys.get()
            label5=Label(root,text=names+" your CGPA is "+result1)
            label5.grid(row=13)
            label5.after(5000,label5.destroy)

        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            name.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()    
            
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="PE - 5")
        label2=Label(root,text="PE - 6")
        label3=Label(root,text="OE - 3")
        label4=Label(root,text="Project Stage - 2")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        button1.grid(row=12,column=2)
        button2.grid(row=12,column=1)
    elif groups=="AERO" and years==1 and sems==1:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(6):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[4,4,4,3,1.5,1.5]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/18
            result1=str(result)
            names=entrys.get()
            label7=Label(root,text=names+" your CGPA is "+result1)
            label7.grid(row=15)
            label7.after(5000,label7.destroy)
            
        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            name.destroy()
            label6.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()
                    
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="Mathematics 1")
        label2=Label(root,text="Engineering Physics")
        label3=Label(root,text="PPS")
        label4=Label(root,text="EG")
        label5=Label(root,text="Engineering Physics Lab")
        label6=Label(root,text="PPS Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        button1.grid(row=14,column=2)
        button2.grid(row=14,column=1)
    elif groups=="AERO" and years==1 and sems==2:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(7):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[4,4,4,2.5,2,1.5,1]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/19
            result1=str(result)
            names=entrys.get()
            label8=Label(root,text=names+" your CGPA is "+result1)
            label8.grid(row=16)
            label8.after(5000,label8.destroy)

        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()

        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="Mathematics 2")
        label2=Label(root,text="Chemistry")
        label3=Label(root,text="EM")
        label4=Label(root,text="Engineering Workshop")
        label5=Label(root,text="English")
        label6=Label(root,text="Chemistry Lab")
        label7=Label(root,text="ELCS Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        button1.grid(row=15,column=2)
        button2.grid(row=15,column=1)
    elif groups=="AERO" and years==2 and sems==1:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(8):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[4,3,3,3,4,1,2,1]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/21
            result1=str(result)
            names=entrys.get()
            label9=Label(root,text=names+" your CGPA is "+result1)
            label9.grid(row=17)
            label9.after(5000,label9.destroy)

        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            entry8.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()       
            
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="PSCV")
        label2=Label(root,text="BEEE")
        label3=Label(root,text="TS")
        label4=Label(root,text="FMH")
        label5=Label(root,text="Aerodynamics-1")
        label6=Label(root,text="MS Lab")
        label7=Label(root,text="FMH Lab")
        label8=Label(root,text="BEEE Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entry8=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        label8.grid(row=15,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        entry8.grid(row=15,column=1)
        button1.grid(row=16,column=2)
        button2.grid(row=16,column=1)
    elif groups=="AERO" and years==2 and sems==2:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(8):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[4,3,4,4,3,1,1,1]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/21
            result1=str(result)
            names=entrys.get()
            label9=Label(root,text=names+" your CGPA is "+result1)
            label9.grid(row=17)
            label9.after(5000,label9.destroy)

        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            entry8.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()       
            
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="PDNM")
        label2=Label(root,text="LSA")
        label3=Label(root,text="AMP")
        label4=Label(root,text="AAS")
        label5=Label(root,text="Aero - Thermodynamics")
        label6=Label(root,text="Aerodynamics Lab")
        label7=Label(root,text="AS Lab")
        label8=Label(root,text="AMP Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entry8=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        label8.grid(row=15,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        entry8.grid(row=15,column=1)
        button1.grid(row=16,column=2)
        button2.grid(row=16,column=1)
    elif groups=="AERO" and years==3 and sems==1:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get(),entry9.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(9):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[4,3,3,3,3,3,1,1,1]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/22
            result1=str(result)
            names=entrys.get()
            label10=Label(root,text=names+" your CGPA is "+result1)
            label10.grid(row=18)
            label10.after(5000,label10.destroy)

        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            label9.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            entry8.destroy()
            entry9.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()    
            
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="AP")
        label2=Label(root,text="HSA")
        label3=Label(root,text="FEM")
        label4=Label(root,text="BEFA")
        label5=Label(root,text="ASC")
        label6=Label(root,text="APS")
        label7=Label(root,text="CAAED")
        label8=Label(root,text="FC Lab")
        label9=Label(root,text="AP Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entry8=Entry(root,width=10,borderwidth=5)
        entry9=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        label8.grid(row=15,column=0)
        label9.grid(row=16,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        entry8.grid(row=15,column=1)
        entry9.grid(row=16,column=1)
        button1.grid(row=17,column=2)
        button2.grid(row=17,column=1)
    elif groups=="AERO" and years==3 and sems==2:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get(),entry9.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(9):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[3,4,3,3,3,3,1,1,1]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/22
            result1=str(result)
            names=entrys.get()
            label10=Label(root,text=names+" your CGPA is "+result1)
            label10.grid(row=18)
            label10.after(5000,label10.destroy)

        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            label9.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            entry8.destroy()
            entry9.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()    
            
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="SP")
        label2=Label(root,text="CA")
        label3=Label(root,text="HA")
        label4=Label(root,text="PE - 1")
        label5=Label(root,text="OE - 1")
        label6=Label(root,text="AD")
        label7=Label(root,text="AP Lab")
        label8=Label(root,text="CFD Lab")
        label9=Label(root,text="ACS Lab")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entry8=Entry(root,width=10,borderwidth=5)
        entry9=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        label8.grid(row=15,column=0)
        label9.grid(row=16,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        entry8.grid(row=15,column=1)
        entry9.grid(row=16,column=1)
        button1.grid(row=17,column=2)
        button2.grid(row=17,column=1)
    elif groups=="AERO" and years==4 and sems==1:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(8):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[3,3,3,3,3,2,1,3]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/21
            result1=str(result)
            names=entrys.get()
            label9=Label(root,text=names+" your CGPA is "+result1)
            label9.grid(row=17)
            label9.after(5000,label9.destroy)

        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entry5.destroy()
            entry6.destroy()
            entry7.destroy()
            entry8.destroy()
            name.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()       
            
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="VAE")
        label2=Label(root,text="PE - 2")
        label3=Label(root,text="PE - 3")
        label4=Label(root,text="PE - 4")
        label5=Label(root,text="OE - 2")
        label6=Label(root,text="Mini Project/Summer Internship")
        label7=Label(root,text="Seminar")
        label8=Label(root,text="Project Stage - 1")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entry5=Entry(root,width=10,borderwidth=5)
        entry6=Entry(root,width=10,borderwidth=5)
        entry7=Entry(root,width=10,borderwidth=5)
        entry8=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        label5.grid(row=12,column=0)
        label6.grid(row=13,column=0)
        label7.grid(row=14,column=0)
        label8.grid(row=15,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        entry5.grid(row=12,column=1)
        entry6.grid(row=13,column=1)
        entry7.grid(row=14,column=1)
        entry8.grid(row=15,column=1)
        button1.grid(row=16,column=2)
        button2.grid(row=16,column=1)
    elif groups=="AERO" and years==4 and sems==2:
        def calculate_result():
            result_array=[entry1.get(),entry2.get(),entry3.get(),entry4.get()]
            grades_array=['O','A+','A','B+','B','C','F','Ab']
            numbers=[10,9,8,7,6,5,0,0]
            final_array=[]
            for i in range(4):
                for j in range(7):
                    if result_array[i]==grades_array[j]:
                        final_array.append(numbers[j])
            credits_array=[3,3,3,7]
            sums=0
            for i in range(len(final_array)):
                sums=sums+final_array[i]*credits_array[i]
            result=sums/16
            result1=str(result)
            names=entrys.get()
            label5=Label(root,text=names+" your CGPA is "+result1)
            label5.grid(row=13)
            label5.after(5000,label5.destroy)

        def clearing():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            name.destroy()
            entry1.destroy()
            entry2.destroy()
            entry3.destroy()
            entry4.destroy()
            entrys.destroy()
            button1.destroy()
            button2.destroy()    
            
        label0=Label(root,text="Note:-Please enter your grades to calculate the CGPA")
        label1=Label(root,text="PE - 5")
        label2=Label(root,text="PE - 6")
        label3=Label(root,text="OE - 3")
        label4=Label(root,text="Project Stage - 2")
        name=Label(root,text="Name")
        entry1=Entry(root,width=10,borderwidth=5)
        entry2=Entry(root,width=10,borderwidth=5)
        entry3=Entry(root,width=10,borderwidth=5)
        entry4=Entry(root,width=10,borderwidth=5)
        entrys=Entry(root,width=35,borderwidth=5)
        button1=Button(root,text="Submit",padx=10,pady=10,command=calculate_result)
        button2=Button(root,text="Clear",padx=10,pady=10,command=clearing)
        label0.grid(row=6)
        name.grid(row=7,column=0)
        label1.grid(row=8,column=0)
        label2.grid(row=9,column=0)
        label3.grid(row=10,column=0)
        label4.grid(row=11,column=0)
        entrys.grid(row=7,column=1)
        entry1.grid(row=8,column=1)
        entry2.grid(row=9,column=1)
        entry3.grid(row=10,column=1)
        entry4.grid(row=11,column=1)
        button1.grid(row=12,column=2)
        button2.grid(row=12,column=1)
    else:
        def clearings():
            labelss.destroy()
            buttonss.destroy()
        labelss=Label(root,text="Please enter valid details")
        buttonss=Button(root,text="Clear",padx=10,pady=10,command=clearings)
        labelss.grid(row=6,column=0)
        buttonss.grid(row=5,column=1)
group=Label(root,text="Group")
year=Label(root,text="Year")
sem=Label(root,text="Semester")

group_entry=Entry(root,width=35,borderwidth=5)
year_entry=Entry(root,width=35,borderwidth=5)
sem_entry=Entry(root,width=35,borderwidth=5)

group_button=Button(root,text="Submit",padx=0,pady=0,command=group_click)
year_button=Button(root,text="Submit",padx=0,pady=0,command=year_click)
sem_button=Button(root,text="Submit",padx=0,pady=0,command=sem_click)

group.grid(row=0,column=0)
year.grid(row=2,column=0)
sem.grid(row=4,column=0)

group_entry.grid(row=0,column=1)
year_entry.grid(row=2,column=1)
sem_entry.grid(row=4,column=1)

group_button.grid(row=0,column=2)
year_button.grid(row=2,column=2)
sem_button.grid(row=4,column=2)
root.mainloop()
