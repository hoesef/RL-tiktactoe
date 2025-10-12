import pygame as pg

from screen_manager import ScreenManager

class AppContext():
    
    def __init__(self):
        pg.init()
        self.running = True
        
        ## Display 
        self.RES = (800, 600)
        self.WIN = pg.display.set_mode(self.RES)

        ## Clock
        self.CLOCK = pg.time.Clock()
        self.fps = 60

        ## Mouse
        self.pos = pg.mouse.get_pos()

        ## Update
        self.updateArea = []
        self.doDisplayUpdate = True

    ## Set the window title
    def set_title(self, title):
        pg.display.set_caption(title)

    ## Handle clock tick
    def tick(self):
        self.CLOCK.tick(self.fps)

    ## Update window
    def update_display(self):
        if not (self.doDisplayUpdate or self.updateArea):
            return

        if self.updateArea:
            pg.display.update(self.updateArea)
        else:
            pg.display.flip()

        self.doDisplayUpdate = False
        self.updateArea = []

    ## QUit applicaiton
    def stop(self):
        self.running = False

    def __del__(self):
        pg.quit()

def main():
    app = AppContext()
    screenManager = ScreenManager(app)
    while app.running:
        screenManager.event_loop()
        screenManager.update_loop()
        screenManager.draw()
        app.update_display()
        app.tick()

if __name__ == '__main__':
    main()