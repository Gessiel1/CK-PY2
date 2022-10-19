salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 18783.27587  # количество денег, чтобы прожить 10 месяцев
for months in range(1,10):
    new_salary = 5000*10
    spend2 = (spend*increase) + spend
    spend3 = (spend2*increase) + spend2
    spend4 = (spend3*increase) + spend3
    spend5 = (spend4*increase) + spend4
    spend6 = (spend5*increase) + spend5
    spend7 = (spend6*increase) + spend6
    spend8 = (spend7*increase) + spend7
    spend9 = (spend8*increase) + spend8
    spend10 = (spend9*increase) + spend9

need_money=(spend+spend2+spend3+spend4+spend5+spend6+spend7+spend8+spend9+spend10)- new_salary

# TODO Оформить решение

print(round(need_money))
