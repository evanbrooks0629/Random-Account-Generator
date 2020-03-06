import sys
from PyQt5.QtWidgets import *
import app


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 1000, 600)
        self.setWindowTitle('Random Account Generator')
        self.UI()

    def UI(self):
        self.numberLabel = QLabel("Input the number of random accounts you want to generate:", self)
        self.numberLabel.move(100, 150)
        self.numberTextbox = QLineEdit(self)
        self.numberTextbox.move(500, 150)
        self.randomLabel = QLabel("Do you want the names to be random?", self)
        self.randomLabel.move(100, 200)
        self.yes = QRadioButton("Yes", self)
        self.yes.move(350, 190)
        self.no = QRadioButton("No", self)
        self.no.move(350, 210)
        self.nameLabel = QLabel("If no, enter your name: ", self)
        self.nameLabel.move(100, 250)
        self.nameTextbox = QLineEdit(self)
        self.nameTextbox.move(270, 250)
        self.emailLabel = QLabel("Enter the email you want to send the accounts to: ", self)
        self.emailLabel.move(100, 300)
        self.emailTextbox = QLineEdit(self)
        self.emailTextbox.move(430, 300)
        button = QPushButton("Generate", self)
        button.move(100, 500)
        button.clicked.connect(self.getValues)
        self.show()

    def getValues(self):
        num = int(self.numberTextbox.text())
        if self.yes.isChecked():
            name = False
            is_rand = True
            all_names = app.random_name_generator(num, is_rand, name)
        else:
            name = self.nameTextbox.text()
            is_rand = False
            all_names = app.random_name_generator(num, is_rand, name)
        client_email = self.emailTextbox.text()
        all_emails = app.random_email_generator(num)
        all_pws = app.random_password_generator(num)
        all_numbers = app.random_number_generator(num)
        fields = ['Name', 'Email', 'Password', 'Phone Number']
        app.write_csv_file(fields, all_names, all_emails, all_pws, all_numbers, client_email)



def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
