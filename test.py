import tkinter as tk
from tkinter import ttk

# -------------------- QUIZ DATA -------------------- #

QUIZ = {
    "Easy": {
        "Round1": [
            ("Which prints a string?", ["print(10)", 'print("hi")', "print(True)", "print(4.5)"], 'print("hi")'),
            ("Immutable data type?", ["List", "Set", "String", "Dict"], "String"),
            ("Mutable data type?", ["Tuple", "Int", "String", "Dictionary"], "Dictionary"),
            ("// operator does?", ["Division", "Remove decimal", "Multiply", "Add"], "Remove decimal"),
            ("Variables are?", ["Fixed", "Unknown values", "Only int", "Only str"], "Unknown values"),
            ("Correct string input?", ['x = input("name")', 'x = int("name")', 'input=x()', 'print(input)'], 'x = input("name")'),
            ("Used after if?", ["else", "elif", "repeat", "loop"], "elif"),
        ],
        "Round2": [
            ("Python file extension?", [".pt", ".pyt", ".py", ".python"], ".py"),
            ("Boolean values?", ["Yes/No", "1/0", "True/False", "On/Off"], "True/False"),
            ("Used for comments?", ["//", "#", "/* */", "--"], "#"),
            ("Keyword for loop?", ["repeat", "loop", "for", "iterate"], "for"),
            ("len() gives?", ["Type", "Length", "Value", "Index"], "Length"),
            ("print() is a?", ["Variable", "Function", "Loop", "Module"], "Function"),
            ("Python is?", ["Low-level", "Machine code", "High-level", "Binary"], "High-level"),
        ]
    },

    "Medium": {
        "Round1": [
            ("Which is NOT a data type?", ["List", "Tuple", "Loop", "Set"], "Loop"),
            ("Index starts from?", ["1", "0", "-1", "Any"], "0"),
            ("Which is mutable?", ["Tuple", "String", "List", "Int"], "List"),
            ("Used to define function?", ["def", "fun", "define", "func"], "def"),
            ("Logical AND?", ["&&", "and", "&", "AND"], "and"),
            ("Correct comparison?", ["=", "==", "!=", "<>"], "=="),
            ("Range example?", ["range(5)", "range[5]", "range{5}", "range<5>"], "range(5)"),
        ],
        "Round2": [
            ("Python creator?", ["Dennis Ritchie", "Guido van Rossum", "James Gosling", "Elon Musk"], "Guido van Rossum"),
            ("PEP stands for?", ["Python Easy Program", "Python Enhancement Proposal", "Program Execution Plan", "Python Entry Point"], "Python Enhancement Proposal"),
            ("Python released in?", ["1989", "1991", "1999", "2005"], "1991"),
            ("IDLE is?", ["Editor", "Compiler", "OS", "Browser"], "Editor"),
            ("Used to handle errors?", ["try-except", "if-else", "loop", "break"], "try-except"),
            ("List method?", ["add()", "append()", "push()", "insert()"], "append()"),
            ("Tuple is?", ["Mutable", "Immutable", "Dynamic", "Editable"], "Immutable"),
        ]
    },

    "Hard": {
        "Round1": [
            ("Time complexity of binary search?", ["O(n)", "O(log n)", "O(n²)", "O(1)"], "O(log n)"),
            ("Lambda is?", ["Loop", "Anonymous function", "Module", "Class"], "Anonymous function"),
            ("Which creates generator?", ["[]", "{}", "()", "yield"], "yield"),
            ("Global keyword does?", ["Delete var", "Access global var", "Create class", "Exit loop"], "Access global var"),
            ("__init__ is?", ["Destructor", "Constructor", "Function", "Variable"], "Constructor"),
            ("PEP 8 is?", ["Library", "Style guide", "Compiler", "Framework"], "Style guide"),
            ("is vs ==", ["Same", "Identity vs value", "Assignment", "Loop"], "Identity vs value"),
        ],
        "Round2": [
            ("Python uses which GC?", ["Manual", "Reference counting", "Mark & sweep", "None"], "Reference counting"),
            ("Virtualenv is for?", ["Speed", "Isolation", "Debugging", "GUI"], "Isolation"),
            ("__name__ == '__main__' means?", ["Importing", "Running directly", "Error", "Loop"], "Running directly"),
            ("Decorators are?", ["Loops", "Functions modifying functions", "Classes", "Variables"], "Functions modifying functions"),
            ("List comprehension returns?", ["Tuple", "Set", "List", "Dict"], "List"),
            ("GIL affects?", ["Memory", "Threads", "Files", "Syntax"], "Threads"),
            ("Python typing module gives?", ["Speed", "Hints", "Errors", "Loops"], "Hints"),
        ]
    }
}

TIME_LIMIT = 60

