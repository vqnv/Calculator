import pygame
import sys
pygame.font.init()
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("Glorious Morning 2.mp3")
pygame.mixer.music.set_volume(0.1)
"""
These are variables used during the process
"""
before_click = (15, 15, 15)
after_click = (1, 1, 1)
time = pygame.time.Clock()
string = ""
final_answer = False
music = False
music1 = False


def checkstring(x, button):
    if len(x) < 20:
        return x + button
    return x
def checksong():
    global music
    if music:
        pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.pause()

def draw_text(text, font, rect):
    text_surface = font.render(text, True, "white")  # Render the text onto a surface
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)


screen = pygame.display.set_mode((400, 550))
running = True
font = pygame.font.SysFont("Arial", 36)  # Initialize the font object


"""
Making all the number buttons, and the list that stores both number BUTTONS and the string integer for that
"""

button1 = pygame.Rect(0, 460, 80, 80)
pygame.draw.rect(screen, before_click, button1)
button2 = pygame.Rect(100, 460, 80, 80)
pygame.draw.rect(screen, before_click, button2)
button3 = pygame.Rect(200, 460, 80, 80)
pygame.draw.rect(screen, before_click, button3)
button4 = pygame.Rect(0, 360, 80, 80)
pygame.draw.rect(screen, before_click, button4)
button5 = pygame.Rect(100, 360, 80, 80)
pygame.draw.rect(screen, before_click, button5)
button6 = pygame.Rect(200, 360, 80, 80)
pygame.draw.rect(screen, before_click, button6)
button7 = pygame.Rect(0, 260, 80, 80)
pygame.draw.rect(screen, before_click, button7)
button8 = pygame.Rect(100, 260, 80, 80)
pygame.draw.rect(screen, before_click, button8)
button9 = pygame.Rect(200, 260, 80, 80)
pygame.draw.rect(screen, before_click, button9)
"""
Operator Buttons
"""
add = pygame.Rect(290, 188, 95, 65)
pygame.draw.rect(screen, (140, 140, 140), add)
divide = pygame.Rect(290, 260, 95, 65)
pygame.draw.rect(screen, (140, 140, 140), divide)
multiply = pygame.Rect(290, 332, 95, 65)
pygame.draw.rect(screen, (140, 140, 140), multiply)
subtract = pygame.Rect(290, 404, 95, 65)
pygame.draw.rect(screen, (140, 140, 140), subtract)
equals = pygame.Rect(290, 476, 95, 65)
pygame.draw.rect(screen, (140, 140, 140), equals)

"""
Backspace/CE/Output/Volume Buttons
"""
backspace = pygame.Rect(200, 188, 80, 65)
pygame.draw.rect(screen, before_click, backspace)
CE = pygame.Rect(100, 188, 80, 65)
pygame.draw.rect(screen, before_click, CE)
Output = pygame.Rect(0, 30, 400, 130)
pygame.draw.rect(screen, before_click, Output)
Song = pygame.Rect(0, 188, 80, 65)
pygame.draw.rect(screen, before_click, Song)


"""
The full screen for the entire project. This is the lighter background, with the buttons in front
"""
full_screen = pygame.Rect(0, 0, 400, 550)
pygame.draw.rect(screen, (40, 40, 40), full_screen)
"""
The entire list of the all values, and string values of the integer
"""
coords = {
    "1": [0, 460, 80, 80],
    "2": [100, 460, 80, 80],
    "3": [200, 460, 80, 80],
    "4": [0, 360, 80, 80],
    "5": [100, 360, 80, 80],
    "6": [200, 360, 80, 80],
    "7": [0, 260, 80, 80],
    "8": [100, 260, 80, 80],
    "9": [200, 260, 80, 80],
    "÷": [290, 260, 95, 65],
    "x": [290, 332, 95, 65],
    "-": [290, 404, 95, 65],
    "+": [290, 188, 95, 65],
    "=": [290, 476, 95, 65],
    "CE": [100, 188, 80, 65],
    "<>": [200, 188, 80, 65],
    "Output": [0, 0, 360, 130],
    ">>": [0, 188, 80, 65]
}
buttons = {"1": button1, "2": button2, "3": button3,
           "4": button4, "5": button5, "6": button6,
           "7": button7, "8": button8, "9": button9,
           "÷": divide, "x": multiply, "-": subtract,
           "=": equals, "+": add, "<>": backspace,
           "CE": CE, "Output": Output, ">>": Song}
"""
This is the command line used for all the buttons pressed and time flow of the program
"""
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        # This is the line if there is a click
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for button in buttons:
                # If the click does not equal equals, and is a click
                if buttons[button].collidepoint(event.pos) and button != "=" and button != "CE" and button != "<>" and button != ">>":
                    # Change the color of the rectangle
                    pygame.draw.rect(screen, after_click, buttons[button])
                    # Add the button to the string
                    if final_answer:
                        string = button
                        final_answer = False
                    else:
                        string = checkstring(string, button)
                    time.tick(25)
                    pygame.display.update()
                    continue
            # If the button pressed is the equal sign
            if buttons["="].collidepoint(event.pos):
                # Replace the normal string into a final string, replacing non operand "human" operators
                final_string = string.replace("÷", "/")
                final_string = final_string.replace("x", "*")
                # Evaluate the final string and print it
                try:
                    answer = eval(final_string)
                    string = str(round(float(answer), 3))
                    final_answer = True
                except OverflowError:
                    string = "big number u suck"
                    final_answer = True
                except SyntaxError:
                    string = "u suck"
                    final_answer = True

            elif buttons["<>"].collidepoint(event.pos):
                string = string[:-1]
            elif buttons["CE"].collidepoint(event.pos):
                string = ""
            elif buttons[">>"].collidepoint(event.pos):
                if not music:
                    music = True
                    if not music1:
                        pygame.mixer.music.play(loops=-1)
                        music1 = True
                    checksong()
                else:
                    music = False
                    checksong()
        # For the first colour change if the mouse was clicked, then it would switch colours.
        # For the next loop, nothing has been clicked, so it will switch back
        elif event.type != pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                pygame.draw.rect(screen, before_click, buttons[button])
    for button, rect in buttons.items():
        if button == "Output":
            draw_text(string, font, rect)
        else:
            draw_text(button, font, rect)
    pygame.display.update()

