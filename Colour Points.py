# Short script that draws coloured squares on a click using PyGLet
# The colours of the squares are retrieved from the Hexbot API using the Requests library

import requests
import pyglet

window = pyglet.window.Window()
window.push_handlers(pyglet.window.event.WindowEventLogger())  # debugging purposes
col_array = []
pyglet.gl.glPointSize(20)


class ColourSquare:

    def __init__(self, inx, iny, incol):
        self.x = inx
        self.y = iny
        self.col = incol


def poll_colour():
    colour_json = requests.get('http://api.noopschallenge.com/hexbot').json()
    colhex = colour_json['colors'][0]['value']
    colhex = int(colhex[1:], 16)
    bm = 0xFF
    return [(colhex >> 4) & bm, (colhex >> 2) & bm, colhex & bm]


@window.event
def on_draw():
    window.clear()
    for square in col_array:
        pyglet.graphics.draw(1, pyglet.gl.GL_POINTS, ('v2f', (square.x, square.y)), ('c3B', square.col))


@window.event
def on_mouse_press(x, y, button, modifiers):
    new_square = ColourSquare(x, y, poll_colour())
    col_array.append(new_square)


if __name__ == '__main__':
    pyglet.app.run()
