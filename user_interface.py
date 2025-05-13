import tkinter
from tkinter import Tk, Label, Button, Text, Canvas, PhotoImage
from PIL import Image, ImageTk
from word_generator import SentenceGenerator
from arbiter import Arbiter

MAIN_THEME_COLOR = "#A3E4EF"
GREEN = "#599116"
YELLOW = "#C0A840"
FONT = "Bookman Old Style"



class UI:
    def __init__(self):
        with open("highscores.txt", mode="r") as file:
            lines = file.readlines()
            self.cps = float(lines[0].strip().split(":")[1])
            self.wpm = float(lines[1].strip().split(":")[1])
            self.acc = float(lines[2].strip().split(":")[1])

        self.window = Tk()
        self.window.title("Speedy")
        self.window.config(bg=MAIN_THEME_COLOR)
        icon = PhotoImage(file="data/speed_icon.png")
        self.window.iconphoto(False, icon)

        self.load_main_menu()

    def clear_screen(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def load_main_menu(self):
        self.clear_screen()
        self.status_timer = None
        self.seconds_timer = None
        self.test = None
        self.seconds = 0
        self.logo_display = Canvas(self.window, width=600, height=400, bg=MAIN_THEME_COLOR, borderwidth=0, highlightthickness=0)
        self.logo_display.grid(row=0, column=0, columnspan=2, pady=5)
        self.window.update_idletasks()

        logo = Image.open("data/speedometer.png")

        target_width = 400
        target_height = int(target_width * logo.height / logo.width)

        logo = logo.resize((target_width, target_height), resample=Image.Resampling.LANCZOS)

        logo_tk = ImageTk.PhotoImage(logo)

        self.logo_display.create_image(300, 200, image=logo_tk, anchor="center")

        self.title = Label(self.window, text="Test Your Typing Speed... Ready?", fg="black", bg=MAIN_THEME_COLOR, font=(FONT, 30, "bold"))
        self.title.grid(row=1, column=0, columnspan=2)

        self.start_button = Button(self.window, text="START", font=(FONT, 20, "normal"), fg="white", bg=GREEN, relief="groove", width=10, command=self.load_test_screen)
        self.start_button.grid(row=2, column=0, pady=20)

        self.window.update_idletasks()

        self.info_button = Button(self.window, text="INFO", font=(FONT, 20, "normal"), fg="white", bg=YELLOW, relief="groove", width=10, command=self.load_info_screen)
        self.info_button.grid(row=2, column=1, pady=20)

        self.window.minsize(self.window.winfo_width(), self.window.winfo_height())
        self.window.maxsize(self.window.winfo_width(), self.window.winfo_height())

        self.window.mainloop()



    def load_info_screen(self):
        self.clear_screen()
        self.info_label_1 = Label(self.window,
                                  wraplength=580,
                                  text="GAME INSTRUCTIONS:",
                                  font=(FONT, 15, "bold"),
                                  bg=MAIN_THEME_COLOR,
                                  fg="black",
                                  justify="left",
                                  )
        self.info_label_1.grid(row=0, column=0, sticky="w", padx=10, pady=5)

        self.info_label_2 = Label(self.window,
                                  wraplength=580,
                                  text="Make sure you have an internet connection. The game requires an internet connection to generate your test.",
                                  font=(FONT, 11, "normal"),
                                  bg=MAIN_THEME_COLOR,
                                  fg="black",
                                  justify="left"
                                  )
        self.info_label_2.grid(row=1, column=0, sticky="w", padx=10, pady=5)

        self.info_label_3 = Label(self.window,
                                  wraplength=580,
                                  text="Once you click the 'START' button, your test will be generated, and the 'START TEST' button will be activated. Once you click the 'START TEST' button, a group of words will appear and a text area for your input will be activated.",
                                  font=(FONT, 11, "normal"),
                                  bg=MAIN_THEME_COLOR,
                                  fg="black",
                                  justify="left"
                                  )
        self.info_label_3.grid(row=2, column=0, sticky="w", padx=10, pady=5)

        self.info_label_4 = Label(self.window,
                                  wraplength=580,
                                  text="As soon as this happens, a counter will begin counting the time in seconds. Type the words you see exactly (with a space after each word), and once you are done, press ENTER on your keyboard.",
                                  font=(FONT, 11, "normal"),
                                  bg=MAIN_THEME_COLOR,
                                  fg="black",
                                  justify="left"
                                  )
        self.info_label_4.grid(row=3, column=0, sticky="w", padx=10, pady=5)

        self.info_label_5 = Label(self.window,
                                  wraplength=580,
                                  text="Finally, your scores will be calculated and shown. Click on 'NEW TEST' to start a new test, or 'MAIN MENU' to go back to main menu.",
                                  font=(FONT, 11, "normal"),
                                  bg=MAIN_THEME_COLOR,
                                  fg="black",
                                  justify="left"
                                  )
        self.info_label_5.grid(row=4, column=0, sticky="w", padx=10, pady=5)

        self.i_understand = Button(self.window, text="I UNDERSTAND", font=(FONT, 15, "normal"), bg=YELLOW, fg="white", relief="groove", command=self.load_main_menu)
        self.i_understand.grid(row=5, column=0, pady=5, padx=10, sticky="w")

    def load_test_screen(self, status="GENERATING TEST...", test=""):
        self.clear_screen()
        self.seconds = 0
        self.high_scores_title = Label(
            self.window,
            text="High Scores:",
            font=(FONT, 15, "bold"),
            bg=MAIN_THEME_COLOR,
            fg="black",
            justify="left"
        )
        self.high_scores_title.grid(row=0, column=0, sticky="w", padx=10, pady=5)

        self.high_scores = Label(
            self.window,
            text=f"Net characters per second: {self.cps} | Net words per minute: {self.wpm} | Accuracy: {self.acc}%",
            font=(FONT, 13, "normal"),
            bg=MAIN_THEME_COLOR,
            fg="black",
            justify="left",
            wraplength=580,
        )
        self.high_scores.grid(row=1, column=0, sticky="w", padx=10, pady=5)

        self.status_title = Label(
            self.window,
            text="Test Status:",
            font=(FONT, 15, "bold"),
            bg=MAIN_THEME_COLOR,
            fg="black",
            justify="left"
        )
        self.status_title.grid(row=2, column=0, sticky="w", padx=10, pady=5)

        self.status = Label(
            self.window,
            text=status,
            font=(FONT, 13, "normal"),
            bg=MAIN_THEME_COLOR,
            fg="black",
            justify="left"
        )
        self.status.grid(row=3, column=0, sticky="w", padx=10, pady=5)

        if status == "TEST IS READY!":
            self.text_title = Label(
                self.window,
                text="Words To Type:",
                font=(FONT, 15, "bold"),
                bg=MAIN_THEME_COLOR,
                fg="black",
                justify="left"
            )
            self.text_title.grid(row=4, column=0, sticky="w", padx=10, pady=5)

            self.text = Label(
                self.window,
                width=70,
                relief="sunken",
                height=5,
                bg=MAIN_THEME_COLOR,
            )
            self.text.grid(row=5, column=0, padx=10, pady=5, sticky="w")

            self.input_title = Label(
                self.window,
                text="Type Words Here:",
                font=(FONT, 15, "bold"),
                bg=MAIN_THEME_COLOR,
                fg="black",
                justify="left"
            )
            self.input_title.grid(row=6, column=0, sticky="w", padx=10, pady=5)

            self.input = Text(
                self.window,
                width=70,
                height=5,
                bg=MAIN_THEME_COLOR,
                font=("Arial", 11, "italic"),
                state="disabled"
            )
            self.input.grid(row=7, column=0, padx=10, pady=5, sticky="w")

            self.start_test_button = Button(self.window, text="START TEST", font=(FONT, 15, "normal"), bg=GREEN, fg="white", relief="groove", command=self.start_test)
            self.start_test_button.grid(row=8, column=0, padx=10, pady=5, sticky="w")

        elif status == "TEST ONGOING":
            def count():
                self.seconds += 1
                self.status.config(text=f"TEST ONGOING | Elapsed Time: {self.seconds}s")
                self.seconds_timer = self.window.after(1000, count)

            self.status.config(text=f"TEST ONGOING | Elapsed Time: {self.seconds}s")
            self.seconds_timer = self.window.after(1000, count)

            self.text_title = Label(
                self.window,
                text="Words To Type:",
                font=(FONT, 15, "bold"),
                bg=MAIN_THEME_COLOR,
                fg="black",
                justify="left"
            )
            self.text_title.grid(row=4, column=0, sticky="w", padx=10, pady=5)

            self.text = Label(
                self.window,
                text=self.test,
                font=("Arial", 11, "italic"),
                relief="sunken",
                bg=MAIN_THEME_COLOR,
                wraplength=580
            )
            self.text.grid(row=5, column=0, padx=10, pady=5, sticky="w")

            self.input_title = Label(
                self.window,
                text="Type Words Here:",
                font=(FONT, 15, "bold"),
                bg=MAIN_THEME_COLOR,
                fg="black",
                justify="left"
            )
            self.input_title.grid(row=6, column=0, sticky="w", padx=10, pady=5)

            self.window.update_idletasks()

            self.input = Text(
                self.window,
                width=70,
                height=5,
                bg=MAIN_THEME_COLOR,
                font=("Arial", 11, "italic"),
            )
            self.input.grid(row=7, column=0, padx=10, pady=5, sticky="w")
            self.input.bind("<Return>", self.evaluate_score)

            self.input.focus()
        else:
            self.text_title = Label(
                self.window,
                text="Words To Type:",
                font=(FONT, 15, "bold"),
                bg=MAIN_THEME_COLOR,
                fg="black",
                justify="left"
            )
            self.text_title.grid(row=4, column=0, sticky="w", padx=10, pady=5)

            self.text = Label(
                self.window,
                width=70,
                height=5,
                relief="sunken",
                bg=MAIN_THEME_COLOR,
                wraplength=580,
            )
            self.text.grid(row=5, column=0, padx=10, pady=5, sticky="w")

            self.input_title = Label(
                self.window,
                text="Type Words Here:",
                font=(FONT, 15, "bold"),
                bg=MAIN_THEME_COLOR,
                fg="black",
                justify="left"
            )
            self.input_title.grid(row=6, column=0, sticky="w", padx=10, pady=5)

            self.input = Text(
                self.window,
                width=70,
                height=5,
                bg=MAIN_THEME_COLOR,
                font=("Arial", 11, "italic"),
                state="disabled"
            )
            self.input.grid(row=7, column=0, padx=10, pady=5, sticky="w")

            self.start_test_button = Button(self.window, text="START TEST", font=(FONT, 15, "normal"), bg=GREEN, fg="white", relief="flat", state="disabled")
            self.start_test_button.grid(row=8, column=0, padx=10, pady=5, sticky="w")

            self.window.after(500, self.generate_test)


    def generate_test(self):
        generator = SentenceGenerator()
        self.test = generator.random_sentence()

        if self.test:
            current_status = "TEST IS READY!"

            if self.status_timer:
                self.window.after_cancel(self.status_timer)

            self.load_test_screen(status=current_status, test=self.test)
        else:
            self.status.config(text="NETWORK ERROR. RECONNECTING...")
            self.status_timer = self.window.after(2000, self.load_test_screen)

    def start_test(self):
        self.load_test_screen(status="TEST ONGOING", test=self.test)

    def evaluate_score(self, event):
        if self.seconds_timer:
            self.window.after_cancel(self.seconds_timer)

        test_words = self.test.strip().split()
        test_words = " ".join(test_words)
        player_words = self.input.get("1.0", tkinter.END).strip().split()
        player_words = " ".join(player_words)
        elapsed_time = self.seconds

        arbiter = Arbiter()

        scores = arbiter.calculate_score(
            words=player_words,
            reference=test_words,
            time=elapsed_time,
            method="levenshtein",
        )

        # print(f"Net characters per second: {scores['cps']: .2f}\nNet words per minute: {scores['wpm']: .2f}\nAccuracy: {scores['acc']: .2f}")

        cps = round(float(scores['cps']), 2)
        wpm = round(float(scores['wpm']), 2)
        acc = round(float(scores['acc']), 2)

        with open("highscores.txt", mode="w") as file:
            file.write("")

        if cps > self.cps:
            self.cps = cps

        with open("highscores.txt", mode="a") as file:
            file.write(f"cps:{self.cps}\n")

        if wpm > self.wpm:
            self.wpm = wpm

        with open("highscores.txt", mode="a") as file:
            file.write(f"wpm:{self.wpm}\n")

        if acc > self.acc:
            self.acc = acc

        with open("highscores.txt", mode="a") as file:
            file.write(f"acc:{self.acc}")

        self.load_results_screen(
            cps=cps,
            wpm=wpm,
            acc=acc,
        )



    def load_results_screen(self, cps, wpm, acc):
        self.clear_screen()
        self.results_title = Label(
            self.window,
            text="Test Results:",
            font=(FONT, 15, "bold"),
            bg=MAIN_THEME_COLOR
        )
        self.results_title.grid(row=0, column=0, padx=10, sticky="w")

        # CPS
        self.cps_label = Label(
            self.window,
            text="Net characters per second:",
            font=(FONT, 11, "normal"),
            bg=MAIN_THEME_COLOR
        )
        self.cps_label.grid(row=1, column=0, padx=10, sticky="w")

        self.cps_content = Label(
            self.window,
            text=f"{cps}",
            font=(FONT, 11, "normal"),
            bg=MAIN_THEME_COLOR
        )
        self.cps_content.grid(row=1, column=1, padx=10, sticky="w")

        # WPM
        self.wpm_label = Label(
            self.window,
            text="Net words per minute:",
            font=(FONT, 11, "normal"),
            bg=MAIN_THEME_COLOR
        )
        self.wpm_label.grid(row=2, column=0, padx=10, sticky="w")

        self.wpm_content = Label(
            self.window,
            text=f"{wpm}",
            font=(FONT, 11, "normal"),
            bg=MAIN_THEME_COLOR
        )
        self.wpm_content.grid(row=2, column=1, padx=10, sticky="w")

        # ACC
        self.acc_label = Label(
            self.window,
            text="Accuracy:",
            font=(FONT, 11, "normal"),
            bg=MAIN_THEME_COLOR
        )
        self.acc_label.grid(row=3, column=0, padx=10, sticky="w")

        self.acc_content = Label(
            self.window,
            text=f"{acc}%",
            font=(FONT, 11, "normal"),
            bg=MAIN_THEME_COLOR
        )
        self.acc_content.grid(row=3, column=1, padx=10, sticky="w")

        self.main_menu = Button(
            self.window,
            text="MAIN MENU",
            font=(FONT, 15, "normal"),
            bg=YELLOW,
            fg="white",
            width=11,
            command=self.load_main_menu,
            relief="groove"
        )
        self.main_menu.grid(row=4, column=0, padx=10, pady=5, sticky="w")

        self.window.update_idletasks()

        self.new_test = Button(
            self.window,
            text="NEW TEST",
            font=(FONT, 15, "normal"),
            bg=GREEN,
            fg="white",
            width=11,
            command=self.load_test_screen,
            relief="groove",
        )
        self.new_test.grid(row=5, column=0, padx=10, sticky="w")