# -------------------- APP -------------------- #

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Quiz")
        self.root.configure(bg="#eef4ff")

        # Fullscreen
        self.root.attributes("-fullscreen", True)
        self.root.bind("<Escape>", lambda e: self.root.attributes("-fullscreen", False))

        self.frame = tk.Frame(root, bg="#eef4ff")
        self.frame.pack(fill="both", expand=True)

        # Robot pointer with arrow
        self.robot = tk.Label(self.frame, text="🤖👉", font=("Arial", 22), bg="#eef4ff")
        self.robot.place_forget()

        self.show_menu()

    def clear(self):
        for w in self.frame.winfo_children():
            if w != self.robot:
                w.destroy()

    # ---------------- MENU ---------------- #

    def show_menu(self):
        self.clear()
        tk.Label(self.frame, text="PYTHON QUIZ", font=("Arial", 36, "bold"), bg="#eef4ff").pack(pady=50)

        for level in QUIZ:
            btn = tk.Button(
                self.frame, text=level, font=("Arial", 22, "bold"),
                bg="#6aa9ff", fg="black", width=25,
                activebackground="#ffeb3b",
                command=lambda l=level: self.start_round(l, "Round1")
            )
            btn.pack(pady=20)
            btn.bind("<Enter>", lambda e, b=btn: self.on_hover(b))
            btn.bind("<Leave>", lambda e: self.robot.place_forget())

    def on_hover(self, button):
        # Robot points left of button vertically centered
        x = button.winfo_x() - 80
        y = button.winfo_y() + button.winfo_height()//4
        self.robot.place(x=x, y=y)

    # ---------------- QUIZ ---------------- #

    def start_round(self, level, round_name):
        self.level = level
        self.round = round_name
        self.questions = QUIZ[level][round_name]
        self.q_index = 0
        self.score = 0
        self.time_left = TIME_LIMIT

        self.clear()

        self.timer_label = tk.Label(self.frame, font=("Arial", 22), bg="#eef4ff")
        self.timer_label.pack(pady=15)

        self.progress = ttk.Progressbar(self.frame, length=600, maximum=7)
        self.progress.pack(pady=15)

        self.q_label = tk.Label(self.frame, font=("Arial", 24), wraplength=1000, bg="#eef4ff")
        self.q_label.pack(pady=25)

        self.buttons = []
        for _ in range(4):
            b = tk.Button(self.frame, font=("Arial", 20, "bold"),
                          bg="white", fg="black", width=40, relief="raised", bd=4)
            b.pack(pady=12)
            b.bind("<Enter>", lambda e, btn=b: self.on_hover(btn))
            b.bind("<Leave>", lambda e: self.robot.place_forget())
            self.buttons.append(b)

        self.feedback = tk.Label(self.frame, font=("Arial", 20), bg="#eef4ff")
        self.feedback.pack(pady=20)

        self.load_question()
        self.update_timer()

    def load_question(self):
        if self.q_index == 7:
            self.end_round()
            return

        q, opts, ans = self.questions[self.q_index]
        self.correct = ans

        self.q_label.config(text=f"Q{self.q_index + 1}. {q}")
        self.progress["value"] = self.q_index

        for i, opt in enumerate(opts):
            self.buttons[i].config(
                text=opt,
                command=lambda o=opt: self.check_answer(o)
            )

        self.feedback.config(text="")

    def check_answer(self, choice):
        if choice == self.correct:
            self.score += 1
            self.feedback.config(text="Correct ✅", fg="green")
        else:
            self.feedback.config(text=f"Incorrect ❌ Correct: {self.correct}", fg="red")

        self.root.after(1000, self.next_question)

    def next_question(self):
        self.q_index += 1
        self.load_question()

    def update_timer(self):
        self.timer_label.config(text=f"Time left: {self.time_left}s")
        if self.time_left > 0:
            self.time_left -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.end_round()

    # ---------------- END ROUND ---------------- #

    def end_round(self):
        self.clear()
        tk.Label(self.frame, text=f"Score: {self.score}/7",
                 font=("Arial", 26, "bold"), bg="#eef4ff").pack(pady=25)

        if self.round == "Round1" and self.score >= 5:
            tk.Label(self.frame, text="🎉 Congratulations!\nYou entered Round 2",
                     font=("Arial", 22, "bold"), bg="#eef4ff").pack(pady=20)
            tk.Button(self.frame, text="Continue to Round 2",
                      font=("Arial", 22, "bold"), bg="#6aa9ff", fg="black",
                      command=lambda: self.start_round(self.level, "Round2")).pack(pady=15)
        else:
            tk.Button(self.frame, text="Restart Quiz",
                      font=("Arial", 22, "bold"), bg="#ff9999", fg="black",
                      command=self.show_menu).pack(pady=15)

# ---------------- RUN ---------------- #

root = tk.Tk()
QuizApp(root)
root.mainloop()



