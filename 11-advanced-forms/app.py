
from flask import Flask, render_template, request

app = Flask(__name__)



@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        
        student_name = request.form.get("student_name", "").strip()
        email = request.form.get("email", "").strip()
        age = request.form.get("age", "").strip()
        course = request.form.get("course", "").strip()
        study_mode = request.form.get("study_mode", "").strip()

        if not student_name or not email or not age or not course or not study_mode:
            return "Error: Please fill in all required fields.", 400

        if not age.isdigit() or int(age) < 1 or int(age) > 120:
            return "Error: Please enter a valid age.", 400

        phone = request.form.get("phone", "").strip()
        skills = request.form.getlist("skills")



        
        return render_template(
            "result.html",
            student_name=student_name,
            email=email,
            age=int(age),
            phone=phone,
            course=course,
            study_mode=study_mode,
            skills=skills
        )


    return render_template("register.html")



if __name__ == "__main__":
    app.run(debug=True)
