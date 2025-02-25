from screen import Screen
from button import Button
from panel import Panel
from label import Label
import pygame

class MainMenu(Screen):
    def __init__(self,actions):
        self.COLORS={"GRAY":pygame.Color("#A15511"),
                     "MAIN_SCREEN":pygame.Color("#CF278C")}
        super().__init__()

        # Defining and appending UI Elements to Main Menu Screen

        # First element added is Title Label, screen_elements[0] is label
        self.screen_elements.append(Label(262,177,476,104,self.COLORS["MAIN_SCREEN"],"Booltro"))

        # Second element added is Button Panel, (Holds buttons on main menu), screen_elements[1] is button panel
        self.screen_elements.append(Panel(257,436,476,70))

        # Appending Buttons to button Panel, 
            # Play, Options, Quit, Collection
        self.screen_elements[1].panel_elements.append(Button(274,447,80,47,self.COLORS["GRAY"],"Play",actions[0],18,))
        self.screen_elements[1].panel_elements.append(Button(394,447,80,47,self.COLORS["GRAY"],"Options",actions[1],18,))
        self.screen_elements[1].panel_elements.append(Button(514,447,80,47,self.COLORS["GRAY"],"Quit",actions[2],18))
        self.screen_elements[1].panel_elements.append(Button(634,447,80,47,self.COLORS["GRAY"],"Collection",actions[3],18))