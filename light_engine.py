import numpy
import pyglet



class LightEngine(object):
    
    
    def __init__(self, width, height, sources, blocks):
        self.sources = sources
        self.blocks = blocks
        self.field = numpy.ones((height,width), dtype=bool)
        
    def update(self):
        source = self.sources[0]
        inds = numpy.indices(self.field.shape)
        inds[0] -= source.y
        inds[1] -= source.x
        angles = numpy.arctan2(inds[1],inds[0])
        radii = numpy.sqrt(inds[0]**2+inds[1]**2)
        for block in self.blocks:
            corners = numpy.array([[block.x,block.y],
                                   [block.x+block.width,block.y],
                                   [block.x,block.y+block.height],
                                   [block.x+block.width,block.y+block.height]])
            block_angles = numpy.arctan2(corners[:,0],corners[:,1])
            start_ang = block_angles.min()
            stop_ang = block_angles.max()
            shadow = numpy.logical_and(angles>start_ang,angles<stop_ang)
            shadow[radii<numpy.sqrt(block.x**2+block.y**2)] = False
            self.field[shadow] = False
    
    def return_field(self):
        return self.field
        
        
class dummy(object):
    
    def __init__(self, x=0, y=0, width=0, height=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
if __name__ == "__main__":
    from matplotlib import pyplot
    source = dummy(x=320, y=240)
    block = dummy(x=64, y=64, width=20, height=20)
    engine = LightEngine(640,480,[source],[block])
    engine.update()
    img = engine.return_field()
    pyplot.imshow(img)
    pyplot.plot(block.x,block.y,"g.")
    pyplot.plot(source.x,source.y,"k.")
    pyplot.show()
    
