


Using Gmail with screen readers

project in py
Inbox
	
AttachmentsMon, 13 Sept 2021, 21:29
	


	

import time
import tabulate
import mysql.connector
import datetime
import random
def loading(line):
     print('',end="")
     print()
     print(line,end="")
     for j in range(4):
          time.sleep(1)
          print('.', end='')
     print()
     print()
     time.sleep(0.5)
def again(input_field,count): # cheking for Yes while creating another account
     if count<2:
          input_field=input("                                               You have entered incorrect value, please re-enter >>  ")
     else:
          input_field=input("                            You have entered incorrect value, please re-enter or type 'q' to end >>  ")
     return input_field
def check_empty(field,typee):
     if typee==4:# if user(customer) id not exist will show error, not opeing new account
          counting=1
          cur.execute("select cust_userID from cust_mst") 
          storage1=cur.fetchall()
          while (field,) not in storage1:
               
               if counting<2:
                    field=input("                                               You have entered incorrect value, please re-enter >>  ")
               else:
                    field=input("                            You have entered incorrect value, please re-enter or type 'q' to end >>  ")
                    if field.upper()=="Q":
                         return field,counting
               counting+=1
          return field,counting
     elif typee==2:   # cheking for address if blank
          counting=1
          while field.strip()=="":
               if counting<2:
                    field=input("                                               You have entered incorrect value, please re-enter >>  ")
               else:
                    field=input("                            You have entered incorrect value, please re-enter or type 'q' to end >>  ")
                    if field.upper()=="Q":
                         return field,counting
               counting+=1
          return field,counting
     elif typee==3:  # pin code ,if blank or not digit
          counting=1
          while field.strip()=="" or len(field.split())!=1 or not field.isdigit():
               if counting<2:
                    field=input("                                               You have entered incorrect value, please re-enter >>  ")
               else:
                    field=input("                            You have entered incorrect value, please re-enter or type 'q' to end >>  ")
                    if field.upper()=="Q":
                         return field,counting
               counting+=1
          return field,counting
     elif typee==1:   # cheking for city
          counting=1
          while field.strip()=="" or len(field.split())!=1:
               if counting<2:
                    field=input("                                               You have entered incorrect value, please re-enter >>  ")
               else:
                    field=input("                            You have entered incorrect value, please re-enter or type 'q' to end >>  ")
                    if field.upper()=="Q":
                         return field,counting
               counting+=1
          return field,counting
     elif typee=='amt': # checking for amount if blank or negative or npt digit or greater the balance
          counting=1
          while field.strip()=="" or not field.isdigit() or float(field)>balance or float(field)<0: # change
               if counting<2:
                    field=input("                                 You have entered incorrect value or more than current balance, please re-enter >>  ")
               else:
                    field=input("              You have entered incorrect value or more than current balance, please re-enter or type 'q' to end >>  ")
                    if field.upper()=="Q":
                         return field,counting
               counting+=1
          return field,counting
     elif typee=='dep':
          counting=1
          while field.strip()=="" or not field.isdigit() or float(field)<=0:
               if counting<2:
                    field=input("                                               You have entered incorrect value, please re-enter >>  ")
               else:
                    field=input("                            You have entered incorrect value, please re-enter or type 'q' to end >>  ")
                    if field.upper()=="Q":
                         return field,counting
               counting+=1
          return field,counting
     elif typee==5: # if useid already exist while creating new userid
          counting=1
          cur.execute("select cust_userid from cust_mst") 
          storage1=cur.fetchall()
          while field.strip()=="" or len(field.split())!=1 or (field,) in storage1:
               if counting<2:
                    field=input("                                      You have entered incorrect value or already exists, please re-enter >>  ")
               else:
                    field=input("                  You have entered incorrect value or already exists, please re-enter or type 'q' to end >>  ")
                    if field.upper()=="Q":
                         return field,counting
               counting+=1
          return field,counting
     elif typee==6: # account code not exist for cust id
          counting=1
          cur.execute("select acc_code from cust_acc where close_dt is NULL")
          storage1=cur.fetchall()
          while field.strip()=="" or len(field.split())!=1 or not (field,) in storage1 or field==acc_code:
               if counting<2:
                    field=input("                                      You have entered incorrect value or doesn't exist, please re-enter >>  ")
               else:
                    field=input("                   You have entered incorrect value or doesn't exist, please re-enter or type 'q' to end >>  ")
                    if field.upper()=="Q":
                         return field,counting
               counting+=1
          return field,counting
     elif typee=='acc': # if acc code not exist whilr deposite money for account code
          counting=1
          cur.execute("select acc_code from cust_acc where cust_userid='"+newID+"' and close_dt is NULL")
          asd=cur.fetchall()
          while not (field,) in asd:
               if counting<2:
                    field=input("                                               You have entered incorrect value, please re-enter >>  ")
               else:
                    field=input("                            You have entered incorrect value, please re-enter or type 'q' to end >>  ")
                    if field.upper()=="Q":
                         return field,counting
               counting+=1
          return field,counting
     elif typee[:-1]=='opt':
          counting=1
          while field.strip()=="" or not field.isdigit() or not int(field) in tuple(i for i in range(1,int(typee[-1])+1)):
               if counting<2:
                    field=input("                                               You have entered incorrect value, please re-enter >>  ")
               else:
                    field=input("                            You have entered incorrect value, please re-enter or type 'q' to end >>  ")
                    if field.upper()=="Q":
                         return field,counting
               counting+=1
          return field,counting
     
     elif typee=='mob':
          counting=0
          while not field.isdigit() or len(str(int(field)))!=5:
               if counting<1:
                    field=input("                                               You have entered incorrect value, please re-enter >>  ")
               else:
                    field=input("                            You have entered incorrect value, please re-enter or type 'q' to end >>  ")
                    if field.upper()=="Q":
                         return field,counting
               counting+=1
          return field,counting
     elif typee=='mail':
          counting=0
          while '@' not in field or '.' not in field.split('@')[1] or len(field.split('@'))!=2 or len(field.split('.'))!=2 or not ''.join(''.join(field.split('.')).split('@')).isalnum():
               if counting<1:
                    field=input("                                               You have entered incorrect value, please re-enter >>  ")
               else:
                    field=input("                            You have entered incorrect value, please re-enter or type 'q' to end >>  ")
                    if field.upper()=="Q":
                         return field,counting
               counting+=1
          return field,counting
     elif typee=="integer":
          counting=1
          print(newID)
          cur.execute("select cust_PIN from cust_mst where cust_userID='"+newID+"'")
          storage1=cur.fetchall()
          print(storage1[0][0])
          while (field,) not in storage1:
               if counting<2:
                    field=input("                                               You have entered incorrect value, please re-enter >>  ")
               else:
                    
                    field=input("                            You have entered incorrect value, please re-enter or type 'q' to end >>  ")
                    if field.upper()=="Q":
                         return field,counting
               counting+=1
          return field,counting
     elif typee=="name": # name is numbers 
          counting=1
          names=field.split()
          while field.isdigit()or len(field.split())!=1 :
               
               if counting<2:
                    field=input("                                               You have entered incorrect value, please re-enter >>  ")
               else:
                    field=input("                            You have entered incorrect value, please re-enter or type 'q' to end >>  ")
                    if field.upper()=="Q":
                         return field,counting
               counting+=1
          return field,counting
    

