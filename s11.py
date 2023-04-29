# import pygame
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)

# pygame.init()
# size = (700, 500)
# screen = pygame.display.set_mode(size)
# clock = pygame.time.Clock()
# pos_x = 6
# pos_y = 6
# pos_x_change = 1
# pos_y_change = 1

# done = True

# while done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_ESCAPE:
#                 done = False
#     screen.fill(BLACK)
#     pygame.draw.circle(screen, RED, [pos_x, pos_y], 6)
# pos_x += pos_x_change
# pos_y += pos_y_change
# if pos_x > 694 or pos_x < 0:
#     pos_x_change = pos_x_change * -1
# if pos_y > 494 or pos_y < 0:
#     pos_y_change = pos_y_change * -1
#     mousepos = pygame.mouse.get_pos()
#     mouse_x = mousepos[0]
#     mouse_y = mousepos[1]
#     pos_x = mouse_x
#     pos_y = mouse_y

#     pygame.display.flip()
#     clock.tick(600)

# pygame.quit()


'''
* * * * * * * * * *
'''

# print('* ' * 10)
# for i in range(10):
#     print("*", end=' ')

'''
* * * * * * * * * *
* * * * *
* * * * * * * * * * * * * * * * * * * *
'''

# print("* " * 10)
# print("* " * 5)
# print("* " * 20)
# for i in range(10):
#     print("*", end=" ")
# print()
# for i in range(5):
#     print("*", end=" ")
# print()
# for i in range(20):
#     print("*", end=" ")

'''
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
'''
# for row in range(8):
#     print("* " * 10)
# for row in range(8):
#     for col in range(10):
#         print("*", end=" ")
#     print()
# exercise1
'''
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''
# exercise2 :
'''
* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * *
'''

'''
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9

'''
# for row in range(10):
#     for col in range(10):
#         print(col, end=" ")
#     print()
# exercise 3:
'''
0 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1
2 2 2 2 2 2 2 2 2 2
3 3 3 3 3 3 3 3 3 3
4 4 4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5 5
6 6 6 6 6 6 6 6 6 6
7 7 7 7 7 7 7 7 7 7
8 8 8 8 8 8 8 8 8 8
9 9 9 9 9 9 9 9 9 9
'''

'''
0
0 1
0 1 2
0 1 2 3
0 1 2 3 4
0 1 2 3 4 5
0 1 2 3 4 5 6
0 1 2 3 4 5 6 7
0 1 2 3 4 5 6 7 8
0 1 2 3 4 5 6 7 8 9

'''
# for row in range(10):
#     for col in range(row + 1):
#         print(col, end=" ")
#     print()

'''
0 1 2 3 4 5 6 7 8 9
  0 1 2 3 4 5 6 7 8
    0 1 2 3 4 5 6 7
      0 1 2 3 4 5 6
        0 1 2 3 4 5
          0 1 2 3 4
            0 1 2 3
              0 1 2
                0 1
                  0


'''
for row in range(10):
    for j in range(row):
        print(" ", end=" ")
    for j in range(10-row):
        print(j, end=" ")
    print()
