from flask import Flask, render_template, request, jsonify
import pandas as pd
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Load your CSV (adjust path if needed)
internships_df = pd.read_csv("research_internships.csv")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    data = request.get_json()
    user_title = data.get("title", "").strip().lower()

    results = []

    # Use 'Role' instead of 'Title' since your CSV has that column
    for _, row in internships_df.iterrows():
        role = str(row.get("Role", "")).lower()
        if user_title in role:
            results.append({
                "title": row.get("Role", "Unknown"),
                "company": row.get("Company", "Unknown"),
                "location": row.get("Location", "Unknown"),
                "link": row.get("Application", "#")
            })

    return jsonify({"opportunities": results})

if __name__ == "__main__":
    app.run(debug=True)
