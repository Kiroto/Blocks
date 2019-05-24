import math
from pyglet.window import key

class Player:
    def __init__(self, **kwargs):

        self.position = kwargs.get('position', [0, 0, 0])
        self.rotation = kwargs.get('rotation', [0, 0])
        self.speed = kwargs.get('speed', 5)
        self.sensivity = kwargs.get('sensivity', 8)

    def mouseMove(self, dx, dy):
        dx /= self.sensivity
        dy /= self.sensivity
        self.rotation[0] += dy
        self.rotation[1] -= dx
        if self.rotation[1] >= 360:
            self.rotation[1] -= 360
        elif self.rotation[1] <= -360:
            self.rotation[1] += 360
        if self.rotation[0] > 90:
            self.rotation[0] = 90
        elif self.rotation[0] < -90:
            self.rotation[0] = -90

    def keyPress(self, dt, keys):
        s = dt*5
        rotationY = -self.rotation[1]/180*math.pi
        # print(math.sin(rotationY))
        dx = s*math.sin(rotationY) # Number between -1 and 1, how east im facing
        dz = s*math.cos(rotationY) # How north im facing
        if keys[key.W]:
            self.position[0]+=dx
            self.position[2]-=dz
        if keys[key.A]:
            self.position[0]-=dz
            self.position[2]-=dx
        if keys[key.S]:
            self.position[0]-=dx
            self.position[2]+=dz
        if keys[key.D]:
            self.position[0]+=dz
            self.position[2]+=dx

        if keys[key.SPACE]:
            self.position[1] += s

        if keys[key.LSHIFT]:
            self.position[1] -= s