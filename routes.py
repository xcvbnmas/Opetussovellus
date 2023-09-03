from flask import render_template, request, redirect
import users
import exercises
import messagefunctions
import announcements
from app import app

@app.route("/")
def index():
    return render_template("index.html", exercises=exercises.get_exercises(), announcements=announcements.get_list())


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
def add_exercise():
    users.role(2)

    if request.method == "GET":
        return render_template("add.html")

    if request.method == "POST":
        users.check_csrf()

        name = request.form["name"]
        if len(name) < 1 or len(name) > 20:
            return render_template("error.html", message="Nimessä tulee olla 1-20 merkkiä")
         
        instructions = request.form["instructions"]
        if len(instructions) < 1:
            return render_template("error.html", message="Lisää tehtävänanto")
        if len(instructions) > 10000:
            return render_template("error.html", message="Tehtävänanto on liian pitkä")
            
        model_answer = request.form["model_answer"] 
        if len(model_answer) < 1:
            return render_template("error.html", message="Lisää mallivastaus")
        if len(model_answer) > 10000:
            return render_template("error.html", message="Mallivastaus on liian pitkä")

        exercise_id = exercises.add_exercise(name, instructions, model_answer)
        return redirect("/")
        
        
@app.route("/exercise/<int:exercise_id>")
def show_exercise(exercise_id):
    exercise = exercises.get_exercise(exercise_id)
    answer = exercises.get_answer(users.user_id(), exercise_id)
    
    user_id = users.user_id() 
    user_answer = exercises.get_answer(exercise_id, users.user_id())
    model_answer = exercise.model_answer
  
    return render_template("exercise.html", id=exercise_id, name=exercise[0], instructions=exercise[1], exercise=exercise, user_answer=user_answer, model_answer=model_answer)
    
@app.route("/submit_answer", methods=["POST"])
def submit_answer():
    users.check_csrf()  

    exercise_id = int(request.form["exercise_id"])
    answer = request.form["answer"]

    exercises.submit_answer(exercise_id, answer, users.user_id())

    return redirect(f"/exercise/{exercise_id}")
    
    
@app.route("/remove", methods=["GET", "POST"])
def remove_exercise():
    users.role(2)

    if request.method == "GET":
        exerciselist = exercises.get_exercises()
        return render_template("remove.html", list=exerciselist)

    if request.method == "POST":
        users.check_csrf()

        if "exercise" in request.form:
            exercise = request.form["exercise"]
            exercises.remove_exercise(exercise, users.user_id())

    return redirect("/")
    
 
@app.route("/messages", methods=["GET", "POST"])
def messages():
    list = messagefunctions.get_list()
    return render_template("messages.html", count=len(list), messages=list)

@app.route("/new", methods=["GET", "POST"]) 
def new():
    if request.method == "GET":
        return render_template("new.html")
    
    if request.method == "POST":
        content = request.form["content"]
        if messagefunctions.send(content):
            return redirect("/messages")
        else:
            return render_template("error.html", message="Viestin lähetys ei onnistunut")
        
@app.route("/send", methods=["GET", "POST"])
def send():
    content = request.form["content"]
    if messagefunctions.send(content):
        return redirect("/messages")
    else:
        return render_template("error.html", message="Viestin lähetys ei onnistunut")
        
@app.route("/add_announcement", methods=["GET", "POST"])
def add_announcement():
    users.role(2)

    if request.method == "GET":
        return render_template("add_announcement.html")

    if request.method == "POST":
        users.check_csrf()

        content = request.form["content"]
        if len(content) < 1:
            return render_template("error.html", message="Lisää ilmoitus.")

        announcement_id = announcements.add_announcement(content)
        return redirect("/")
        
@app.route("/remove_announcement", methods=["GET", "POST"])
def remove_announcement():
    users.role(2)

    if request.method == "GET":
        announcementlist = announcements.get_list()
        return render_template("remove_announcement.html", list=announcementlist)

    if request.method == "POST":
        users.check_csrf()

        if "announcement" in request.form:
            announcement_id = request.form["announcement"]  # Corrected variable name
            announcements.remove_announcement(announcement_id)
            
    return redirect("/")
     
        
