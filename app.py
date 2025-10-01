from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = [length_error, digit_error, uppercase_error, lowercase_error, symbol_error]
    strength = 5 - sum(errors)

    if strength == 5:
        return "✅ Strong Password"
    elif 3 <= strength < 5:
        return "⚠️ Medium Strength Password"
    else:
        return "❌ Weak Password"

# 🔹 Allow GET + POST here
@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        password = request.form["password"]
        result = check_password_strength(password)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
