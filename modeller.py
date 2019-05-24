import pyglet
import pyglet.gl as gl

class Block:
    def __init__(self, textures, origin = [0, 0, 0], size = 1, rot = [0,0]):
        self.batch = pyglet.graphics.Batch()
        self.origin = origin
        self.size = size
        self.tex = [] # Used by the drawing method
        self.updateTextures(textures)
        self.reloadTextures()

    def updateTextures(self, textures):
        if len(textures) == 1:
            for _ in range(6):
                self.tex.append(textures[0])
        
        elif len(textures) == 2:
            self.tex.append(textures[0])
            for _ in range(4):
                self.tex.append(textures[1])
            self.tex.append(textures[0])

        elif len(textures) == 3:
            self.tex.append(textures[0])
            for _ in range(4):
                self.tex.append(textures[1])
            self.tex.append(textures[2])

        elif len(textures) == 4 or len(textures) == 5:
            self.tex.append(textures[0])
            for _ in range(2):
                self.tex.append(textures[1])
                self.tex.append(textures[2])
            self.tex.append(textures[3])
        
        elif len(textures) == 6:
            for texture in textures:
                self.tex.append(texture)
        
        else:
            raise "Invalid Amount of Textures %s" % len(textures) 

        assert len(self.tex) == 6

    def reloadTextures(self):
        self.batch = pyglet.graphics.Batch()
        for i in range(6):
            self.batch.add(4, gl.GL_QUADS, self.tex[i], ('v3f',(self.toFigure(i))), ('t2f',(0,0,1,0,1,1,0,1)))

    def sideQuer(self, side):
        return [[[self.size, self.size, 0], [0, self.size, 0], [0, self.size, self.size], [self.size, self.size, self.size]], # Top
                [[0, 0, self.size], [self.size, 0, self.size], [self.size, self.size, self.size], [0, self.size, self.size]], # North
                [[0, 0, 0], [0, 0, self.size],[0, self.size, self.size], [0, self.size, 0]], # East
                [[self.size, 0, 0], [0, 0, 0], [0, self.size, 0], [self.size, self.size, 0]], # South
                [[self.size, 0, self.size], [self.size, 0, 0], [self.size, self.size, 0], [self.size, self.size, self.size]], # West
                [[0, 0, 0],[self.size, 0, 0],[self.size, 0, self.size], [0, 0, self.size]]][side] # Bottom

    def toFigure(self, side):
        sideAdd = self.sideQuer(side)
        return (self.origin[0]+sideAdd[0][0],self.origin[1]+sideAdd[0][1],self.origin[2]+sideAdd[0][2],
                self.origin[0]+sideAdd[1][0],self.origin[1]+sideAdd[1][1],self.origin[2]+sideAdd[1][2],
                self.origin[0]+sideAdd[2][0],self.origin[1]+sideAdd[2][1],self.origin[2]+sideAdd[2][2],
                self.origin[0]+sideAdd[3][0],self.origin[1]+sideAdd[3][1],self.origin[2]+sideAdd[3][2])

