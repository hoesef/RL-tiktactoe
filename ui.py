import pygame as pg

class Button():

    def __init__(self, x, y, width, height, colour, text="", boarder=1):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.hoverColour = (0, 255, 0)
        self.bgc = (150, 150, 150)
        self.currentColour = colour
        self.boarder = boarder
        self.text = text

        self.buttonSurf = pg.Surface((self.width, self.height))
        self.doDisplayUpdate = True

    def fit_text(self, textSize):
        """
        First checks tries to wrap text
        Then checks if vertical height exceeds button height
        Reduces size and try again
        """

        

        raise NotImplemented("fit_text() is not yet implemented")

    def hovering(self, x, y):
        return ((self.x + self.boarder <= x) and (x <= self.x + self.width - self.boarder) and
                (self.y + self.boarder <= y) and (y <= self.y + self.height - self.boarder))         
    
    def update(self, pos):
        if self.hovering(*pos) and (self.currentColour != self.hoverColour):
            self.currentColour = self.hoverColour
            self.doDisplayUpdate = True
        elif not self.hovering(*pos) and (self.currentColour != self.colour):
            self.currentColour = self.colour
            self.doDisplayUpdate = True
    
    def draw(self, surf):
        if not self.doDisplayUpdate:
            return
        
        self.buttonSurf.fill(self.bgc)
        self.buttonSurf.fill(self.currentColour, (self.boarder, self.boarder, self.width - (2 * self.boarder), self.height - (2 * self.boarder)))#, pg.Rect(self.x + self.boarder, self.y + self.boarder, self.width - self.boarder, self.height - self.boarder))
        surf.blit(self.buttonSurf, (self.x, self.y))
        self.doDisplayUpdate = False

        return (self.x, self.y, self.width, self.height)    

from random import randint

if __name__ == '__main__':
    pg.init()
    WIN = pg.display.set_mode((800, 600))
    WIN.fill((100, 100, 100))
    clock = pg.time.Clock()
    fps = 60

    button = Button(50, 50, 50, 50, (255, 0, 0), boarder=2)

    button.colour = (randint(0, 255), randint(0, 255), randint(0, 255))
    button.hoverColour = (randint(0, 255), randint(0, 255), randint(0, 255))
    button.bgc = (randint(0, 255), randint(0, 255), randint(0, 255))

    run = True
    while run:
        pos = pg.mouse.get_pos()

        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                run = False
            if button.hovering(*pos) and event.type == pg.MOUSEBUTTONDOWN:
                print("click")

        button.draw(WIN)
        button.update(pos)
        pg.display.update()
        clock.tick(fps)
    
    pg.quit()
        