import pygame as pg

class Text():

    def __init__(self, text: str, fontName: str, fontSize: int, pos: tuple[int, int], **kwargs) -> None:
        """
        Creates an instance of the Text class

        :params: text: (str), fontName: (str)

        This class has many optional arguments that can be passed in using **kwargs. These include:
        - wrap: bool -> indicate if the text should wrap around a text box of be clipped by it
        - textBox: tuple[int|None, int|None] -> defines the textBox that text should be rendered within
        - padding: tuple[int, int, int, int] -> specifies the amount of padding between the text surface and the text box (right, top, left, bottom)
        - boarder: tuple[int, int, int, int] -> specifies any boarder between the button surface and the writable area
        - center: tuple[bool, bool] -> specifies if the text should be centered (horizontal, vertical)
        - bgc: tuple[int, int, int] -> specifies the background colour for the rendered text
        - bold: bool -> indicate if the text should be bold
        - italic: bool -> indicate if the text should be italic
        - textColour: tuple[int, int, int] -> specify the colour to render the text
        - minSize: int -> spcify the minimum size to try and render the text

        :returns: None
        """
        if not pg.font.get_init():
            pg.font.init()

        self.lines = None

        self.text = text
        self.fontName = fontName
        self.fontSize = fontSize
        self.pos = pos

        self.wrap = kwargs.get("wrap", False)
        self.textBox = kwargs.get("textBox", (None, None))
        self.padding = kwargs.get("padding", (0, 0, 0, 0))
        self.boarder = kwargs.get("boarder", (0, 0, 0, 0))
        self.center = kwargs.get("center", (False, False))
        self.bgc = kwargs.get("bgc", (255,255,255))
        self.bold = kwargs.get("bold", False)
        self.italic = kwargs.get("italic", False)
        self.textColour = kwargs.get("textColour", (0, 0, 0))
        self.minSize = kwargs.get("minSize", 1)
        self.transparentBackground = kwargs.get("transparentBackground", True)

        self.font = pg.font.SysFont(self.fontName, fontSize)
        self.font.set_bold(self.bold)
        self.font.set_italic(self.italic)

        if self.wrap and (self.textBox == (None, None)):
            raise ValueError("Cannot wrap text: No text box dimensions given.")
        if not self.wrap and (self.center != (False, False)):
            raise ValueError("Cannot center text when not wrapping")
        
    def toggle_bold(self) -> None:
        self.bold = not self.bold
        self.font.set_bold(self.bold)

    #TODO: Thought 002
    def get_lines(self) -> None:
        """
        Returns the display text split into N lines depending on the text settings
        """

        def _wrap_recurse(size: int) -> list[str]:
            """
            Helper function to split text into lines that can be rendered by a font into a known text box.

            For a given font size it:
            - Finds the maximum number of words that can fit inside the width of the text box
                - If no word fits, reduce the font size and try again
            - Checks that the height of all of these lines fits inside the height of the text box
                - If it cannot, reduce the font size and try again

            :params: size: int
            :returns: lines: list[str]
            """
            self.font = pg.font.SysFont(self.fontName, size)
            self.font.set_bold(self.bold)
            self.font.set_italic(self.italic)

            if size < self.minSize:
                return []
            
            words = self.text.split()
            lines = []

            while len(words) > 0:
                line = []
                while len(words) > 0:
                    fw, _ = self.font.size(' '.join(line + words[:1]))
                    if fw >= self.textBox[0] - (self.boarder[0] + self.boarder[2] + self.padding[0] + self.padding[2]):
                        break 
                    line.append(words.pop(0))
                
                if len(line) == 0:
                    return _wrap_recurse(size - 1)

                line = ' '.join(line)
                lines.append(line)
            
            if len(lines) * self.font.get_linesize() > self.textBox[1] - (self.boarder[1] + self.boarder[3] + self.padding[1] + self.padding[3]):
                return _wrap_recurse(size - 1)
            
            return lines

        if not self.wrap:
            self.lines = [self.text]
        else:
            self.lines = _wrap_recurse(self.fontSize)
    
    def render(self, surf: pg.SurfaceType) -> None:
        """
        Renders the text to a surface according to the text settings

        :params: surf: pg.SurfaceType
        :returns: None
        """
        if self.lines == None:
            self.get_lines()
        
        x, y = self.pos[0] + self.boarder[0] + self.padding[0], self.pos[1] + self.boarder[1] + self.padding[1]

        if self.center[1]:
            y_top = (self.pos[1] + self.boarder[1] + self.padding[1]  - self.boarder[3] - self.padding[3])
            text_height = len(self.lines) * self.font.get_linesize()
            y = y_top + (self.textBox[1] - text_height) // 2
        
        for i, line in enumerate(self.lines):
            text_surf = self.font.render(line, True, self.textColour, self.bgc)
            if self.center[0]:
                x = self.boarder[0] + (((self.textBox[0] - self.boarder[0] + self.padding[0] - self.boarder[2] - self.padding[2])) - text_surf.get_width()) // 2
            
            pos = (x, y + i * self.font.get_linesize())
            surf.blit(text_surf, pos)

    def __del__(self):
        pg.font.quit()

if __name__ == '__main__':
    pass