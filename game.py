import pygame
from mainmenu import MainMenu
from pausemenu import PauseMenu

# Initialize pygame
pygame.init()

# Define a custom event for button press
BUTTON_CLICK_EVENT = pygame.USEREVENT + 1  # A custom event type



class Game:
    def __init__(self):
        pygame.init()
        self.running = True
        self.actions = [self.play_action,self.options_action,self.quit_action,self.collection_action]
        self.screen_stack = []
        self.push_screen(MainMenu(self.actions))
        self.clock = pygame.time.Clock()
        self.screen_resolution = [1000,562]
        self.screen = pygame.display.set_mode(self.screen_resolution)

    def push_screen(self, screen):
        self.screen_stack.append(screen)

    def pop_screen(self):
      """Remove the top screen (go back to the previous one)."""
      if len(self.screen_stack) > 1:
        self.screen_stack.pop()

    def update(self):
        """Update game logic here"""
        pass

    def draw(self):
        """Draw all screens (bottom-to-top), keeping background screens visible."""
        self.screen.fill((0, 0, 0))  # Clear screen
        for screen in self.screen_stack:
            screen.draw(self.screen)  # Draw each screen
        pygame.display.flip()

    def events(self):
        """Handle events like keyboard/mouse input"""
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            self.running = False  # Exit the game loop
          elif event.type == BUTTON_CLICK_EVENT:
            print("Button clicked!")
            # Handle button click (e.g., trigger game logic)
          
          for screen in self.screen_stack:
            screen.handle_events(event)  # Delegate event handling to the screen

    def game_start(self):
        """Main game loop"""
        while self.running:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(60)  # Limit FPS to 60
    
    def play_action(self):
      print("Play button clicked - Starting the game!")

    def quit_action(self):
      pygame.quit()  # Exit Pygame
      quit()  # Exit the program
    
    def options_action(self):
       actions = [self.resume_action,self.quit_action ]
       self.push_screen(PauseMenu(actions))
    
    def collection_action(self):
      pass
    
    def resume_action(self):
        self.pop_screen()

# To run the game:
if __name__ == "__main__":
    game = Game()
    game.game_start()
    pygame.quit()
