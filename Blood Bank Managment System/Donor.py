class Donor:
    def __init__(self,dname=" ",dmob=0,dbg=0):
        self.dname = dname
        self.dmob = dmob
        self.dbg = dbg

    def __str__(self):
        return f"{self.dname}, {self.dmob}, {self.dbg} \n"
    
    def displayDonor(self):
        try:
            with open("donor.txt", "r") as f:
                print(f"{'Name':<10} {'Contact':<14} {'Group':<8}")
                print("-" * 35)
                for line in f:
                    dname,dmob,dbg=line.strip().split(',')
                    print(f"{dname:<10} {dmob:<14} {dbg:<8}")
        except FileNotFoundError:
            print("No donor records available.")



    def donorinfo(self):
        try:
            attempts = 0
            while attempts < 3:
                nm = input("Enter Name: ")
                if nm.replace(" ", "").isalpha():  # allows alphabets + spaces
                    break
                else:
                    print(" Invalid name! Only alphabets allowed.")
                    attempts += 1
            
            attempts = 0
            while attempts < 3:
                mob = input("Enter Mobile number: ")
                if not mob.isdigit() or len(mob) != 10:
                    print("Invalid mobile number! Please enter 10 digits.")
                    attempts +=1
                else:
                    break
                

            valid_bgs = {"A+","A-","B+","B-","AB+","AB-","O+","O-"}
            attempts = 0
        
            while attempts < 3:
                b = input("Enter Blood Group: ").upper()#Input taken as upperCase
                if b in valid_bgs:
                    break
                else:
                    print(" Invalid blood group! Try again (Example: A+, O-).")
                    attempts += 1
            
            d = Donor(nm,mob,b)

            with open("donor.txt","a") as f1:
                    f1.write(str(d))

        except ValueError:
            print("Please Enter Numeric input")
            Donor.donorinfo(self)


    

    #===Web Code===
    def addDonor_web(self, name, mobile, bg):
        with open("donor.txt", "a") as f:
            f.write(f"{name},{mobile},{bg}\n")

    def getDonor_web(self):
        donors = []
        try:
            with open("donor.txt", "r") as f:
                for line in f:
                    donors.append(line.strip().split(","))
        except FileNotFoundError:
            pass
        return donors





         