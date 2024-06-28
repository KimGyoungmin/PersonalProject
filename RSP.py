# 플레이어가 가위, 바위, 보 중 하나를 입력한다
# 컴퓨터도 무작위로 가위, 바위, 보 중 하나를 선택한다
# 플레이어와 컴퓨터의 선택을 비교하여 승패를 판정한다.
# 결과를 출력하여 플레이어가 이겼는지, 컴퓨터가 이겼는지, 비겼는지를 알려준다
import random

rsp = ['가위','바위','보']
com = random.choice(rsp)  ## 가위바위보중 랜덤 1개를 com변수에 저장
game_exit = True
w_cnt = 0  ## 사용자가 이긴횟수
l_cnt = 0  ## 사용자가 진 횟수
d_cnt = 0  ## 사용자가 비긴 횟수
while game_exit:  ## True값이 지속되는 동안
    player = input("가위, 바위, 보 중 하나를 선택하세요: ") ## 플레이어 입력
    if player in rsp:  ## 만약 rsp의 값들 중 입력한 값이 있다면
        if player == com: ##비겼을때
            print("비겼습니다")
            d_cnt += 1    ## 무승부 cnt를 1 증가시켜준다
            while True:
                chk_regame = input("다시 하시겠습니까? (y/n):")   ## 재실행 여부 확인
                if chk_regame == 'y' or chk_regame == 'Y':   ## 만약 y나 Y를 입력했을시
                    com = random.choice(rsp)   ## 컴퓨터의 값을 다시 새로 넣어준다
                    print("게임을 다시 시작합니다!")
                    break   ## 재실행 여부에서 벗어남
                elif chk_regame == 'n' or chk_regame == 'N':   ## 만약 게임 종료 키를 눌럿다면
                    game_exit = False   ## 게임 동작 여부를 False로 전환
                    print("게임을종료합니다")
                    print(f"승: {w_cnt} 패: {l_cnt} 무승부: {d_cnt}")   ## 지금까지의 승패 기록을 보여준다
                    break
                else:  ## 만약 다른 값을 넣었다면
                    print("다시 입력해주세요")  ## 출력과함께 다시 재실행 여부 루프
        elif(player=='가위' and com=='바위') or (player=='바위' and com=='보') or (player=='보' and com=='가위'): ##플레이어가 졌을때
            print("컴퓨터가 승리하였습니다")
            l_cnt += 1   ## 패 cnt를 1 증가
            while True:
                chk_regame = input("다시 하시겠습니까? (y/n):")   ## .lower함수도 고려해봄
                if chk_regame == 'y' or chk_regame == 'Y':
                    com = random.choice(rsp)
                    print("게임을 다시 시작합니다!")
                    break
                elif chk_regame == 'n' or chk_regame == 'N':
                    game_exit = False
                    print("게임을종료합니다")
                    print(f"승: {w_cnt} 패: {l_cnt} 무승부: {d_cnt}")
                    break
                else:
                    print("다시 입력해주세요")
        elif (player == '가위' and com == '보') or (player == '바위' and com == '가위') or (player == '보' and com == '바위'):  ## 플레이어가 이겼을때
            print("플레이어가 승리하였습니다")
            w_cnt += 1  ## 승리 cnt를 1증가
            while True:
                chk_regame = input("다시 하시겠습니까? (y/n):")
                if chk_regame == 'y' or chk_regame == 'Y':
                    com = random.choice(rsp)
                    print("게임을 다시 시작합니다!")
                    break
                elif chk_regame == 'n' or chk_regame == 'N':
                    game_exit = False
                    print("게임을종료합니다")
                    print(f"승: {w_cnt} 패: {l_cnt} 무승부: {d_cnt}")
                    break
                else:
                    print("다시 입력해주세요")
    else:  ## 가위,바위,보 중에 player값이랑 똑같은 값이 없다면
        print("다시 입력해주세요")
    if game_exit == False:   ## 만약 재실행여부 루프에서 n키를 눌럿다면 game_exit은 false로 전환후 모든실행 break
        break

# 게임의 승, 패, 무승부 횟수를 기록하고, 게임 종료 시에 플레이어에게 통계를 제공한다.
# 플레이어가 입력할 때 대소문자를 구분하지 않도록 프로그램을 개선
# 플레이어가 게임을 반복하고 싶을 경우, 게임 재시작 여부를 묻고 그에 따라 게임을 초기화하거나 종료하는 기능을 추가