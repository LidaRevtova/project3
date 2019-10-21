# В далеком будущем ученые случайно выпустили в мир опаснейший
# вирус - KTS. Началось моментальное заражение. Ученые начали
# разрабатывать вакцину. Успеют ли они спасти человечество?

# скорость распространения вируса (чел/день)
SPEED = 20_000
# скорость умирания людей (чел/день)
DEATH = 20_000
# скорость приготовления вакц(вакц/день)
VACCINE = 2_000

population = 0
for mainland in ['ЕВРАЗИИ', 'АФРИКЕ', 'СЕВЕРНОЙ АМЕРИКЕ',
                 'ЮЖНОЙ АМЕРИКЕ', 'АВСТАЛИИ']:
    print('Сколько людей живет в', mainland+
          '? Введите число не больше 1_000: ')
    quantity = int(input())
    while quantity > 1_000:
        print('Еще раз введите численность, которая не'
              ' превышает 1000')
        quantity = int(input())
    quantity = quantity * 1_000_000
    population += quantity
print(population)
print('Сколько дней назад началось заражение?')
days = int(input())

s_infected = 0
s_dead = 0
s_vaccine = 0
for day in [days]:
    # вычисляет колво незараженных
    infected = population - SPEED - DEATH - VACCINE
    s_infected += infected
    # высчисляет колво живых
    dead = population - SPEED + VACCINE - DEATH
    s_dead += dead
    # вычисляет колво, не принявших вакцину
    after_vaccine = s_infected - VACCINE - DEATH
    s_vaccine += after_vaccine

# остатки живых
leftovers = population - s_dead

if s_vaccine == leftovers:
    print('KTS больше не угрожает! Ученые смогли '
          'полностью избавиться от болезни!!! В живых'
          'осталось', leftovers, 'человек')
elif leftovers <= 0:
    print('Увы! Но человечество погибло, никто не смог '
          'справиться с KTS')
else:
    print('У вас все еще есть шанс спасти часть человечества'
          'В живых осталось', leftovers, 'человек. Смерть '
          'все ближе')
    percent = 100 * leftovers / population
    percent = ('{:.2}'.format(percent))
    print('В живых осталось',percent, 'процентов'
      ' Ты еще можешь их спасти')