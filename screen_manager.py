from screen import MenuScreen, PlayScreen, TrainingScreen

class ScreenManager():

    def __init__(self, appContext):
        self.appContext = appContext
        self.currentScreen = MenuScreen(self.appContext, self.switch_screen)

    def switch_screen(self, switch):
        self.currentScreen.doFullDraw = True
        if switch == 'p':
            screen = PlayScreen
        if switch == 'm':
            screen = MenuScreen
        if switch == 't':
            screen = TrainingScreen
        
        self.currentScreen = screen(self.appContext, self.switch_screen)

        self.appContext.doDisplayUpdate = True

    def event_loop(self):
        self.currentScreen.event_loop()

    def update_loop(self):
        self.currentScreen.update_loop()

    def draw(self):
        self.currentScreen.draw()

if __name__ == '__main__':
    pass