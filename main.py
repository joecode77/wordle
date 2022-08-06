from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QMessageBox, QRadioButton)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QSize
from backend import Backend
import sys

class WordleInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.wordle_backend = Backend()
        self.initializeUI()
        self.create_central_widget()
        self.set_layout()
        self.display_word()
        self.display_keypad()
        self.create_title_bar()
        
        self.show()

    def initializeUI(self):
        self.setWindowTitle("Wordle")
        
        self.resize(500, 500)

    def display_word(self):
        self.display_00 = QLineEdit(self.wordle_backend.BOARD[0][0]['value'])
        self.display_01 = QLineEdit(self.wordle_backend.BOARD[0][1]['value'])
        self.display_02 = QLineEdit(self.wordle_backend.BOARD[0][2]['value'])
        self.display_03 = QLineEdit(self.wordle_backend.BOARD[0][3]['value'])
        self.display_04 = QLineEdit(self.wordle_backend.BOARD[0][4]['value'])
        self.display_10 = QLineEdit(self.wordle_backend.BOARD[1][0]['value'])
        self.display_11 = QLineEdit(self.wordle_backend.BOARD[1][1]['value'])
        self.display_12 = QLineEdit(self.wordle_backend.BOARD[1][2]['value'])
        self.display_13 = QLineEdit(self.wordle_backend.BOARD[1][3]['value'])
        self.display_14 = QLineEdit(self.wordle_backend.BOARD[1][4]['value'])
        self.display_20 = QLineEdit(self.wordle_backend.BOARD[2][0]['value'])
        self.display_21 = QLineEdit(self.wordle_backend.BOARD[2][1]['value'])
        self.display_22 = QLineEdit(self.wordle_backend.BOARD[2][2]['value'])
        self.display_23 = QLineEdit(self.wordle_backend.BOARD[2][3]['value'])
        self.display_24 = QLineEdit(self.wordle_backend.BOARD[2][4]['value'])
        self.display_30 = QLineEdit(self.wordle_backend.BOARD[3][0]['value'])
        self.display_31 = QLineEdit(self.wordle_backend.BOARD[3][1]['value'])
        self.display_32 = QLineEdit(self.wordle_backend.BOARD[3][2]['value'])
        self.display_33 = QLineEdit(self.wordle_backend.BOARD[3][3]['value'])
        self.display_34 = QLineEdit(self.wordle_backend.BOARD[3][4]['value'])
        self.display_40 = QLineEdit(self.wordle_backend.BOARD[4][0]['value'])
        self.display_41 = QLineEdit(self.wordle_backend.BOARD[4][1]['value'])
        self.display_42 = QLineEdit(self.wordle_backend.BOARD[4][2]['value'])
        self.display_43 = QLineEdit(self.wordle_backend.BOARD[4][3]['value'])
        self.display_44 = QLineEdit(self.wordle_backend.BOARD[4][4]['value'])
        self.display_50 = QLineEdit(self.wordle_backend.BOARD[5][0]['value'])
        self.display_51 = QLineEdit(self.wordle_backend.BOARD[5][1]['value'])
        self.display_52 = QLineEdit(self.wordle_backend.BOARD[5][2]['value'])
        self.display_53 = QLineEdit(self.wordle_backend.BOARD[5][3]['value'])
        self.display_54 = QLineEdit(self.wordle_backend.BOARD[5][4]['value'])

        for x in range(6):
            for y in range(5):
                eval(f"self.display_{x}{y}").setFont(QFont('helvetica', 22))
                eval(f"self.display_{x}{y}").setMaxLength(1)
                eval(f"self.display_{x}{y}").setAlignment(Qt.AlignCenter)

        for x in range(6):
            for y in range(5):
                eval(f"self.display_{x}{y}").setStyleSheet(f"color:white; border:1px solid #3a3a3c; background-color:{self.wordle_backend.board_box_color};")
  
        for count in range (6):
            for x in range(6):
                for y in range(5):
                    eval(f"self.board_row{x}_display").addWidget(eval(f"self.display_{x}{y}"))


    def display_keypad(self):
       
        self.button_00 = QPushButton()
        self.button_01 = QPushButton()
        self.button_02 = QPushButton()
        self.button_03 = QPushButton()
        self.button_04 = QPushButton()
        self.button_05 = QPushButton()
        self.button_06 = QPushButton()
        self.button_07 = QPushButton()
        self.button_08 = QPushButton()
        self.button_09 = QPushButton()
        self.button_10 = QPushButton()
        self.button_11 = QPushButton()
        self.button_12 = QPushButton()
        self.button_13 = QPushButton()
        self.button_14 = QPushButton()
        self.button_15 = QPushButton()
        self.button_16 = QPushButton()
        self.button_17 = QPushButton()
        self.button_18 = QPushButton()
        self.button_20 = QPushButton()
        self.button_21 = QPushButton()
        self.button_22 = QPushButton()
        self.button_23 = QPushButton()
        self.button_24 = QPushButton()
        self.button_25 = QPushButton()
        self.button_26 = QPushButton()
        self.button_27 = QPushButton()
        self.button_28 = QPushButton()
        
        length_of_columns = [10, 9, 9]
        keys = self.wordle_backend.KEYS

        for i in range(3):
            
            keypad_layout = eval(f"self.keypad_row{i}")
            keypad_layout.addStretch()

            
            for column in range(length_of_columns[i]):
                
                if keys[i][column]['value'] != '':
                    
                    button_text = keys[i][column]['value']
                    button_color = keys[i][column]['color']

                    button = eval(f"self.button_{i}{column}")
                    button.setText(button_text)
                    button.setStyleSheet(f'color:#eeeeee; background-color:{button_color}; border-radius:5px;')
                else:
                    
                    button_text = keys[i][column]['value']
                    button_color = keys[i][column]['color']

                    button = eval(f"self.button_{i}{column}")
                    button.setText(button_text)
                    button.setIcon(QIcon('icons/backspace.png'))
                    button.setIconSize(QSize(30, 30))
                    button.setStyleSheet(f'color:#eeeeee; background-color:{button_color}; border-radius:5px;')

                button.clicked.connect(self.button_clicked)

                button.setFont(QFont('helvetica', 15))
                keypad_layout.addWidget(button)

                
            keypad_layout.addStretch()
        
    
    def refresh_board(self):
        theme = self.wordle_backend.THEME
        for x in range(6):
            for y in range(5):
                eval(f"self.display_{x}{y}").setText(self.wordle_backend.BOARD[x][y]['value'].upper())
                if self.wordle_backend.BOARD[x][y]['color'] == "#121213" or self.wordle_backend.BOARD[x][y]['color'] == "#ffffff":
                    eval(f"self.display_{x}{y}").setStyleSheet(f"color:{'white' if theme == 'DARK' else 'black'}; border:{'1px solid #3a3a3c' if theme == 'DARK' else '1px solid #d2d5d9'}; background-color:{self.wordle_backend.board_box_color};")
                else:
                    eval(f"self.display_{x}{y}").setStyleSheet(f"color:{'white' if theme == 'DARK' else 'black'}; border:{'1px solid #3a3a3c' if theme == 'DARK' else '1px solid #d2d5d9'}; background-color:{self.wordle_backend.BOARD[x][y]['color']};")


    def refresh_keypad(self):
        length_of_columns = [10, 9, 9]
        keys = self.wordle_backend.KEYS
        for row in range(3):
            for column in range(length_of_columns[row]):
                button_color = keys[row][column]['color']
                button = eval(f"self.button_{row}{column}")
                button.setStyleSheet(f'color:#eeeeee; background-color:{button_color}; border-radius:5px;')



    def create_central_widget(self):
        self.widget = QWidget()
        self.setCentralWidget(self.widget)

    def create_title_bar(self):
        self.title = QLabel('Wordle')
        self.title.setFont(QFont('sans-serif', 16))

        self.dark_rad_button = QRadioButton("Dark Mode")
        self.light_rad_button = QRadioButton("Light Mode")
        self.dark_rad_button.toggled.connect(self.changeTheme)
        self.dark_rad_button.setChecked(True)

        
        self.light_rad_button.toggled.connect(self.changeTheme)
        self.dark_rad_button.toggled.connect(self.changeTheme)

        self.title_layout.addWidget(self.dark_rad_button)
        self.title_layout.addWidget(self.light_rad_button)
        self.title_layout.addStretch(2)
        self.title_layout.addWidget(self.title)
        self.title_layout.addStretch(3)

        
    
    def set_layout(self):
        self.main_layout = QVBoxLayout()
        self.widget.setLayout(self.main_layout)

        self.title_layout = QHBoxLayout()
        
        self.board_wrap_layout = QHBoxLayout()
        self.board_display_layout = QVBoxLayout()
        self.board_row0_display = QHBoxLayout()
        self.board_row1_display = QHBoxLayout()
        self.board_row2_display = QHBoxLayout()
        self.board_row3_display = QHBoxLayout()
        self.board_row4_display = QHBoxLayout()
        self.board_row5_display = QHBoxLayout()

        self.board_display_layout.addStretch()
        self.board_display_layout.addLayout(self.board_row0_display)
        self.board_display_layout.addLayout(self.board_row1_display)
        self.board_display_layout.addLayout(self.board_row2_display)
        self.board_display_layout.addLayout(self.board_row3_display)
        self.board_display_layout.addLayout(self.board_row4_display)
        self.board_display_layout.addLayout(self.board_row5_display)
        self.board_display_layout.addStretch()
        
        self.board_wrap_layout.addStretch()
        self.board_wrap_layout.addLayout(self.board_display_layout)
        self.board_wrap_layout.addStretch()



        self.keypad_wrap_layout = QHBoxLayout()
        self.keypad_display_layout = QVBoxLayout()
        self.keypad_row0 = QHBoxLayout()
        self.keypad_row1 = QHBoxLayout()
        self.keypad_row2 = QHBoxLayout()

        self.keypad_wrap_layout.addLayout(self.keypad_display_layout)

        self.keypad_display_layout.addLayout(self.keypad_row0)
        self.keypad_display_layout.addLayout(self.keypad_row1)
        self.keypad_display_layout.addLayout(self.keypad_row2)
        
        self.main_layout.addLayout(self.title_layout)
        self.main_layout.addLayout(self.board_wrap_layout)
        self.main_layout.addLayout(self.keypad_wrap_layout)

    def button_clicked(self):
        sender = self.sender()
        text = sender.text()

        result = self.wordle_backend.button_clicked(text)
        if result == 'INCOMPLETE':
            QMessageBox().information(self, "Incomplete Input", "Not Enough letters", QMessageBox.Ok)
        elif result == 'INEXISTENT':
            QMessageBox().information(self, "", "Not in word lint", QMessageBox.Ok)

        self.refresh_board()
        self.refresh_keypad()

        check_win = self.wordle_backend.check_win()

        if check_win:
            replay = QMessageBox().question(self, "Win!!!", "Congratulations!!! You have won the game\nDo you wish to play again?", QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)
            if replay == QMessageBox.Yes:
                self.close()
                self.window = WordleInterface()
                self.window.show()
            else:
                self.close()

    def changeTheme(self):
        if self.dark_rad_button.isChecked():
            self.wordle_backend.THEME = 'DARK'
            self.setStyleSheet("background-color:#121213; color:white;")
            self.title.setStyleSheet("color:white;")
            self.light_rad_button.setStyleSheet('color:white;')   
            self.dark_rad_button.setStyleSheet('color:white;') 
            self.wordle_backend.board_box_color = "#121213"
            self.refresh_board()

        elif self.light_rad_button.isChecked():
            self.wordle_backend.THEME = 'LIGHT'
            self.setStyleSheet("color:black; background-color:#ffffff;")  
            self.light_rad_button.setStyleSheet('color:black;')   
            self.dark_rad_button.setStyleSheet('color:black;') 
            self.title.setStyleSheet('color:black;')
            self.wordle_backend.board_box_color = "#ffffff;"
            self.refresh_board()
                

    
styleSheet = """

QLineEdit{
    padding:25px 0px 25px 0px;
    padding-top:25px;
    padding-bottom:25px;
    padding-left:0px;
    padding-right:0px;

    font:bold;
}

QPushButton{
    padding:auto;
}

QPushButton#menu_button{
    padding:0px;
    border:0px sol;
}

QWidget{
    background-color:#121213;
    color:white;
}

"""


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WordleInterface()
    app.setStyleSheet(styleSheet)
    app.exec_()