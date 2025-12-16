from flask import Flask, render_template, request
from scraper import scrape_visible_text
from summarizer import WebSummarizer

app = Flask(__name__)
summarizer = WebSummarizer()

@app.route("/", methods=["GET", "POST"])
def index():
    summary = None
    error = None

    if request.method == "POST":
        url = request.form.get("url")

        text = scrape_visible_text(url)

        if text:
            summary = summarizer.summarize(text)
        else:
            error = "Failed to extract text from the URL."

    return render_template("index.html", summary=summary, error=error)

if __name__ == "__main__":
    app.run(debug=True)
