from flask import Flask, render_template, request

app = Flask(__name__)

# Correct login details
CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "1234"

@app.route("//", methods=["GET", "POST"])
def login():
    error_message = ""
    isHidden = True
    success_message = ""

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
            success_message = "Login Successful!"
        else:
            isHidden = False
            error_message = "Incorrect username or password"

    return render_template(
        "login.html",
        error_message=error_message,
        isHidden=isHidden,
        success_message=success_message
    )

if __name__ == "__main__":
    app.run(debug=True)