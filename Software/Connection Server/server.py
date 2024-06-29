from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__,template_folder='templates')

# Replace with your actual login credentials
USERNAME = "nurse1"
PASSWORD = "012345"

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/auth", methods=["POST"])
def authenticate():
    input_username = request.form["username"]
    input_password = request.form["password"]
    
    if input_username == USERNAME and input_password == PASSWORD:
        return redirect(url_for("control_panel"))
    else:
        return "Authentication failed. Invalid username or password."

@app.route("/control_panel")
def control_panel():
    return render_template("index.html")



# Dictionary mapping board names to their unique identifiers
board_identifiers = {
    "Board 1": "esp32_1",
    "Board 2": "esp32_2",
}

# Function to control the selected board (replace with your logic)
def control_board(board_id):
    # Implement your logic to send commands and control the selected ESP32 board here
    return f"Controlling board: {board_id}"

@app.route('/')
def index():
    return render_template('index.html', boards=board_identifiers.keys())

@app.route('/control', methods=['POST'])
def control():
    selected_board = request.form.get('board')
    result = control_board(board_identifiers[selected_board])
    return result

if __name__ == '__main__':
    app.run(debug=True)