trainings ={    
    'Онбордінг': {
        'відповідальний': 'Григоров О.С.',
        'теми': ['техніка безпеки', 'робота в команді'],
        'дата': '15.05'
    },
    'Підвищення кваліфікації': {
        'відповідальний': 'Череватий К. І.',
        'теми': ['лідерство','комп. грамотність'],
        'дата': '20.11'
    }
}
print("Тренінги ProTeam")
print("1-назви тренінгів, 2-інфо про тренінг")
while True:
    answer = input("Номер дії (off-вийти):")
    if answer == "off":
        break
    elif answer == "1":
        print("-Онбордінг")
        print("-Підвищення кваліфікації")
    elif answer == "2":
        training_name = input("Назва тренінга: ")
        if training_name in trainings:
            print(trainings[training_name]['відповідальний'])
            print(trainings[training_name]['теми'])
            print(trainings[training_name]['дата'])
        else:
            print("Такого тренінгу не існує!")
    else:
        print("Невірний номер дії. Спробуйте ще раз.")
