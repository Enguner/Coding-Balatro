import pygame

class Label:
    def __init__(self, x, y, width, height, color, text,text_color=(0,0,0)):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.font = pygame.font.SysFont('Arial', 24)
        self.text_color = text_color  

    def draw(self, screen):
        """Draw the label with centered text and customizable text color"""
        pygame.draw.rect(screen, self.color, self.rect)
        
        # Render the text with the specified text color
        text_surface = self.font.render(self.text, True, self.text_color)
        
        # Center the text inside the rect
        text_rect = text_surface.get_rect(center=self.rect.center)
        
        # Draw the text on the screen
        screen.blit(text_surface, text_rect)

    def handle_event(self,event):
        pass