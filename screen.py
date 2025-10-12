import pygame as pg
from ui import Button

class BaseScreen():

    def __init__(self, appContext, switch_callback):
        """
        Initalizes a screen instance\n
        Takes in the appContext and the function that should be used to change screens

        :params: appContext, switch_callback
        :returns: 
        """
        self.appContext = appContext
        self.switch_callback = switch_callback
        self.doFullDraw = True
    
    def event_loop(self):
        """
        Handles the basic events all screens need (exiting functionallity)
        """
        self.appContext.pos = pg.mouse.get_pos()

        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.appContext.running = False
    
    def update_loop(self):
        """
        Updates all elements on the screen
        """
        print("You are using the update loop from BaseScreen. This does nothing!")
        self.appContext.stop()

    def draw(self):
        """
        Draws all elements on the screen
        """
        print("You are using the draw loop from BaseScreen. This does nothing!")
        self.appContext.stop()

class MenuScreen(BaseScreen):

    def __init__(self, appContext, switch_callback):
        super().__init__(appContext, switch_callback)
        self.appContext.set_title("Menu")

        self.buttons = {"play": Button(50, 50, 50, 50, (255,0,0), boarder=2),
                        "train": Button(110, 50, 50, 50, (200, 200, 200), boarder=2)}
        
        self.click = False
    
    def event_loop(self):
        """
        Handles user events:
        - Exiting
        - switching screens
        """
        ## Check for exit condition
        super().event_loop()

        mouse_buttons = pg.mouse.get_pressed()
        ## Check if left mouse is pressed
        if not mouse_buttons[0]:
            self.click = False
            return
        
        ## Check if screen was clicked (not on a button) and then dragged over button
        ## Prevents this from registering as a button press
        if self.click:
            return
        
        ## If left mouse pressed, check if mouse is over button
        if self.buttons["play"].hovering(*self.appContext.pos):
            self.switch_callback('p')
        if self.buttons["train"].hovering(*self.appContext.pos):
            self.switch_callback('t')

        self.click = True
    
    def update_loop(self):
        pos = pg.mouse.get_pos()
        for button in self.buttons.values():
            button.update(pos)

    def full_draw(self):
        """
        Redraw the entire screen
        """
        self.appContext.WIN.fill((100, 100, 100)) ## TODO: Thought 001
        for button in self.buttons.values():
            button.draw(self.appContext.WIN)
        self.appContext.doDisplayUpdate = True
        self.doFullDraw = False

    def partial_draw(self):
        """
        Redraws only the elements that have changes since the last frame
        """
        for button in self.buttons.values():
            self.appContext.updateArea.append(button.draw(self.appContext.WIN))

    def draw(self):
        """
        Calls either full_draw() or partial_draw() depending on what needs updating
        """
        if self.doFullDraw:
            self.full_draw()
        else:
            self.partial_draw()

class PlayScreen(BaseScreen):

    def __init__(self, appContext, switch_callback):
        super().__init__(appContext, switch_callback)
        self.appContext.set_title("Play")
    
    def event_loop(self):
        """
        Handles user events:
        - Exiting
        - switching screens
        """
        super().event_loop()
        
        keys = pg.key.get_pressed()
        if keys[pg.K_m]:
            self.switch_callback('m')
        elif keys[pg.K_t]:
            self.switch_callback('t')
    
    def update_loop(self):
        pass

    def full_draw(self):
        """
        Redraw the entire screen
        """
        self.appContext.WIN.fill((200, 0, 40))
        self.doFullDraw = False

    def paritial_draw(self):
        """
        Redraws only the elements that have changes since the last frame
        """
        pass
    
    def draw(self):
        """
        Calls either full_draw() or partial_draw() depending on what needs updating
        """
        if self.doFullDraw:
            self.full_draw()
        else:
            self.paritial_draw()

class TrainingScreen(BaseScreen):

    def __init__(self, appContext, switch_callback):
        super().__init__(appContext, switch_callback)
        self.appContext.set_title("Training")
    
    def event_loop(self):
        """
        Handles user events:
        - Exiting
        - switching screens
        """
        super().event_loop()
        
        keys = pg.key.get_pressed()
        if keys[pg.K_m]:
            self.switch_callback('m')
        elif keys[pg.K_p]:
            self.switch_callback('p')

    def update_loop(self):
        pass

    def full_draw(self):
        """
        Redraw the entire screen
        """
        self.appContext.WIN.fill((50, 120, 58))
        self.doFullDraw = False
    
    def partial_draw(self):
        """
        Redraws only the elements that have changes since the last frame
        """
        pass
    
    def draw(self):
        """
        Calls either full_draw() or partial_draw() depending on what needs updating
        """
        if self.doFullDraw:
            self.full_draw()
        else:
            self.partial_draw()

if __name__ == '__main__':
    pass