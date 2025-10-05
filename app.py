from flask import Flask, render_template, request, jsonify
import json
import pandas as pd
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

with open("front-end/data/keywords.json") as f:
    keywords_db = json.load(f)

internships_df = pd.read_csv("research_internships.csv")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    data = request.get_json()
    user_title = data.get("title", "").strip().lower()  # User input

    # Get keywords from JSON mapping (case-insensitive)
    keywords = keywords_db.get(user_title.title(), [])  # Maps 'software engineer' -> 'Software Engineer' key

    results = []
    for _, row in internships_df.iterrows():
        # Check if any keyword exists in the CSV title
        if any(kw.lower() in row['Title'].lower() for kw in keywords):
            results.append({
                "title": row['Title'],
                "company": row.get('Company', 'Unknown'),
                "location": row.get('Location', 'Unknown'),
                "link": row.get('Link', '#')
            })

    return jsonify({"keywords": keywords, "opportunities": results})


if __name__ == "__main__":
    app.run(debug=True)
