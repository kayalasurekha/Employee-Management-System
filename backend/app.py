from flask import Flask
from routes.employee_routes import employee_bp

app = Flask(__name__)
app.register_blueprint(employee_bp)

@app.route("/")
def home():
    return {"message":"Employee Management API"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


