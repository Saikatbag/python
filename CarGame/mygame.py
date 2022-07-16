import pygame 
pygame.init() 

grey = (119, 119, 119) 
black = (0, 0, 0)  
display = pygame.display.set_mode((800, 600)) 
bg = pygame.image.load("CarGame/img/bg.png")
bg = pygame.transform.scale(bg, (800, 600))

pygame.display.set_caption("Car Game")  
carimg = pygame.image.load("CarGame/img/car9.png")  
carimg = pygame.transform.scale(carimg, (100, 200))
car_width = 100
import time  
import random  


def policecar(police_startx, police_starty, police):  
    if police == 0: 
        police_come = pygame.image.load("CarGame/img/car2.png")  
        police_come = pygame.transform.scale(police_come, (100, 200))
        police_come = pygame.transform.rotate(police_come, 180)

    if police == 1: 
        police_come = pygame.image.load("CarGame/img/car3.png")  
        police_come = pygame.transform.scale(police_come, (100, 200))
        police_come = pygame.transform.rotate(police_come, 180)
    if police == 2:
        police_come = pygame.image.load("CarGame/img/car1.png")  
        police_come = pygame.transform.scale(police_come, (100, 200))
        police_come = pygame.transform.rotate(police_come, 180)
    if police == 3:
        police_come = pygame.image.load("CarGame/img/car4.png")  
        police_come = pygame.transform.scale(police_come, (100, 200))
        police_come = pygame.transform.rotate(police_come, 180)
    if police == 4:
        police_come = pygame.image.load("CarGame/img/car5.png") 
        police_come = pygame.transform.scale(police_come, (100, 200))
        police_come = pygame.transform.rotate(police_come, 180)
    if police == 5:
        police_come = pygame.image.load("CarGame/img/car6.png") 
        police_come = pygame.transform.scale(police_come, (100, 200))
        police_come = pygame.transform.rotate(police_come, 180)
    if police == 6:
        police_come = pygame.image.load("CarGame/img/car7.png") 
        police_come = pygame.transform.scale(police_come, (100, 200))
        police_come = pygame.transform.rotate(police_come, 180)
    if police == 7:
        police_come = pygame.image.load("CarGame/img/car8.png")  
        police_come = pygame.transform.scale(police_come, (100, 200))
        police_come = pygame.transform.rotate(police_come, 180)


    display.blit(police_come, (police_startx, police_starty))


def crash():
    message_display("Car Crashed", 400, 300) 
def sc_display(n):
    font = pygame.font.Font("CarGame/font/Handwriting.ttf", 20) 
    textsurf, textrect = text_object("CarPassing- " + str(n), font)  
    textrect.center = ((60), (20))  
    display.blit(textsurf, textrect) 




def message_display(text, x, y): 
    largetext = pygame.font.Font("font/Oranville.otf", 80) 
    textsurf, textrect = text_object(text, largetext) 
    textrect.center = ((x), (y)) 
    display.blit(textsurf, textrect)  
    pygame.display.update() 
    time.sleep(3) 
    loop() 


def text_object(text, font): 
    textsurface = font.render(text, True, black) 
    return textsurface, textsurface.get_rect()  


def background():
    display.blit(bg, (0, 0))
   


def car(x, y): 
    display.blit(carimg, (x, y)) 



def loop(): # all the function are called using this function
    scor = 0
    x = 350  
    y = 405  
    x_change = 0 
    y_change = 0  
    policecar_speed = 20  
    police = 0  
    police_width = 80  
    police_height = 160  
    police_startx = random.randrange(150, (650 - police_width))  
    police_starty = -600  


    bumped = False  # if game is not any problem to start
    while not bumped:  # game is start
        for event in pygame.event.get():  # if any input is given
            if event.type == pygame.QUIT:  # if quit input is given
                bumped = True		#game is stop
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_LEFT:  
                    x_change = -15 
                if event.key == pygame.K_RIGHT:  
                    x_change = 15 
            if event.type == pygame.KEYUP:  
                x_change = 0
        x += x_change


        display.fill(grey)   
        background()
        
        

        police_starty -= (policecar_speed / 4)  
        policecar(police_startx, police_starty, police)  
        police_starty += policecar_speed  
        car(x, y)  
        sc_display(scor)
        if x < 150 or x > 650 - car_width:  
            bumped=True				
            crash()  
            scor = 0
        if police_starty > 600: 
            police_starty = 0 - police_height  
            police_startx = random.randrange(150, 550)  
            police = random.randrange(0, 7)  
            scor = scor + 1
            if scor%5 == 0:
                policecar_speed +=1
           
           


        if y < police_starty + police_height:  
            if x > police_startx and x < police_startx + police_width or x + car_width > police_startx and x + car_width < police_startx + police_width:
                crash()  # crash the car
                scor = 0



        pygame.display.update()  # update the display


loop()  # call the loop function
pygame.quit()  # package is stop
quit()  