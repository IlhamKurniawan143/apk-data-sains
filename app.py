from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load dataset
dataset = pd.read_csv("dataset.csv")

@app.route('/')
def home():
    return render_template("dataset.html", data=dataset.to_dict(orient="records"), total=len(dataset))

if __name__ == '__main__':
    app.run(debug=True)
