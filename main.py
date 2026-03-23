import pyglet
import json
from pyglet import shapes
from pyglet.window import mouse
from pyglet.window import key

batch = pyglet.graphics.Batch()
display = pyglet.display.get_display()
screen = display.get_default_screen()
W = screen.width
H = screen.height
circles = []
window = pyglet.window.Window(width=W, height=H, caption='Rugby Call Planner')
batch = pyglet.graphics.Batch()

rw, rh = 572, 400 # 1.43:1 ratio for rugby pitch
rx, ry = W // 2 + rw // 4, H // 2 - rh // 2
p_radius = 10 # player radius
px, py = 0, 0

rect = shapes.BorderedRectangle(rx, ry, rw, rh, border=4, color=(0,0,0), border_color=(255,255,255), batch=batch)
top_line = shapes.Line(rx, ry + rh * 0.85, rx + rw, ry + rh * 0.85, thickness=2, color=(255,255,255), batch=batch)
mid_line = shapes.Line(rx + rw // 2, ry + rh * 0.85, rx + rw // 2, ry, thickness=2, color=(255,255,255), batch=batch)
fm_line = shapes.Line(rx + rw // 2.5, ry + rh * 0.65, rx + rw - rw // 2.5, ry + rh * 0.65, thickness=2, color=(255,255,255), batch=batch)
tm_line = shapes.Line(rx + rw // 2.5, ry + rh * 0.2, rx + rw - rw // 2.5, ry + rh * 0.2, thickness=2, color=(255,255,255), batch=batch)

def load_call(filename, play):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data[play]

def apply_call(play_name):
    targets = load_call('calls.json', play_name)
    for circle, target in zip(b_player, targets):
        circle.target_x = target['tx']
        circle.target_y = target['ty']


class rPlayer:
    def __init__(self, x, y, label_text):
        self.circle = shapes.Circle(x, y, 10, color=(255, 0, 0), batch=batch)
        self.label = pyglet.text.Label(
            label_text,
            font_size=12,
            color=(255, 255, 255),
            x=x, y=y,
            anchor_x='center', anchor_y='center',
            batch=batch)


class bPlayer:
    def __init__(self, x, y, label_text, target_x=None, target_y=None, speed=200):
        self.circle = shapes.Circle(x, y, 10, color=(0, 0, 255), batch=batch)
        self.label = pyglet.text.Label(
            label_text,
            font_size=12,
            color=(255, 255, 255),
            x=x, y=y,
            anchor_x='center', anchor_y='center',
            batch=batch)
        self.target_x = target_x if target_x is not None else x
        self.target_y = target_y if target_y is not None else y
        self.speed = speed 

    def update(self, dt):
        dx = self.target_x - self.circle.x
        dy = self.target_y - self.circle.y
        dist = (dx**2 + dy**2) ** 0.5

        if dist < 2:
            self.circle.x = self.target_x
            self.circle.y = self.target_y
        else:
            self.circle.x += (dx / dist) * self.speed * dt
            self.circle.y += (dy / dist) * self.speed * dt
        
        self.label.x = self.circle.x
        self.label.y = self.circle.y

r_player = [
    rPlayer(rx + rw // 2.2, ry + rh * 0.65 - 2 * p_radius, "1"),
    rPlayer(rx + rw // 2.2, ry + rh * 0.65 - 5 * p_radius, "2"),
    rPlayer(rx + rw // 2.2, ry + rh * 0.65 - 8 * p_radius, "3"),
    rPlayer(rx + rw // 2.2, ry + rh * 0.65 - 11 * p_radius, "4"),
    rPlayer(rx + rw // 2.2, ry + rh * 0.65 - 14 * p_radius, "5")
]

b_player = [
    bPlayer(rx + rw - rw // 2.2, ry + rh * 0.65 - 2 * p_radius, "1"),
    bPlayer(rx + rw - rw // 2.2, ry + rh * 0.65 - 5 * p_radius, "2"),
    bPlayer(rx + rw - rw // 2.2, ry + rh * 0.65 - 8 * p_radius, "3"),
    bPlayer(rx + rw - rw // 2.2, ry + rh * 0.65 - 11 * p_radius, "4"),
    bPlayer(rx + rw - rw // 2.2, ry + rh * 0.65 - 14 * p_radius, "5")
]

def update(dt):
    for player in b_player:
        player.update(dt)

pyglet.clock.schedule_interval(update, 1/60)

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key._1:
        apply_call('Reverse_67')

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        circle = shapes.Circle(x, y, 10, color=(50, 225, 30), batch=batch)
        circles.append(circle)
        print(x,y)

    elif button == mouse.RIGHT:
        
        for circle in circles[:]:  
            dx = x - circle.x
            dy = y - circle.y
            if dx*dx + dy*dy <= circle.radius * circle.radius:
                circles.remove(circle)
                circle.delete()  
                break  

@window.event
def on_draw():
    window.clear()
    batch.draw()

pyglet.app.run()