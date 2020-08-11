import pygame
import math
import random
import Words
import os

pygame.init()
WIDTH, HEIGHT = 800, 500
window = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Hangman")
clock = pygame.time .Clock()
run = True

attempts = 0
word = random.choice(Words.words).upper()
guessed = []

letterFont = pygame.font.SysFont('Georgia', 30)
wordFont = pygame.font.SysFont('Georgia', 40)

images = []
for i in range(7):
    images.append(pygame.image.load("images/hangman"+str(i)+".png"))
print(images)

RADIUS = 20
GAP = 15
letters = []
startX = round((WIDTH - (RADIUS * 2 + GAP) * 12 - 2 * RADIUS) / 2)
startY = 400
char = 65
for i in range(26):
    x = startX + RADIUS + ((RADIUS * 2 + GAP) * (i % 13))
    y = startY + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(char+i)])


def draw():
    window.fill((255, 255, 255))
    displayWord = ""
    for letter in word:
        if letter in guessed:
            displayWord += letter + " "
        else:
            displayWord += "_ "
    text = wordFont.render(displayWord, 1, (0, 0, 0))
    window.blit(text, (400, 200))

    for letter in letters:
        coordX, coordY, symbol = letter
        pygame.draw.circle(window, (0, 0, 0), (coordX, coordY), RADIUS, 3)
        text = letterFont.render(symbol, 1, (0, 0, 0))
        window.blit(text, (coordX - text.get_width()//2, coordY - text.get_height()//2))
    window.blit(images[attempts], (125, 100))
    pygame.display.update()


def display_message(message):
    pygame.time.delay(1000)
    window.fill((255, 255, 255))
    text = wordFont.render(message, 1, (0, 0, 0))
    window.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(3000)

while run:
    clock.tick(60)
    draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clickX, clickY = pygame.mouse.get_pos()
            for letter in letters:
                coordX, coordY, symbol = letter
                dis = math.sqrt((coordX-clickX)**2 + (coordY-clickY)**2)
                if dis < RADIUS:
                    guessed.append(symbol)
                    letters.pop(letters.index(letter))
                    if symbol not in word:
                        attempts += 1

    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break
    if won:
        display_message("Congrats! You Won!")
        break
    if attempts == 6:
        display_message("You Lost! Better Luck Next Time!")
        break
pygame.quit()
