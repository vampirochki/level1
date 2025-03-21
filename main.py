from PyQt5.QtWidgets import QApplication
app = QApplication([])


from main_window import *
from menu_window import *
from random import choice , shuffle
from time import sleep
class Question:
    def __init__(self, question, answer, wrong_answer_1,wrong_answer_2,wrong_answer_3):
        self.question = question
        self.answer = answer
        self.wrong_answer_1 = wrong_answer_1
        self.wrong_answer_2 =wrong_answer_2
        self.wrong_answer_3 = wrong_answer_3
        self.count_ask = 0
        self.count_correct = 0

    def got_right(self):
        self.count_ask += 1
        self.count_correct += 1
    def got_wrong(self):
        self.count_ask += 1

q1 = Question('Яблуко', 'apple', 'application', 'pinapple', 'apply')
q2 = Question('Дім', 'house', 'horse', 'hurry', 'hour')
q3 = Question('Миша', 'mouse', 'mouth', 'muse', 'museum')
q4 = Question('Число', 'number', 'digit', 'amount', 'summary')

questions = [q1, q2, q3, q4]

radio_buttons = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def new_question():
    global current_question
    current_question = choice(questions)
    lb_Question.setText(current_question.question)
    lb_Correct.setText(current_question.answer)
    shuffle(radio_buttons)

    radio_buttons[0].setText(current_question.wrong_answer_1)
    radio_buttons[1].setText(current_question.wrong_answer_2)
    radio_buttons[2].setText(current_question.wrong_answer_3)
    radio_buttons[3].setText(current_question.answer) #ПРАВИЛЬНА ВІДПОВІДЬ!!!


def check():
    RadioGroup.setExclusive(False)
    for answe in radio_buttons:
        if answe.isChecked():
            if answe.text() == lb_Correct.text():
                current_question.got_right()
                lb_Result.setText("Вірно!")
                answe.setChecked(False)
            else:
                lb_Result.setText("Не вірно!")
                current_question.got_wrong()
                answe.setChecked(False)
    RadioGroup.setExclusive(True)
    print(current_question.count_ask)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText("Наступне питання")
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def show_question():   
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText("Відповісти")

def rest():
    main_window.hide()
    n = box_Minutes.value()
    sleep(n)
    main_window.show()

def switch_screen():
    if btn_OK.text() == "Відповісти":
        check()
        show_result()
    else:
        new_question()
        show_question()

new_question()
btn_OK.clicked.connect(switch_screen)
btn_Sleep.clicked.connect(rest)

main_window.show()
app.exec_()