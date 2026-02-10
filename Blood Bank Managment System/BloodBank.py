import ExceptionClass as ex
from Blood import Blood
from datetime import datetime 


try:
     
    class BloodBank:
        def __init__(self):
            self.bname = "Jivan"

        def addBlood(self):
            try:
                bid = int(input("Enter Blood Id: "))
                # Check if id is already present because id is unic
                with open("data.txt", "r") as f1:
                    for line in f1:
                        list1 = line.strip().split(',')
                        if list1[0] == str(bid):
                            raise ex.DuplicateId()    
                        

                valid_bgs = {"A+","A-","B+","B-","AB+","AB-","O+","O-"}
                i = 0  
                while i<3:                  
                        bgroup = input("Enter Blood Group: ").upper()  # Enter Blood group converted into the upperCase
                        if bgroup in valid_bgs:
                            break
                        else:
                            print(" Invalid blood group! Try again (Example: A+, O-).")
                            i += 1


                count = int(input("Enter Number of Blood Bags: "))  #We cant add same bloodgroup count in count becouse expiry differ
                expDate = input("Enter Expiry date (YYYY-MM-DD): ")

                try:
                    expDate = datetime.strptime(expDate, "%Y-%m-%d").date()
                except ValueError:
                    print("Invalid date ! Please use YYYY-MM-DD")
                    BloodBank.addBlood(self)

                g = Blood(bid,bgroup,count,expDate)

                with open("data.txt","a") as f1:
                    f1.write(str(g))

            except ValueError:
                print("Please Enter Numeric input")
                BloodBank.addBlood(self)

            
            except ex.DuplicateId:
                print("Blood Id alredy exist.")
                BloodBank.addBlood(self)

        
        

        def displayBlood(self):
            try:
                with open("data.txt", "r") as f1:
                    print(f"{'Blood ID':<10} {'Group':<8} {'Count':<8} {'Expiry Date':<12}")
                    print("-" * 45)
                    for line in f1:
                        bid, bgroup, count, expDate = line.strip().split(",")
                        print(f"{bid:<10} {bgroup:<8} {count:<8} {expDate:<12}")
            except FileNotFoundError:
                print("data.txt not found!")





        def searchBlood(self):
            try:
                print("\n1.Blood Id \n2.Blood Group")
                ch = int(input('\nEnter Choice: '))
                if ch==1:
                    id = int(input("Enter Blood id: "))
                    with open("data.txt","r") as f1:
                        for b in f1:
                            bid, bgroup, count, expDate = b.strip().split(",")
                            if bid == str(id):
                                print(f"\nBlood Id:{bid}\nGroup:{bgroup}\nCount:{count}\nExpiry Date:{expDate}")
                                break
                        else:
                            print("Not Found")

                elif ch==2:
                    valid_bgs = {"A+","A-","B+","B-","AB+","AB-","O+","O-"}
                    i = 0  
                    while i<3:                  
                            bg = input("Enter Blood Group: ").upper()  # Enter Blood group converted into the upperCase
                            if bg in valid_bgs:
                                break
                            else:
                                print(" Invalid blood group! Try again (Example: A+, O-).")
                                i += 1
                    with open("data.txt","r") as f1:
                        for b in f1:
                            bid, bgroup, count, expDate = b.strip().split(",")
                            if bgroup == str(bg):
                                print(f"\nBlood Id:{bid}\nGroup:{bgroup}\nCount:{count}\nExpiry Date:{expDate}")
                                break
                        else:
                            print("Not Found")
                
                else:
                    raise ex.CorrectChoice()
                
            except ex.CorrectChoice:
                print("Enter Correct choice") 
                BloodBank.searchBlood(self)  
            
            except ValueError:
                print("Please Enter Numeric input: ")
                BloodBank.searchBlood(self)

        

        def updateBlood(self):
            container = []
            found = False
            print("1.Blood Id \n2.Blood Group")
            ch = int(input('\nEnter Choice: '))
            try:
                if (ch==1):
                    id = int(input("Enter Blood id: "))
                    with open("data.txt","r") as f1:
                        for b in f1:
                            list1 = b.strip().split(',')
                            if list1[0] == str(id) :
                                print("\n1.Add Blood Bag Count")
                                print("2.Minus Blood Bag Count")
                                found = True

                                ch = int(input("\nEnter choice: "))
                                count = int(list1[2])  # current count as integer

                                if ch == 1:
                                    c = int(input("Enter count to be added: "))
                                    count += c
                                    print(f"\nAdded successfully!  blood bags: {count}")
                                elif ch == 2:
                                    c = int(input("Enter count to be minus: "))
                                    if count >= c:
                                        count -= c
                                        print(f"\nMinus successfully! Remaining blood bags: {count}")
                                        # Price calculation
                                        print(f"\nTotal Price for {c} bags = {c * 100} Rs") 
                                    else:
                                        print(f"\nNot enough bags! Current available: {count}")
                                else:
                                    raise ex.CorrectChoice()

                                list1[2] = str(count)
                                
                                b = ",".join(list1)+"\n" #New record added in conatiner then add in new line
                                container.append(b)
                            else:
                                container.append(b)


                elif (ch==2):
                    valid_bgs = {"A+","A-","B+","B-","AB+","AB-","O+","O-"}
                    i = 0  
                    while i<3:                  
                            bg = input("Enter Blood Group: ").upper()  # Enter Blood group converted into the upperCase
                            if bg in valid_bgs:
                                break
                            else:
                                print("Invalid blood group! Try again (Example: A+, O-).")
                                i += 1
                    with open("data.txt","r") as f1:
                        for b in f1:
                            list1 = b.strip().split(',')
                            if list1[1]==str(bg):
                                print("1.Add Blood Bag Count")
                                print("2.Minus Blood Bag Count")
                                found = True

                                ch = int(input("Enter choice: "))
                                count = int(list1[2])  # current count as integer

                                if ch == 1:
                                    c = int(input("Enter count to be added: "))
                                    count += c
                                    print(f"Added successfully!  blood bags: {count}")
                                elif ch == 2:
                                    c = int(input("Enter count to be minus: "))
                                    if count >= c:
                                        count -= c
                                        print(f" Minus successfully! Remaining blood bags: {count}")
                                        # Price calculation
                                        print(f"Total Price for {c} bags = {c * 100} Rs") 
                                    else:
                                        print(f" Not enough bags! Current available: {count}")
                                else:
                                    raise ex.CorrectChoice()

                                list1[2] = str(count)
                                
                                b = ",".join(list1)+"\n" #New record added in conatiner then add in new line
                                container.append(b)
                            else:
                                container.append(b)

                else:
                    raise ex.CorrectChoice()
                
            except ex.CorrectChoice:
                print("Enter Correct choice") 
                BloodBank.updateBlood(self)  
            
            except ValueError:
                print("Please Enter Numeric input: ")
                BloodBank.updateBlood(self)

            if found == False:
                print("Not Found")   #if not present then why should repeate the update function
                
            else:
                # If record found then only process
                with open("data.txt","w") as f1:
                    for b in container:#Record back to file from container
                        f1.write(b)



        def deleteBlood(self):
            container = []
            expDate = input("Enter Expiry date (YYYY-MM-DD): ")

            try:
                expDate = datetime.strptime(expDate, "%Y-%m-%d").date()
            except ValueError:
                print("Invalid date format! Please use YYYY-MM-DD")
                BloodBank.deleteBlood(self)

            found = False

            try:
                with open("data.txt", "r") as f1:
                    for b in f1:
                        list1 = b.strip().split(',')  # split fields                        
                        date = datetime.strptime(list1[3], "%Y-%m-%d").date()
                        
                        if date > expDate:   # keep only records that have not yet expired
                            container.append(b)
                        else:
                            found = True

                if found == True:
                    with open("data.txt", "w") as f1:
                        for b in container:
                            f1.write(b)
                    print("Expired record deleted successfully!")
                else:
                    print("No expired records found.")


            except FileNotFoundError:
                print("data.txt file not found!")


        # ===== WEB METHODS (NEW) =====

    

        def addBlood_web(self, bid, bgroup, count, expDate):
            g = Blood(bid, bgroup, count, expDate)
            with open("data.txt", "a") as f:
                f.write(str(g))

        def getAllBlood_web(self):
            records = []
            try:
                with open("data.txt", "r") as f:
                    for line in f:
                        records.append(line.strip().split(","))
            except FileNotFoundError:
                pass
            return records

        def deleteBlood_web(self, expDate):
            from datetime import datetime
            expDate = datetime.strptime(expDate, "%Y-%m-%d").date()
            container = []

            with open("data.txt", "r") as f:
                for line in f:
                    bid, bg, cnt, ed = line.strip().split(",")
                    if datetime.strptime(ed, "%Y-%m-%d").date() > expDate:
                        container.append(line)

            with open("data.txt", "w") as f:
                f.writelines(container)



except ValueError:
    print("Please Enter Numeric input: ")

except ex.CorrectChoice:
    print("Enter Correct choice")

    
except:
    print("Something Wrong. Please Try Again!!")







