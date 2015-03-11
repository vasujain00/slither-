import pygame
import time
import random

pygame.init()
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
green=(0,155,0)
display_width=800
display_hieght=600
block_size=20
fps=20
AppleThickness=30
direction="right"
img=pygame.image.load('Untitled.png')
appleimg=pygame.image.load('apple.png')
smallFont=pygame.font.SysFont("comicsansms",25)
mediumFont=pygame.font.SysFont("comicsansms",50)
largeFont=pygame.font.SysFont("comicsansms",75)

def pause():
    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused=False

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()



        gameDisplay.fill(white)
        message_to_screen("paused",black,-100,size="large")
        message_to_screen("press c to continue or q to quit",black,25,size="medium")
        pygame.display.update()
        clock.tick(5)

def randAppleGen():
     randomAppleX=round(random.randrange(0,display_width-block_size))#/10.0)*10.0
     randomAppleY=round(random.randrange(0,display_hieght-block_size))#/10.0)*10.0
     return randomAppleX,randomAppleY

def score(score):
    text=smallFont.render("Score:"+str(score), True , black)
    gameDisplay.blit(text,[0,0])

def game_intro():

    intro=True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_c:
                    intro = False

                if event.key == pygame.K_q:
                    pygame.quit
                    quit()



    
                
        gameDisplay.fill(white)

        message_to_screen("Welcome to slither",green,-100,"large")
        message_to_screen("the objective of game is to eat red apples",black,-30,"small")
        message_to_screen("the more apples you eat the longer you get",black,10,"small")
        message_to_screen("if you run into yourself you will die fucker",black,50,"small")
        message_to_screen("press c to play or q to quit or p to pause",black,180,size="small")
        pygame.display.update()
        clock.tick(15)



def snake(block_size,snakeList):
    if  direction=="right":
        head=pygame.transform.rotate(img,270)

    if  direction=="left":
        head=pygame.transform.rotate(img,90)


    if  direction=="up":
        head=img


    if  direction=="down":
        head=pygame.transform.rotate(img,180)


    

        
    gameDisplay.blit(head,(snakeList[-1][0],snakeList[-1][1]))
    for XnY in snakeList[:-1]:
        pygame.draw.rect(gameDisplay,green,[XnY[0],XnY[1],block_size,block_size])

def text_Objects(text,color,size):
    if size=="small":
         textSurface=smallFont.render(text,True,color)
    elif size=="medium":
         textSurface=mediumFont.render(text,True,color)
    elif size=="large":
         textSurface=largeFont.render(text,True,color)
    


    return textSurface,textSurface.get_rect()
    
    
            
   

    
    
def message_to_screen(msg,color,y_displace=0,size="small"):
    textSurf,textRect= text_Objects(msg,color,size)
   
    textRect.center=(display_width/2),(display_hieght/2)+ y_displace
    gameDisplay.blit(textSurf,textRect)


pygame.display.set_caption('Slither')
icon=pygame.image.load('apple.png')
pygame.display.set_icon(icon)
gameDisplay=pygame.display.set_mode((display_width,display_hieght))
pygame.display.update()
clock=pygame.time.Clock()

def gameloop():
    global direction
    direction="right"
    gameExit=False
    gameOver=False
    lead_X=display_width/2
    lead_Y=display_hieght/2
    lead_x_change=10
    lead_y_change=0
     
    
    snakeList=[]
    snakeLenght=1
    randomAppleX,randomAppleY =randAppleGen()

    #randomAppleX=round(random.randrange(0,display_width-AppleThickness))#/10.0)*10.0
    #randomAppleY=round(random.randrange(0,display_hieght-AppleThickness))#/10.0)*10.0
    
    while not gameExit:
        while gameOver==True:
            gameDisplay.fill(red)
            message_to_screen("GAME OVER",white,-50,size="large")
            message_to_screen("press C to play Again or Q to Quit",black,50,size="medium")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    gameExit=True
                    gameOver=False

                
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        gameExit=True
                        gameOver=False

                    if event.key==pygame.K_c:
                        gameloop()



        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameExit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    direction="left"
                    lead_x_change=-block_size
                    lead_y_change=0
                    
                elif event.key==pygame.K_RIGHT:
                    direction="right"
                    lead_x_change=block_size
                    lead_y_change=0
                elif event.key==pygame.K_UP:
                    direction="up"
                    lead_y_change=-block_size
                    lead_x_change=0
                elif event.key==pygame.K_DOWN:
                    direction="down"
                    lead_y_change=block_size
                    lead_x_change=0


                elif event.key ==pygame.K_p:
                     pause()

                

            #if event.type==pygame.KEYUP:
                #f event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    #ead_x_change=0

            
        if lead_X >=display_width or lead_X<0 or lead_Y >=display_hieght or lead_Y <0:
          gameOver=True

        lead_X +=lead_x_change
        lead_Y +=lead_y_change
        






        
        #print(event)

        gameDisplay.fill(white)
      
        #pygame.draw.rect(gameDisplay,red,[randomAppleX,randomAppleY,AppleThickness,AppleThickness])
        gameDisplay.blit(appleimg,(randomAppleX, randomAppleY))
       
        snakeHead=[]
        snakeHead.append(lead_X)
        snakeHead.append(lead_Y)
        snakeList.append(snakeHead)
       
        if len(snakeList)>snakeLenght:
            del snakeList[0]


        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver=True


        
                
        snake(block_size,snakeList)   
            
            

        
        
        #gameDisplay.fill(red,rect=[200,200,50,50])

        score(snakeLenght-1)
        pygame.display.update()


##        if lead_X >=randomAppleX and lead_X <= randomAppleX +AppleThickness:
##             if lead_Y >=randomAppleY and lead_Y <= randomAppleY +AppleThickness:
##                 randomAppleX=round(random.randrange(0,display_width-block_size))#/10.0)*10.0
##                 randomAppleY=round(random.randrange(0,display_hieght-block_size))#/10.0)*10.0
##                 snakeLenght+=1
##    
           
        if lead_X > randomAppleX and lead_X < randomAppleX + AppleThickness or lead_X + block_size >randomAppleX and lead_X + block_size < randomAppleX + AppleThickness:
            if lead_Y >randomAppleX and lead_Y < randomAppleY + AppleThickness:
                
                randomAppleX,randomAppleY =randAppleGen()

                snakeLenght+=1


            elif lead_Y + block_size > randomAppleY and lead_Y + block_size < randomAppleY + AppleThickness:
                randomAppleX,randomAppleY =randAppleGen()

              
                snakeLenght+=1

                
                 
                 

                 
                 
                  
            


                 
                

            
            
              
              
                  
                  
                  

             

              
             
                  
             

            
              
              
            

        

        clock.tick(fps)



    pygame.quit()
    quit()

game_intro()
gameloop()
