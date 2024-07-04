import csv
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


def write_to_file(data):
    email = data["email"]
    subject = data["subject"]
    message = data["message"]

    db = open("./database.txt", "a")
    file = db.write(f"\n \n Email: {email} \n Subject: {subject} \n Message: {message}")


def write_to_csv(data):
    email = data["email"]
    subject = data["subject"]
    message = data["message"]

    with open("database.csv", "a", newline="") as db:
        csv_writer = csv.writer(
            db, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL
        )
        csv_writer.writerow([email, subject, message])


@app.route("/")
def my_home():
    return render_template("index.html")


@app.route("/<string:page_name>")
def handle_page(page_name="/"):
    return render_template(page_name)


@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            # write_to_file(data)
            write_to_csv(data)
            return redirect("thankyou.html")
        except:
            return "Did not save to database"
    else:
        return "Something went wrong"
