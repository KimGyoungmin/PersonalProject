import random
answer = random.randint(1, 100) ## 정답
cnt = 0  ## 틀린 횟수
chance_num = [(answer // 10) * 10,(answer // 10) * 10 + 10]  ## 유효한 범위의 숫자내에서 힌트
best_score = []  ## 시도횟수 저장 리스트
best_score.sort()  ## 가장 낮은 횟수를 인덱스 0값으로
game_exit = True  ## 게임 종료 여부 확인


while game_exit:
    try:
        if best_score and cnt == 0:  ## 시도횟수 리스트에 값이 있고 처음에만 출력
            print(f"가장 정답을 빨리 맞춘 횟수는 {best_score[0]}회입니다")  ## 제일 최소 횟수번을 출력
        insert_val = int(input("1~100 숫자를 입력해주세요 : "))    ## 입력한 값을 변수에 저장
        if insert_val > 100:   ## 숫자가 100이 넘어갔을때는 문구를 남겨주고 continue
            print("100이하의 숫자를 입력해주세요")
            continue
        cnt += 1  ## 옳바른 값을 넣었다면 카운트 1 증가
        print(f"시도하는 횟수는 {cnt}번입니다.")
        if insert_val > answer: ## 입력값이 더크다면
            print("다운")
            if cnt >= 5:  ## 기회가 5이상으로 넘어갔다면
                print(f"정답은 {chance_num[0]}~{chance_num[1]}사이의 입니다") ## 정답사이의 10의 배수 값 2개를 보여준다
        elif insert_val < answer: ## 입력값이 정답보다 낮다면
            print("업")
            if cnt >= 5:
                print(f"정답은 {chance_num[0]}~{chance_num[1]}사이의 숫자입니다")
        elif insert_val == answer:  ## 정답을 맞췄을때
            print(f"정답입니다. {cnt}번 안에 맞추셨습니다")
            while True:     ## 잘못 입력했을시 정확한 값을 얻기 위한 반복
                try_game = input((f"재도전하시겠습니까?(y/n)"))
                if try_game == 'y' or try_game == 'Y':   ## y를 입력했을시
                    best_score.append(cnt)    ## cnt 기록을 리스트에 저장
                    answer = random.randint(1, 100)  ## 새로운 정답을 answer에 저장
                    chance_num = [(answer // 10) * 10, (answer // 10) * 10 + 10]  ## 새로운 유효검사도 도출
                    cnt = 0
                    print("새로운 게임을 시작합니다!")
                    break     ## while true문을 벗어나기위한 break
                elif try_game == 'n' or try_game == 'N':     ## n을 입력했을시
                    print("게임을 종료합니다.")
                    game_exit = False
                    break
                else:  ## 값을 잘못 입력했을시
                    print("정확하게 입력해주세요")
        if not game_exit: ## False 값 즉 n을 입력하면 game_exit이 False로 전환되므로 무한루프 종료
            break
    except ValueError:
        print("숫자만 입력해주세요")








