from lib import *

Window.size = (360, 760)
# Window.fullscreen = 'auto'

gameButtons = """
MDRectangleFlatButton:
    fonty: 60
    text: 'REPLACE' 
    theme_text_color: 'Custom'
    text_color: [1, 1, 1, 1]
    md_bg_color: [0, .569, .918, 1]
    size_hint: (0,0)
    font_size: self.fonty
"""
# pos_hint: {'center_x': .5, 'center_y': .5}
gameLayoutPreset = """
GridLayout:
    cols: REPLACE
    rows: REPLACE
    spacing: 4
"""

progressPreset = """
MDProgressBar:
    id: pb
    value: 0
    min: 0
    max: 16
    pos_hint: {'center_x': .5, 'center_y': .09}
    size_hint_x: .8
    height: 20
"""

updateLabel = """
Label:
    text:'0'
    color: [0, 0.69, 1, 1]
    font_size: 40
    pos_hint:{'center_x': .5, 'center_y': .925}
    bold: True
"""

secondLabel = """
Label:
    text:'Timer:'
    color: [0, 0.69, 1, 1]
    font_size: 20
    pos_hint:{'center_x': .5, 'center_y': .97}
"""

thirdLabel = """
Label:
    text:'Current Score: 0'
    color: [0.251, 0.769, 1, 1]
    font_size: 20
    pos_hint:{'center_x': .5, 'center_y': .05}
"""
#
backgroundPreset = """
Widget:
    animated_color: (0.98, 0.98, 0.98, 1)
    canvas:
        Color:
            rgba: self.animated_color
        Rectangle:
            size: self.size
            pos: self.pos
"""

gridLayoutPreset = """
GridLayout:
    amountRows: 2
    row_force_default:True
    col_force_default:True
    col_default_width:100
    spacing:1
    row_default_height: ((root.height*0.77)/ (float(self.amountRows))) - 1
    pos: (root.width/2 -151, root.height/2-root.height + 290)
    height:self.minimum_height
    width:self.minimum_width
"""


#    pos_hint:{"x": 0.08, "y": -0.12}
#    size_hint:(1, 1)
#    pos: (root.width/2, root.height/2-root.height)
#    pos_hint:{"x": 0.5, "y": 0.5}


def randomNumbers(amount):
    """
    Generates a randomized order list of size argument\n

    :param amount: length of the list and the value of the highest number
    :type amount: int
    :return: list containing continuous ints from 1 to amount (inclusive) in a randomized order
    """
    listy = []
    for y in range(1, amount + 1):
        listy.append(y)
    random.shuffle(listy)
    return listy


class TableApp(MDApp):

    def pressed(self, l):
        print(l.text)
        global listy2
        global score

        if int(l.text) == listy2[0]:
            listy2.pop(0)
            score += 1
            print("CORRECT")
            self.progressbar.value += 1
            # assert isinstance(self.background.canvas, object)
            h = self.background.animated_color
            print(h)
            self.background.animated_color = (0, 0.784, 0.325, 1)
            animation1 = Animation(animated_color=(0.98, 0.98, 0.98, 1))
            animation1.start(self.background)
        else:
            print("INCORRECT")
            self.background.animated_color = (1, 0.09, 0.267, 1)
            animation2 = Animation(animated_color=(0.98, 0.98, 0.98, 1))
            animation2.start(self.background)

        print('score: ' + str(score))
        if score >= tiles:
            self.timer.cancel()
            self.labely2.text = ""
            self.labely.font_size = 20
            self.labely.text = "Final Time: " + self.labely.text + " seconds"
            self.labely3.text = str(tiles)
        else:
            self.labely3.text = "Current Score: " + str(int(listy2[0]) - 1)

    def on_start(self):
        self.timer = Clock.schedule_interval(self.updateLabel, 1)

    # def stop(self, *args):
    #    self.timer.cancel()

    def updateLabel(self, *args):
        updated = self.labely.text
        updated = int(updated)
        updated += 1
        updated = str(updated)
        self.labely.text = updated

    def build(self):
        global tiles
        screen = MDScreen()

        self.background = Builder.load_string(backgroundPreset)
        screen.add_widget(self.background)

        gameLayout = gameLayoutPreset.replace("REPLACE", str(int(math.sqrt(tiles))))
        gameLayout2 = Builder.load_string(gameLayout)

        cwidth = Window.width / 2 - 206
        cheight = Window.height / 2 + 110
        gameLayout2 = Builder.load_string(gridLayoutPreset)
        gameLayout2.cols = 3
        if tiles % 3 == 0:
            gameLayout2.rows = int(int(tiles / 3))
            gameLayout2.amountRows = int(int(tiles / 3))
        else:
            gameLayout2.rows = int(int(tiles / 3) + 1)
            gameLayout2.amountRows = int(int(tiles / 3) + 1)
        screen.add_widget(gameLayout2)

        myList = randomNumbers(tiles)
        for x in range(0, tiles):
            buttonText = str(myList[x])
            gameButtons2 = gameButtons.replace('REPLACE', buttonText)
            self.gameButton = Builder.load_string(gameButtons2)
            self.gameButton.bind(on_press=self.pressed)
            self.gameButton.fonty = int((104 - tiles))
            gameLayout2.add_widget(self.gameButton)

        self.labely = Builder.load_string(updateLabel)
        screen.add_widget(self.labely)

        self.labely2 = Builder.load_string(secondLabel)
        screen.add_widget(self.labely2)

        self.progressbar = Builder.load_string(progressPreset)
        self.progressbar.max = tiles
        screen.add_widget(self.progressbar)

        self.labely3 = Builder.load_string(thirdLabel)
        screen.add_widget(self.labely3)

        # self.window = gameLayout
        return screen


if __name__ == "__main__":
    tiles = int(input("Select Number of tiles: "))
    score = 0
    listy2 = []
    for z in range(1, tiles + 1):
        listy2.append(z)

    TableApp().run()