#A savings /fixed / recurring bank deposit account can be opened by a minor of any age through his/her natural or legally appointed guardian.
#Minors above the age of 10 years may be allowed to open and operate savings bank accounts independently, if they so desire
def acc_check():
     global ch
     global newID
     ch=1
     count1=0
     acc=input("                                                    Do you already have an account with us.(Y/N) >>  ")
     print()
     while acc.upper() not in ('YES','Y','NO','N'):
          count1+=1
          acc=again(acc,count1)
          if count1>=2 and acc.upper()=='Q':
               ch=2
               print('',end="")
               break
     while ch!=2:#matlab jab sahi value input ki acc mei
          if acc.upper() in ('YES','Y'):
               print()
               newID=input("                                                          Enter your UserID >>  ")
               newID,count2=check_empty(newID,4)
               if count2>=2 and newID.upper()=='Q':
                    ch=2
                    print('',end="")
                    break
               PIN=input("                                                             Enter your PIN >>  ")
               PIN,count3=check_empty(PIN,"integer") 
               if count3>=2 and PIN.upper()=="Q":
                    ch=2
                    print('',end="")
                    break
               loading("                                                                       Loading")
               print("Successfully Logged In".center(154))
               break
          else:
               print()
               print("-----   .*.*.*.*.    According to our Bank's policy, Account code cannot be changed once created     .*.*.*.*.   -----".center(153))
               print()
               print("For registering with us: ".center(154))
               print()
               newID=input("                                                          Enter your New UserID >>  ")
               newID,count4=check_empty(newID,5)
               if count4>=2 and newID.upper()=='Q':
                    ch=2
                    print('',end="")
                    break
               name=input("                                                           Enter your Full Name >>  ")
               name,count5=check_empty(name,"name")
               if count5>=2 and name.upper()=="Q":
                    ch=2
                    print('',end="")
                    break
               sex=input("                                                            Enter your sex(M/F) >>  ")
               count6=0
               while sex.upper() not in ('MALE','FEMALE','M','F'):
                    count6+=1
                    sex=again(sex,count6)
                    if count6>=2 and sex.upper()=='Q':
                         ch=2
                         print('',end="")
                         break
               if ch==2:
                    break
               if sex.upper() in ('MALE','M'):
                    sex="M"
               else:
                    sex="F"
               add=input("                                                   Enter your Address(In short) >>  ")
               add,count7=check_empty(add,2)
               if count7>=2 and add.upper()=='Q':
                    ch=2
                    print('',end="")
                    break
               city=input("                                                                Enter your City >>  ")
               city,count8=check_empty(city,1)
               if count8>=2 and city.upper()=='Q':
                    ch=2
                    print('',end="")
                    break
               dob=input("                                           Enter your Date of birth(YYYY-MM-DD) >>  ")
              
               
               mob=input("                                                       Enter your mobile number >>  ")
               mob,count10=check_empty(mob,"mob")
               if count10>=1 and mob.upper()=="Q":
                    ch=2
                    print('',end="")
                    break
               email=input("                                                      Enter your E-mail address >>  ")
               email,count11=check_empty(email,"mail")
               if count11>=1 and email.upper()=="Q":
                    ch=2
                    print('',end="")
                    break
               while True:
                    newPIN1=input("                                                             Enter your New PIN >>  ")
                    newPIN1,count12=check_empty(newPIN1,3)
                    if count12>=2 and newPIN1.upper()=='Q':
                         ch=2
                         print('',end="")
                         break
                    newPIN2=input("                                                           Enter your PIN again >>  ")
                    if newPIN1==newPIN2:
                        
                         loading("                                                                       Loading")
                         print("Your account has been successfully registered and Logged In".center(154))
                         break
                    print()
                    print("Both Pins Didn't match, please re-enter".center(154))
                    print()
               if ch==2:
                    break
               #cust_userID cust_PIN Cust_name Cust_sex cust_add Cust_city Cust_DOB cust_mobile Cust_Email
               cur.execute("select count(*) from cust_acc where acc_code like 'A%'")# Automatic accound code will generate 
               myrecords=cur.fetchall()
               for x in myrecords:
                         rows=x[0]      
               rows=rows+1 
               code="A0"+str(rows)
               cur.execute("insert into cust_mst values('"+newID+"','"+newPIN2+"','"+name+"','"+sex+"','"+add+"','"+city+"','"+str(dob)+"',"+mob+",'"+email+"')")
               mydb.commit()
               cur.execute("insert into cust_acc values('"+newID+"','SNG0123456','"+code+"','"+str(datetime.date.today())+"',NULL,4.00,0.00)")
               mydb.commit()
               print("Congratulations, Your New Account has been created.".center(154))
               print("                                Account code for new account is "+code+". All your other credentials are same for this Account.")
               print()
               break
