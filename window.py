import pyglet
import pyglet.gl as gl
from pyglet.window import key
from player import Player as Player

class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_minimum_size(200, 150)
        self.timer = 0
        self.keys = key.KeyStateHandler()
        self.push_handlers(self.keys)
        self.mouse_lock = False

        pyglet.clock.schedule(self.update)

        self.models = []
        self.player = Player(speed=10, sensivity=16)
        gl.glEnable(gl.GL_DEPTH_TEST)
        gl.glClearColor(0.6,0.8,1,1)

    def setLock(self,state):
        self.lock = state
        self.set_exclusive_mouse(state)
    lock = False; mouse_lock = property(lambda self:self.lock,setLock)

    def Projection(self):
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
    def Model(self):
        gl.glMatrixMode(gl.GL_MODELVIEW)
        gl.glLoadIdentity()
    def set3d(self):
        self.Projection()
        gl.gluPerspective(50,self.width/self.height, 0.05,1000)
        self.Model()
    def push(self,pos,rot):
        gl.glPushMatrix()
        gl.glRotatef(-rot[0],1,0,0)
        gl.glRotatef(-rot[1],0,1,0)
        gl.glTranslatef(-pos[0],-pos[1],-pos[2],)

    def addModel(self, model):
        self.models.append(model)

    def on_mouse_motion(self, x, y, dx, dy):
        if self.mouse_lock:
            self.player.mouseMove(dx, dy)
    
    def on_key_press(self, KEY, MOD):
        if KEY == key.ESCAPE:
            self.close()
        elif KEY == key.E:
            self.mouse_lock = not self.mouse_lock

    def update(self,dt):
        self.timer += 1
        #if self.timer % 1 == 0:
         #   self.models[0].move([0.001,0.001,0.001])
        if self.timer % 60 == 0:
            print('Y rotation is: %s' % self.player.rotation[1])
            print(pyglet.clock.get_fps())
            for model in range(len(self.models)):
                print(('Model %s is in position ' % model) + str(self.models[model].getPosition()))
        self.player.keyPress(dt, self.keys)

    def on_draw(self):
        self.clear()
        self.set3d()
        self.push(self.player.position, self.player.rotation)
        for model in self.models:
            model.draw()
        gl.glPopMatrix()