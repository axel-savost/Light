import pyglet

print "Welcome to the Pyglet powered Light Engine!"

# Constants
GAME_WIDTH  = 640
GAME_HEIGHT = 480
GAME_FPS    = 30

# Variables
x           = 0
mod         = 1 

# Define window
window = pyglet.window.Window()


# Functions
def update(dt):
    global mod
    bulb.x += mod
    if bulb.x > GAME_WIDTH-32:
        mod = -1
    if bulb.x < 0:
        mod = 1
    
    
@window.event
def on_draw():
    window.clear()
    label.draw()
    bulb.draw()

# Actual code
bulb_img = pyglet.resource.image('Sprites/Lightbulb.png')
bulb     = pyglet.sprite.Sprite(bulb_img,64,64)

label = pyglet.text.Label('Light engine',
                      font_name='Times New Roman',
                      font_size=36,
                      x=window.width//2, y=window.height//2,
                      anchor_x='center', anchor_y='center')
                      
pyglet.clock.schedule(update)
pyglet.app.run()
