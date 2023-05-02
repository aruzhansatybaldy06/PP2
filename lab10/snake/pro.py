import pygame 
import sys
from snake import game
import psycopg2
 
pygame.init()
display = pygame.display.set_mode((400, 500))
score_db = 0
class TextInput(pygame.sprite.Sprite):
    def __init__(self, x, y, width=100, height=50, color=(0, 0, 0),
                 bgcolor=(0,255,0), selectedColor=(255,255,255)):
        super().__init__()
        self.text_value = ""
        self.isSelected = False
        self.color = color
        self.bgcolor = bgcolor
        self.selectedColor = selectedColor
       
        self.font = pygame.font.SysFont("Verdana", 20)
        self.text = self.font.render(self.text_value, True, self.color)
        self.bg = pygame.Rect(x, y, width, height)
 
    def clicked(self, mousePos):
        if self.bg.collidepoint(mousePos):
            self.isSelected = not(self.isSelected)
            return True
        return False 
    
    def stop(self):
        self.isSelected = not(self.isSelected)

 
    def update_text(self, new_text):
        temp = self.font.render(new_text, True, self.color)
        if temp.get_rect().width >= (self.bg.width - 20):
            return
        self.text_value = new_text
        self.text = temp
                 
    def render(self, display):
        self.pos = self.text.get_rect(center = (self.bg.x + self.bg.width/2,
                                                self.bg.y + self.bg.height/2))
        if self.isSelected:
            pygame.draw.rect(display, self.selectedColor, self.bg)
        else:
            pygame.draw.rect(display, self.bgcolor, self.bg)
        display.blit(self.text, self.pos)
 
class CustomGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.current = None
     
    def current(self):
        return self.current
 
TextInputGroup = CustomGroup()
TextInputGroup.add(TextInput(x=100, y=100, width = 200))
 
ibeam = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_IBEAM)
 
def console():
    run = True

    while run:
        mouse_pos = pygame.mouse.get_pos()
        for textinput in TextInputGroup:
            textinput.update(mouse_pos)
            textinput.render(display)
        if TextInputGroup.current and TextInputGroup.current.bg.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(ibeam)
        else:
            pygame.mouse.set_cursor(pygame.cursors.Cursor())


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for textinput in TextInputGroup:
                    if textinput.clicked(mouse_pos): 
                        if TextInputGroup.current:
                            TextInputGroup.current.isSelected = False
                        textinput.isSelected = True
                        TextInputGroup.current = textinput
                        break
            if event.type == pygame.TEXTINPUT:
                TextInputGroup.current.update_text(TextInputGroup.current.text_value + event.text)
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    TextInputGroup.current.update_text(TextInputGroup.current.text_value[:-1])
                    
                if event.key == pygame.K_RETURN:
                    if TextInputGroup.current:
                        global name
                        name = TextInputGroup.current.text_value
                        print(name)
                    global score_db
                    score_db = game()
                    run = False
                    
    
        pygame.display.update()

def insert(username, scoredb):
    sql = """ INSERT INTO snake (username, score) VALUES(%s, %s); """
    conn = None

    try:
        conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="seidazym", port = 5432)

        cur = conn.cursor()

        cur.execute(sql, (username, scoredb))

        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()


    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    console()
    insert(name, score_db)