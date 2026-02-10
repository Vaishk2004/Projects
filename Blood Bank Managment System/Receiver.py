class Receiver: 
    def receiver(self):
        bgroup = input("Which Blood group you want: ").upper()

        found = False
        container = []

        # First check in stock (data.txt)
        with open("data.txt","r") as f1:
            for line in f1:
                record = line.strip().split(',')
                if record[1] == bgroup:
                    count = int(input("How many Bags: "))
                    available = int(record[2])
                    if available >= count:
                        available -= count
                        print(f" Blood issued successfully! Charges: ₹{count * 100}")
                        
                        if available == 0:
                            print("Stock for this blood group is now empty. Removing record...")
                            # Do not append this record (deletes from file)
                            found = True
                            continue
                        else:
                            record[2] = str(available)
                       

                    else:
                        print(f"Not enough stock! Only {available} bags available.")
                    line = ",".join(record) + "\n"
                    found = True
                    
                container.append(line)

        if found:
            # Update file with reduced stock
            with open("data.txt", "w") as f1:
                for line in container:
                    f1.write(line)
        else:
            # If blood not available check donor list
            print("Requested blood group not Available.")
            
            donors_found = False
            try:
                with open("donor.txt","r") as f2:
                    for line in f2:
                        dname, dmob, dbg = line.strip().split(',')
                        if dbg.strip() == bgroup:
                            if not donors_found:
                                print("\nYou can contact these donors directly:")
                                donors_found = True
                            print(f"\nName: {dname}\nMobile: {dmob}\nBlood Group: {dbg}")
            except FileNotFoundError:
                print("No donor records available.")

            if not donors_found:
                print("No donors available with requested blood group either.")





    def receiver_web(self, bg, qty):
        container = []
        message = "Blood not available"

        with open("data.txt", "r") as f:
            for line in f:
                r = line.strip().split(',')
                if r[1] == bg and int(r[2]) >= qty:
                    r[2] = str(int(r[2]) - qty)
                    message = f"Blood issued. Charges ₹{qty*100}"
                container.append(",".join(r) + "\n")

        with open("data.txt", "w") as f:
            f.writelines(container)

        return message



    def receiver_web(self, bg, qty):
        container = []
        donors = []
        issued = False

        with open("data.txt", "r") as f:
            for line in f:
                r = line.strip().split(',')
                if r[1] == bg and int(r[2]) >= qty and not issued:
                    r[2] = str(int(r[2]) - qty)
                    issued = True
                container.append(",".join(r) + "\n")

        if issued:
            with open("data.txt", "w") as f:
                f.writelines(container)
            return {"status": "issued", "message": f"Blood issued. Charges ₹{qty*100}"}

        # If blood not available → fetch donors
        try:
            with open("donor.txt", "r") as f:
                for line in f:
                    name, mob, dbg = line.strip().split(',')
                    if dbg.strip() == bg:
                        donors.append([name, mob, dbg])
        except FileNotFoundError:
            pass

        return {"status": "not_available", "donors": donors}
