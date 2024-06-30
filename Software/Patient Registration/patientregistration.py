import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class RegisterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Patient Registration")
        self.setGeometry(100, 100, 300, 200)

        self.name_label = QLabel("Name:", self)
        self.name_label.move(50, 50)
        self.name_input = QLineEdit(self)
        self.name_input.move(150, 50)

        self.gender_label = QLabel("Gender:", self)
        self.gender_label.move(50, 80)
        self.gender_input = QLineEdit(self)
        self.gender_input.move(150, 80)

        self.age_label = QLabel("Age:", self)
        self.age_label.move(50, 110)
        self.age_input = QLineEdit(self)
        self.age_input.move(150, 110)

        self.bed_label = QLabel("Bed Number:", self)
        self.bed_label.move(50, 140)
        self.bed_input = QLineEdit(self)
        self.bed_input.move(150, 140)

        self.register_button = QPushButton("Register", self)
        self.register_button.move(100, 170)
        self.register_button.clicked.connect(self.register_patient)

    def register_patient(self):
        name = self.name_input.text()
        gender = self.gender_input.text()
        age = self.age_input.text()
        bed_number = self.bed_input.text()

        # Save the patient details to a database or perform any other required actions

        patient_details = {
            1: {"saline_flow_rate": 10, "saline_bottles": 2},
            2: {"saline_flow_rate": 8, "saline_bottles": 3},
            # Add more patient details here
        }
        show_details_window(patient_details)

    def show_details_window(self, details):
        self.close()
        details_window = DetailsWindow(details)
        details_window.show()

class DetailsWindow(QMainWindow):
    def __init__(self, patient_details):
        super().__init__()
        self.setWindowTitle("Patient Details")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()
        for bed, details in patient_details.items():
            label = QLabel(f"Bed Number: {bed}\nSaline Flow Rate: {details['saline_flow_rate']}\nNumber of Saline Bottles: {details['saline_bottles']}")
            layout.addWidget(label)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    register_window = RegisterWindow()
    register_window.show()

    sys.exit(app.exec_())
