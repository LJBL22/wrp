from cs50 import SQL
from flask import Flask, render_template, request

# Configure application
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"]

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///price.db")

db.execute("""
            CREATE TABLE IF NOT EXISTS records (
                Timestamp DEFAULT CURRENT_TIMESTAMP,
                relation TEXT NOT NULL,
                showup TEXT NOT NULL,
                venue TEXT NOT NULL,
                add_adult INTEGER NOT NULL,
                add_child INTEGER NOT NULL,
                add_money INTEGER NOT NULL,
                total_amount INTEGER NOT NULL
           )
        """)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calculator", methods=["GET", "POST"])
def calculator():
    venues = db.execute("SELECT * FROM venues")
    relationship = db.execute("SELECT * FROM relationship")
    total = 0

    if request.method == "POST":
        relationship_option = request.form.get("relationship")
        print(relationship_option)
        if not (relationship_option):
            return render_template("error.html", error_msg = "Please choose a RELATION option")
        showup_option = request.form.get("showup")
        venue_option = request.form.get("venue")
        if not (venue_option):
            return render_template("error.html", error_msg = "Please choose a VENUE option")
        adult = int(request.form.get("adult", 0))
        child = int(request.form.get("child", 0))
        optional = int(request.form.get("optional", 0))

        # Retrieve prices from the database based on user selections
        price_relationship = db.execute("SELECT price FROM relationship WHERE relation = ?", relationship_option)[0]["price"]

        price_showup = 0
        if (showup_option == "yes"):
            price_showup = 400
        else:
            price_showup = -800

        price_venue = db.execute("SELECT price FROM venues WHERE place = ?", venue_option)[0]["price"]

        # to name the conditions
        single = price_relationship + price_showup + price_venue
        add_adult = adult * (price_relationship + price_venue)
        add_child = child * 600

        # Calculate total based on prices and user input
        total = total + single + add_adult + add_child + optional

        ###### DEV ONLY
        # print("original: ", total)

        total = replace_digit(total)

        ###### DEV ONLY
        # print(total, single, adult, add_adult, add_child, optional)

        if total <= 600:
            total = replace_digit(price_relationship)
        db.execute("INSERT INTO records (relation, showup, venue, add_adult, add_child, add_money, total_amount) VALUES(?, ?, ?, ?, ?, ?, ?)", relationship_option, showup_option, venue_option, adult, child, optional, total)

    return render_template("calculator.html", venues=venues, relationship=relationship, total=total, records=db.execute("SELECT * FROM records ORDER BY Timestamp DESC LIMIT 5"))

def replace_digit(number):
    if number < 10000:
        while '4' in str(number) or '8' in str(number) or number in range(1000, 9000, 2000): #from 1000 to 9000, gap 2000
            if number == 9800:
                return number + 100
            number += 200
        return number
    elif number >= 10000:
        # to thousand, last three digits are 000
        number = ((number + 999) // 1000) * 1000

        # last check
        while '4' in str(number) or '8' in str(number):
            number += 2000
        return number

###### DEV ONLY
original_number = 9000
modified_number = replace_digit(original_number)
print(f"{original_number} becomes {modified_number}")

@app.route("/records", methods=["GET", "POST"])
def records():
    """Show records of search"""
    records=db.execute("SELECT * FROM records ORDER BY Timestamp DESC")
    if records:
        return render_template("records.html", records=records)


def ntd(value):
    """Format value as NTD."""
    return f"NTD${value:,}"

# Custom filter
app.jinja_env.filters["ntd"] = ntd
