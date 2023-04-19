import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import Image
from tkinter.ttk import *
import os
from PIL import ImageTk, Image

home = Tk()
home.minsize(700, 550)
home.title("Abdalla Shalaby")
def about_page():
    about_me = Toplevel(home)
    about_me.title("About Me")
    about_me.geometry("1050x900")
    Label(about_me, text = "    My name is Abdalla Shalaby I was born on 1/1/2011\n"
                           "I'm a Passionate person who loved to know about everything around him\n"
                           "My father were a boxer, So he go me to train boxing.I was very good at it\n"
                           "that I took a gold medal on Egypt for my weight four times respectively.\n"
                           "Also my dad is a programmer, So he made me learn programming.\n"
                           "All of that and I was still 10, So I had a great ambition from my family\n").pack(side = "left")
    poten = tkinter.PhotoImage(file = "great_potential.gif")
    img = Label(about_me, image = poten)
    img.poten = poten
    img.pack(side = "bottom")

def prog_life():
        program_life = Toplevel(home)
        program_life.title = "Programming Life"
        program_life.geometry("752x1000")
        background = tkinter.PhotoImage(file = "ACPC_2021_gang.gif")
        labl = Label(program_life, text="", image = background)
        labl.background = background
        labl.pack(side = "right")
        Label(program_life, text="    As I told you before that my father is a developer (he writes Elixir ta2reeban)\n"
              "So I started learning programming by the basics of python at age of 9\n"
              "Then I went to Coach Academy to learn competitive programming with C++\n"
              "I learned the basics of C++ in level 1, and I participated in that year's ACPC teens\n"
              "It was the first time for ACPC(Arab & Africa Collegiate Programming Contest) to make a\n"
              " version for teens so I participated\n"
              "I qualified from the online filtration and went to the finals on Alex in Arab Academy\n"
              'for Science and Technology(AAST) and I were the 34 on Egypt because my teammate was absent :"(\n'
              "Then I took level 2 in Coach Academy and entered that year's ACPC teens again\n"
              "And all the same happened qualified to final and lost because my teammate was absent\n"
              "Then in 2022 I participated in IIOT(International Informatics Olympiad in Teams) \n"
              "It was the first time for IOI to be in teams for Egypt\n"
              "And I think you guessed It, Yes I went to finals in AAST and lost it but not because\n"
              "my team were absent because we didn't do will in the problemset.\n"
              "Now I'm taking a computer science diploma in Coach Academy.\n"
              "And also I will take level 3 for competitive programming.\n"
              "I have registered in this year's ACPC teens and it will start soon (pray for me :D)").pack(side = "left")


def sport_life():
    sports_life = Toplevel(home)
    sports_life.title = "Sports Life"
    sports_life.geometry("752x1000")
    background = tkinter.PhotoImage(file="first_gold.gif")
    labl = Label(sports_life, text="", image=background)
    labl.background = background
    labl.pack(side="right")
    Label(sports_life, text="    And also as I told you before that my dad was a boxer, \n"
          "So I went to train Kickboxing with a Coach that my dad was his idol LOL XD\n"
          "When he was little, he saw my dad playing it and he liked it and become a coach\n"
          "So I trained with him and after only 2 months of training I went to a championship\n"
          "My coach was still playing and coaching so me and him played on one ring :D\n"
          "Me and him took the first place on our weighs and ages.\n"
          "7 month later I went to another championship, me and my coach as a player XD\n"
          "History repeating itself, we both took first places.\n"
          "And this scenario repeated 2 times again.\n"
          "Then I travelled so I stopped to train.After I came back, I started training swimming\n"
          "But just for fun, my coach told me that my level is good and I should take star 1\n"
          "And I passed it's test and I took star 1.But I stopped training again beacause of winter.\n"
          "And now I returned to my kickboxing coach and I told him that I wanted to play boxing\n"
          "And he told me that he is a boxer chiefly so he can train me boxing, and now I'm a boxer").pack(
        side="left")

def the_note():
    note = Toplevel(home)
    note.title = "Note To Coach Menna"
    note.geometry("752x1000")
    text = Label(note, text="    I wanted to thank you my coach for great information and detailed explanation\n"
          "and covering everything about the topic, and the most important thing\n"
          "answering our questions eagerly and giving us time to try the code by ourselves\n"
          "Hope I complete this course with you and complete the course firstly XD")
    text.pack(side="top")
style = ttk.Style()
background = tkinter.PhotoImage(file = "backg.gif")
Label(home, text="", image = background).pack(side = "top")
about = Button(home, text="About Me", width = 20, command = about_page)
about.pack()
about.place(x = 310, y = 120)
p_life = Button(home, text="Programming Life", width = 20, command = prog_life)
p_life.pack()
p_life.place(x = 310, y = 200)
s_life = Button(home, text="Sports Life", width = 20, command = sport_life)
s_life.pack()
s_life.place(x = 310, y = 280)
note = Button(home, text="Note To Coach Menna", width = 20, command = the_note)
note.pack()
note.place(x = 310, y = 360)
style.theme_use("classic")
home.mainloop()