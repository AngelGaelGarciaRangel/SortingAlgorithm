import pygame
import random
import math
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
  FONT = pygame.font.SysFont("cimicsans", 30)
  LARGE_FONT = pygame.font.SysFont("cimicsans", 40)
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
    self.block_height = math.floor(self.height - self.TOP_PAD) / (self.max_val - self.min_val)
    self.start_x = self.SIDE_PAD // 2
def draw(draw_info, algo_name, ascending):
  draw_info.window.fill(draw_info.BACKGROUND_COLOR)
  title = draw_info.LARGE_FONT.render(f'{algo_name} -{"Ascending" if ascending else "Descending"}', 1, draw_info.GREEN)
  draw_info.window.blit(title, (draw_info.width/2 - title.get_width()/2, 5))
  controls = draw_info.FONT.render("R - Reset | Space - Start sorting | A - Ascending | D - Descending", 1, draw_info.BLACK)
  draw_info.window.blit(controls, (draw_info.width/2 - controls.get_width()/2, 45))
  sorting = draw_info.FONT.render("I - Insertion Sort | B - Bubble Sort | S - Swap Sort | E - Selection Sort", 1, draw_info.BLACK)
  draw_info.window.blit(sorting, (draw_info.width/2 - sorting.get_width()/2, 75))
  draw_list(draw_info)
  pygame.display.update()
def draw_list(draw_info, color_position={}, clear_background = False):
  lst = draw_info.lst
  if clear_background:
    clear_rect = (draw_info.SIDE_PAD//2, draw_info.TOP_PAD, draw_info.width - draw_info.SIDE_PAD, draw_info.height - draw_info.TOP_PAD)
    pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)
  for i, val in enumerate(lst):
    x = draw_info.start_x + i * draw_info.block_width
    y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height
    color = draw_info.GRADIENTS[i % 3] #in order to have different colors between recs
    if i in color_position:
      color = color_position[i]
    pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height))
  if clear_background:
    pygame.display.update()
def generate_starting_list(n, min_val, max_val):
  lst = []
  for _ in range(n):
    val = random.randint(min_val, max_val)
    lst.append(val)
  return lst
def quickSort_helper(draw_info, start, end):
  lst = draw_info.lst
  if(start >= end):
    return;
  else:
    pivot = start;
    left_pointer = start + 1;
    right_pointer = end;
    while(left_pointer <= right_pointer):
      if(lst[left_pointer] > lst[pivot] and lst[right_pointer] < lst[pivot]):
        lst[left_pointer], lst[right_pointer] = lst[right_pointer], lst[left_pointer]
        draw_list(draw_info, {left_pointer:draw_info.GREEN, right_pointer:draw_info.RED}, True)
        yield True
      if(lst[left_pointer] <= lst[pivot]):
        left_pointer = left_pointer + 1
      if(lst[right_pointer] >= lst[pivot]):
        right_pointer = right_pointer - 1
    lst[pivot], lst[right_pointer] = lst[right_pointer], lst[pivot]
    draw_list(draw_info, {pivot:draw_info.GREEN, right_pointer:draw_info.RED}, True)
    yield True
    if((right_pointer - 1) - start <= end - (right_pointer + 1)):
      quickSort_helper(draw_info, start, right_pointer - 1);
      quickSort_helper(draw_info, right_pointer + 1, end);
    else:
      quickSort_helper(draw_info, right_pointer + 1, end);
      quickSort_helper(draw_info, start, right_pointer - 1);
  return lst
def quickSort_sort(draw_info):
  lst = quickSort_helper(draw_info, 0, len(draw_info.lst) - 1)
  return lst
def selection_sort(draw_info, ascending=True):
  lst = draw_info.lst
  for i in range(len(lst) - 1):
    valorMinimoIndice = i
    for j in range(i + 1, len(lst)):
      if(lst[j] < lst[valorMinimoIndice] and ascending) or (lst[j] > lst[valorMinimoIndice] and not ascending):
        valorMinimoIndice = j;
    lst[i], lst[valorMinimoIndice] = lst[valorMinimoIndice], lst[i]
    draw_list(draw_info, {i:draw_info.GREEN, i + 1:draw_info.RED}, True)
    yield True
  return lst
def swap_sort(draw_info, ascending=True):
  lst = draw_info.lst
  for n in range(len(lst) - 1):
    for i in range(n + 1, len(lst)):
      if (lst[n] > lst[i] and ascending) or (lst[n] < lst[i] and not ascending) :
        lst[n], lst[i] = lst[i], lst[n]
        draw_list(draw_info, {i:draw_info.GREEN, i + 1:draw_info.RED}, True)
        yield True
  return lst
def bubble_sort(draw_info, ascending=True):
  lst = draw_info.lst
  for i in range(len(lst) - 1):
    for j in range(len(lst) - 1 - i):
      num1 = lst[j]
      num2 = lst[j + 1]
      if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
        lst[j], lst[j + 1] = lst[j + 1], lst[j]
        draw_list(draw_info, {j:draw_info.GREEN, j + 1:draw_info.RED}, True)
        yield True
  return lst
def insertion_sort(draw_info, ascending = True):
  lst = draw_info.lst
  for i in range(1, len(lst)):
    current = lst[i]
    while True:
      asceding_sort = i > 0 and lst[i - 1] > current and ascending
      descending_sort = i > 0 and lst[i - 1] < current and not ascending
      if not asceding_sort and not descending_sort:
        break
      lst[i] = lst[i - 1]
      i = i - 1
      lst[i] = current
      draw_list(draw_info, {i: draw_info.GREEN, i - 1: draw_info.RED}, True)
      yield True
  return lst  
def main():
  run = True
  clock = pygame.time.Clock()
  n = 50
  min_val = 0
  max_val = 100
  lst = generate_starting_list(n, min_val, max_val)
  draw_info = information(800, 600, lst)
  sorting = False
  ascending = True
  sorting_algoritm = bubble_sort
  sorting_algo_name = "Bubble Sort"
  sorting_algoritm_generator = None
  while run:
    clock.tick(60)
    if sorting:
      try:
        next(sorting_algoritm_generator)
      except StopIteration:
        sorting = False
    else:
      draw(draw_info, sorting_algo_name, ascending)
    for event in pygame.event.get(): #events that happened
      if event.type == pygame.QUIT:
        run = False #finish
      if event.type != pygame.KEYDOWN:
        continue
      if event.key == pygame.K_r:
        lst = generate_starting_list(n, min_val, max_val)
        draw_info.set_list(lst)
        sorting = False
      elif event.key == pygame.K_SPACE and sorting == False:
        sorting = True
        sorting_algoritm_generator = sorting_algoritm(draw_info)
      elif event.key == pygame.K_a and not sorting:
        ascending = True
      elif event.key == pygame.K_d and not sorting:
        ascending = False
      elif event.key == pygame.K_i and not sorting:
        sorting_algoritm = insertion_sort
        sorting_algo_name = "Insertion  Sort"
      elif event.key == pygame.K_b and not sorting:
        sorting_algoritm = bubble_sort
        sorting_algo_name = "Bubble Sort"
      elif event.key == pygame.K_s and not sorting:
        sorting_algoritm = swap_sort
        sorting_algo_name = "Swap Sort"
      elif event.key == pygame.K_e and not sorting:
        sorting_algoritm = selection_sort
        sorting_algo_name = "Selection Sort"
      elif event.key == pygame.K_q and not sorting:
        sorting_algoritm = quickSort_sort
        sorting_algo_name = "Quicksort"
        
  pygame.quit()
if __name__ == "__main__":
  main()
