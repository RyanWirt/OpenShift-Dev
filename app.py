from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = ""
    expr = ""
    if request.method == "POST":
        expr = request.form.get("expr", "")
        button = request.form.get("button", "")
        if button == "C":
            expr = ""
        elif button == "=":
            try:
                # Evaluate the expression safely
                result = str(eval(expr))
                expr = result
            except Exception:
                result = "Error"
                expr = ""
        else:
            expr += button
    return render_template("calculator.html", expr=expr, result=result)

if __name__ == "__main__":
    app.run(debug=True)
