import pyglet
from pyglet.window import key

print "Welcome to the Pyglet powered Light Engine!"

# Constants
GAME_WIDTH  = 640
GAME_HEIGHT = 480
GAME_FPS    = 30

# Variables
dx          = 0
dy          = 0
speed       = 1

# Define window
window = pyglet.window.Window()


# Functions
def update(dt):
    global dx, dy
    bulb.x += dx
    bulb.y += dy
    
    
@window.event
def on_draw():
    window.clear()
    bg.draw()
    label.draw()
    bulb.draw()

@window.event
def on_key_press(symbol, modifiers):
    global dx, dy
    if symbol == key.SPACE:
        label.x = 0
        print "This works"
    if symbol == key.W:
        dy = speed
    if symbol == key.S:
        dy = -1 * speed
    if symbol == key.D:
        dx = speed
    if symbol == key.A:
        dx = -1 * speed

@window.event        
def on_key_release(symbol, modifiers):
    global dx, dy
    if symbol == key.W:
        dy = 0
    if symbol == key.S:
        dy = 0
    if symbol == key.D:
        dx = 0
    if symbol == key.A:
        dx = 0

# Actual code
bulb_img = pyglet.resource.image('Sprites/Lightbulb.png')
bulb     = pyglet.sprite.Sprite(bulb_img,64,64)

bg_img   = pyglet.resource.image('Sprites/BG_Grass.png')
bg       = pyglet.sprite.Sprite(bg_img,0,0)

label = pyglet.text.Label('Light engine',
                      font_name='Times New Roman',
                      font_size=36,
                      x=window.width//2, y=window.height//2,
                      anchor_x='center', anchor_y='center')
                      
pyglet.clock.schedule(update)
pyglet.app.run()
