import random

people = {
    'Computer Science': [
        'Lourdes Agapito',
        'Marta Betcke',
        'David Barber',
        'Ingemar Cox',
        'Marc Deisenroth',
        'Benjamin Guedj',
        'Mark Herbster',
        'Dimitrios Kanoulas',
        'Matt Kusner',
        'Brooks Paige',
        'Massimiliano Pontil',
        'Sebastian Riedel',
        'John Shawe-Taylor',
        'Pontus Stenetorp',
        'Emine Yilmaz',
    ],
    'Gatsby Computational Neuroscience Unit': [
        'Arthur Gretton',
        'Ferenc Huszar',
        'Peter Latham',
        'Peter Orbanz',
        'Maneesh Sahani',
    ],
    'Statistics': [
        'Alexandros Beskos',
        'Francois-Xavier Briol',
        'Petros Dellaportas',
        'Jim Griffin',
        'Serge Guillas',
        'Ioanna Manolopoulou',
        'Ricardo Silva',
        'Tengyao Wang',
        'Jinghao Xue'
    ]
}

images = [
    'cabin',
    'cake',
    'circus',
    'game',
    'safe',
    'submarine',
]

base = "---\nlayout: default\nmodal-id: 1\ndate: 2020-09-14\nimg: {}.png\nalt: image-alt\ninterests: TBA\ndepartment: {}\nname: {}\ndescription: Lorem ipsum dolor sit amet, consectetur adipisicing elit. Mollitia neque assumenda ipsam nihil, molestias magnam, recusandae quos quis inventore quisquam velit asperiores, vitae? Reprehenderit soluta, eos quod consequuntur itaque. Nam.\n---\n"

dpt_str = {
    'Computer Science': 'cs',
    'Gatsby Computational Neuroscience Unit': 'g',
    'Statistics': 's'
}
for department, names in people.items():
    for name in names:
        img = random.choice(images)

        file_name = dpt_str[department]+'_'+name.lower().replace(' ', '_')

        file = base.format(img, department, name)

        with open(f'2020-09-14-{file_name}.markdown', 'w') as f:
            f.write(file)
