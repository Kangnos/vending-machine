goods = {'1.coke':1000, '2.cider':1000, '3.fanta':1000, '4.sprite':1200, '5.bong bong':900}
goods_names = list(goods.keys())
prices = list(goods.values())

# print(goods_names)
# print(prices)

input_amount = int(input("금액을 넣어주세요>> "))
print("물건들: 1. 코카콜라, 2.사이다, 3.판타, 4.스프라이트, 5.봉봉")
user_input = int(input("물건을 선택하세요>> ")) - 1

ask = ''

while True:
    if input_amount < prices[user_input]:
        change = prices[user_input] - input_amount
        pick = int(input(f'금액이 무족합니다 1. 다른 음료를 선택하시거나, 2.{change}원 더 넣으세요'))
        if pick == 2: 
            input_amount = input_amount + int(input('금액을 더 넣어주세요>> '))
            continue
        else:
            user_input = int(input("물건을 다시 선택하세요")) - 1
            continue
    else:
        change = prices[user_input] - input_amount
        print(f'{goods_names[user_input][2:]}을/를 받으세요. 남은 금액은 {change}원 입니다')
        ask = input("계속 하시겠습니까? [Y/N]")
        if ask == "N" or ask == "n":
            print(f"잔돈은 {change}원 입니다")
            break
        else:
            input_amount = change
            user_input = int(input("물건을 선택하세요")) - 1
        