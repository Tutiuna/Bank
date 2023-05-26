per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money =int(input("Введите сумму:"))

procent = list(per_cent.values())
ТКБ = round(procent[0]/100*money)
СКБ = round(procent[1]/100*money)
ВТБ = round(procent[2]/100*money)
СБЕР = round(procent[3]/100*money)
deposit = [ТКБ, СКБ, ВТБ, СБЕР]
max_deposit = max(deposit)
print("Возможный доход:", deposit)
print("Максимальный доход:", max_deposit)