def menu():
     global ch
     global newID
     global acc_code
     global balance
     acc_if=1
     while ch!=2:
          print()
          print()
          print('',end='')
          print()
          print()
          cur.execute("select cust_name from cust_mst where cust_userid='"+newID+"'")
          storage1=cur.fetchall()
          print("                                             Hello",list(storage1[0])[0],"   ----  &&&&  ----    Today is",datetime.date.today())
          cur.execute("select count(*) from cust_acc where cust_userid='"+newID+"' and close_dt is NULL")
          if cur.fetchall()[0]==(0,):
               print()
               print("Your all Accounts are closed with this User ID".center(154))
               print()
               print()
               print("                                           We offer Following Services:")
               print()
               print("                                                               >>  Open an Account           (1)")
               print("                                                               >>  Exit                      (2)")
               print()
               option=input("                                        To Choose any above option, type the number which is in front of them >>  ")
               option,count19=check_empty(option,"opt2")
               if count19>=2 and option.upper()=="Q":
                    ch=2
                    print('',end="")
                    break
               print()
               if option=='1':
                    cur.execute("select count(*) from cust_acc where acc_code like 'A%'")
                    myrecords=cur.fetchall()
                    for x in myrecords:
                         rows=x[0]      
                    rows=rows+1 
                    code="A0"+str(rows)
                    cur.execute("insert into cust_acc values('"+newID+"','SNG0123456','"+code+"','"+str(datetime.date.today())+"',NULL,4.00,0.00)")
                    mydb.commit()
                    loading("                                                                       Loading")
                    print()
                    print("Congratulations, Your New Account has been created.".center(154))
                    print("                                Account code for new account is "+code+". All your other credentials are same for this Account.")
               elif option=='2':
                    print()
                    print("Successfully Logged out".center(153))
                    ch=2
                    print('',end="")
                    break
          cur.execute("select count(*) from cust_acc where cust_userid='"+newID+"' and close_dt is NULL")
          if cur.fetchall()[0]!=(0,):
               if acc_if==1:
                    cur.execute("select acc_code,cur_bal from cust_acc where cust_userid='"+newID+"' and close_dt is NULL")
                    storageacc=cur.fetchall()
                    (acc_code,balance)=storageacc[0]
               cur.execute("select acc_code,cur_bal from cust_acc where cust_userid='"+newID+"' and close_dt is NULL")
               storageacc=cur.fetchall()
               print()
               print("                                                      ---  You are currently using account",acc_code,"---")
               print()
               print("----".center(153))
              
               print()
               print()
               print("                                           We offer Following Services:")
               print()
               print("                                                               >>  Pay                       (1)")
               print("                                                               >>  Passbook                  (2)")
               print("                                                               >>  Update Details            (3)")
               print("                                                               >>  Deposit Money             (4)")
               print("                                                               >>  View your Credentials     (5)")
               print("                                                               >>  Open another Account      (6)")
               print("                                                               >>  Close an Account          (7)")
               print("                                                               >>  Exit                      (8)")
              
               print("                                                               >>  Use another Account       (9)")
               print()
               option=input("                                        To Choose any above option, type the number which is in front of them >>  ")
               
               if option=='1':
                    amt=input("                                                         Enter amount to be paid(in INR) >>  ")
                    amt,count13=check_empty(amt,"amt")
                    if count13>=2 and amt.upper()=="Q":
                         ch=2
                         print('',end="")
                         break
                    tran_to_id=input("                                    Enter the Account Code to which payment will be done >>  ")
                    tran_to_id,count14=check_empty(tran_to_id,6)
                    if count14>=2 and tran_to_id.upper()=='Q':
                         ch=2
                         print('',end="")
                         break
                    cur.execute("select emp_code,emp_name from emp_mst")
                    (empcode,empname,)=random.choice(cur.fetchall())
                    cur.execute("select cust_userid,cur_bal,bank_IFEC_code from cust_acc where acc_code='"+tran_to_id+"'")
                    (ucode2,cur_bal2,bcode2)=cur.fetchall()[0]
                    cur.execute("insert into bank_tran values('SNG0123456','"+newID+"','"+acc_code+"','"+str(datetime.datetime.now().strftime('%Y-%m-%d %X'))+"','credit',"+amt+",'"+empname+"','"+empcode+"',"+str(float(balance))+","+str(float(balance))+"-"+amt+")")
                    mydb.commit()
                    cur.execute("insert into bank_tran values('"+bcode2+"','"+ucode2+"','"+tran_to_id+"','"+str(datetime.datetime.now().strftime('%Y-%m-%d %X'))+"','debit',"+amt+",'"+empname+"','"+empcode+"',"+str(float(cur_bal2))+","+str(float(cur_bal2))+"+"+amt+")")
                    mydb.commit()
                    cur.execute("update cust_acc set cur_bal=cur_bal-"+amt+" where acc_code='"+acc_code+"'")
                    mydb.commit()
                    cur.execute("update cust_acc set cur_bal=cur_bal+"+amt+" where acc_code='"+tran_to_id+"'")
                    mydb.commit()
                    loading("                                                                       Loading")
                    print("Transaction Successful".center(154))
               elif option=='2':
                    cur.execute("select * from bank_tran where acc_code='"+acc_code+"' order by date_time_tran")
                    print()
                    lasd=["Bank IFSC Code","User ID","Acc Code","Date and Time","Type","Amount","Emp Name","Emp Code","Opening Balance","Closing Balance"]
                    print(tabulate.tabulate(cur.fetchall(),headers=lasd,tablefmt="grid"))
               elif option=='3':
                    print()
                    print()
                    print("****As mentioned at the time of creation of account, Account code cannot be changed****".center(153))
                    print()
                    print("                                  Following credentials can be changed/updated:")
                    print()
                    #print("                                                               >>  User ID                   (1)")
                    print("                                                               >>  PIN                       (1)")
                    print("                                                               >>  Full Name                 (2)")
                    print("                                                               >>  Address and City          (3)")
                    print("                                                               >>  Mobile Number             (4)")
                    print("                                                               >>  Email Address             (5)")
                    print()
                    up=input("                                        To Choose any above option, type the number which is in front of them >>  ")
                    
                    
                   
                    if up=='1':
                         while True:
                              newPIN1=input("                                                             Enter your New PIN >>  ")
                              newPIN1,count21=check_empty(newPIN1,3)
                              if count21>=2 and newPIN1.upper()=='Q':
                                   ch=2
                                   print('',end="")
                                   break
                              newPIN2=input("                                                           Enter your PIN again >>  ")
                              if newPIN1==newPIN2:
                                   cur.execute("update cust_mst set cust_PIN='"+newPIN2+"' where cust_userid='"+newID+"'")
                                   mydb.commit()
                                   print()
                                   loading("                                                                       Loading")
                                   print()
                                   print("Successfully Updated PIN".center(154))
                                   break
                              print()
                              print("Both Pins Didn't match, please re-enter".center(154))
                              print()
                    elif up=='2':
                         name=input("                                                           Enter your Full Name >>  ")
                         name,count22=check_empty(name,"name")
                         if count22>=2 and name.upper()=="Q":
                              ch=2
                              print('',end="")
                              break
                         cur.execute("update cust_mst set cust_name='"+name+"' where cust_userid='"+newID+"'")
                         mydb.commit()                    
                         print()
                         loading("                                                                       Loading")
                         print()
                         print("Successfully Updated Name".center(154))
                    elif up=='3':
                         add=input("                                                   Enter your Address(In short) >>  ")
                         add,count23=check_empty(add,2)
                         if count23>=2 and add.upper()=='Q':
                              ch=2
                              print('',end="")
                              break
                         city=input("                                                                Enter your City >>  ")
                         city,count24=check_empty(city,1)
                         if count24>=2 and city.upper()=='Q':
                              ch=2
                              print('',end="")
                              break
                         cur.execute("update cust_mst set cust_add='"+name+"', cust_city='"+city+"' where cust_userid='"+newID+"'")
                         mydb.commit()                    
                         print()
                         loading("                                                                       Loading")
                         print()
                         print("Successfully Updated Address and City".center(154))
                    elif up=='4':
                         mob=input("                                                       Enter your mobile number >>  ")
                         mob,count25=check_empty(mob,"mob")
                         if count25>=1 and mob.upper()=="Q":
                              ch=2
                              print('',end="")
                              break
                         cur.execute("update cust_mst set cust_mobile='"+mob+"' where cust_userid='"+newID+"'")
                         mydb.commit()                    
                         print()
                         loading("                                                                       Loading")
                         print()
                         print("Successfully Updated Mobile Number".center(154))
                    elif up=='5':
                         email=input("                                                      Enter your E-mail address >>  ")
                         email,count26=check_empty(email,"mail")
                         if count26>=1 and email.upper()=="Q":
                              ch=2
                              print('',end="")
                              break
                         cur.execute("update cust_mst set cust_email='"+email+"' where cust_userid='"+newID+"'")
                         mydb.commit()                    
                         print()
                         loading("                                                                       Loading")
                         print()
                         print("Successfully Updated Mobile Number".center(154))
                    print()
                    print("Your Updated Credentials are:-".center(154))
                    print()
                    cur.execute("select * from cust_mst where cust_userid='"+newID+"'")
                    print()
                    lasd1=["User ID","PIN","Name","Sex","Address","City","DOB","Mobile Number","Email Address"]
                    print(tabulate.tabulate(cur.fetchall(),headers=lasd1,tablefmt="grid"))
                    lasd1=["Number of Accounts Active","Account Code(s)"]
                    cur.execute("select acc_code from cust_acc where cust_userid='"+newID+"'and close_dt is NULL" )
                    acodelist=cur.fetchall()
                    print(tabulate.tabulate(((str(len(acodelist)),)+(' '.join(list(i for (i,) in acodelist)),),),headers=lasd1,tablefmt="grid"))
               elif option=='4':
                    amt=input("                                                    Enter amount to be deposited(in INR) >>  ")
                    amt,count17=check_empty(amt,"dep")
                    if count17>=2 and amt.upper()=="Q":
                         ch=2
                         print('',end="")
                         break
                    cur.execute("select emp_code,emp_name from emp_mst")
                    (empcode,empname,)=random.choice(cur.fetchall())
                    cur.execute("insert into bank_tran values('SNG0123456','"+newID+"','"+acc_code+"','"+str(datetime.datetime.now().strftime('%Y-%m-%d %X'))+"','Deposit',"+amt+",'"+empname+"','"+empcode+"',"+str(float(balance))+","+str(float(balance))+"+"+amt+")")
                    mydb.commit()
                    cur.execute("update cust_acc set cur_bal=cur_bal+"+amt+" where acc_code='"+acc_code+"'")
                    mydb.commit()
                    loading("                                                                       Loading")
                    print("Transaction Successful".center(154))
               elif option=='5':
                    print("Your Credentials are:-".center(154))
                    print()
                    cur.execute("select * from cust_mst where cust_userid='"+newID+"'")
                    print()
                    lasd1=["User ID","PIN","Name","Sex","Address","City","DOB","Mobile Number","Email Address"]
                    print(tabulate.tabulate(cur.fetchall(),headers=lasd1,tablefmt="grid"))
                    lasd1=["Account Code","Current Balance","Opening Date","Closing Date"]
                    cur.execute("select acc_code,cur_bal,close_dt from cust_acc where cust_userid='"+newID+"'")
                    print(tabulate.tabulate(cur.fetchall(),headers=lasd1,tablefmt="grid"))
               elif option=='6':
                    print()
                    accs=input("                                             Are you sure that you want to create another account? (Y/N) >>  ")
                    count18=0
                    while accs.upper() not in ('YES','NO','Y','N'):
                         count18+=1
                         accs=again(accs,count18)
                         if count18>=2 and accs.upper()=='Q':
                              ch=2
                              print('',end="")
                              break
                    if accs.upper() in ('YES','Y'):
                         cur.execute("select count(*) from cust_acc where acc_code like 'A%'")
                         (rows,)=cur.fetchall()[0]
                         rows=int(rows)+1
                         code="A0"+str(rows)
                         cur.execute("insert into cust_acc values('"+newID+"','SNG0123456','"+code+"','"+str(datetime.date.today())+"',NULL,4.00,0.00)")
                         mydb.commit()
                         print()
                         loading("                                                                       Loading")
                         print()
                         print("Congratulations, Your New Account has been created.".center(154))
                         print("                                Account code for new account is "+code+". All your other credentials are same for this Account.")
               elif option=='7':
                    print()
                    print("                                               You have following Accounts registered on",newID,"User ID:")
                    print()
                    lasd1=["                        Active Account Code(s)                         ","                            Current Balance(INR)                           "]
                    print(tabulate.tabulate(storageacc,headers=lasd1,tablefmt="grid"))
                    print()
                    acc_rem=input("                                                        Type the Account Code you want to close >>  ")
                    acc_rem,count28=check_empty(acc_rem,"acc")
                    if count28>=2 and acc_rem.upper()=="Q":
                         ch=2
                         print('',end="")
                         break
                    print()
                    if acc_rem==acc_code:
                         acc_if=1           
                    cur.execute("update cust_acc set close_dt='"+str(datetime.date.today())+"' where acc_code='"+acc_rem+"'")
                    mydb.commit()
                    print("Successfully closed".center(154))
               elif option=='8':
                    print("Successfully Logged out".center(153))
                    ch=2
                    print('',end="")
                    break
               elif option=='9':
                    print()
                    print("                                               You have following Accounts registered on",newID,"User ID:")
                    print()
                    lasd1=["                        Active Account Code(s)                         ","                            Current Balance(INR)                           "]
                    print(tabulate.tabulate(storageacc,headers=lasd1,tablefmt="grid"))
                    print()
                    acc_choice=input("                                                      Type the Account Code you want to swap to >>  ")
                    acc_choice,count27=check_empty(acc_choice,"acc")
                    if count27>=2 and acc_choice.upper()=="Q":
                         ch=2
                         print('',end="")
                         break
                    print()
                    print("Successfully changed".center(154))
                    acc_if=2     # use another account
                    acc_code=acc_choice
                    cur.execute("select cur_bal from cust_acc where acc_code='"+acc_code+"'")
                    (balance,)=cur.fetchall()[0]
               print()
               print()
               ask=input("                                                      Do you again want to go to menu?(Y/N) >>  ")
               count16=0
               while ask.upper() not in ('YES','Y','NO','N'):
                    count16+=1
                    ask=again(ask,count16)
               if (count16>=2 and ask.upper()=='Q') or ask.upper() in ('NO','N'):
                    ch=2
                    print('',end="")
                    break
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="banking_system")
cur=mydb.cursor()
loading("        Getting Banking Systems Online")
print("        Secure Connection Established",end="")
print()
print()
print()
print()
time.sleep(1.3)
print("----    Welcome to SNG Bank Portal    ----".center(154))
print()
print()
time.sleep(0.4)
print("**********SNG Bank never asks for PIN and OTP from customers**********".center(154))
print()
print()
print()
print()
time.sleep(0.4)
acc_check()
while ch!=2:
     menu()
     ch=2
else:
     print()
     print("Thank you for your valuable time!!!".center(154))


final-copy_-_Copy.py
Displaying final-copy_-_Copy.py.
