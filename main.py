import pygame
import random
import sys
pygame.init()
#Constants and window
class information:
  BLACK = 0, 0, 0
  WHITE = 255, 255, 255
  GREEN = 0, 255, 0
  RED = 255, 0, 0
  BACKGROUND_COLOR = WHITE
  SIDE_PAD = 100
  TOP_PAD = 150
  GRADIENTS = [(128, 128, 128), (160, 160, 160), (192, 192, 192)]
  def __init__(self, width, height, lst):
    self.width = width
    self.height = height
    self.window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Sorting Algorithm Visualization")
    self.set_list(lst)
  def set_list(self, lst):
    self.lst = lst
    self.max_val = max(lst)
    self.min_val = min(lst)
    self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
    self.block_height = (self.height - self.TOP_PAD) / (self.max_val - self.min_val)
    self.start_x = self.SIDE_PAD // 2
def draw(draw_info):
  draw_info.window.fill(draw_info.BACKGROUND_COLOR)
  draw_list(draw_info)
  pygame.display.update()
def draw_list(draw_info):
  lst = draw_info.lst
  for i, val in enumerate(lst):
    x = draw_info.start_x + i * draw_info.block_width
    y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height
    color = draw_info.GRADIENTS[i % 3] #in order to have different colors between recs
    pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height))
def generate_starting_list(n, min_val, max_val):
  lst = []
  for _ in range(n):
    val = random.randint(min_val, max_val)
    lst.append(val)
  return lst
#Function that will be checking for the events
def main():
  run = True
  clock = pygame.time.Clock()
  n = 50
  min_val = 0
  max_val = 100
  lst = generate_starting_list(n, min_val, max_val)
  draw_info = information(800, 600, lst)
  while run:
    clock.tick(60)
    draw(draw_info)
    for event in pygame.event.get(): #events that happened
      if event.type == pygame.QUIT:
        run = False #finish
  pygame.quit()
  sys.exit()
if __name__ == "__main__":
  main()
