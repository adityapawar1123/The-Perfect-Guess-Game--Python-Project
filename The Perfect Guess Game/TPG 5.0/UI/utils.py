import pygame
import os
pygame.mixer.init()

UI_path = os.path.dirname(os.path.abspath(__file__))
TPG_path = os.path.dirname(UI_path)
sound_effect_path = os.path.join(TPG_path, "audio", "sound_effect")

class Button : 

   def __init__(self, img1, img2, img3, posn_percentage, screen, screen_width, screen_height) : 
      self.img1 = pygame.image.load(os.path.join(TPG_path, "UI", "ui", "buttons", img1)).convert_alpha()
      self.img2 = pygame.image.load(os.path.join(TPG_path, "UI", "ui", "buttons", img2)).convert_alpha()
      self.img3= pygame.image.load(os.path.join(TPG_path, "UI", "ui", "buttons", img3)).convert_alpha()

      self.img = self.img1
      self.screen = screen
      
      x = screen_width*posn_percentage[0] # x = [0]% from the left
      y = screen_height*posn_percentage[1] #y = [1]% from the top ---> So the button aligns perfectly even at diff res
      self.rect = self.img.get_rect(center=(x, y))
      # Center is a keyword used my pygame's rect method, it works like : 
      # Pygame, give me the invisible rectangle (Rect object) around this image, and place its center at coordinates (x, y)

      self.clicked = False 
      self.hover = False 

   def draw(self) : 
      mx, my = pygame.mouse.get_pos()

      if self.rect.collidepoint(mx, my) : 
         if pygame.mouse.get_pressed()[0] : #Mouse clicks --> for press = 0, 1, 2.... for event = 1, 2, 3... (leftclick, middle, rightclick)
            self.img = self.img3
            self.clicked = True 
         
         else : 
            while not self.hover : 
               select_sound_effect = pygame.mixer.Sound(os.path.join(sound_effect_path, "cursor_select.wav"))
               select_sound_effect.set_volume(0.6)
               select_sound_effect.play()
               self.hover = True

            self.img = self.img2

            if self.clicked : 
               keyboard_click = pygame.mixer.Sound(os.path.join(sound_effect_path, "keyboard_click.wav"))
               keyboard_click.set_volume(0.6)
               keyboard_click.play()
               
               self.clicked = False 
               return True #Button was clicked and released 
      
      else : 
         self.img = self.img1
         self.clicked = False 
         self.hover = False # So it resets only when the mouse goes outside of the button
      
      self.screen.blit(self.img, self.rect)
