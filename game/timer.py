import time
import pygame

class Timer:
    """
    A simple timer class to manage countdowns in the game.
    
    Attributes:
    - duration (float): The total duration of the timer in seconds.
    - time_left (float): The remaining time left on the timer in seconds.
    - last_update_time (float): The last time the timer was updated (using the Python time library).
    
    Methods:
    - update(): Updates the timer by calculating the time passed since the last update. Decremenets the time_left accordingly.
    - increment(seconds): Increments the time left by a specified number of seconds.
    - decrement(seconds): Decrements the time left by a specified number of seconds.
    - reset(): Resets the time left to the original duration.
    - is_finished(): Checks if the timer has finished (when the time left is zero or less).
    - display_output(): Returns a Pygame surface with the current time left rendered as text.
    """

    def __init__(self, duration):
        """
        Initializes the Timer with a specified duration.

        Agruments:
        - duration (float): The total duration of the timer in seconds.

        Outputs: None
        """
        self.duration = duration
        self.time_left = duration
        self.last_update_time = time.time()

    def update(self):
        """
        Updates the timer by calculating the time passed since the last update.

        Arguments: None
        Outputs: None
        """
        time_passed = time.time() - self.last_update_time
        self.last_update_time = time.time()
        self.time_left -= time_passed
        if self.time_left <= 0:
            self.time_left = 0

    def increment(self, seconds):
        """
        Increments the time left by a specified number of seconds.
        
        Arguments:
        - seconds (float): The number of seconds to add to the time left.
        
        Outputs: None
        """
        self.time_left += seconds
        if self.time_left > self.duration:
            self.time_left = self.duration
    
    def decrement(self, seconds):
        """
        Decrements the time left by a specified number of seconds.
        
        Arguments:
        - seconds (float): The number of seconds to subtract from the time left.
        
        Outputs: None
        """
        self.time_left -= seconds
        if self.time_left < 0:
            self.time_left = 0

    def reset(self):
        """
        Resets the time left to the original duration.

        Arguments: None
        Outputs: None
        """
        self.time_left = self.duration

    def is_finished(self):
        """
        Checks if the timer has finished (when the time left is zero or less).

        Arguments: None

        Outputs:
        - bool: True if the timer has finished, False otherwise.
        """
        return self.time_left <= 0

    def display_output(self):
        """
        Returns a Pygame surface with the current time left rendered as text.

        Arguments: None

        Outputs:        
        - pygame.Surface: A surface containing the rendered timer text.
        """
        font = pygame.font.Font(None, 36)
        timer_text = font.render(f"Time Left:\n{int(self.time_left)}s", True, (255, 255, 255))  # white text
        return timer_text