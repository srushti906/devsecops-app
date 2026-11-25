from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello DevSecOps v2</h1>"

@app.route("/health")
def health():
    return "ok"

if __name__ == "__main__":
    # 0.0.0.0 is intentionally required for container networking
    app.run(host="0.0.0.0", port=5000, debug=False)  # nosec B104
    AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
