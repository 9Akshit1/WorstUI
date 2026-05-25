"""
Title: Mole Class
Course: ICS4U
Author: Akshit Erukulla
Summary: Defines a Mole class that represents a mole (the number). The mole can be whacked by the player and has an animation for going up and down.
History: May 25th, 2026
"""

import pygame
import time

class Mole:
    """
    A class representing a mole in the Whack-a-Mole game. The mole can be whacked by the player and has an animation for going up and down.
    
    Attributes:
    - initial_position (tuple): The initial (x, y) coordinates of the mole on the screen.
    - position (tuple): The current (x, y) coordinates of the mole on the screen.
    - is_whacked (bool): A boolean indicating whether the mole has been whacked or not.
    - image (pygame.Surface): The image (pygame will load it after given the path) representing the mole.
    - width (int): The width of the mole image.
    - height (int): The height of the mole image.
    - duration (float): The duration for the mole to go up and down in seconds.
    - start_time (float): The time when the mole was created or reset, used for animation timing.
    
    Methods:
    - __init__(self, position, image, duration): Initializes the mole with a specified position and image.
    - reset(self): Resets the mole to its initial state (not whacked and original position).
    - draw(self, screen): Draws the mole on the screen if it has not been whacked.
    - check_whack(self, click_position): Checks if the mole has been whacked based on the click position of the cursor.
    - animate(self, screen): Animates the mole by making it go up (appear to be whacked) and down (after duration for its movement is).
    """

    def __init__(self, position, image, duration):
        """
        Initializes the Mole with a specified position and image.
        
        Arguments:
        - position (tuple): The (x, y) coordinates of the mole's position on the screen.
        - image (pygame.Surface): The image (the number) file path for the mole.
        - duration (float): The duration for the mole to go up and down in seconds.
        
        Outputs: None
        """
        self.initial_position = position
        self.position = position
        self.is_whacked = False
        self.image = pygame.image.load(image)
        self.width = 50
        self.height = 50
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.duration = duration
        self.start_time = time.time()

    def reset(self):
        """
        Resets the mole to its initial state (not whacked and original position).

        Arguments: None
        Outputs: None
        """
        self.is_whacked = False
        self.position = self.initial_position
        self.start_time = time.time()

    def draw(self, screen):
        """
        Draws the mole on the screen if it has not been whacked.

        Arguments:
        - screen (pygame.Surface): The surface on which to draw the mole.

        Outputs: None
        """
        if not self.is_whacked:       # so if it is whacked, then the mole would vanish (since it would not be drawn on the screen)
            screen.blit(self.image, self.position)

    def check_whack(self, click_position):
        """
        Checks if the mole has been whacked based on the click position.
        
        Arguments:
        - click_position (tuple): The (x, y) coordinates of the click.
        
        Outputs:
        - bool: True if the mole was whacked, False otherwise.
        """
        if self.is_whacked:
            return False  # already whacked

        mole_rect = pygame.Rect(self.position[0], self.position[1], self.width, self.height)
        if mole_rect.collidepoint(click_position):        # check if the click is within the mole's area
            self.is_whacked = True
            return True
        return False
    
    def animate(self, screen):
        """
        Animates the mole by making it go up (appear to be whacked) and down (after duration for its movement is ).

        Arguments:
        - screen (pygame.Surface): The surface on which to draw the mole.

        Outputs: None
        """
        # position for the mole should be a parabolic movement (using the current time), we can use a simple sine wave for the animation. as in like the mole goes up (15% of duration) and stays there for 70% of the time, and then goes down (15% of duration)
        self.position = (self.initial_position[0], self.initial_position[1] - 20 * (1 - abs((time.time() - self.last_update_time) / self.duration - 0.5) * 2))  # simple parabolic movement
        self.draw(screen)