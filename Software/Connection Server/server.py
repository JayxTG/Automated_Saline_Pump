"""
Author: Jayamadu Gammune

This script implements a Hole Centering Tool using computer vision techniques.
It detects circular shapes (holes) from a webcam feed and provides visual feedback
to align these holes with a crosshair displayed on the screen.

Permission is hereby granted, free of charge, to any person obtaining a copy of 
this software and associated documentation files (the "Software"), to deal in 
the Software without restriction, including without limitation the rights to 
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies 
of the Software, and to permit persons to whom the Software is furnished to do 
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all 
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
SOFTWARE.
"""

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
