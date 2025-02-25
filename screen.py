
class Screen:
    def __init__(self):
        self.resolution = [1000, 562]
        self.screen_elements = []  # List to store buttons and other UI elements

    def get_resolution(self):
        return self.resolution

    def add_element(self, button):
        """Add a button to the screen"""
        self.screen_elements.append(button)

    def draw(self, screen):
        """Draw all elements onto the screen"""
        screen.fill((0, 0, 0))  # Fill the screen with black
        for element in self.screen_elements:
            element.draw(screen)  # Delegate drawing to each button

    def update(self):
        pass

    def handle_events(self, event):
        """Handle events for all elements on the screen"""
        for element in self.screen_elements:
            element.handle_event(event)  # Handle button-specific events
