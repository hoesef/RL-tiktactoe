import pygame as pg

class BaseScreen():

    def __init__(self, appContext, switch_callback):
        self.appContext = appContext
        self.switch_callback = switch_callback
    
    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.appContext.running = False
    
    def update_loop(self):
        print("You are using the update loop from BaseScreen. This does nothing!")
        self.appContext.stop()

class MenuScreen(BaseScreen):

    def __init__(self, appContext, switch_callback):
        super().__init__(appContext, switch_callback)
        self.appContext.set_title("Menu")
    
    def event_loop(self):
        super().event_loop()

        keys = pg.key.get_pressed()
        if keys[pg.K_p]:
            self.switch_callback('p')
        elif keys[pg.K_t]:
            self.switch_callback('t')
    
    def update_loop(self):
        self.appContext.WIN.fill((100, 100, 100))
        self.appContext.doDisplayUpdate = True

class PlayScreen(BaseScreen):

    def __init__(self, appContext, switch_callback):
        super().__init__(appContext, switch_callback)
        self.appContext.set_title("Play")
    
    def event_loop(self):
        super().event_loop()
        
        keys = pg.key.get_pressed()
        if keys[pg.K_m]:
            self.switch_callback('m')
        elif keys[pg.K_t]:
            self.switch_callback('t')
    
    def update_loop(self):
        self.appContext.WIN.fill((200, 0, 40))
        self.appContext.doDisplayUpdate = True

class TrainingScreen(BaseScreen):

    def __init__(self, appContext, switch_callback):
        super().__init__(appContext, switch_callback)
        self.appContext.set_title("Training")
    
    def event_loop(self):
        super().event_loop()
        
        keys = pg.key.get_pressed()
        if keys[pg.K_m]:
            self.switch_callback('m')
        elif keys[pg.K_p]:
            self.switch_callback('p')

    def update_loop(self):
        self.appContext.WIN.fill((50, 120, 58))
        self.appContext.doDisplayUpdate = True

if __name__ == '__main__':
    pass