class Wedge:
    def __init__(self, textures, origin = [0, 0, 0], size = 1, rot = [0,0]): # 0 is Top, 1 is North, 2 is East, 3 is West, 4 is Bottom
        self.batch = pyglet.graphics.Batch()
        self.origin = origin
        self.size = size
        self.rot = [rot[0]%4, rot[1]%6]
        self.tex = [] # Used by the drawing method
        self.updateTextures(textures)
        self.reloadTextures()
    
    def sideQuer(self, side):
        if self.rot[0] == 0:
            quer = [[[self.size, 0, 0], [0, 0, 0], [0, self.size, self.size], [self.size, self.size, self.size]], # Top
                    [[0, 0, self.size], [self.size, 0, self.size], [self.size, self.size, self.size], [0, self.size, self.size]], # North
                    [[0, 0, self.size], [0, 0, 0], [0, 0, self.size], [0, self.size, self.size]], # East
                    [[self.size, 0, self.size], [self.size, 0, 0], [self.size, 0, self.size], [self.size, self.size, self.size]], # West
                    [[0, 0, 0],[self.size, 0, 0],[self.size, 0, self.size], [0, 0, self.size]]] # Bottom
        
        elif self.rot[0] == 1:
            quer = [[[self.size, self.size, 0], [0, 0, 0], [0, 0, self.size], [self.size, self.size, self.size]], # Top
                    [[self.size, 0, self.size], [self.size, 0, 0], [self.size, self.size, 0], [self.size, self.size, self.size]], # North
                    [[self.size, 0, self.size], [0, 0, self.size], [self.size, 0, self.size], [self.size, self.size, self.size]], # East
                    [[self.size, 0, 0], [0, 0, 0], [self.size, 0, 0], [self.size, self.size, 0]], # West
                    [[0, 0, 0],[self.size, 0, 0],[self.size, 0, self.size],[0, 0, self.size]]] # Bottom
        
        elif self.rot[0] == 2:
            quer = [[[self.size, self.size, 0], [0, self.size, 0], [0, 0, self.size], [self.size, 0, self.size]], # Top
                    [[0, 0, 0], [self.size, 0, 0], [self.size, self.size, 0], [0, self.size, 0]], # North
                    [[self.size, 0, 0], [self.size, 0, self.size], [self.size, 0, 0], [self.size, self.size, 0]], # East
                    [[0, 0, 0], [0, 0, self.size], [0, 0, 0], [0, self.size, 0]], # West
                    [[0, 0, 0],[self.size, 0, 0],[self.size, 0, self.size], [0, 0, self.size]]] # Bottom

        elif self.rot[0] == 3:
            quer = [[[self.size, 0, 0], [0, self.size, 0], [0, self.size, self.size], [self.size, 0, self.size]], # Top
                    [[0, 0, self.size], [0, 0, 0], [0, self.size, 0], [0, self.size, self.size]], # North
                    [[0, 0, 0], [0, self.size, 0], [self.size, 0, 0], [self.size, 0, 0]], # East
                    [[0, 0, self.size], [0, self.size, self.size], [self.size, 0, self.size], [self.size, 0, self.size]], # West
                    [[0, 0, 0],[self.size, 0, 0],[self.size, 0, self.size],[0, 0, self.size]]] # Bottom

        return quer[side]

    def toFigure(self, side):
        sideAdd = self.sideQuer(side)
        return (self.origin[0]+sideAdd[0][0],self.origin[1]+sideAdd[0][1],self.origin[2]+sideAdd[0][2],
                self.origin[0]+sideAdd[1][0],self.origin[1]+sideAdd[1][1],self.origin[2]+sideAdd[1][2],
                self.origin[0]+sideAdd[2][0],self.origin[1]+sideAdd[2][1],self.origin[2]+sideAdd[2][2],
                self.origin[0]+sideAdd[3][0],self.origin[1]+sideAdd[3][1],self.origin[2]+sideAdd[3][2])

    def updateTextures(self, textures):
        if len(textures) == 1:
            for _ in range(5):
                self.tex.append(textures[0])
        
        elif len(textures) == 2:
            self.tex.append(textures[0])
            for _ in range(4):
                self.tex.append(textures[1])

        elif len(textures) == 3:
            self.tex.append(textures[0])
            for _ in range(3):
                self.tex.append(textures[1])
            self.tex.append(textures[2])

        elif len(textures) == 4:
            self.tex.append(textures[0])
            self.tex.append(textures[1])
            for _ in range(2):
                self.tex.append(textures[2])
            self.tex.append(textures[1])
        
        elif len(textures) == 5:
            for texture in textures:
                self.tex.append(texture)
        
        else:
            raise "Invalid Amount of Textures %s" % len(textures) 

        assert len(self.tex) == 5

    def reloadTextures(self):
        self.batch = pyglet.graphics.Batch()
        for i in range(5):
            self.batch.add(4, gl.GL_QUADS, self.tex[i], ('v3f',(self.toFigure(i))), ('t2f',(0,0,1,0,1,1,0,1)))

class Model:
    def __init__(self, **kwargs):
        Figure = kwargs.get('Figure', None)
        origin = kwargs.get('origin', [0, 0, 0])
        size = kwargs.get('size', 1)
        rotation = kwargs.get('rotation', [0, 0])
        textures = kwargs.get('textures', None)

        if textures != None:
            if Figure == 'Block':
                self.Figure = Block(textures, origin, size, rotation)
            elif Figure == 'Wedge':
                self.Figure = Wedge(textures, origin, size, rotation)
            else:
                print("You need to specify a Figure whenever you're creating a model!")
        else:
            print("You can't make a spriteless Figure")
    
    def update(self):
        self.Figure.reloadTextures()

    def move(self, newPos=[0,0,0]):
        for i in range(len(newPos)):
            self.Figure.origin[i] += newPos[i]
        self.update()

    def setPosition(self, newPos):
        for i in range(len(newPos)):
            self.Figure.origin[i] = newPos[i]
        self.update()

    def rotate(self, amount=0):
        self.Figure.rot[0] = (self.Figure.rot[0] + amount) % 4
        self.update()

    def draw(self):
        self.Figure.batch.draw()

    def getPosition(self):
        return self.Figure.origin

# def makePyTexture(file):
#     tex = pyglet.image.load(file).texture
#     gl.glTexParameterf(gl.GL_TEXTURE_2D,gl.GL_TEXTURE_MIN_FILTER,gl.GL_NEAREST)
#     gl.glTexParameterf(gl.GL_TEXTURE_2D,gl.GL_TEXTURE_MAG_FILTER,gl.GL_NEAREST)
#     return pyglet.graphics.TextureGroup(tex)

# def packTextures(textureLib, textureNames):
#     textures = []
#     for name in textureNames:
#         textures.append(makePyTexture(textureLib[name]))
#     return textures

# textureLib = loadTextures()

# pyTextures = {}

# def reloadPyTextures(**kwargs):
#     loadingPyTextures = utils.pyPackTextures(**kwargs)
#     return loadingPyTextures


# pyTextures = reloadPyTextures(debug=True)
# # def generateFigureList(blockList):
# #     for block in blockList:
# #         if block

# blocks = {
#     'woodBox': Model(pyTextures['woodBox'], Block),
#     'testBox': Model(pyTextures['testBox'], Block)
#     }