from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)

# Load Trained Model
MODEL_PATH = "model/house_model.pkl"

if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
else:
    model = None


def indian_currency(num):
    """
    Convert number to Indian Currency Format
    Example:
    12500000 -> ₹1,25,00,000
    """
    num = int(round(num))

    s = str(num)

    if len(s) <= 3:
        return "₹" + s

    last3 = s[-3:]
    rest = s[:-3]

    parts = []

    while len(rest) > 2:
        parts.insert(0, rest[-2:])
        rest = rest[:-2]

    if rest:
        parts.insert(0, rest)

    return "₹" + ",".join(parts + [last3])


# =========================
# ROUTES
# =========================

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/faq")
def faq():
    return render_template("faq.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")



# ADD THIS HERE
@app.route("/price-trends")
def price_trends():
    return render_template("price_trends.html")


# =========================
# PREDICTION ROUTE
# =========================

@app.route("/predict", methods=["POST"])
def predict():

    if model is None:
        return render_template(
            "result.html",
            prediction="Model not found! Please run train_model.py first."
        )

    try:

        area = float(request.form["area"])
        bedrooms = int(request.form["bedrooms"])
        bathrooms = int(request.form["bathrooms"])

        prediction = model.predict([[area, bedrooms, bathrooms]])[0]

        prediction = max(prediction, 0)

        formatted_price = indian_currency(prediction)

        return render_template(
            "result.html",
            area=area,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            prediction=formatted_price
        )

    except Exception as e:

        return render_template(
            "result.html",
            prediction=f"Error : {e}"
        )


if __name__ == "__main__":
    app.run(debug=True)