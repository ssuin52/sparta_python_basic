import pprint
people = [
    ("Blake Howell", "Jamaica", 18, "aw@jul.bw"),
    ("Peter Bowen", "Burundi", 30, "vinaf@rilkov.il"),
    ("Winnie Hall", "Palestinian Territories", 22, "moci@pacivhe.net"),
    ("Alfred Schwartz", "Syria", 29, "ic@tolseuc.pr"),
    ("Carrie Palmer", "Mauritius", 28, "fenlofi@tor.aq"),
    ("Rose Tyler", "Martinique", 17, "as@forebjab.et"),
    ("Katharine Little", "Anguilla", 29, "am@kifez.et"),
    ("Brent Peterson", "Svalbard & Jan Mayen", 22, "le@wekciga.lr"),
    ("Lydia Thornton", "Puerto Rico", 19, "lefvoru@itbewuk.at"),
    ("Richard Newton", "Pitcairn Islands", 17, "da@lasowiwa.su"),
    ("Eric Townsend", "Svalbard & Jan Mayen", 22, "jijer@cipzo.gp"),
    ("Trevor Hines", "Dominican Republic", 15, "ev@hivew.tm"),
    ("Inez Little", "Namibia", 26, "meewi@mirha.ye"),
    ("Lloyd Aguilar", "Swaziland", 16, "oza@emneme.bb"),
    ("Erik Lane", "Turkey", 30, "efumazza@va.hn"),
]
people = list(filter(lambda x: x[2] >= 20, people))
people.sort(key=lambda x: x[2])
# some code

pprint.pprint(people)

"""
- filter 혹은 리스트 축약식을 사용해 코드를 작성해주세요
- 제공 된 사용자들 중 나이가 20살 미만인 사람들은 제외해주세요
- 사용자들을 나이 순으로 정렬해주세요
[('Winnie Hall', 'Palestinian Territories', 22, 'moci@pacivhe.net'),
 ('Brent Peterson', 'Svalbard & Jan Mayen', 22, 'le@wekciga.lr'),
 ('Eric Townsend', 'Svalbard & Jan Mayen', 22, 'jijer@cipzo.gp'),
 ('Inez Little', 'Namibia', 26, 'meewi@mirha.ye'),
 ('Carrie Palmer', 'Mauritius', 28, 'fenlofi@tor.aq'),
 ('Alfred Schwartz', 'Syria', 29, 'ic@tolseuc.pr'),
 ('Katharine Little', 'Anguilla', 29, 'am@kifez.et'),
 ('Peter Bowen', 'Burundi', 30, 'vinaf@rilkov.il'),
 ('Erik Lane', 'Turkey', 30, 'efumazza@va.hn')]
"""