from customtkinter import *
from tkinter import messagebox  # For warning popup

#========================================initializing values============================================================
salutation = "MR"
after_id = None
global action
action = "withdraw"
reciept_text = ""
#=========================================class skeleton================================================================
class Account:
    def __init__(self,acc_name,acc_no,acc_type,balance):
        self.acc_name = acc_name
        self.acc_no = acc_no
        self.acc_type = acc_type
        self.balance = int(balance)
#=====================================User Defined Functions============================================================

#--------------------------Cancel info disappear schedule if another button pressed while timer active------------------
def cancel_after_timer():
    global after_id
    if after_id:
        label0.after_cancel(after_id)
        after_id = None  # Reset after_id
#--------------------------Salutation based on the gender selected------------------------------------------------------
def gender_selected(choice):
    global salutation
    match choice:
        case "Male":
            salutation = "MR"
        case "Female":
            salutation = "MRS"
        case "Unspecified":
            salutation = "MR/MRS"
#--------------------------Update Transaction Frame Action--------------------------------------------------------------
def update_transaction_frame(new_action):
    action = new_action
    okay_button.configure(command=lambda: on_okay_button(action))
    label5.configure(text=f"Amount to {action}")
#===================================BUTTON PRESSES======================================================================

#-------------------------UI Deposit button-----------------------------------------------------------------------------
def on_deposit_button():
    update_transaction_frame("deposit")
    global after_id
    cancel_after_timer()
    # label0.configure(text="Deposit Button Pressed")
    after_id = label0.after(1000, lambda: label0.configure(text=""))
    ui_frame.pack_forget()
    transaction_frame.pack()
#-------------------------UI Withdraw button----------------------------------------------------------------------------
def on_withdraw_button():
    update_transaction_frame("withdraw")
    global after_id
    cancel_after_timer()
    # label0.configure(text="Withdraw Button Pressed")
    after_id = label0.after(1000, lambda: label0.configure(text=""))
    #Hiding current frame and unhiding transaction frame
    ui_frame.pack_forget()
    transaction_frame.pack()
#-------------------------UI Balance button-----------------------------------------------------------------------------
def on_balance_button():
    global after_id
    cancel_after_timer()
    # label0.configure(text="Balance Button Pressed")
    after_id = label0.after(1000, lambda: label0.configure(text=""))
    reciept_text = f"""
    {8*"*"} RECIEPT {8*"*"}
    
    ACCOUNT NAME    : {account.acc_name}
    ACCOUNT NUMBER  : {account.acc_no}
    ACCOUNT TYPE    : {account.acc_type}
    ACCOUNT BALANCE : {account.balance}
    
    {7*"*"} THANK YOU {7*"*"}"""
    label_reciept.configure(text=reciept_text.upper(), anchor="w", justify="left")

    ui_frame.pack_forget()
    reciept_frame.pack()
#-------------------------UI Info button--------------------------------------------------------------------------------
def on_print_statement_button():
    global after_id
    cancel_after_timer()
    # label0.configure(text="Info Button Pressed")
    after_id = label0.after(1000, lambda: label0.configure(text=""))
    reciept_text = f"""
        {8 * "*"} RECIEPT {8 * "*"}

        ACCOUNT NAME    : {account.acc_name}
        ACCOUNT NUMBER  : {account.acc_no}
        ACCOUNT TYPE    : {account.acc_type}
        ACCOUNT BALANCE : {account.balance}

        {7 * "*"} THANK YOU {7 * "*"}"""
    label_reciept.configure(text=reciept_text.upper(), anchor="w", justify="left")

    ui_frame.pack_forget()
    reciept_frame.pack()
#-------------------------Button Press : login button-------------------------------------------------------------------
def on_login_button():
    global is_logged_in, account
    is_logged_in = True

    #If any fields are left empty show warning message
    entry_lst = [entry1,entry2,entry3]
    for i in entry_lst:
        if not i.get().strip():
            # messagebox.showwarning("Warning","Fields cannot be empty")
            label0.configure(text="Fields cannot be empty")
            break
    else :
        acc_name = entry1.get()
        acc_no = entry2.get()
        acc_type = combo1.get()
        balance = entry3.get()
        if balance.isdigit():
            account = Account(acc_name,acc_no,acc_type,balance)

            name_label.configure(text=f"WELCOME {salutation}.{acc_name.upper()}")

            login_frame.pack_forget()
            ui_frame.pack()
        else:
            # messagebox.showwarning("warning","Invalid Balance Amount")
            label0.configure(text="Invalid Balance Amount")
#-------------------------Transaction Okay button-----------------------------------------------------------------------
def on_okay_button(action):
    amount = int(amount_entry.get())
    match action:
        case "withdraw":
            if amount <= account.balance:
                account.balance -= amount
                label0.configure(text="TRANSACTION COMPLETE")
                after_id = label0.after(1000, lambda: label0.configure(text=""))
                print(f"new_balance = {account.balance}")
                transaction_frame.pack_forget()
                ui_frame.pack()
            else:
                label0.configure(text="INSUFFICIENT FUNDS")
        case "deposit":
            account.balance += amount
            label0.configure(text="TRANSACTION COMPLETE")
            after_id = label0.after(1000, lambda: label0.configure(text=""))
            print(f"new_balance = {account.balance}")
            transaction_frame.pack_forget()
            ui_frame.pack()
    amount_entry.delete(0,'end')
