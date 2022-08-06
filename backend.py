import random
class Backend:
    def __init__(self):
        self.THEME = 'DARK'
        if self.THEME == 'DARK':
            self.board_box_color = "#121213"
        else:
            self.board_box_color = "#ffffff"


        
        self.BOARD = [
                [{'value':'', 'color': self.board_box_color}, {'value':'', 'color': self.board_box_color}, {'value':'', 'color': self.board_box_color}, {'value':'', 'color': self.board_box_color}, {'value':'', 'color': self.board_box_color}], 
                [{'value':'', 'color': self.board_box_color}, {'value':'', 'color': self.board_box_color}, {'value':'', 'color': self.board_box_color}, {'value':'', 'color': self.board_box_color}, {'value':'', 'color': self.board_box_color}], 
                [{'value':'', 'color': self.board_box_color}, {'value':'', 'color': self.board_box_color}, {'value':'', 'color': self.board_box_color}, {'value':'', 'color': self.board_box_color}, {'value':'', 'color': self.board_box_color}], 
                [{'value':'', 'color': self.board_box_color}, {'value':'', 'color': self.board_box_color}, {'value':'', 'color': self.board_box_color}, {'value':'', 'color': self.board_box_color}, {'value':'', 'color': self.board_box_color}], 
                [{'value':'', 'color': self.board_box_color}, {'value':'', 'color': self.board_box_color}, {'value':'', 'color': self.board_box_color}, {'value':'', 'color': self.board_box_color}, {'value':'', 'color': self.board_box_color}], 
                [{'value':'', 'color': self.board_box_color}, {'value':'', 'color': self.board_box_color}, {'value':'', 'color': self.board_box_color}, {'value':'', 'color': self.board_box_color}, {'value':'', 'color': self.board_box_color}], 
                ]

        self.KEYS = [[{'value':'Q', 'color': '#818384'}, {'value':'W', 'color': '#818384'}, {'value':'E', 'color': '#818384'},{'value':'R', 'color': '#818384'}, {'value':'T', 'color': '#818384'}, {'value':'Y', 'color': '#818384'}, {'value':'U', 'color': '#818384'}, {'value':'I', 'color': '#818384'}, {'value':'O', 'color': '#818384'}, {'value':'P', 'color': '#818384'}],
                [{'value':'A', 'color': '#818384'}, {'value':'S', 'color': '#818384'}, {'value':'D', 'color': '#818384'},{'value':'F', 'color': '#818384'}, {'value':'G', 'color': '#818384'}, {'value':'H', 'color': '#818384'}, {'value':'J', 'color': '#818384'}, {'value':'K', 'color': '#818384'}, {'value':'L', 'color': '#818384'}],
                [{'value':'ENTER', 'color': '#818384'}, {'value':'Z', 'color': '#818384'}, {'value':'X', 'color': '#818384'},{'value':'C', 'color': '#818384'}, {'value':'V', 'color': '#818384'}, {'value':'B', 'color': '#818384'}, {'value':'N', 'color': '#818384'}, {'value':'M', 'color': '#818384'}, {'value':'', 'color': '#818384'},],
                ]
        self.INVERTED_INDEX = {}
        

        length_of_column = [10, 9, 9]
        for x in range(3):
            for y in range(length_of_column[x]):
                self.INVERTED_INDEX[self.KEYS[x][y]['value'].upper()] = (x, y)


        

        self.active_row = 0
        self.active_column = 0
        self.WORD_FILE_PATH = 'dictionary.txt'
        self.input_word = ""
        self.score = 0
        
        self.get_wordle_word(self.WORD_FILE_PATH )

    def get_wordle_word(self, wordle_file):
        with open(wordle_file, 'r') as f:  
            word_list = f.read().split()   
            self.WORD_LIST = word_list          
            self.WORDLE_WORD = random.choice(word_list)
            print(self.WORDLE_WORD)
            



    def button_clicked(self, letter):
        if letter != 'ENTER' and letter != '' and self.active_row < 6:
            if self.active_column < 5:
                
                self.BOARD[self.active_row][self.active_column]['value'] = letter.lower()
                self.input_word+= letter
                self.active_column += 1

        elif letter == '':
            if self.active_column > 0:

                self.active_column -= 1
                self.BOARD[self.active_row][self.active_column] = {'value':'', 'color': '#121213'}
                self.input_word = self.input_word[:len(self.input_word)-1]
        
        elif letter == 'ENTER':
            if len(self.input_word) != 5:
                return 'INCOMPLETE'

            elif self.input_word.lower() not in self.WORD_LIST:
                return 'INEXISTENT'

            else:
                wordle_split_word = []
                for i in self.WORDLE_WORD:
                    wordle_split_word.append(i.lower())
                input_split_word = []
                for i in self.input_word:
                    input_split_word.append(i.lower())

                check_row = 0
                check_column = 0

                for column in range(5):
                    current_input_letter = input_split_word[column]
                    index = self.INVERTED_INDEX[input_split_word[column].upper()]

                    if self.BOARD[self.active_row][column]['value'] == wordle_split_word[column]:
                        self.BOARD[self.active_row][column] = {'value':f'{current_input_letter}', 'color': '#538d4e'}

                        self.KEYS[index[0]][index[1]] = {'value':f'{current_input_letter}', 'color': '#538d4e'}
                        
                        self.score += 1

                    elif self.BOARD[self.active_row][column]['value'] in wordle_split_word:
                        self.BOARD[self.active_row][column] = {'value':f'{current_input_letter}', 'color': '#b59f3b'}

                        self.KEYS[index[0]][index[1]] = {'value':f'{current_input_letter}', 'color': '#b59f3b'}

                        self.score = 0

                    else:
                        self.BOARD[self.active_row][column] = {'value':f'{current_input_letter}', 'color': '#3a3a3c'}

                        self.KEYS[index[0]][index[1]] = {'value':f'{current_input_letter}', 'color': '#3a3a3c'}

                        self.score = 0

                if self.active_row < 6:
                    self.input_word = ""
                    self.active_row += 1
                    self.active_column = 0

    def check_win(self):
        if self.score == 5:
            return True
