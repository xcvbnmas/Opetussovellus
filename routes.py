from app import app
from flask import render_template, request, redirect
import users
import courses

@app.route("/")
def index():
    return render_template("index.html", courses=courses.get_courses())


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Virheellinen tunnus tai salasana")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POSt"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        username = request.form["username"]
        if len(username) < 1 or len(username) > 15:
            return render_template("error.html", message="Käyttäjätunnuksen tulee olla 1-15 merkkiä pitkä")

        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 == "":
            return render_template("error.html", message="Lisää salasana")
        if password1 != password2:
            return render_template("error.html", message="Varmista, että salasanat ovat samat")
        role = request.form["role"]
        if role not in ("1", "2"):
            return render_template("error.html", message="Valitse rooli")
        if not users.register(username, password1, role):
            return render_template("error.html", message="Rekisteröinti epäonnistui")
           
        return redirect("/")
        
        
@app.route("/add", methods=["GET", "POST"])
def add_course():
    users.role(2)

    if request.method == "GET":
        return render_template("add.html")

    if request.method == "POST":
        users.check_csrf()

        name = request.form["name"]
        if len(name) < 1 or len(name) > 15:
            return render_template("error.html", message="Nimessä tulee olla 1-15 merkkiä")

        course_id = courses.add_course(name, visible, users.user_id())
        return redirect("/add")
        
        
@app.route("/course/<int:course_id>")
def show_course(course_id):
    course = courses.get_course(course_id)

    return render_template("course.html", id=course_id, name=course[0], creator=course[1])
    
    
@app.route("/remove", methods=["GET", "POST"])
def remove_course():
    users.role(2)

    if request.method == "GET":
        courselist = courses.get_courses()
        return render_template("remove.html", list=courselist)

    if request.method == "POST":
        users.check_csrf()

        if "course" in request.form:
            course = request.form["course"]
            courses.remove_course(course, users.user_id())

    return redirect("/")
        
        
        