#-------------------------Transaction Okay button-----------------------------------------------------------------------
def on_reciept_okay_button():
    reciept_frame.pack_forget()
    ui_frame.pack()
#--------------------------On sign out button---------------------------------------------------------------------------
def on_sign_out_button():
    ui_frame.pack_forget()
    login_frame.pack()
    label0.configure(text="SUCCESSFULLY SIGNED OUT")
    after_id = label0.after(1000, lambda: label0.configure(text=""))
    for i in [entry1,entry2,entry3]:
        i.delete(0,'end')
#-----------------------------------------------------------------------------------------------------------------------
app = CTk()
app.title("ATM INTERFACE")
set_appearance_mode("light")
app.geometry("500x600")
#==============================UI FRAME=================================================================================
ui_frame = CTkFrame(app)
name_label = CTkLabel(ui_frame,text=f"WELCOME MR/MRS : ",font=("Arial",15,"bold"))
name_label.grid(row= 1,column=4)
button1 = CTkButton(ui_frame,text="Deposit",font=("Arial",14,"bold"),command=on_deposit_button,width=250,height=80)
button1.grid(row=3,column=4,pady=10,padx=20)
button1 = CTkButton(ui_frame,text="Withdraw",font=("Arial",14,"bold"),command=on_withdraw_button,width=250,height=80)
button1.grid(row=4,column=4,pady=10,padx=20)
button1 = CTkButton(ui_frame,text="Print Reciept",font=("Arial",14,"bold"),command=on_balance_button,width=250,height=80)
button1.grid(row=5,column=4,pady=10,padx=20)

sign_out_button = CTkButton(ui_frame,text="Sign Out",width=100,height=50,fg_color="red",hover_color="dark red",command=on_sign_out_button)
sign_out_button.grid(row=6,column=4,pady=10,padx=20)
# button1 = CTkButton(ui_frame,text="Statement",font=("Arial",14,"bold"),command=on_print_statement_button,width=250,height=80)
# button1.grid(row=6,column=4,pady=10,padx=20)


label0 = CTkLabel(app,text = "",text_color="#f00",font=("Arial",15,"bold"))
label0.pack(padx=10,pady=20)
#==============================LOGIN FRAME==============================================================================
login_frame = CTkFrame(app)
login_frame.pack(pady = 50)

label1 = CTkLabel(login_frame, text="ACCOUNT NAME    : ", anchor="e", width=150)
label2 = CTkLabel(login_frame, text="ACCOUNT NUMBER  : ", anchor="e", width=150)
label3 = CTkLabel(login_frame, text="ACCOUNT TYPE    : ", anchor="e", width=150)
label4 = CTkLabel(login_frame, text="ACCOUNT BALANCE : ", anchor="e", width=150)
label5 = CTkLabel(login_frame, text="GENDER : ", anchor="e", width=150)


label1.grid(row=0,column=0,padx=10,pady=10)
label2.grid(row=1,column=0,padx=10,pady=10)
label3.grid(row=2,column=0,padx=10,pady=10)
label4.grid(row=3,column=0,padx=10,pady=10)
label5.grid(row=4,column=0,padx=10,pady=10)

entry1 = CTkEntry(login_frame)
entry1.grid(row=0,column=1,padx=30,pady=10)
entry2 = CTkEntry(login_frame)
entry2.grid(row=1,column=1,padx=10,pady=10)
combo1 = CTkComboBox(login_frame,values=["Savings", "Checking", "Fixed Deposit", "Current", "Salary"])
combo1.grid(row=2,column=1,padx=10,pady=10)
entry3 = CTkEntry(login_frame)
entry3.grid(row=3,column=1,padx=10,pady=10)
combo2 = CTkComboBox(login_frame,values=["Male","Female","Unspecified"],command=gender_selected)
combo2.grid(row=4,column=1,padx=10,pady=10)

login_button = CTkButton(login_frame,text="LOGIN",command=on_login_button)
login_button.grid(row=5,column=1,pady=10)

#====================================TRANSACTION FRAME==================================================================
transaction_frame = CTkFrame(app)
transaction_frame.pack()
label5 = CTkLabel(transaction_frame,text=f"Amount to {action}")
label5.pack(pady=20,padx=20)
amount_entry = CTkEntry(transaction_frame)
amount_entry.pack(pady=20,padx=20)
okay_button = CTkButton(transaction_frame,text="Okay",command= lambda:on_okay_button(action))
okay_button.pack(pady=20,padx=20)

transaction_frame.pack_forget()
#====================================RECIEPT FRAME======================================================================
reciept_frame = CTkFrame(app,width=400)
reciept_text = "sample text"
label_reciept = CTkLabel(reciept_frame,text=reciept_text,font=("Courier",14),height=400,width=300)
label_reciept.pack()
reciept_okay_button = CTkButton(reciept_frame,text="okay",command=on_reciept_okay_button)
reciept_okay_button.pack(padx=10,pady=10)

#-----------------------------------------------------------------------------------------------------------------------
app.mainloop()