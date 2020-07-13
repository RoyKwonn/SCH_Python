import pygame.mixer

def wait_finish(channel):
    while channel.get_busy():
        pass

sounds = pygame.mixer
sounds.init()

correct_s = sounds.Sound("sound/correct.wav")
wrong_s = sounds.Sound("sound/wrong.wav")

prompt = "정답 1, 오답 2, 종료 0을 누르세요: "

number_asked = 0
number_correct = 0
number_wrong = 0

choice = input(prompt)

while choice != '0':
    if choice == '1':
        number_correct = number_correct + 1
        wait_finish(correct_s.play())
    if choice == '2':

        number_wrong = number_wrong + 1
        wait_finish(wrong_s.play())
    number_asked = number_asked + 1
    choice = input(prompt)

print("질문 수 : " + str(number_asked))
print("정답 수 : " + str(number_correct))
print("오답 수 : " + str(number_wrong))
