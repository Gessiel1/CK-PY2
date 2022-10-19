money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

# количество месяцев, которое можно прожить

# TODO Оформить решение
money_available = money_capital - spend
money_cap = salary + money_available

spending = (spend*increase)+spend #new spending due to increase
money2 = money_cap - spending #for the 2nd month

money_cap1= salary+money2 #for the 3rd month
spend1= (spending*increase)+spending #spending for the 3rd month
money3= money_cap1-spend1 #what stay as available capital
new_spending=(spend1*increase)+spend1
money4=money3+salary
stay_money= money4-new_spending

total_money=money2+money3

month= money_capital/total_money

print(round(month))






