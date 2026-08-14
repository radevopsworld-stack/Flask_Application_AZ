from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory "database" — just a Python dictionary.
# Key = username, Value = password
# NOTE: This resets every time the server restarts (that's expected for this assignment).
users = {}


@app.route("/add", methods=["POST"])
def add_user():
    # Step 1: Parse the incoming JSON body sent by the client.
    # silent=True means: if the body isn't valid JSON, return None instead of crashing.
    data = request.get_json(silent=True)

    # Step 2: Validate that we actually got JSON, and that it has the fields we need.
    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Request must include 'username' and 'password' fields"}), 400

    username = data["username"]
    password = data["password"]

    # Step 3: Store it in our in-memory dictionary.
    users[username] = password

    # Step 4: Confirm success back to the client.
    return jsonify({"message": f"User '{username}' added successfully"}), 201


@app.route("/get/<username>", methods=["GET"])
def get_password(username):
    # Step 1: Check if the username exists in our dictionary.
    if username not in users:
        # Step 2: If not, return a proper 404 error — don't just crash or return blank.
        return jsonify({"error": f"Username '{username}' not found"}), 404

    # Step 3: If it exists, return the password.
    return jsonify({"username": username, "password": users[username]}), 200


if __name__ == "__main__":
    # debug=True auto-reloads the server when you save changes — helpful while developing.
    app.run(debug=True)