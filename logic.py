import pyglet
from stager import stager
from window import Window as Window

def main(**kwargs):
    debug = kwargs.get('debug', False)
    # textureLib = loadTextures(debug)
    stager.loadWindow()
    stager.loadStage(stage='testStage', verbose=debug)
    #window = Window(width=400, height=300, caption='Blocks', resizable = True)
    #window.addModel(blocks['testBox'])
    pyglet.app.run()

if __name__ == '__main__':

    main(debug=True)