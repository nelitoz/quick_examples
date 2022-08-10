from flask import Flask, render_template, abort, jsonify, request, redirect, url_for
from model import db, save_db

app = Flask(__name__)
visits = 0


@app.route("/")
def welcome():
    welcome_message = "Protect yourself, don't forget the mask"
    return render_template("welcome.html",
                           message=welcome_message,
                           db_data=db
                           )


@app.route("/cards/<int:index>")
def cards(index):
    try:
        card = db[index]
        max_index = len(db)
        return render_template("card.html", card=card, index=index, max_index=max_index)
    except IndexError:
        abort(404)


@app.route("/add_card", methods=["GET", "POST"])
def add_card():
    if request.method == "POST":
        card = {"question": request.form['question'], "answer": request.form['answer']}
        db.append(card)
        save_db()
        return redirect(url_for("cards", index=len(db)-1))
    else:
        return render_template("add_card.html")


@app.route("/remove_card/<int:index>", methods=["GET", "POST"])
def remove_card(index):
    try:
        if request.method == "POST":
            del db[index]
            save_db()
            return redirect(url_for("welcome"))
        else:
            return render_template("remove_card.html", card=db[index])
    except IndexError:
        abort(404)



@app.route("/db_test")
def db_test():
    return render_template("db_test.html", db=db)


##
# SHOW API VIEWS
##
@app.route("/api/cards/")
def api_card_list():
    return jsonify(db)


@app.route("/api/card/<int:index>")
def api_card_detail(index):
    try:
        return db[index]
    except IndexError:
        abort(404)
