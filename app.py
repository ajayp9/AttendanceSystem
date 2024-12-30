from flask import Flask
from tkinter import Tk
from main import Face_Recognition_System  # Assuming main.py is in the same directory

app = Flask(__name__)

# Route for home page
@app.route('/')
def home():
    return 'Welcome to the Flask App! Use the /start-gui route to open the Face Recognition GUI.'

# Route to start the Tkinter GUI
@app.route('/start-gui')
def start_gui():
    print("Starting the Face Recognition GUI...")
    root = Tk()
    app = Face_Recognition_System(root)  # This starts the Tkinter GUI
    root.mainloop()  # Starts Tkinter main loop
    return 'Face Recognition GUI opened.'

if __name__ == '__main__':
    app.run(debug=True)
