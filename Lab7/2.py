import pygame
import os

pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Music Player")
def show_hotkeys():

    print(" SPACE - Воспроизвести музыку")
    print(" S - Остановить музыку")
    print(" N - Следующий трек")
    print(" P - Предыдущий трек")

show_hotkeys()

musics=['Нюша и Кайрат Нуртас - Алматы тундери.mp3','Naughty Boy Ft. Sam Smith - LaLaLa.mp3','Ulukmanapo - Летали.mp3','V S X V Prince - Цветы.mp3','D-Block Europe ft. Central Cee - Overseas.mp3']
track=0

pygame.mixer.music.load(musics[track])

def play():
    pygame.mixer.music.play()
def stop():
    pygame.mixer.music.stop()
def next():
    global track
    track=(track+1)%len(musics)
    pygame.mixer.music.load(musics[track])
    play()
def prev():
    global track
    track=(track-1)%len(musics)
    pygame.mixer.music.load(musics[track])
    play()
run=True
while run:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                play()
            elif event.key==pygame.K_s:
                stop()
            elif event.key==pygame.K_n:
                next()
            elif event.key == pygame.K_p:
                prev()
    pygame.display.flip()
pygame.quit()



