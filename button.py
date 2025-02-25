import pygame
# Define a custom event for button press
BUTTON_CLICK_EVENT = pygame.USEREVENT + 1  # A custom event type

class Button:

    def __init__(self, x, y, width, height, color, text,action,font_size=24):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.font = pygame.font.SysFont('Arial', font_size)
        self.action = action

    def draw(self, screen):
        """Draw the button onto the given screen surface"""
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        # Center the text inside the rect
        screen.blit(text_surface, (self.rect.x + 10, self.rect.y + 10))

    def handle_event(self, event):
        """Detect mouse click on button and post a custom event"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):  # Check if mouse click is within button bounds
                if self.action:
                    self.action()