from flask import Flask, render_template, request, redirect, session
from BloodBank import BloodBank
from Donor import Donor
from Receiver import Receiver

app = Flask(__name__)
app.secret_key = "bloodbank_secret_key_123"

b = BloodBank()
d = Donor()
r = Receiver()

ADMIN_USERNAME = "Vaishak"
ADMIN_PASSWORD = "Vaish123"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/admin", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        user = request.form.get("username")
        pwd = request.form.get("password")

        if user == ADMIN_USERNAME and pwd == ADMIN_PASSWORD:
            session["admin"] = True
            return redirect("/admin/dashboard")
        else:
            return render_template("admin_login.html", error="Invalid credentials")

    return render_template("admin_login.html")


@app.route("/admin/dashboard", methods=["GET", "POST"])
def admin_dashboard():
    if "admin" not in session:
        return redirect("/admin")

    search_result = None

    if request.method == "POST":
        action = request.form.get("action")

        # ADD BLOOD
        if action == "add":
            b.addBlood_web(
                request.form["bid"],
                request.form["bgroup"].upper(),
                request.form["count"],
                request.form["expDate"]
            )

        # DELETE EXPIRED BLOOD
        elif action == "delete":
            b.deleteBlood_web(request.form["expDate"])

        # SEARCH BLOOD
        elif action == "search":
            value = request.form["search_value"]
            for r in b.getAllBlood_web():
                if r[0] == value or r[1] == value.upper():
                    search_result = r
                    break

        # UPDATE BLOOD COUNT
        elif action == "update":
            bid = request.form["bid"]
            new_count = request.form["new_count"]

            records = b.getAllBlood_web()
            updated = []
            for r in records:
                if r[0] == bid:
                    r[2] = new_count
                updated.append(",".join(r) + "\n")

            with open("data.txt", "w") as f:
                f.writelines(updated)

    records = b.getAllBlood_web()
    return render_template(
        "admin.html",
        records=records,
        search_result=search_result
    )





@app.route("/receiver", methods=["GET", "POST"])
def receiver():
    result = None

    if request.method == "POST":
        group = request.form.get("group")
        qty = request.form.get("qty")

        if not group or not qty:
            return render_template("receiver.html", message="Please fill all fields")

        result = r.receiver_web(group.upper(), int(qty))

    return render_template("receiver.html", result=result)





@app.route("/donor", methods=["GET", "POST"])
def donor():
    message = None

    if request.method == "POST":
        name = request.form.get("name")
        mobile = request.form.get("mobile")
        group = request.form.get("group")

        if not name or not mobile or not group:
            return render_template(
                "donor.html",
                message="Please fill all fields"
            )

        d.addDonor_web(name, mobile, group.upper())
        message = "Donor added successfully"

    return render_template("donor.html", message=message)




@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
