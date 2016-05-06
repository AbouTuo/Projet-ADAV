"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
 
Show everything we can pull off the joystick
"""
import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
class TextPrint(object):
    """
    This is a simple class that will help us print to the screen
    It has nothing to do with the joysticks, just outputting the
    information.
    """
    def __init__(self):
        """ Constructor """
        self.reset()
        self.x_pos = 10
        self.y_pos = 10
        self.font = pygame.font.Font(None, 20)
 
    def print(self, my_screen, text_string):
        """ Draw text onto the screen. """
        text_bitmap = self.font.render(text_string, True, BLACK)
        my_screen.blit(text_bitmap, [self.x_pos, self.y_pos])
        self.y_pos += self.line_height
 
    def reset(self):
        """ Reset text to the top of the screen. """
        self.x_pos = 10
        self.y_pos = 10
        self.line_height = 15
 
    def indent(self):
        """ Indent the next line of text """
        self.x_pos += 10
 
    def unindent(self):
        """ Unindent the next line of text """
        self.x_pos -= 10
 
 
pygame.init()
 
# Set the width and height of the screen [width,height]
size = [500, 500]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Buttons list")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Initialize the joysticks
pygame.joystick.init()
 
# Get ready to print
textPrint = TextPrint()
import serial
ser = serial.Serial("COM4",timeout=1,baudrate=115200)
print(ser)
value='0'
import time
dt=0.01
# -------- Main Program Loop -----------
while not done:
    # EVENT PROCESSING STEP
    textPrint.print(screen, "Number of joysticks: {}".format(1))
    textPrint.indent()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    value_axe0='D'+str(-int(joystick.get_axis(0)*250))
    ser.write(value_axe0.encode('ascii'))
    time.sleep(dt)


    value_axe1='C'+str(-int(joystick.get_axis(1)*250))
    ser.write(value_axe1.encode('ascii'))
    print(value_axe1)
    time.sleep(dt)

    
    value_axe2='L'+str(-int(joystick.get_axis(2)*250))
    ser.write(value_axe2.encode('ascii'))
    time.sleep(dt)


    value_btnA='A'+str(joystick.get_button(0))
    ser.write(value_btnA.encode('ascii'))
    time.sleep(dt)


    value_btnB='B'+str(joystick.get_button(1))
    ser.write(value_btnB.encode('ascii'))
    time.sleep(dt)


    value_btnX='X'+str(joystick.get_button(2))
    ser.write(value_btnX.encode('ascii'))
    time.sleep(dt)


    value_btnY='Y'+str(joystick.get_button(3))
    ser.write(value_btnY.encode('ascii'))
    time.sleep(dt)


    value_btn_start='S'+str(joystick.get_button(7))
    ser.write(value_btn_start.encode('ascii'))
    time.sleep(dt)

    
            
        
                
                
    screen.fill(WHITE)
    textPrint.reset()
 

    name = joystick.get_name()
    textPrint.print(screen, "Joystick name: {}".format(name))

    axes = joystick.get_numaxes()
    textPrint.print(screen, "Number of axes: {}".format(axes))
    textPrint.indent()

    for i in range(axes):
        axis = joystick.get_axis(i)
        textPrint.print(screen, "Axis {} value: {:>6.3f}".format(i, axis))
    textPrint.unindent()

    buttons = joystick.get_numbuttons()
    textPrint.print(screen, "Number of buttons: {}".format(buttons))
    textPrint.indent()

    for i in range(buttons):
        button = joystick.get_button(i)
        textPrint.print(screen, "Button {:>2} value: {}".format(i, button))
    textPrint.unindent()

    # Hat switch. All or nothing for direction, not like joysticks.
    # Value comes back in an array.
    hats = joystick.get_numhats()
    textPrint.print(screen, "Number of hats: {}".format(hats))
    textPrint.indent()

    for i in range(hats):
        hat = joystick.get_hat(i)
        textPrint.print(screen, "Hat {} value: {}".format(i, str(hat)))
    textPrint.unindent()

    textPrint.unindent()

    pygame.display.flip()
 
# Close the window and quit.
pygame.quit()
