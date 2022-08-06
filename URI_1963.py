
# Aluna Diana Faustino de Siqueira
# Exercícios aula 18

sel = 'S'
while sel == 'S':
    pais_input = str(input('Informe o país: '))

    a = {'brasil': 'Feliz Natal!',
        'alemanha': 'Frohliche Weihnachten!',
        'austria': 'Frohe Weihnacht!',
        'coreia': 'Chuk Sung Tan!',
        'espanha': 'Feliz Navidad!',
        'grecia': 'Kala Christougena!',
        'estados-unidos': 'Merry Christmas!',
        'inglaterra': 'Merry Christmas!',
        'australia': 'Merry Christmas!',
        'portugal': 'Feliz Natal!',
        'suecia': 'God Jul!',
        'turquia': 'Mutlu Noeller',
        'argentina': 'Feliz Navidad!',
        'chile': 'Feliz Navidad!',
        'mexico': 'Feliz Navidad!',
        'antardida': 'Merry Christmas!',
        'canada': 'Merry Christmas!',
        'irlanda': 'Nollaig Shona Dhuit!',
        'belgica': 'Zalig Kerstfeest!',
        'italia': 'Buon Natale!',
        'libia': 'Buon Natale!',
        'siria': 'Milad Mubarak!',
        'marrocos': 'Milad Mubarak!',
        'japao': 'Merii Kurisumasu!'}

    print(a.get(pais_input, '--- NOT FOUND ---'))
    sel = input('Deseja continuar? [S/N]\n>>> ').upper()