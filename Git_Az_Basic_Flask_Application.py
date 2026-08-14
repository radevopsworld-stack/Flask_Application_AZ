from flask import Flask # Import the Flask Binaries
app = Flask(__name__)
@app.route("/") # Base Page
def home():
    return "Welcome to Flask Application!" 

@app.route("/health")
def health():
    return "Health App is running!" 
if __name__ == "__main__":
    app.run(debug=True)