import pygame
# Define a custom event for button press
BUTTON_CLICK_EVENT = pygame.USEREVENT + 1  # A custom event type
class Panel:
    def __init__(self, x, y, width, height, color=(175,175,175), text=""):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.font = pygame.font.SysFont('Arial', 24)
        self.panel_elements = []

    def add_elements(self,element):
        self.panel_elements(element)

    def draw(self, screen):
        """Draw the button onto the given screen surface"""
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        screen.blit(text_surface, (self.rect.x + 10, self.rect.y + 10))
        for element in self.panel_elements:
            element.draw(screen)

    def handle_event(self, event):
        for element in self.panel_elements:
            element.handle_event(event)