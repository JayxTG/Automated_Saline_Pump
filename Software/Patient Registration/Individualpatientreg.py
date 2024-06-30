import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QDialog, QLineEdit, QComboBox
from PyQt5.QtGui import QIcon  # Import QIcon from PyQt5.QtGui

import serial

class BedWidget(QWidget):
    def __init__(self, bed_number):
        super().__init__()
        self.bed_number = bed_number
        self.initUI()

    def initUI(self):
        # Create labels for bed information
        bed_label = QLabel(f"Bed {self.bed_number}")
        name_label = QLabel("Name:")
        age_label = QLabel("Age:")
        gender_label = QLabel("Gender:")
        saline_rate_label = QLabel("Saline Flow Rate:")
        bottle_level_label = QLabel("Saline Bottle Level:")
        bottle_count_label = QLabel("Number of Saline Bottles:")

        # Create buttons for bed registration
        register_button = QPushButton("Register Patient")
        register_button.clicked.connect(self.openRegistrationWindow)

        # Create button for updating number of saline bottles
        update_button = QPushButton("Update Bottles")
        update_button.clicked.connect(self.openUpdateBottlesWindow)  # Connect the button to open the update bottles window

        # Create layout for bed widget
        layout = QVBoxLayout()
        layout.addWidget(bed_label)
        layout.addWidget(name_label)
        layout.addWidget(age_label)
        layout.addWidget(gender_label)
        layout.addWidget(saline_rate_label)
        layout.addWidget(bottle_level_label)
        layout.addWidget(bottle_count_label)
        layout.addWidget(register_button)
        layout.addWidget(update_button)

        self.setLayout(layout)

    def openRegistrationWindow(self):
        registration_window = RegistrationWindow(self)
        if registration_window.exec_() == QDialog.Accepted:
            name = registration_window.nameLineEdit.text()
            age = registration_window.ageLineEdit.text()
            gender = registration_window.genderComboBox.currentText()
            # Update the bed widget with the submitted details
            self.updateDetails(name, age, gender)
            self.resetBottles()  # Reset the number of bottles to 0

    def updateDetails(self, name, age, gender):
        # Update the labels with the submitted details
        self.layout().itemAt(1).widget().setText(f"Name: {name}")
        self.layout().itemAt(2).widget().setText(f"Age: {age}")
        self.layout().itemAt(3).widget().setText(f"Gender: {gender}")

    def openUpdateBottlesWindow(self):
        update_bottles_window = UpdateBottlesWindow(self)  # Open the update bottles window
        update_bottles_window.exec_()

    def resetDetails(self):
        # Reset the labels to their initial values
        self.layout().itemAt(1).widget().setText("Name:")
        self.layout().itemAt(2).widget().setText("Age:")
        self.layout().itemAt(3).widget().setText("Gender:")

    def resetBottles(self):
        # Reset the number of saline bottles to 0
        self.layout().itemAt(6).widget().setText("Number of Saline Bottles: 0")

class RegistrationWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Patient Registration")
        self.initUI()

    def initUI(self):
        # Create labels and input fields for patient details
        name_label = QLabel("Name:")
        self.nameLineEdit = QLineEdit()
        age_label = QLabel("Age:")
        self.ageLineEdit = QLineEdit()
        gender_label = QLabel("Gender:")
        self.genderComboBox = QComboBox()
        self.genderComboBox.addItems(["Male", "Female"])

        # Create button for submitting registration
        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.accept)

        # Create layout for registration window
        layout = QVBoxLayout()
        layout.addWidget(name_label)
        layout.addWidget(self.nameLineEdit)
        layout.addWidget(age_label)
        layout.addWidget(self.ageLineEdit)
        layout.addWidget(gender_label)
        layout.addWidget(self.genderComboBox)
        layout.addWidget(submit_button)

        self.setLayout(layout)

class UpdateBottlesWindow(QDialog):  # Add a new class for the update bottles window
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Update Bottles")
        self.initUI()

    def initUI(self):
        # Create labels and input field for updating number of bottles
        bottle_count_label = QLabel("Number of Saline Bottles:")
        self.bottle_countLineEdit = QLineEdit()

        # Create button for updating number of bottles
        update_button = QPushButton("Update")
        update_button.clicked.connect(self.updateBottles)

        # Create layout for update bottles window
        layout = QVBoxLayout()
        layout.addWidget(bottle_count_label)
        layout.addWidget(self.bottle_countLineEdit)
        layout.addWidget(update_button)

        self.setLayout(layout)

    def updateBottles(self):
        # Update the number of saline bottles
        bottle_count = self.bottle_countLineEdit.text()
        self.parent().layout().itemAt(6).widget().setText(f"Number of Saline Bottles: {bottle_count}")

class WardWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create layout for ward widget
        layout = QHBoxLayout()

        # Create bed widgets and add them to the layout
        for i in range(1, 9):
            bed_widget = BedWidget(i)
            layout.addWidget(bed_widget)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #app.setWindowIcon(QIcon('c:\Users\jayam\Downloads\Flow Guard.png'))  # Set the app icon
    ward_widget = WardWidget()
    ward_widget.show()
    sys.exit(app.exec_())
