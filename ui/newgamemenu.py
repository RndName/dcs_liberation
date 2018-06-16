from tkinter import *
from tkinter.ttk import *

from ui.window import *


class NewGameMenu(Menu):
    selected_country = None  # type: IntVar
    selected_terrain = None  # type: IntVar
    sams = True

    def __init__(self, window: Window, callback: typing.Callable):
        super(NewGameMenu, self).__init__(window, None, None)
        self.frame = window.right_pane
        self.callback = callback

        self.selected_country = IntVar()
        self.selected_country.set(0)

        self.selected_terrain = IntVar()
        self.selected_terrain.set(0)

        self.sams = BooleanVar()
        self.sams.set(1)

    @property
    def player_country_name(self):
        if self.selected_country.get() == 0:
            return "USA"
        else:
            return "Russia"

    @property
    def enemy_country_name(self):
        if self.selected_country.get() == 1:
            return "USA"
        else:
            return "Russia"

    @property
    def terrain_name(self) -> str:
        if self.selected_terrain.get() == 0:
            return "caucasus"
        elif self.selected_terrain.get() == 1:
            return "nevada"
        else:
            return "persiangulf"

    def display(self):
        self.window.clear_right_pane()

        Label(self.frame, text="Player country").grid(row=0, column=0)
        Radiobutton(self.frame, text="USA", variable=self.selected_country, value=0).grid(row=1, column=0)
        Radiobutton(self.frame, text="Russia", variable=self.selected_country, value=1).grid(row=2, column=0)

        Label(self.frame, text="Terrain").grid(row=0, column=1)
        Radiobutton(self.frame, text="Caucasus", variable=self.selected_terrain, value=0).grid(row=1, column=1)
        Radiobutton(self.frame, text="Nevada", variable=self.selected_terrain, value=1).grid(row=2, column=1)
        Radiobutton(self.frame, text="Persian Gulf", variable=self.selected_terrain, value=2).grid(row=3, column=1)

        Label(self.frame, text="Options").grid(row=1, column=2)
        Checkbutton(self.frame, text="SAMs", variable=self.sams).grid(row=1, column=2)

        Button(self.frame, text="Proceed", command=self.proceed).grid(row=4, column=0, columnspan=3)

    def proceed(self):
        self.callback(self.player_country_name, self.enemy_country_name, self.terrain_name, bool(self.sams.get()))
