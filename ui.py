import pygame as pg

from text import Text

class Button():

    def __init__(self, x, y, width, height, text="", **kwargs):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.colour = kwargs.get("colour", (100, 100, 100))
        self.hoverColour = kwargs.get("hoverColour", (100, 150, 100))
        self.bgc = kwargs.get("bgc", (150, 150, 150))
        self.boarder = kwargs.get("boarder", (0, 0, 0, 0))
        
        self.currentColour = self.colour

        print(f"{self.colour = }, {self.currentColour = }, {self.bgc = }")

        ## Text settings
        if text:
            try:
                self.textSettings = kwargs["textSettings"]
            except KeyError:
                raise ValueError("No text settings supplied to the button.")
            textSettings["boarder"] = self.boarder
            textSettings["bgc"] = self.currentColour
            if textSettings["wrap"]:
                textSettings["textBox"] = (width, height)
            self.text = Text(text, **textSettings)

        self.buttonSurf = pg.Surface((self.width, self.height))
        self.doDisplayUpdate = True

    def hovering(self, x, y):
        return ((self.x + self.boarder[0] <= x) and (x <= self.x + self.width - self.boarder[2]) and
                (self.y + self.boarder[1] <= y) and (y <= self.y + self.height - self.boarder[3]))         
    
    def update(self, pos):
        if self.hovering(*pos) and (self.currentColour != self.hoverColour):
            self.currentColour = self.hoverColour
            self.doDisplayUpdate = True
            self.text.bgc = self.currentColour
        elif not self.hovering(*pos) and (self.currentColour != self.colour):
            self.currentColour = self.colour
            self.doDisplayUpdate = True
            self.text.bgc = self.currentColour
    
    def draw(self, surf):
        if not self.doDisplayUpdate:
            return
        
        self.buttonSurf.fill(self.bgc)
        self.buttonSurf.fill(self.currentColour, (self.boarder[0], self.boarder[1], self.width - (self.boarder[0] + self.boarder[2]), self.height - (self.boarder[1] + self.boarder[3])))#, pg.Rect(self.x + self.boarder, self.y + self.boarder, self.width - self.boarder, self.height - self.boarder))
        self.text.render(self.buttonSurf)
        surf.blit(self.buttonSurf, (self.x, self.y))
        self.doDisplayUpdate = False

        return (self.x, self.y, self.width, self.height)  


if __name__ == '__main__':
    pg.init()
    WIN = pg.display.set_mode((800, 600))
    WIN.fill((100, 100, 100))
    clock = pg.time.Clock()
    fps = 60

    textSettings = {"fontName": "Arial", "fontSize": 30, "pos": (0, 0), 
                    "wrap": True, "textBox": (None, None), "padding": (5, 0, 5, 0),
                    "boarder": (0, 0, 0), "center": (True, True), "bgc": (255, 255, 255),
                    "bold": False, "italic": False, "textColour": (0, 0, 0), "minSize": 1}
    
    buttonSettings = {"colour": (255, 0, 0), "hoverColour": (0, 255, 0), 
                      "bgc": (150, 150, 150), "boarder": (2, 2, 2, 2), 
                      "textSettings": textSettings}
    
    text = "Multiple words to check that it is working"
    button = Button(50, 50, 100, 100, text=text, **buttonSettings)

    run = True
    while run:
        pos = pg.mouse.get_pos()

        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                run = False
            if button.hovering(*pos) and event.type == pg.MOUSEBUTTONDOWN:
                print("click")
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                button.text.toggle_bold()
                button.doDisplayUpdate = True

        button.update(pos)
        button.draw(WIN)
        pg.display.update()
        clock.tick(fps)
    
    pg.font.quit()
    pg.quit()
        