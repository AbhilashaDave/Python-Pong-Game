import simplegui
import random
# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HALF_WIDTH = WIDTH / 2
HEIGHT = 400  
HALF_HEIGHT = HEIGHT / 2
ball_radius = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
LEFT = False
RIGHT = True
#score globals
score1 = 0
score2 = 0
#paddles
pad1_pos = HEIGHT / 2.5
pad2_pos = HEIGHT / 2.5
pad1_vel = 0
pad2_vel = 0
pad_vel = 5
# initialize ball_pos and ball_vel for new bal in middle of table
ball_pos = [HALF_WIDTH, HALF_HEIGHT]
ball_vel = [0,1]

def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [HALF_WIDTH, HALF_HEIGHT]   
    ball_vel[0] = -random.randrange(100,200) / 100
    if direction == True:
        ball_vel[0] *= -1
    ball_vel[1] = -random.randrange(100, 200) / 100

def new_game():
    global pad1_pos, pad2_pos # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    spawn_ball(0)
    pad1_pos = HEIGHT / 2.5
    pad2_pos = HEIGHT / 2.5

def draw(canvas):
    global score1, score2, pad1_pos, pad2_pos, ball_pos, ball_vel, ball_radius, PAD_HEIGHT
 
       
    # draw mid line and gutters
    canvas.draw_line([HALF_WIDTH, 0],[HALF_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
       
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
   
    if ball_pos[0] <= (ball_radius + PAD_WIDTH) or ball_pos[0] >= (WIDTH - PAD_WIDTH - ball_radius):       
        ball_vel[0] *= -1
       
        if (ball_pos[0] > HALF_WIDTH):            
            if (ball_pos[1] < pad2_pos or ball_pos[1] > pad2_pos + PAD_HEIGHT):
                score1 += 1
                spawn_ball(LEFT)
            else: ball_vel[0] += .1 * ball_vel[0]
           
        if (ball_pos[0] < HALF_WIDTH):
            if (ball_pos[1] < pad1_pos or ball_pos[1] > pad1_pos + PAD_HEIGHT ):
                score2 += 1
                spawn_ball(RIGHT)
            else: ball_vel[0] += .1 * ball_vel[0]
       
    if ball_pos[1] <= ball_radius or ball_pos[1] >= (HEIGHT - ball_radius):
        ball_vel[1] *= -1
   
    # draw scores
    canvas.draw_text(str(score1), [225, 100], 60, "white")   
    canvas.draw_text(str(score2), [350, 100], 60, "white")
           
    # draw ball
    canvas.draw_circle(ball_pos, ball_radius, 2, "white", "white")
    # update paddle's vertical position, keep paddle on the screen
    global pad1_vel, pad2_vel
   
    if (pad1_pos <= HEIGHT - PAD_HEIGHT and pad1_vel > 0) or (pad1_pos >= 0 and pad1_vel < 0) :
        pad1_pos += pad1_vel   
    elif (pad2_pos <= HEIGHT - PAD_HEIGHT and pad2_vel > 0) or (pad2_pos >= 0 and pad2_vel < 0) :
        pad2_pos += pad2_vel 
    # draw paddles
    canvas.draw_polygon([[0, pad1_pos], [PAD_WIDTH, pad1_pos],[PAD_WIDTH, (pad1_pos) + PAD_HEIGHT ],[0, (pad1_pos) + PAD_HEIGHT]],1, "green", "blue")
    canvas.draw_polygon([[WIDTH, pad2_pos], [WIDTH - PAD_WIDTH, pad2_pos], [WIDTH - PAD_WIDTH, pad2_pos + PAD_HEIGHT], [WIDTH, pad2_pos + PAD_HEIGHT]],1, "green", "red")
    # determine whether paddle and ball collide   
   
def keyup(key):
    global pad1_vel, pad2_vel
    #player1
    if key == simplegui.KEY_MAP["s"]:
        pad1_vel = 0
    elif key == simplegui.KEY_MAP["x"]:
        pad1_vel = 0
       
    #player2
    if key == simplegui.KEY_MAP["down"]:
        pad2_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        pad2_vel = 0
def keydown(key):
    global pad1_vel, pad2_vel, pad_vel  
    #player1   
    if key == simplegui.KEY_MAP["s"]:
        pad1_vel = -pad_vel    
    elif key == simplegui.KEY_MAP["x"]:
        pad1_vel = pad_vel 
   
    #player2
    if key == simplegui.KEY_MAP["down"]:
        pad2_vel = pad_vel   
    elif key == simplegui.KEY_MAP["up"]:
        pad2_vel = -pad_vel
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 200)
# start frame
new_game()
frame.start()
