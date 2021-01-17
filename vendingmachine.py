drinks = {'1.콜라':1000, '2.사이다':1000, '3.환타':1000, "4.스프라이트":1200, "5.봉봉":900}
drinks_names = list(drinks.keys())
prices = list(drinks.values())

input_amount = int(input("금액 넣어주세요>> ")) 
print("음료수들을 고르세요 1.콜라 1000원, 2.사이다 1000원, 3.환타 1000원, 4.스프라이트 1200원, 5.봉봉 900원")
user_input = int(input("음료수를 선택하세요>> ")) - 1

bought_drinks = []

while True:
    if input_amount < prices[user_input]:
        pick = int(input(f"금액이 부족합니다 1.다른 음료를 선택하시거나 2.{prices[user_input] - input_amount}원 이상 넣으세요>> "))
        if pick == 2:
            input_amount = input_amount + int(input("금액을 더 넣어주세요>> "))
            continue
        else:
            print("음료수들을 고르세요 1.콜라 1000원, 2.사이다 1000원, 3.환타 1000원, 4.스프라이트 1200원, 5.봉봉 900원")
            user_input = int(input("음료수를 선택하세요>> "))
            bought_drinks += drinks_names[user_input][2:]
            continue
    else:
        change = prices[user_input] - input_amount
        print(f'{drinks_names[user_input][2:]}을/를 받으세요. 남은 금액은 {change}입니다')
        bought_drinks += drinks_names[user_input][2:]
        ask = input("계속 하시겠습니까? [Y/N]")
        if ask == "N" or ask == "n":
            print(f"잔돈은 {change}원 입니다.")
            break
        else:
            input_amount = change #남은 돈 = 내가 쓸 돈 
            print("음료수들을 고르세요 1.콜라 1000원, 2.사이다 1000원, 3.환타 1000원, 4.스프라이트 1200원, 5.봉봉 900원")
            user_input = int(input("물건을 선택하세요"))
            bought_drinks += drinks_names[user_input][2:]