from tkinter import *
from tkinter import messagebox as mb
import json

'''
BY IG - @concepts.of.programming 
'''

class Quiz():
    def __init__(self):
        # set question number to 0
        self.q_no = 0

        self.display_title()
        self.display_question()

        self.opt_selected = IntVar()

        # display options for the current question
        self.opts = self.radio_buttons()

        self.display_options()

        self.data_size = len(question)

        self.buttons()

        # no of questions
        self.data_size = len(question)

        # keep a counter of correct answers
        self.correct = 0

    def display_result(self):

        # calculates the wrong count
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"

        # calcultaes the percentage of correct answers
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"

        # Shows a message box to display the result
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")


    def buttons(self):

        # The first button is the Next button to move to the
        # next Question
        next_button = Button(gui, text="Next", command=self.next_btn,
                             width=8, bg="blue", fg="white", font=("ariel", 16, "bold"))

        # palcing the button  on the screen
        next_button.place(x=390, y=380)

        # This is the second button which is used to Quit the GUI
        quit_button = Button(gui, text="Quit", command=gui.destroy,
                             width=5, bg="black", fg="white", font=("ariel", 16, " bold"))

        # placing the Quit button on the screen
        quit_button.place(x=530, y=380)


    def next_btn(self):

        # Check if the answer is correct
        if self.check_ans(self.q_no):
            # if the answer is correct it increments the correct by 1
            self.correct += 1

        # Moves to next Question by incrementing the q_no counter
        self.q_no += 1

        # checks if the q_no size is equal to the data size
        if self.q_no == self.data_size:

            # if it is correct then it displays the score
            self.display_result()

            # destroys the GUI
            gui.destroy()
        else:
            # shows the next question
            self.display_question()
            self.display_options()

    def check_ans(self, q_no):

        # checks for if the selected option is correct
        if self.opt_selected.get() == answer[q_no]:
            # if the option is correct it return true
            return True

    def display_question(self):

        # setting the Quetion properties
        q_no = Label(gui, text=question[self.q_no], width=60,
                     font=('ariel', 16, 'bold'), anchor='w')

        # placing the option on the screen
        q_no.place(x=70, y=170)

    def display_options(self):
        val = 0

        # deselecting the options
        self.opt_selected.set(0)

        # looping over the options to be displayed for the
        # text of the radio buttons.
        for option in options[self.q_no]:
            self.opts[val]['text'] = option
            val += 1

    def display_title(self):

        # The title to be shown
        fm = Frame(gui,background='darkred',border=5)
        fm1 = Frame(fm,background='hotpink',border=0)

        title = Label(fm1, text="PYTHON QUIZ",
                      width=50, height=2, bg="mistyrose", fg="dodgerblue", font=("ariel", 33, "bold"),bd=0)
        # place of the title
        title.pack(padx=10, pady=10)
        fm.pack(padx=0,pady=0)
        fm1.pack(padx=0, pady=0)


    def radio_buttons(self):
        # initialize the list with an empty list of options
        q_list = []

        # position of the first option
        y_pos = 220

        # adding the options to the lis
        while len(q_list) < 4:
            radio_btn = Radiobutton(gui, text=" ", variable=self.opt_selected,
                                    value=len(q_list) + 1, font=("ariel", 14))

            # adding the button to the list
            q_list.append(radio_btn)

            radio_btn.place(x=100, y=y_pos)

            # incrementing the y-axis position by 40
            y_pos += 40

        # return the radio buttons
        return q_list

gui = Tk()
gui.geometry("800x450+240+70")
gui.resizable(0,0)
gui.title("Python Quiz By @concpets.of.programming")
photo = PhotoImage(file = "icon.png")
gui.iconphoto(False, photo)


with open('data1.json') as f:
    data = json.load(f)


question = (data['question'])
options = (data['options'])
answer = (data['answer'])

quiz = Quiz()
gui.mainloop()

'''
BY IG - @concepts.of.programming 
'''
