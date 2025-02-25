import pygame
from screen import Screen
from button import Button

class PauseMenu(Screen):
    def __init__(self,actions):
        super().__init__()
        self.bg_color = (0, 0, 0, 180)  # Semi-transparent black background

        self.resume_button = Button(300, 200, 200, 50, (0, 255, 0), "Resume", actions[0])
        self.quit_button = Button(300, 300, 200, 50, (255, 0, 0), "Quit", actions[1])

        self.screen_elements.append(self.resume_button)
        self.screen_elements.append(self.quit_button)

    def draw(self, screen):
        # Draw a semi-transparent overlay
        overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
        overlay.fill(self.bg_color)
        screen.blit(overlay, (0, 0))

        # Draw buttons
        for element in self.screen_elements:
            element.draw(screen)
