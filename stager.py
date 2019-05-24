from window import Window as Window
import utils
import modeller

class Stager():
    def __init__(self, **kwargs):
        self.verbose = kwargs.get('verbose', False)
        self.blockList = utils.blockList

    def loadWindow(self, **kwargs):
        self.window = Window(
            width=      kwargs.get('width', 400),
            height=     kwargs.get('height', 300),
            caption=    kwargs.get('caption', 'Blocks'),
            resizable=  kwargs.get('resizeable', True)
            )

    def loadStage(self, **kwargs):
        verbose = kwargs.get('verbose', False)
        stageID = kwargs.get('stage', None)
        if not self.window:
            print('No window has been loaded!')
        elif stageID == None:
            print('No stage argument sent!')
        else:
            stage = utils.getStage(stageID, verbose=verbose)

            for y in range(len(stage["map"])):
                for z in range(len(stage["map"][y])):
                    for x in range(len(stage["map"][y][z])):
                        if self.blockList[stage["map"][y][z][x]] == self.blockList[0]:
                            continue
                        self.window.addModel(modeller.Model(
                            textures=utils.getBlockTexture(stage["map"][y][z][x]),
                            origin=[x*stage['scale'], y*stage['scale'], z*stage['scale']],
                            Figure=self.blockList[stage["map"][y][z][x]]['model'],
                            size = stage['scale'] * self.blockList[stage["map"][y][z][x]]['size']        
                            )
                        )
                        

        

stager = Stager(verbose=True)