"""Geographic divisions and coordinates data for eTryvoga."""

OBLAST_REGIONS = [
  "Вінницька область",
  "Волинська область",
  "Дніпропетровська область",
  "Донецька область",
  "Житомирська область",
  "Закарпатська область",
  "Запорізька область",
  "Івано-Франківська область",
  "Київська область",
  "м. Київ",
  "Кіровоградська область",
  "Луганська область",
  "Львівська область",
  "Миколаївська область",
  "Одеська область",
  "Полтавська область",
  "Рівненська область",
  "Сумська область",
  "Тернопільська область",
  "Харківська область",
  "Херсонська область",
  "Хмельницька область",
  "Черкаська область",
  "Чернівецька область",
  "Чернігівська область",
  "АР Крим"
]

OBLAST_TO_DISTRICTS = {
  "Вінницька область": [
    "VINNYTSKYI-DSTR",
    "HAISYNSKYI-DSTR",
    "ZHMERYNSKYI-DSTR",
    "MOHYLIV-PODILSKYI-DSTR",
    "TULCHYNSKYI-DSTR",
    "KHMILNYTSKYI-DSTR"
  ],
  "Волинська область": [
    "VOLODIMIR-VOLINSKYI-DSTR",
    "KAMIN-KASHIRSKYI-DSTR",
    "KOVELSKYI-DSTR",
    "LUCKYI-DSTR",
    "PRYLUTSKYI-DSTR"
  ],
  "Дніпропетровська область": [
    "MARHANETS-CITY",
    "NIKOPOL-CITY",
    "POKROV-CITY",
    "DNIPROVSKYI-DSTR",
    "KAMIANSKYI-DSTR",
    "KRYVORIZKYI-DSTR",
    "NIKOPOLSKYI-DSTR",
    "PAVLOHRADSKYI-DSTR",
    "NOVOMOSKOVSKYI-DSTR",
    "SYNELNYKIVSKYI-DSTR"
  ],
  "Донецька область": [
    "BAKHMUTSKYI-DSTR",
    "VOLNOVASKYI-DSTR",
    "HORLIVSKYI-DSTR",
    "DONETSKYI-DSTR",
    "KALMIUSKYI-DSTR",
    "KRAMATORSKYI-DSTR",
    "MARIUPOLSKYI-DSTR",
    "POKROVSKYI-DSTR",
    "SIEVIERODONETSKYI-DSTR"
  ],
  "Житомирська область": [
    "BERDYCHIVSKYI-DSTR",
    "ZHYTOMYRSKYI-DSTR",
    "NOVOHRAD-VOLYNSKYI-DSTR",
    "KOROSTENSKYI-DSTR"
  ],
  "Закарпатська область": [
    "BEREHIVSKYI-DSTR",
    "MUKACHIVSKYI-DSTR",
    "RAKHIVSKYI-DSTR",
    "TIACHIVSKYI-DSTR",
    "UZHHORODSKYI-DSTR",
    "KHUSTSKYI-DSTR"
  ],
  "Запорізька область": [
    "ZAPORIZHZHIA-CITY",
    "BERDIANSKYI-DSTR",
    "VASYLIVSKYI-DSTR",
    "ZAPORIZKYI-DSTR",
    "MELITOPOLSKYI-DSTR",
    "POLOHIVSKYI-DSTR"
  ],
  "Івано-Франківська область": [
    "IVANO-FRANKIVSKYI-DSTR",
    "VERKHOVYNSKYI-DSTR",
    "KALUSKYI-DSTR",
    "KOLOMYISKYI-DSTR",
    "KOSIVSKYI-DSTR",
    "NADVIRNIANSKYI-DSTR"
  ],
  "Київська область": [
    "SLAVUTICH-CITY",
    "BORYSPILSKYI-DSTR",
    "BROVARSKYI-DSTR",
    "BUCHANSKYI-DSTR",
    "BILOTSERKIVSKYI-DSTR",
    "VYSHHORODSKYI-DSTR",
    "OBUKHIVSKYI-DSTR",
    "FASTIVSKYI-DSTR"
  ],
  "м. Київ": [
    "KIYEW"
  ],
  "Кіровоградська область": [
    "HOLOVANIVSKYI-DSTR",
    "KROPYVNYTSKYI-DSTR",
    "NOVOUKRAINSKYI-DSTR",
    "OLEKSANDRIISKYI-DSTR"
  ],
  "Луганська область": [
    "ALCHEVSKYI-DSTR",
    "DOVZHANSKYI-DSTR",
    "LUHANSKYI-DSTR",
    "ROVENKIVSKYI-DSTR",
    "SVATIVSKYI-DSTR",
    "STAROBILSKYI-DSTR",
    "SHCHASTYNSKYI-DSTR"
  ],
  "Львівська область": [
    "DROGOBICKYI-DSTR",
    "ZOLOCHIVSKYI-DSTR",
    "LVIVSKYI-DSTR",
    "SAMBIRSKYI-DSTR",
    "STRIJSKYI-DSTR",
    "CHERVONOGRADSKYI-DSTR",
    "YAVORIVSKYI-DSTR"
  ],
  "Миколаївська область": [
    "BASHTANSKYI-DSTR",
    "VOZNESENSKYI-DSTR",
    "MYKOLAIVSKYI-DSTR",
    "PERVOMAISKYI-DSTR"
  ],
  "Одеська область": [
    "IZMAILSKYI-DSTR",
    "BEREZIVSKYI-DSTR",
    "BOLHRADSKYI-DSTR",
    "BILHOROD-DNISTROVSKYI-DSTR",
    "KAMIANETS-PODILSKYI-DSTR",
    "ODESKYI-DSTR",
    "PODILSKYI-DSTR",
    "ROZDILNIANSKYI-DSTR"
  ],
  "Полтавська область": [
    "KREMENCHUTSKYI-DSTR",
    "LUBENSKYI-DSTR",
    "MYRHORODSKYI-DSTR",
    "POLTAVSKYI-DSTR"
  ],
  "Рівненська область": [
    "VARASKYI-DSTR",
    "DUBENSKYI-DSTR",
    "RIVNENSKYI-DSTR",
    "SARNENSKYI-DSTR"
  ],
  "Сумська область": [
    "KONOTOPSKYI-DSTR",
    "OKHTYRSKYI-DSTR",
    "ROMENSKYI-DSTR",
    "SUMSKYI-DSTR",
    "SHOSTKYNSKYI-DSTR"
  ],
  "Тернопільська область": [
    "KREMENECKYI-DSTR",
    "TERNOPILSKYI-DSTR",
    "CHORTKIVSKYI-DSTR"
  ],
  "Харківська область": [
    "KHARKIV-CITY",
    "IZIUMSKYI-DSTR",
    "KRASNOHRADSKYI-DSTR",
    "BOHODUKHIVSKYI-DSTR",
    "KUPIANSKYI-DSTR",
    "LOZIVSKYI-DSTR",
    "KHARKIVSKYI-DSTR",
    "CHUHUIVSKYI-DSTR"
  ],
  "Херсонська область": [
    "BERYSLAVSKYI-DSTR",
    "HENICHESKYI-DSTR",
    "KAKHOVSKYI-DSTR",
    "SKADOVSKYI-DSTR",
    "KHERSONSKYI-DSTR"
  ],
  "Хмельницька область": [
    "KHMELNYTSKYI-DSTR",
    "SHEPETIVSKYI-DSTR"
  ],
  "Черкаська область": [
    "ZVENYHORODSKYI-DSTR",
    "ZOLOTONISKYI-DSTR",
    "UMANSKYI-DSTR",
    "CHERKASKYI-DSTR"
  ],
  "Чернівецька область": [
    "VYZHNYTSKYI-DSTR",
    "DNISTROVSKYI-DSTR",
    "CHERNIVETSKYI-DSTR"
  ],
  "Чернігівська область": [
    "KORIUKIVSKYI-DSTR",
    "NOVHOROD-SIVERSKYI-DSTR",
    "NIZHYNSKYI-DSTR",
    "CHERNIHIVSKYI-DSTR"
  ],
  "АР Крим": [
    "SEVASTOPOL-CITY",
    "YEVPATORIISKYI-DSTR",
    "BAKHCHYSARAISKYI-DSTR",
    "BILOHIRSKYI-DSTR",
    "DZHANKOISKYI-DSTR",
    "KERCHENSKYI-DSTR",
    "KURMANSKYI-DSTR",
    "PEREKOPSKYI-DSTR",
    "SIMFEROPOLSKYI-DSTR",
    "FEODOSIISKYI-DSTR",
    "YALTYNSKYI-DSTR"
  ]
}

DISTRICTS_BY_SLUG = {
  "ODESKYI-DSTR": {
    "slug": "ODESKYI-DSTR",
    "title": "Одеський район",
    "rawTitle": "Одеський район",
    "titleEn": "Odesa District",
    "isCity": False
  },
  "SUMSKYI-DSTR": {
    "slug": "SUMSKYI-DSTR",
    "title": "Сумський район",
    "rawTitle": "Сумський район",
    "titleEn": "Sumy District",
    "isCity": False
  },
  "DROGOBICKYI-DSTR": {
    "slug": "DROGOBICKYI-DSTR",
    "title": "Дрогобицький район",
    "rawTitle": "Дрогобицький район",
    "titleEn": "Drogobych District",
    "isCity": False
  },
  "SAMBIRSKYI-DSTR": {
    "slug": "SAMBIRSKYI-DSTR",
    "title": "Самбірський район",
    "rawTitle": "Самбірський район",
    "titleEn": "Sambir District",
    "isCity": False
  },
  "ZOLOCHIVSKYI-DSTR": {
    "slug": "ZOLOCHIVSKYI-DSTR",
    "title": "Золочівський район",
    "rawTitle": "Золочівський район",
    "titleEn": "Zolochiv District",
    "isCity": False
  },
  "STRIJSKYI-DSTR": {
    "slug": "STRIJSKYI-DSTR",
    "title": "Стрийський район",
    "rawTitle": "Стрийський район",
    "titleEn": "Stryi District",
    "isCity": False
  },
  "LVIVSKYI-DSTR": {
    "slug": "LVIVSKYI-DSTR",
    "title": "Львівський район",
    "rawTitle": "Львівський район",
    "titleEn": "Lviv District",
    "isCity": False
  },
  "CHERVONOGRADSKYI-DSTR": {
    "slug": "CHERVONOGRADSKYI-DSTR",
    "title": "Шептицький район",
    "rawTitle": "Шептицький район",
    "titleEn": "Sheptytskyi District",
    "isCity": False
  },
  "YAVORIVSKYI-DSTR": {
    "slug": "YAVORIVSKYI-DSTR",
    "title": "Яворівський район",
    "rawTitle": "Яворівський район",
    "titleEn": "Yavoriv District",
    "isCity": False
  },
  "VOLODIMIR-VOLINSKYI-DSTR": {
    "slug": "VOLODIMIR-VOLINSKYI-DSTR",
    "title": "Володимирський район",
    "rawTitle": "Володимирський район",
    "titleEn": "Volodymyr District",
    "isCity": False
  },
  "KAMIN-KASHIRSKYI-DSTR": {
    "slug": "KAMIN-KASHIRSKYI-DSTR",
    "title": "Камінь-Каширський район",
    "rawTitle": "Камінь-Каширський район",
    "titleEn": "Kamin-Kashyrskyi District",
    "isCity": False
  },
  "KOVELSKYI-DSTR": {
    "slug": "KOVELSKYI-DSTR",
    "title": "Ковельський район",
    "rawTitle": "Ковельський район",
    "titleEn": "Kovel District",
    "isCity": False
  },
  "LUCKYI-DSTR": {
    "slug": "LUCKYI-DSTR",
    "title": "Луцький район",
    "rawTitle": "Луцький район",
    "titleEn": "Lutsk District",
    "isCity": False
  },
  "KREMENECKYI-DSTR": {
    "slug": "KREMENECKYI-DSTR",
    "title": "Кременецький район",
    "rawTitle": "Кременецький район",
    "titleEn": "Kremenets District",
    "isCity": False
  },
  "TERNOPILSKYI-DSTR": {
    "slug": "TERNOPILSKYI-DSTR",
    "title": "Тернопільський район",
    "rawTitle": "Тернопільський район",
    "titleEn": "Ternopil District",
    "isCity": False
  },
  "CHORTKIVSKYI-DSTR": {
    "slug": "CHORTKIVSKYI-DSTR",
    "title": "Чортківський район",
    "rawTitle": "Чортківський район",
    "titleEn": "Chortkiv District",
    "isCity": False
  },
  "VARASKYI-DSTR": {
    "slug": "VARASKYI-DSTR",
    "title": "Вараський район",
    "rawTitle": "Вараський район",
    "titleEn": "Varash District",
    "isCity": False
  },
  "DUBENSKYI-DSTR": {
    "slug": "DUBENSKYI-DSTR",
    "title": "Дубенський район",
    "rawTitle": "Дубенський район",
    "titleEn": "Dubenskiy District",
    "isCity": False
  },
  "RIVNENSKYI-DSTR": {
    "slug": "RIVNENSKYI-DSTR",
    "title": "Рівненський район",
    "rawTitle": "Рівненський район",
    "titleEn": "Rivnenskiy District",
    "isCity": False
  },
  "SARNENSKYI-DSTR": {
    "slug": "SARNENSKYI-DSTR",
    "title": "Сарненський район",
    "rawTitle": "Сарненський район",
    "titleEn": "Sarnenskiy District",
    "isCity": False
  },
  "BEREHIVSKYI-DSTR": {
    "slug": "BEREHIVSKYI-DSTR",
    "title": "Берегівський район",
    "rawTitle": "Берегівський район",
    "titleEn": "Beregove District",
    "isCity": False
  },
  "MUKACHIVSKYI-DSTR": {
    "slug": "MUKACHIVSKYI-DSTR",
    "title": "Мукачівський район",
    "rawTitle": "Мукачівський район",
    "titleEn": "Mukachevo District",
    "isCity": False
  },
  "RAKHIVSKYI-DSTR": {
    "slug": "RAKHIVSKYI-DSTR",
    "title": "Рахівський район",
    "rawTitle": "Рахівський район",
    "titleEn": "Rahiv District",
    "isCity": False
  },
  "TIACHIVSKYI-DSTR": {
    "slug": "TIACHIVSKYI-DSTR",
    "title": "Тячівський район",
    "rawTitle": "Тячівський район",
    "titleEn": "Tyachiv District",
    "isCity": False
  },
  "UZHHORODSKYI-DSTR": {
    "slug": "UZHHORODSKYI-DSTR",
    "title": "Ужгородський район",
    "rawTitle": "Ужгородський район",
    "titleEn": "Uzhhorod District",
    "isCity": False
  },
  "KHUSTSKYI-DSTR": {
    "slug": "KHUSTSKYI-DSTR",
    "title": "Хустський район",
    "rawTitle": "Хустський район",
    "titleEn": "Khustskiy District",
    "isCity": False
  },
  "VERKHOVYNSKYI-DSTR": {
    "slug": "VERKHOVYNSKYI-DSTR",
    "title": "Верховинський район",
    "rawTitle": "Верховинський район",
    "titleEn": "Verkhovyna District",
    "isCity": False
  },
  "IVANO-FRANKIVSKYI-DSTR": {
    "slug": "IVANO-FRANKIVSKYI-DSTR",
    "title": "Івано-Франківський район",
    "rawTitle": "Івано-Франківський район",
    "titleEn": "Ivano-Frankivsk Disctrict",
    "isCity": False
  },
  "KALUSKYI-DSTR": {
    "slug": "KALUSKYI-DSTR",
    "title": "Калуський район",
    "rawTitle": "Калуський район",
    "titleEn": "Kalush District",
    "isCity": False
  },
  "KOLOMYISKYI-DSTR": {
    "slug": "KOLOMYISKYI-DSTR",
    "title": "Коломийський район",
    "rawTitle": "Коломийський район",
    "titleEn": "Kolomyia District",
    "isCity": False
  },
  "KOSIVSKYI-DSTR": {
    "slug": "KOSIVSKYI-DSTR",
    "title": "Косівський район",
    "rawTitle": "Косівський район",
    "titleEn": "Kosiv District",
    "isCity": False
  },
  "NADVIRNIANSKYI-DSTR": {
    "slug": "NADVIRNIANSKYI-DSTR",
    "title": "Надвірнянський район",
    "rawTitle": "Надвірнянський район",
    "titleEn": "Nadvirna District",
    "isCity": False
  },
  "KAMIANETS-PODILSKYI-DSTR": {
    "slug": "KAMIANETS-PODILSKYI-DSTR",
    "title": "Кам'янець-Подільський район",
    "rawTitle": "Кам'янець-Подільський район",
    "titleEn": "Kamianets-Podilskyi District",
    "isCity": False
  },
  "KHMELNYTSKYI-DSTR": {
    "slug": "KHMELNYTSKYI-DSTR",
    "title": "Хмельницький район",
    "rawTitle": "Хмельницький район",
    "titleEn": "Khmelnytskyi District",
    "isCity": False
  },
  "SHEPETIVSKYI-DSTR": {
    "slug": "SHEPETIVSKYI-DSTR",
    "title": "Шепетівський район",
    "rawTitle": "Шепетівський район",
    "titleEn": "Shepetivka District",
    "isCity": False
  },
  "VYZHNYTSKYI-DSTR": {
    "slug": "VYZHNYTSKYI-DSTR",
    "title": "Вижницький район",
    "rawTitle": "Вижницький район",
    "titleEn": "Vyzhnytsya District",
    "isCity": False
  },
  "DNISTROVSKYI-DSTR": {
    "slug": "DNISTROVSKYI-DSTR",
    "title": "Дністровський район",
    "rawTitle": "Дністровський район",
    "titleEn": "Dnistrovskiy District",
    "isCity": False
  },
  "CHERNIVETSKYI-DSTR": {
    "slug": "CHERNIVETSKYI-DSTR",
    "title": "Чернівецький район",
    "rawTitle": "Чернівецький район",
    "titleEn": "Cherniveckiy District",
    "isCity": False
  },
  "BERDYCHIVSKYI-DSTR": {
    "slug": "BERDYCHIVSKYI-DSTR",
    "title": "Бердичівський район",
    "rawTitle": "Бердичівський район",
    "titleEn": "Berdichiv District",
    "isCity": False
  },
  "ZHYTOMYRSKYI-DSTR": {
    "slug": "ZHYTOMYRSKYI-DSTR",
    "title": "Житомирський район",
    "rawTitle": "Житомирський район",
    "titleEn": "Zhytomyr District",
    "isCity": False
  },
  "KOROSTENSKYI-DSTR": {
    "slug": "KOROSTENSKYI-DSTR",
    "title": "Коростенський район",
    "rawTitle": "Коростенський район",
    "titleEn": "Korosten District",
    "isCity": False
  },
  "NOVOHRAD-VOLYNSKYI-DSTR": {
    "slug": "NOVOHRAD-VOLYNSKYI-DSTR",
    "title": "Звягельський район",
    "rawTitle": "Звягельський район",
    "titleEn": "Zvyagel District",
    "isCity": False
  },
  "BILOTSERKIVSKYI-DSTR": {
    "slug": "BILOTSERKIVSKYI-DSTR",
    "title": "Білоцерківський район",
    "rawTitle": "Білоцерківський район",
    "titleEn": "Bila Tserkva District",
    "isCity": False
  },
  "BORYSPILSKYI-DSTR": {
    "slug": "BORYSPILSKYI-DSTR",
    "title": "Бориспільський район",
    "rawTitle": "Бориспільський район",
    "titleEn": "Boryspil District",
    "isCity": False
  },
  "BROVARSKYI-DSTR": {
    "slug": "BROVARSKYI-DSTR",
    "title": "Броварський район",
    "rawTitle": "Броварський район",
    "titleEn": "Brovary District",
    "isCity": False
  },
  "BUCHANSKYI-DSTR": {
    "slug": "BUCHANSKYI-DSTR",
    "title": "Бучанський район",
    "rawTitle": "Бучанський район",
    "titleEn": "Bucha District",
    "isCity": False
  },
  "VYSHHORODSKYI-DSTR": {
    "slug": "VYSHHORODSKYI-DSTR",
    "title": "Вишгородський район",
    "rawTitle": "Вишгородський район",
    "titleEn": "Vyshhorod District",
    "isCity": False
  },
  "OBUKHIVSKYI-DSTR": {
    "slug": "OBUKHIVSKYI-DSTR",
    "title": "Обухівський район",
    "rawTitle": "Обухівський район",
    "titleEn": "Obukhiv District",
    "isCity": False
  },
  "FASTIVSKYI-DSTR": {
    "slug": "FASTIVSKYI-DSTR",
    "title": "Фастівський район",
    "rawTitle": "Фастівський район",
    "titleEn": "Fastiv District",
    "isCity": False
  },
  "KORIUKIVSKYI-DSTR": {
    "slug": "KORIUKIVSKYI-DSTR",
    "title": "Корюківський район",
    "rawTitle": "Корюківський район",
    "titleEn": "Koryukivka District",
    "isCity": False
  },
  "NIZHYNSKYI-DSTR": {
    "slug": "NIZHYNSKYI-DSTR",
    "title": "Ніжинський район",
    "rawTitle": "Ніжинський район",
    "titleEn": "Nizhyn District",
    "isCity": False
  },
  "NOVHOROD-SIVERSKYI-DSTR": {
    "slug": "NOVHOROD-SIVERSKYI-DSTR",
    "title": "Новгород-Сіверський район",
    "rawTitle": "Новгород-Сіверський район",
    "titleEn": "Novhorod-Siverskyi District",
    "isCity": False
  },
  "PRYLUTSKYI-DSTR": {
    "slug": "PRYLUTSKYI-DSTR",
    "title": "Прилуцький район",
    "rawTitle": "Прилуцький район",
    "titleEn": "Pryluky District",
    "isCity": False
  },
  "CHERNIHIVSKYI-DSTR": {
    "slug": "CHERNIHIVSKYI-DSTR",
    "title": "Чернігівський район",
    "rawTitle": "Чернігівський район",
    "titleEn": "Chernihiv District",
    "isCity": False
  },
  "KONOTOPSKYI-DSTR": {
    "slug": "KONOTOPSKYI-DSTR",
    "title": "Конотопський район",
    "rawTitle": "Конотопський район",
    "titleEn": "Konotop District",
    "isCity": False
  },
  "OKHTYRSKYI-DSTR": {
    "slug": "OKHTYRSKYI-DSTR",
    "title": "Охтирський район",
    "rawTitle": "Охтирський район",
    "titleEn": "Okhtyrka District",
    "isCity": False
  },
  "ROMENSKYI-DSTR": {
    "slug": "ROMENSKYI-DSTR",
    "title": "Роменський район",
    "rawTitle": "Роменський район",
    "titleEn": "Romny District",
    "isCity": False
  },
  "SHOSTKYNSKYI-DSTR": {
    "slug": "SHOSTKYNSKYI-DSTR",
    "title": "Шосткинський район",
    "rawTitle": "Шосткинський район",
    "titleEn": "Shostka District",
    "isCity": False
  },
  "VINNYTSKYI-DSTR": {
    "slug": "VINNYTSKYI-DSTR",
    "title": "Вінницький район",
    "rawTitle": "Вінницький район",
    "titleEn": "Vinnickiy District",
    "isCity": False
  },
  "HAISYNSKYI-DSTR": {
    "slug": "HAISYNSKYI-DSTR",
    "title": "Гайсинський район",
    "rawTitle": "Гайсинський район",
    "titleEn": "Haisyn District",
    "isCity": False
  },
  "ZHMERYNSKYI-DSTR": {
    "slug": "ZHMERYNSKYI-DSTR",
    "title": "Жмеринський район",
    "rawTitle": "Жмеринський район",
    "titleEn": "Zhmerynka District",
    "isCity": False
  },
  "MOHYLIV-PODILSKYI-DSTR": {
    "slug": "MOHYLIV-PODILSKYI-DSTR",
    "title": "Могилів-Подільський район",
    "rawTitle": "Могилів-Подільський район",
    "titleEn": "Mohyliv-Podil's'kyi District",
    "isCity": False
  },
  "TULCHYNSKYI-DSTR": {
    "slug": "TULCHYNSKYI-DSTR",
    "title": "Тульчинський район",
    "rawTitle": "Тульчинський район",
    "titleEn": "Tulchinskiy District",
    "isCity": False
  },
  "KHMILNYTSKYI-DSTR": {
    "slug": "KHMILNYTSKYI-DSTR",
    "title": "Хмільницький район",
    "rawTitle": "Хмільницький район",
    "titleEn": "Khmilnyk District",
    "isCity": False
  },
  "ZVENYHORODSKYI-DSTR": {
    "slug": "ZVENYHORODSKYI-DSTR",
    "title": "Звенигородський район",
    "rawTitle": "Звенигородський район",
    "titleEn": "Zvenyhorodka District",
    "isCity": False
  },
  "ZOLOTONISKYI-DSTR": {
    "slug": "ZOLOTONISKYI-DSTR",
    "title": "Золотоніський район",
    "rawTitle": "Золотоніський район",
    "titleEn": "Zolotonosha District",
    "isCity": False
  },
  "UMANSKYI-DSTR": {
    "slug": "UMANSKYI-DSTR",
    "title": "Уманський район",
    "rawTitle": "Уманський район",
    "titleEn": "Uman District",
    "isCity": False
  },
  "CHERKASKYI-DSTR": {
    "slug": "CHERKASKYI-DSTR",
    "title": "Черкаський район",
    "rawTitle": "Черкаський район",
    "titleEn": "Cherkasy District",
    "isCity": False
  },
  "KREMENCHUTSKYI-DSTR": {
    "slug": "KREMENCHUTSKYI-DSTR",
    "title": "Кременчуцький район",
    "rawTitle": "Кременчуцький район",
    "titleEn": "Kremenchuk District",
    "isCity": False
  },
  "LUBENSKYI-DSTR": {
    "slug": "LUBENSKYI-DSTR",
    "title": "Лубенський район",
    "rawTitle": "Лубенський район",
    "titleEn": "Lubny District",
    "isCity": False
  },
  "MYRHORODSKYI-DSTR": {
    "slug": "MYRHORODSKYI-DSTR",
    "title": "Миргородський район",
    "rawTitle": "Миргородський район",
    "titleEn": "Mirgorod District",
    "isCity": False
  },
  "POLTAVSKYI-DSTR": {
    "slug": "POLTAVSKYI-DSTR",
    "title": "Полтавський район",
    "rawTitle": "Полтавський район",
    "titleEn": "Poltava District",
    "isCity": False
  },
  "HOLOVANIVSKYI-DSTR": {
    "slug": "HOLOVANIVSKYI-DSTR",
    "title": "Голованівський район",
    "rawTitle": "Голованівський район",
    "titleEn": "Golovanivskiy District",
    "isCity": False
  },
  "KROPYVNYTSKYI-DSTR": {
    "slug": "KROPYVNYTSKYI-DSTR",
    "title": "Кропивницький район",
    "rawTitle": "Кропивницький район",
    "titleEn": "Kropivnickiy District",
    "isCity": False
  },
  "NOVOUKRAINSKYI-DSTR": {
    "slug": "NOVOUKRAINSKYI-DSTR",
    "title": "Новоукраїнський район",
    "rawTitle": "Новоукраїнський район",
    "titleEn": "Novoukrayinskiy District",
    "isCity": False
  },
  "OLEKSANDRIISKYI-DSTR": {
    "slug": "OLEKSANDRIISKYI-DSTR",
    "title": "Олександрійський район",
    "rawTitle": "Олександрійський район",
    "titleEn": "Oleksandriyskiy District",
    "isCity": False
  },
  "DNIPROVSKYI-DSTR": {
    "slug": "DNIPROVSKYI-DSTR",
    "title": "Дніпровський район",
    "rawTitle": "Дніпровський район",
    "titleEn": "Dnipro District",
    "isCity": False
  },
  "KAMIANSKYI-DSTR": {
    "slug": "KAMIANSKYI-DSTR",
    "title": "Кам'янський район",
    "rawTitle": "Кам'янський район",
    "titleEn": "Kam'yanske District",
    "isCity": False
  },
  "KRYVORIZKYI-DSTR": {
    "slug": "KRYVORIZKYI-DSTR",
    "title": "Криворізький район",
    "rawTitle": "Криворізький район",
    "titleEn": "Kriviy Rih District",
    "isCity": False
  },
  "NIKOPOLSKYI-DSTR": {
    "slug": "NIKOPOLSKYI-DSTR",
    "title": "Нікопольський район",
    "rawTitle": "Нікопольський район",
    "titleEn": "Nikopol District",
    "isCity": False
  },
  "NOVOMOSKOVSKYI-DSTR": {
    "slug": "NOVOMOSKOVSKYI-DSTR",
    "title": "Самарівський район",
    "rawTitle": "Самарівський район",
    "titleEn": "Samar District",
    "isCity": False
  },
  "PAVLOHRADSKYI-DSTR": {
    "slug": "PAVLOHRADSKYI-DSTR",
    "title": "Павлоградський район",
    "rawTitle": "Павлоградський район",
    "titleEn": "Pavlograd District",
    "isCity": False
  },
  "SYNELNYKIVSKYI-DSTR": {
    "slug": "SYNELNYKIVSKYI-DSTR",
    "title": "Синельниківський район",
    "rawTitle": "Синельниківський район",
    "titleEn": "Synel'nykove District",
    "isCity": False
  },
  "BEREZIVSKYI-DSTR": {
    "slug": "BEREZIVSKYI-DSTR",
    "title": "Березівський район",
    "rawTitle": "Березівський район",
    "titleEn": "Berezivka District",
    "isCity": False
  },
  "BILHOROD-DNISTROVSKYI-DSTR": {
    "slug": "BILHOROD-DNISTROVSKYI-DSTR",
    "title": "Білгород-Дністровський район",
    "rawTitle": "Білгород-Дністровський район",
    "titleEn": "Bilhorod-Dnistrovskyi District",
    "isCity": False
  },
  "IZMAILSKYI-DSTR": {
    "slug": "IZMAILSKYI-DSTR",
    "title": "Ізмаїльський район",
    "rawTitle": "Ізмаїльський район",
    "titleEn": "Izmail District",
    "isCity": False
  },
  "PODILSKYI-DSTR": {
    "slug": "PODILSKYI-DSTR",
    "title": "Подільський район",
    "rawTitle": "Подільський район",
    "titleEn": "Podilsk District",
    "isCity": False
  },
  "ROZDILNIANSKYI-DSTR": {
    "slug": "ROZDILNIANSKYI-DSTR",
    "title": "Роздільнянський район",
    "rawTitle": "Роздільнянський район",
    "titleEn": "Rozdilna District",
    "isCity": False
  },
  "BASHTANSKYI-DSTR": {
    "slug": "BASHTANSKYI-DSTR",
    "title": "Баштанський район",
    "rawTitle": "Баштанський район",
    "titleEn": "Bashtanka District",
    "isCity": False
  },
  "VOZNESENSKYI-DSTR": {
    "slug": "VOZNESENSKYI-DSTR",
    "title": "Вознесенський район",
    "rawTitle": "Вознесенський район",
    "titleEn": "Voznesensk District",
    "isCity": False
  },
  "MYKOLAIVSKYI-DSTR": {
    "slug": "MYKOLAIVSKYI-DSTR",
    "title": "Миколаївський район",
    "rawTitle": "Миколаївський район",
    "titleEn": "Mykolaiv District",
    "isCity": False
  },
  "PERVOMAISKYI-DSTR": {
    "slug": "PERVOMAISKYI-DSTR",
    "title": "Первомайський район",
    "rawTitle": "Первомайський район",
    "titleEn": "Pervomaysk District",
    "isCity": False
  },
  "BERYSLAVSKYI-DSTR": {
    "slug": "BERYSLAVSKYI-DSTR",
    "title": "Бериславський район",
    "rawTitle": "Бериславський район",
    "titleEn": "Beryslav District",
    "isCity": False
  },
  "HENICHESKYI-DSTR": {
    "slug": "HENICHESKYI-DSTR",
    "title": "Генічеський район",
    "rawTitle": "Генічеський район",
    "titleEn": "Henichesk District",
    "isCity": False
  },
  "KAKHOVSKYI-DSTR": {
    "slug": "KAKHOVSKYI-DSTR",
    "title": "Каховський район",
    "rawTitle": "Каховський район",
    "titleEn": "Kakhovka District",
    "isCity": False
  },
  "SKADOVSKYI-DSTR": {
    "slug": "SKADOVSKYI-DSTR",
    "title": "Скадовський район",
    "rawTitle": "Скадовський район",
    "titleEn": "Skadovsk District",
    "isCity": False
  },
  "KHERSONSKYI-DSTR": {
    "slug": "KHERSONSKYI-DSTR",
    "title": "Херсонський район",
    "rawTitle": "Херсонський район",
    "titleEn": "Kherson District",
    "isCity": False
  },
  "BERDIANSKYI-DSTR": {
    "slug": "BERDIANSKYI-DSTR",
    "title": "Бердянський район",
    "rawTitle": "Бердянський район",
    "titleEn": "Berdyanskiy District",
    "isCity": False
  },
  "VASYLIVSKYI-DSTR": {
    "slug": "VASYLIVSKYI-DSTR",
    "title": "Василівський район",
    "rawTitle": "Василівський район",
    "titleEn": "Vasilivskiy District",
    "isCity": False
  },
  "ZAPORIZKYI-DSTR": {
    "slug": "ZAPORIZKYI-DSTR",
    "title": "Запорізький район",
    "rawTitle": "Запорізький район",
    "titleEn": "Zaporizhzhia District",
    "isCity": False
  },
  "MELITOPOLSKYI-DSTR": {
    "slug": "MELITOPOLSKYI-DSTR",
    "title": "Мелітопольський район",
    "rawTitle": "Мелітопольський район",
    "titleEn": "Melitopol District",
    "isCity": False
  },
  "POLOHIVSKYI-DSTR": {
    "slug": "POLOHIVSKYI-DSTR",
    "title": "Пологівський район",
    "rawTitle": "Пологівський район",
    "titleEn": "Polohy District",
    "isCity": False
  },
  "BAKHCHYSARAISKYI-DSTR": {
    "slug": "BAKHCHYSARAISKYI-DSTR",
    "title": "Бахчисарайський район",
    "rawTitle": "Бахчисарайський район",
    "titleEn": "Bahchisarayskiy District",
    "isCity": False
  },
  "YEVPATORIISKYI-DSTR": {
    "slug": "YEVPATORIISKYI-DSTR",
    "title": "Євпаторійський район",
    "rawTitle": "Євпаторійський район",
    "titleEn": "Ievpatoriyskiy District",
    "isCity": False
  },
  "KURMANSKYI-DSTR": {
    "slug": "KURMANSKYI-DSTR",
    "title": "Курманський район",
    "rawTitle": "Курманський район",
    "titleEn": "Kurmanskiy District",
    "isCity": False
  },
  "PEREKOPSKYI-DSTR": {
    "slug": "PEREKOPSKYI-DSTR",
    "title": "Перекопський район",
    "rawTitle": "Перекопський район",
    "titleEn": "Perekopskiy District",
    "isCity": False
  },
  "SIMFEROPOLSKYI-DSTR": {
    "slug": "SIMFEROPOLSKYI-DSTR",
    "title": "Сімферопольський район",
    "rawTitle": "Сімферопольський район",
    "titleEn": "Simferopolskiy District",
    "isCity": False
  },
  "FEODOSIISKYI-DSTR": {
    "slug": "FEODOSIISKYI-DSTR",
    "title": "Феодосійський район",
    "rawTitle": "Феодосійський район",
    "titleEn": "Feodosiyskiy District",
    "isCity": False
  },
  "DZHANKOISKYI-DSTR": {
    "slug": "DZHANKOISKYI-DSTR",
    "title": "Джанкойський район",
    "rawTitle": "Джанкойський район",
    "titleEn": "Dzhankoyskiy District",
    "isCity": False
  },
  "YALTYNSKYI-DSTR": {
    "slug": "YALTYNSKYI-DSTR",
    "title": "Ялтинський район",
    "rawTitle": "Ялтинський район",
    "titleEn": "Yaltinskiy District",
    "isCity": False
  },
  "BOHODUKHIVSKYI-DSTR": {
    "slug": "BOHODUKHIVSKYI-DSTR",
    "title": "Богодухівський район",
    "rawTitle": "Богодухівський район",
    "titleEn": "Bogoduhiv District",
    "isCity": False
  },
  "IZIUMSKYI-DSTR": {
    "slug": "IZIUMSKYI-DSTR",
    "title": "Ізюмський район",
    "rawTitle": "Ізюмський район",
    "titleEn": "Izyum District",
    "isCity": False
  },
  "KRASNOHRADSKYI-DSTR": {
    "slug": "KRASNOHRADSKYI-DSTR",
    "title": "Берестинський район",
    "rawTitle": "Берестинський район",
    "titleEn": "Berestyn District",
    "isCity": False
  },
  "KUPIANSKYI-DSTR": {
    "slug": "KUPIANSKYI-DSTR",
    "title": "Куп'янський район",
    "rawTitle": "Куп'янський район",
    "titleEn": "Kup'yansk District",
    "isCity": False
  },
  "LOZIVSKYI-DSTR": {
    "slug": "LOZIVSKYI-DSTR",
    "title": "Лозівський район",
    "rawTitle": "Лозівський район",
    "titleEn": "Lozova District",
    "isCity": False
  },
  "KHARKIVSKYI-DSTR": {
    "slug": "KHARKIVSKYI-DSTR",
    "title": "Харківський район",
    "rawTitle": "Харківський район",
    "titleEn": "Kharkiv District",
    "isCity": False
  },
  "CHUHUIVSKYI-DSTR": {
    "slug": "CHUHUIVSKYI-DSTR",
    "title": "Чугуївський район",
    "rawTitle": "Чугуївський район",
    "titleEn": "Chuhuiv District",
    "isCity": False
  },
  "BAKHMUTSKYI-DSTR": {
    "slug": "BAKHMUTSKYI-DSTR",
    "title": "Бахмутський район",
    "rawTitle": "Бахмутський район",
    "titleEn": "Bakhmut District",
    "isCity": False
  },
  "VOLNOVASKYI-DSTR": {
    "slug": "VOLNOVASKYI-DSTR",
    "title": "Волноваський район",
    "rawTitle": "Волноваський район",
    "titleEn": "Volnovaskiy District",
    "isCity": False
  },
  "HORLIVSKYI-DSTR": {
    "slug": "HORLIVSKYI-DSTR",
    "title": "Горлівський район",
    "rawTitle": "Горлівський район",
    "titleEn": "Horlivka District",
    "isCity": False
  },
  "DONETSKYI-DSTR": {
    "slug": "DONETSKYI-DSTR",
    "title": "Донецький район",
    "rawTitle": "Донецький район",
    "titleEn": "Donetsk District",
    "isCity": False
  },
  "KALMIUSKYI-DSTR": {
    "slug": "KALMIUSKYI-DSTR",
    "title": "Кальміуський район",
    "rawTitle": "Кальміуський район",
    "titleEn": "Kalmiuske District",
    "isCity": False
  },
  "KRAMATORSKYI-DSTR": {
    "slug": "KRAMATORSKYI-DSTR",
    "title": "Краматорський район",
    "rawTitle": "Краматорський район",
    "titleEn": "Kramatorsk District",
    "isCity": False
  },
  "MARIUPOLSKYI-DSTR": {
    "slug": "MARIUPOLSKYI-DSTR",
    "title": "Маріупольський район",
    "rawTitle": "Маріупольський район",
    "titleEn": "Mariupol District",
    "isCity": False
  },
  "POKROVSKYI-DSTR": {
    "slug": "POKROVSKYI-DSTR",
    "title": "Покровський район",
    "rawTitle": "Покровський район",
    "titleEn": "Pokrovsk District",
    "isCity": False
  },
  "ALCHEVSKYI-DSTR": {
    "slug": "ALCHEVSKYI-DSTR",
    "title": "Алчевський район",
    "rawTitle": "Алчевський район",
    "titleEn": "Alchevskiy District",
    "isCity": False
  },
  "DOVZHANSKYI-DSTR": {
    "slug": "DOVZHANSKYI-DSTR",
    "title": "Довжанський район",
    "rawTitle": "Довжанський район",
    "titleEn": "Dovzhanskiy District",
    "isCity": False
  },
  "LUHANSKYI-DSTR": {
    "slug": "LUHANSKYI-DSTR",
    "title": "Луганський район",
    "rawTitle": "Луганський район",
    "titleEn": "Luganskiy District",
    "isCity": False
  },
  "SVATIVSKYI-DSTR": {
    "slug": "SVATIVSKYI-DSTR",
    "title": "Сватівський район",
    "rawTitle": "Сватівський район",
    "titleEn": "Svativskiy District",
    "isCity": False
  },
  "SIEVIERODONETSKYI-DSTR": {
    "slug": "SIEVIERODONETSKYI-DSTR",
    "title": "Сіверськодонецький район",
    "rawTitle": "Сіверськодонецький район",
    "titleEn": "Siverskodoneckiy District",
    "isCity": False
  },
  "STAROBILSKYI-DSTR": {
    "slug": "STAROBILSKYI-DSTR",
    "title": "Старобільський район",
    "rawTitle": "Старобільський район",
    "titleEn": "Starobilsk District",
    "isCity": False
  },
  "SHCHASTYNSKYI-DSTR": {
    "slug": "SHCHASTYNSKYI-DSTR",
    "title": "Щастинський район",
    "rawTitle": "Щастинський район",
    "titleEn": "Shchastinskiy District",
    "isCity": False
  },
  "ROVENKIVSKYI-DSTR": {
    "slug": "ROVENKIVSKYI-DSTR",
    "title": "Ровеньківський район",
    "rawTitle": "Ровеньківський район",
    "titleEn": "Rovenkivskiy District",
    "isCity": False
  },
  "BOLHRADSKYI-DSTR": {
    "slug": "BOLHRADSKYI-DSTR",
    "title": "Болградський район",
    "rawTitle": "Болградський район",
    "titleEn": "Bolgrad District",
    "isCity": False
  },
  "BILOHIRSKYI-DSTR": {
    "slug": "BILOHIRSKYI-DSTR",
    "title": "Білогірський район",
    "rawTitle": "Білогірський район",
    "titleEn": "Bilogirskiy District",
    "isCity": False
  },
  "KERCHENSKYI-DSTR": {
    "slug": "KERCHENSKYI-DSTR",
    "title": "Керченський район",
    "rawTitle": "Керченський район",
    "titleEn": "Kerchenskiy District",
    "isCity": False
  },
  "KIYEW": {
    "slug": "KIYEW",
    "title": "Київ",
    "rawTitle": "Київ",
    "titleEn": "Kyiv",
    "isCity": False
  },
  "KHARKIV-CITY": {
    "slug": "KHARKIV-CITY",
    "title": "м. Харків (місто)",
    "rawTitle": "Харків",
    "titleEn": "Kharkiv",
    "isCity": True
  },
  "MARHANETS-CITY": {
    "slug": "MARHANETS-CITY",
    "title": "м. Марганець (місто)",
    "rawTitle": "Марганець",
    "titleEn": "Marganec",
    "isCity": True
  },
  "NIKOPOL-CITY": {
    "slug": "NIKOPOL-CITY",
    "title": "м. Нікополь (місто)",
    "rawTitle": "Нікополь",
    "titleEn": "Nikopol",
    "isCity": True
  },
  "ZAPORIZHZHIA-CITY": {
    "slug": "ZAPORIZHZHIA-CITY",
    "title": "м. Запоріжжя (місто)",
    "rawTitle": "Запоріжжя",
    "titleEn": "Zaporizhzhia",
    "isCity": True
  },
  "SEVASTOPOL-CITY": {
    "slug": "SEVASTOPOL-CITY",
    "title": "м. Севастополь (місто)",
    "rawTitle": "Севастополь",
    "titleEn": "Sevastopol",
    "isCity": True
  },
  "POKROV-CITY": {
    "slug": "POKROV-CITY",
    "title": "м. Покров (місто)",
    "rawTitle": "Покров",
    "titleEn": "Pokrov",
    "isCity": True
  },
  "SLAVUTICH-CITY": {
    "slug": "SLAVUTICH-CITY",
    "title": "м. Славутич (місто)",
    "rawTitle": "Славутич",
    "titleEn": "Slavutych",
    "isCity": True
  }
}

DISTRICT_TO_CITIES = {
  "ODESKYI-DSTR": [
    "Єгорівка",
    "Барабой",
    "Болгарка",
    "Білярі",
    "Біляївка",
    "Великий",
    "Великий Дальник",
    "Великодолинське",
    "Вигода",
    "Грибівка",
    "Дальник",
    "Дачне",
    "Доброслав",
    "Лиманка",
    "Маяки",
    "Молодіжне",
    "Овідіополь",
    "Одеса",
    "Олександрівка",
    "Південне",
    "Південне (Южне)",
    "Роксолани",
    "Санжійка",
    "Усатове",
    "Фонтанка",
    "Чабанка",
    "Чорноморськ",
    "Чорноморське"
  ],
  "SUMSKYI-DSTR": [
    "Іскрисківщина",
    "Атинське",
    "Басівка",
    "Будки",
    "Білопілля",
    "Велика",
    "Велика Чернеччина",
    "Верхня",
    "Верхня Сироватка",
    "Волфине",
    "Ворожба",
    "Катеринівка",
    "Краснопілля",
    "Кіндратівка",
    "Лебедин",
    "Мезенівка",
    "Миколаївка",
    "Миропілля",
    "Могриця",
    "Ободи",
    "Павлівка",
    "Рижівка",
    "Річки",
    "Степанівка",
    "Стецьківка",
    "Суми",
    "Токарі",
    "Угроїди",
    "Хотінь",
    "Юнаківка"
  ],
  "DROGOBICKYI-DSTR": [
    "Дрогобич"
  ],
  "SAMBIRSKYI-DSTR": [
    "Самбір"
  ],
  "ZOLOCHIVSKYI-DSTR": [
    "Буськ",
    "Золочів"
  ],
  "STRIJSKYI-DSTR": [
    "Стрий",
    "Ходорів"
  ],
  "LVIVSKYI-DSTR": [
    "Бібрка",
    "Городок",
    "Львів"
  ],
  "CHERVONOGRADSKYI-DSTR": [],
  "YAVORIVSKYI-DSTR": [
    "Яворів"
  ],
  "VOLODIMIR-VOLINSKYI-DSTR": [],
  "KAMIN-KASHIRSKYI-DSTR": [
    "Камінь-Каширський",
    "Любешів",
    "Маневичі"
  ],
  "KOVELSKYI-DSTR": [
    "Голоби",
    "Ковель",
    "Любомль",
    "Ратне",
    "Стара",
    "Стара Вижівка",
    "Турійськ",
    "Шацьк"
  ],
  "LUCKYI-DSTR": [
    "Горохів",
    "Ківерці",
    "Луцьк",
    "Рожище"
  ],
  "KREMENECKYI-DSTR": [
    "Кременець",
    "Ланівці",
    "Шумськ"
  ],
  "TERNOPILSKYI-DSTR": [
    "Бережани",
    "Збараж",
    "Зборів",
    "Козова",
    "Підволочиськ",
    "Підгайці",
    "Теребовля",
    "Тернопіль"
  ],
  "CHORTKIVSKYI-DSTR": [
    "Борщів",
    "Бучач",
    "Гусятин",
    "Заліщики",
    "Монастириська",
    "Чортків"
  ],
  "VARASKYI-DSTR": [
    "Вараш"
  ],
  "DUBENSKYI-DSTR": [
    "Дубно"
  ],
  "RIVNENSKYI-DSTR": [
    "Березне",
    "Здолбунів",
    "Корець",
    "Костопіль",
    "Острог",
    "Рівне"
  ],
  "SARNENSKYI-DSTR": [
    "Дубровиця",
    "Рокитне",
    "Сарни"
  ],
  "BEREHIVSKYI-DSTR": [
    "Берегове",
    "Виноградів"
  ],
  "MUKACHIVSKYI-DSTR": [
    "Воловець",
    "Мукачево",
    "Свалява"
  ],
  "RAKHIVSKYI-DSTR": [
    "Рахів"
  ],
  "TIACHIVSKYI-DSTR": [
    "Тячів"
  ],
  "UZHHORODSKYI-DSTR": [
    "Великий",
    "Великий Березний",
    "Перечин",
    "Ужгород"
  ],
  "KHUSTSKYI-DSTR": [
    "Іршава",
    "Міжгір'Я",
    "Хуст"
  ],
  "VERKHOVYNSKYI-DSTR": [
    "Верховина"
  ],
  "IVANO-FRANKIVSKYI-DSTR": [
    "Івано-Франківськ",
    "Богородчани",
    "Бурштин",
    "Галич",
    "Рогатин",
    "Тлумач"
  ],
  "KALUSKYI-DSTR": [
    "Долина",
    "Калуш",
    "Рожнятів"
  ],
  "KOLOMYISKYI-DSTR": [
    "Городенка",
    "Коломия",
    "Снятин"
  ],
  "KOSIVSKYI-DSTR": [
    "Косів"
  ],
  "NADVIRNIANSKYI-DSTR": [
    "Надвірна",
    "Яремче"
  ],
  "KAMIANETS-PODILSKYI-DSTR": [
    "Кам'Янець-Подільський"
  ],
  "KHMELNYTSKYI-DSTR": [
    "Адампіль",
    "Волочиськ",
    "Красилів",
    "Старокостянтинів",
    "Теофіполь",
    "Хмельницький"
  ],
  "SHEPETIVSKYI-DSTR": [
    "Нетішин",
    "Полонне",
    "Славута",
    "Шепетівка"
  ],
  "VYZHNYTSKYI-DSTR": [
    "Вижниця",
    "Мігове",
    "Путила"
  ],
  "DNISTROVSKYI-DSTR": [
    "Кельменці",
    "Сокиряни",
    "Хотин"
  ],
  "CHERNIVETSKYI-DSTR": [
    "Герца",
    "Чернівці"
  ],
  "BERDYCHIVSKYI-DSTR": [
    "Андрушівка",
    "Бердичів",
    "Ружин"
  ],
  "ZHYTOMYRSKYI-DSTR": [
    "Брусилів",
    "Житомир",
    "Коростишів",
    "Любар",
    "Озерне",
    "Попільня",
    "Пулини",
    "Радомишль",
    "Романів",
    "Хорошів",
    "Черняхів",
    "Чуднів"
  ],
  "KOROSTENSKYI-DSTR": [
    "Іршанськ",
    "Коростень",
    "Лугини",
    "Малин",
    "Народичі",
    "Овруч",
    "Олевськ"
  ],
  "NOVOHRAD-VOLYNSKYI-DSTR": [],
  "BILOTSERKIVSKYI-DSTR": [
    "Біла",
    "Біла Церква",
    "Володарка",
    "Рокитне",
    "Сквира",
    "Ставище",
    "Тараща",
    "Тетіїв",
    "Узин"
  ],
  "BORYSPILSKYI-DSTR": [
    "Бориспіль",
    "Переяслав",
    "Яготин"
  ],
  "BROVARSKYI-DSTR": [
    "Баришівка",
    "Бровари",
    "Велика",
    "Велика Димерка",
    "Зазим'Я",
    "Згурівка",
    "Семиполки"
  ],
  "BUCHANSKYI-DSTR": [
    "Ірпінь",
    "Бородянка",
    "Буча",
    "Білогородка",
    "Вишневе",
    "Ворзель",
    "Гаврилівка",
    "Гостомель",
    "Макарів",
    "Наливайківка"
  ],
  "VYSHHORODSKYI-DSTR": [
    "Іванків",
    "Вишгород",
    "Димер",
    "Поліське"
  ],
  "OBUKHIVSKYI-DSTR": [
    "Богуслав",
    "Васильків",
    "Кагарлик",
    "Миронівка",
    "Обухів",
    "Ржищів",
    "Українка",
    "Хотів"
  ],
  "FASTIVSKYI-DSTR": [
    "Боярка",
    "Гатне",
    "Калинівка",
    "Фастів",
    "Чабани"
  ],
  "KORIUKIVSKYI-DSTR": [
    "Корюківка",
    "Мена",
    "Сновськ",
    "Сосниця",
    "Холми"
  ],
  "NIZHYNSKYI-DSTR": [
    "Батурин",
    "Бахмач",
    "Бобровиця",
    "Борзна",
    "Борозна",
    "Носівка",
    "Ніжин"
  ],
  "NOVHOROD-SIVERSKYI-DSTR": [
    "Короп",
    "Новгород-Сіверський",
    "Семенівка"
  ],
  "PRYLUTSKYI-DSTR": [
    "Ічня",
    "Варва",
    "Прилуки",
    "Срібне",
    "Талалаївка"
  ],
  "CHERNIHIVSKYI-DSTR": [
    "Гончарівське",
    "Городня",
    "Десна",
    "Козелець",
    "Куликівка",
    "Любеч",
    "Остер",
    "Ріпки",
    "Славутич",
    "Чернігів"
  ],
  "KONOTOPSKYI-DSTR": [
    "Буринь",
    "Конотоп",
    "Кролевець",
    "Нова",
    "Нова Слобода",
    "Путивль"
  ],
  "OKHTYRSKYI-DSTR": [
    "Велика",
    "Велика Писарівка",
    "Охтирка",
    "Тростянець"
  ],
  "ROMENSKYI-DSTR": [
    "Липова",
    "Липова Долина",
    "Недригайлів",
    "Ромни",
    "Терни"
  ],
  "SHOSTKYNSKYI-DSTR": [
    "Вороніж",
    "Глухів",
    "Есмань",
    "Зноб-Новгородське",
    "Свеса",
    "Середина-Буда",
    "Шалигине",
    "Шостка",
    "Ямпіль"
  ],
  "VINNYTSKYI-DSTR": [
    "Іллінці",
    "Вінниця",
    "Гнівань",
    "Липовець",
    "Літин",
    "Немирів",
    "Оратів",
    "Погребище",
    "Тиврів"
  ],
  "HAISYNSKYI-DSTR": [
    "Бершадь",
    "Гайсин",
    "Ладижин",
    "Теплик",
    "Тростянець",
    "Чечельник"
  ],
  "ZHMERYNSKYI-DSTR": [
    "Бар",
    "Жмеринка",
    "Шаргород"
  ],
  "MOHYLIV-PODILSKYI-DSTR": [
    "Могилів-Подільський",
    "Муровані",
    "Муровані Курилівці",
    "Чернівці",
    "Ямпіль"
  ],
  "TULCHYNSKYI-DSTR": [
    "Крижопіль",
    "Піщанка",
    "Томашпіль",
    "Тульчин"
  ],
  "KHMILNYTSKYI-DSTR": [
    "Калинівка",
    "Козятин",
    "Хмільник"
  ],
  "ZVENYHORODSKYI-DSTR": [
    "Багачеве",
    "Звенигородка"
  ],
  "ZOLOTONISKYI-DSTR": [
    "Золотоноша"
  ],
  "UMANSKYI-DSTR": [
    "Жашків",
    "Умань"
  ],
  "CHERKASKYI-DSTR": [
    "Канів",
    "Корсунь-Шевченківський",
    "Сміла",
    "Черкаси",
    "Чигирин"
  ],
  "KREMENCHUTSKYI-DSTR": [
    "Глобине",
    "Горішні",
    "Горішні Плавні",
    "Градизьк",
    "Кременчук"
  ],
  "LUBENSKYI-DSTR": [
    "Гребінка",
    "Лубни",
    "Оржиця",
    "Пирятин",
    "Хорол"
  ],
  "MYRHORODSKYI-DSTR": [
    "Гадяч",
    "Заводське",
    "Комишня",
    "Лохвиця",
    "Миргород",
    "Ромодан"
  ],
  "POLTAVSKYI-DSTR": [
    "Зіньків",
    "Карлівка",
    "Кобеляки",
    "Котельва",
    "Машівка",
    "Нові",
    "Нові Санжари",
    "Полтава",
    "Решетилівка",
    "Скороходове",
    "Чутове"
  ],
  "HOLOVANIVSKYI-DSTR": [
    "Благовіщенське",
    "Вільшанка",
    "Гайворон",
    "Голованівськ",
    "Новоархангельськ"
  ],
  "KROPYVNYTSKYI-DSTR": [
    "Бобринець",
    "Долинська",
    "Знам'Янка",
    "Компаніївка",
    "Кропивницький",
    "Новгородка",
    "Олександрівка",
    "Устинівка"
  ],
  "NOVOUKRAINSKYI-DSTR": [
    "Добровеличківка",
    "Мала",
    "Мала Виска",
    "Новомиргород",
    "Новоукраїнка"
  ],
  "OLEKSANDRIISKYI-DSTR": [
    "Олександрія",
    "Онуфріївка",
    "Петрове",
    "Світловодськ"
  ],
  "DNIPROVSKYI-DSTR": [
    "Дніпро",
    "Петриківка",
    "Солоне",
    "Царичанка"
  ],
  "KAMIANSKYI-DSTR": [
    "Божедарівка",
    "Верхньодніпровськ",
    "Верхівцеве",
    "Вільногірськ",
    "Жовті",
    "Жовті Води",
    "Кам'Янське",
    "Кринички",
    "П'Ятихатки"
  ],
  "KRYVORIZKYI-DSTR": [
    "Апостолове",
    "Велика",
    "Велика Долина",
    "Зеленодольськ",
    "Кривий",
    "Кривий Ріг",
    "Мар'Янське",
    "Софіївка",
    "Широке"
  ],
  "NIKOPOLSKYI-DSTR": [
    "Марганець",
    "Новопавлівка",
    "Нікополь",
    "Покров",
    "Томаківка",
    "Червоногригорівка"
  ],
  "NOVOMOSKOVSKYI-DSTR": [],
  "PAVLOHRADSKYI-DSTR": [
    "Павлоград",
    "Юріївка"
  ],
  "SYNELNYKIVSKYI-DSTR": [
    "Васильківка",
    "Межова",
    "Петропавлівка",
    "Покровське",
    "Просяна",
    "Синельникове",
    "Чаплине",
    "Шахтарське"
  ],
  "BEREZIVSKYI-DSTR": [
    "Березівка"
  ],
  "BILHOROD-DNISTROVSKYI-DSTR": [
    "Білгород-Дністровський",
    "Затока",
    "Кароліно-Бугаз",
    "Сарата",
    "Сергіївка",
    "Татарбунари",
    "Тузли",
    "Шабо"
  ],
  "IZMAILSKYI-DSTR": [
    "Ізмаїл",
    "Вилкове",
    "Кілія"
  ],
  "PODILSKYI-DSTR": [
    "Любашівка",
    "Подільськ"
  ],
  "ROZDILNIANSKYI-DSTR": [
    "Лиманське",
    "Роздільна"
  ],
  "BASHTANSKYI-DSTR": [
    "Баштанка",
    "Березнегувате",
    "Новий",
    "Новий Буг",
    "Снігурівка"
  ],
  "VOZNESENSKYI-DSTR": [
    "Єланець",
    "Вознесенськ",
    "Південноукраїнськ",
    "Південноукраїнськ (Южноукраїнськ)"
  ],
  "MYKOLAIVSKYI-DSTR": [
    "Березанка",
    "Дмитрівка",
    "Дніпровське",
    "Коблеве",
    "Куцуруб",
    "Миколаїв",
    "Очаків",
    "Рибаківка",
    "Солончаки"
  ],
  "PERVOMAISKYI-DSTR": [
    "Арбузинка",
    "Криве",
    "Криве Озеро",
    "Первомайськ"
  ],
  "BERYSLAVSKYI-DSTR": [
    "Архангельське",
    "Берислав",
    "Велика",
    "Велика Олександрівка",
    "Нововоронцовка",
    "Осокорівка",
    "Суханове",
    "Урожайне"
  ],
  "HENICHESKYI-DSTR": [
    "Генічеськ"
  ],
  "KAKHOVSKYI-DSTR": [
    "Каховка",
    "Нова",
    "Нова Каховка",
    "Таврійськ",
    "Чаплинка"
  ],
  "SKADOVSKYI-DSTR": [
    "Скадовськ"
  ],
  "KHERSONSKYI-DSTR": [
    "Антонівка",
    "Білозерка",
    "Зеленівка",
    "Музиківка",
    "Олександрівка",
    "Олешки",
    "Херсон",
    "Чорнобаївка"
  ],
  "BERDIANSKYI-DSTR": [
    "Бердянськ",
    "Приморськ",
    "Чернігівка"
  ],
  "VASYLIVSKYI-DSTR": [
    "Велика",
    "Велика Білозерка",
    "Енергодар",
    "Кам'Янка-Дніпровська",
    "Михайлівка",
    "Приморське",
    "Степногірськ"
  ],
  "ZAPORIZKYI-DSTR": [
    "Балабине",
    "Біленьке",
    "Вільнянськ",
    "Запоріжжя",
    "Комишуваха",
    "Кушугум",
    "Малокатеринівка",
    "Новомиколаївка",
    "Новомихайлівка",
    "Новоолександрівка",
    "Розумівка",
    "Річне",
    "Таврійське",
    "Тернувате"
  ],
  "MELITOPOLSKYI-DSTR": [
    "Веселе",
    "Мелітополь",
    "Приазовське",
    "Якимівка"
  ],
  "POLOHIVSKYI-DSTR": [
    "Більмак",
    "Гуляйполе",
    "Кам'Янка",
    "Оріхів",
    "Пологи",
    "Розівка",
    "Токмак"
  ],
  "BAKHCHYSARAISKYI-DSTR": [
    "Бахчисарай"
  ],
  "YEVPATORIISKYI-DSTR": [
    "Євпаторія"
  ],
  "KURMANSKYI-DSTR": [
    "Курман"
  ],
  "PEREKOPSKYI-DSTR": [
    "Яни",
    "Яни Капу"
  ],
  "SIMFEROPOLSKYI-DSTR": [
    "Сімферополь",
    "Українка"
  ],
  "FEODOSIISKYI-DSTR": [
    "Феодосія"
  ],
  "DZHANKOISKYI-DSTR": [
    "Джанкой"
  ],
  "YALTYNSKYI-DSTR": [
    "Ялта"
  ],
  "BOHODUKHIVSKYI-DSTR": [
    "Богодухів",
    "Валки",
    "Золочів"
  ],
  "IZIUMSKYI-DSTR": [
    "Ізюм",
    "Балаклія",
    "Барвінкове",
    "Борова"
  ],
  "KRASNOHRADSKYI-DSTR": [],
  "KUPIANSKYI-DSTR": [
    "Великий",
    "Великий Бурлук",
    "Колодязне",
    "Куп'Янськ",
    "Приколотне"
  ],
  "LOZIVSKYI-DSTR": [
    "Близнюки",
    "Златопіль",
    "Лозова"
  ],
  "KHARKIVSKYI-DSTR": [
    "Вільшани",
    "Дергачі",
    "Козача",
    "Козача Лопань",
    "Липці",
    "Люботин",
    "Мерефа",
    "Нова",
    "Нова Водолага",
    "Прудянка",
    "Пісочин",
    "Слатине",
    "Солоницівка",
    "Харків",
    "Циркуни"
  ],
  "CHUHUIVSKYI-DSTR": [
    "Білий",
    "Білий Колодязь",
    "Вовчанськ",
    "Есхар",
    "Зміїв",
    "Коробочкине",
    "Печеніги",
    "Слобожанське",
    "Старий",
    "Старий Салтів",
    "Чугуїв"
  ],
  "BAKHMUTSKYI-DSTR": [
    "Бахмут",
    "Світлодарськ",
    "Соледар",
    "Сіверськ",
    "Торецьк",
    "Часів",
    "Часів Яр"
  ],
  "VOLNOVASKYI-DSTR": [
    "Велика",
    "Велика Новосілка",
    "Вугледар"
  ],
  "HORLIVSKYI-DSTR": [
    "Єнакієве",
    "Горлівка",
    "Сніжне",
    "Чистякове",
    "Шахтарськ"
  ],
  "DONETSKYI-DSTR": [
    "Донецьк",
    "Макіївка",
    "Харцизьк"
  ],
  "KALMIUSKYI-DSTR": [],
  "KRAMATORSKYI-DSTR": [
    "Билбасівка",
    "Дружківка",
    "Костянтинівка",
    "Краматорськ",
    "Лиман",
    "Миколаївка",
    "Новодонецьке",
    "Рай-Олександрівка",
    "Святогірськ",
    "Слов'Янськ"
  ],
  "MARIUPOLSKYI-DSTR": [
    "Кальміуське",
    "Маріуполь"
  ],
  "POKROVSKYI-DSTR": [
    "Авдіївка",
    "Добропілля",
    "Курахове",
    "Мар'Їнка",
    "Мирноград",
    "Покровськ"
  ],
  "ALCHEVSKYI-DSTR": [
    "Алчевськ",
    "Брянка",
    "Кадіївка"
  ],
  "DOVZHANSKYI-DSTR": [
    "Довжанськ"
  ],
  "LUHANSKYI-DSTR": [
    "Луганськ"
  ],
  "SVATIVSKYI-DSTR": [],
  "SIEVIERODONETSKYI-DSTR": [],
  "STAROBILSKYI-DSTR": [
    "Старобільськ"
  ],
  "SHCHASTYNSKYI-DSTR": [
    "Новоайдар"
  ],
  "ROVENKIVSKYI-DSTR": [
    "Антрацит",
    "Ровеньки",
    "Хрустальний"
  ],
  "BOLHRADSKYI-DSTR": [
    "Арциз",
    "Болград"
  ],
  "BILOHIRSKYI-DSTR": [
    "Білогірськ"
  ],
  "KERCHENSKYI-DSTR": [
    "Керч"
  ],
  "KIYEW": [],
  "KHARKIV-CITY": [
    "Харків"
  ],
  "MARHANETS-CITY": [
    "Марганець"
  ],
  "NIKOPOL-CITY": [
    "Нікополь"
  ],
  "ZAPORIZHZHIA-CITY": [
    "Запоріжжя"
  ],
  "SEVASTOPOL-CITY": [
    "Севастополь"
  ],
  "POKROV-CITY": [
    "Покров"
  ],
  "SLAVUTICH-CITY": [
    "Славутич"
  ]
}

CITY_POINTS_BY_SLUG = {
  "ODESA-CITY": [
    30.74383,
    46.48572
  ],
  "SUMY-CITY": [
    34.79906,
    50.91741
  ],
  "BILOPILLIA-CITY": [
    34.31079,
    51.14747
  ],
  "ZATOKA-CITY": [
    30.46265,
    46.07016
  ],
  "DROHOBYCH-CITY": [
    23.51121,
    49.35196
  ],
  "SAMBIR-CITY": [
    23.20133,
    49.51624
  ],
  "ZOLOCHIV-LV-CITY": [
    24.90376,
    49.8074
  ],
  "STRYOI-CITY": [
    23.84845,
    49.26103
  ],
  "LVIV-CITY": [
    24.02324,
    49.83826
  ],
  "CHERVONOHRAD-CITY": [
    24.23935,
    50.39403
  ],
  "YAVORIV-CITY": [
    23.38355,
    49.93774
  ],
  "NOVOVOLYNSK-CITY": [
    24.15976,
    50.72949
  ],
  "KAMIN-KASHIRSKIJ-CITY": [
    24.96276,
    51.62514
  ],
  "KOVEL-CITY": [
    24.70077,
    51.21548
  ],
  "LUTSK-CITY": [
    25.35024,
    50.75784
  ],
  "TERNOPIL-CITY": [
    25.59067,
    49.55404
  ],
  "CHORTKIV-CITY": [
    25.79808,
    49.01701
  ],
  "VARASH-CITY": [
    25.85547,
    51.34038
  ],
  "DUBNO-CITY": [
    25.7624,
    50.40752
  ],
  "RIVNE-CITY": [
    26.23695,
    50.62036
  ],
  "BEREZNE-CITY": [
    26.74618,
    51.00343
  ],
  "KOREC-CITY": [
    27.15795,
    50.61921
  ],
  "SARNI-CITY": [
    26.60693,
    51.33898
  ],
  "BEREHOVE-CITY": [
    22.64453,
    48.20514
  ],
  "MUKACHEVO-CITY": [
    22.718,
    48.44248
  ],
  "RAKHIV-CITY": [
    24.20314,
    48.05472
  ],
  "TIACHIV-CITY": [
    23.57168,
    48.01092
  ],
  "UZHHOROD-CITY": [
    22.2947,
    48.6242
  ],
  "KHUST-CITY": [
    23.29791,
    48.17193
  ],
  "VERKHOVYNA-CITY": [
    24.82986,
    48.15536
  ],
  "IVANO-FRANKIVSK-CITY": [
    24.71248,
    48.92312
  ],
  "KALUSH": [
    24.37206,
    49.02398
  ],
  "KOLOMYIA-CITY": [
    25.03712,
    48.52496
  ],
  "KOSIV-CITY": [
    25.09109,
    48.32051
  ],
  "NADVIRNA-CITY": [
    24.5714,
    48.63659
  ],
  "KAMIANETS-PODILSKYOI-CITY": [
    26.58516,
    48.67882
  ],
  "TEOFIPOL-CITY": [
    26.4204,
    49.83892
  ],
  "STAROKOSTYANTINIV-CITY": [
    27.21229,
    49.75522
  ],
  "VOLOCHISK-CITY": [
    26.20681,
    49.53606
  ],
  "KHMELNYTSKYOI-CITY": [
    26.97936,
    49.41835
  ],
  "SHEPETIVKA-CITY": [
    27.06517,
    50.18118
  ],
  "SLAVUTA-CITY": [
    26.86613,
    50.29609
  ],
  "VYZHNYTSIA-CITY": [
    25.18112,
    48.24482
  ],
  "KELMENTSI-CITY": [
    26.83277,
    48.4664
  ],
  "CHERNIVTSI-CITY": [
    25.93241,
    48.29045
  ],
  "BERDYCHIV-CITY": [
    28.58236,
    49.89421
  ],
  "ZHYTOMYR-CITY": [
    28.67913,
    50.26235
  ],
  "OVRUCK-CITY": [
    28.80165,
    51.3274
  ],
  "KOROSTEN-CITY": [
    28.63859,
    50.9512
  ],
  "NOVOHRAD-VOLYNSKYOI-CITY": [
    27.60884,
    50.59141
  ],
  "UZIN-CITY": [
    30.42487,
    49.82482
  ],
  "SKVIRA-CITY": [
    29.66353,
    49.73401
  ],
  "BILA-TSERKVA-CITY": [
    30.1165,
    49.7994
  ],
  "BORYSPIL-CITY": [
    30.95263,
    50.35051
  ],
  "YAGOTIN-CITY": [
    31.76343,
    50.27535
  ],
  "PEREYASLAV-CITY": [
    31.44969,
    50.06739
  ],
  "BROVARY-CITY": [
    30.79106,
    50.51097
  ],
  "SEMIPOLKI-CITY": [
    30.93441,
    50.72627
  ],
  "ZGURIVKA-CITY": [
    31.77687,
    50.50193
  ],
  "BILOGORODKA-CITY": [
    30.22726,
    50.3898
  ],
  "BORODYANKA-CITY": [
    29.92329,
    50.64306
  ],
  "VISHNEVE-CITY": [
    30.36809,
    50.38834
  ],
  "GOSTOMEL-CITY": [
    30.2651,
    50.56841
  ],
  "IRPIN-CITY": [
    30.24037,
    50.52201
  ],
  "MAKARIV-CITY": [
    29.81455,
    50.45735
  ],
  "BUCHA-CITY": [
    30.20879,
    50.54741
  ],
  "VISHGOROD-CITY": [
    30.48566,
    50.58312
  ],
  "OBUHIV-CITY": [
    30.63329,
    50.11632
  ],
  "KAGARLIK-CITY": [
    30.82327,
    49.859
  ],
  "MIRONIVKA-CITY": [
    30.98225,
    49.66007
  ],
  "VASYLKIV-CITY": [
    30.31189,
    50.18023
  ],
  "FASTIV-CITY": [
    29.91963,
    50.07796
  ],
  "KORIUKIVKA-CITY": [
    32.24747,
    51.7746
  ],
  "BAHMACH-CITY": [
    32.83463,
    51.18144
  ],
  "NIZHYN-CITY": [
    31.88844,
    51.04772
  ],
  "NOSIVKA-CITY": [
    31.58031,
    50.93799
  ],
  "BORZNA-CITY": [
    32.4269,
    51.25343
  ],
  "SEMENIVKA-CITY": [
    32.57755,
    52.17853
  ],
  "NOVHOROD-SIVERSKYI": [
    33.2634,
    52.00684
  ],
  "PRYLUKY-CITY": [
    32.38382,
    50.59525
  ],
  "TALALAYIVKA-CITY": [
    33.14173,
    50.84287
  ],
  "ICHNYA-CITY": [
    32.39129,
    50.85908
  ],
  "GONCHARIVSKE-CITY": [
    30.91984,
    51.29892
  ],
  "DESNA-CITY": [
    30.76678,
    50.92744
  ],
  "OSTER-CITY": [
    30.87735,
    50.94966
  ],
  "CHERNIHIV-CITY": [
    31.28656,
    51.50541
  ],
  "BURIN-CITY": [
    33.83338,
    51.19936
  ],
  "NOVA-SLOBODA-CITY": [
    34.12868,
    51.37492
  ],
  "PUTIVL-CITY": [
    33.86885,
    51.33529
  ],
  "KONOTOP-CITY": [
    33.2004,
    51.23251
  ],
  "OKHTYRKA-CITY": [
    34.89468,
    50.30852
  ],
  "VELIKA-PISARIVKA-CITY": [
    35.48299,
    50.42335
  ],
  "TROSTYANEC-CITY": [
    34.96467,
    50.48046
  ],
  "NEDRIGAJLIV-CITY": [
    33.87848,
    50.83587
  ],
  "ROMNI-CITY": [
    33.4952,
    50.74025
  ],
  "SHOSTKA-CITY": [
    33.47283,
    51.86434
  ],
  "VORONIZH-CITY": [
    33.45944,
    51.77572
  ],
  "SEREDINA-BUDA-CITY": [
    34.03613,
    52.18886
  ],
  "GLUHIV-CITY": [
    33.91682,
    51.67982
  ],
  "SVESA-CITY": [
    33.93383,
    51.95131
  ],
  "SHALIGINE-CITY": [
    34.12507,
    51.56988
  ],
  "ESMAN-CITY": [
    34.06517,
    51.76966
  ],
  "PAVLIVKA-CITY": [
    34.5162883,
    51.224559
  ],
  "ATINSKE-CITY": [
    34.26888,
    51.21882
  ],
  "OBODI-CITY": [
    34.62745,
    51.22236
  ],
  "RIZHIVKA-CITY": [
    34.24895,
    51.25268
  ],
  "KATERINIVKA-CITY": [
    34.244041,
    50.734859
  ],
  "YABUDKI-CITY": [
    34.3338341,
    51.2343624
  ],
  "ISKRISKIVSHIVSHINA-CITY": [
    34.38395,
    51.23877
  ],
  "VOLFINE-CITY": [
    34.46169,
    51.24139
  ],
  "VOROZHBA-CITY": [
    34.22665,
    51.17316
  ],
  "KRASNOPILLYA-CITY": [
    35.2563391,
    50.7712539
  ],
  "MIROPILLYA-CITY": [
    35.24517,
    51.0244
  ],
  "MEZENIVKA-CITY": [
    35.3134,
    50.63486
  ],
  "UGROYIDI-CITY": [
    35.27823,
    50.86293
  ],
  "LEBEDIN-CITY": [
    34.48258,
    50.58228
  ],
  "HOTIN-CITY": [
    34.77302,
    51.07997
  ],
  "KINDRATIVKA-CITY": [
    34.77343,
    51.14326
  ],
  "YUNAKIVKA-CITY": [
    35.0385,
    51.12262
  ],
  "BASIVKA-CITY": [
    35.087929,
    51.181141
  ],
  "MIKOLAYIVKA-CITY": [
    34.3729195,
    50.9395138
  ],
  "MOGRICYA-CITY": [
    35.11312,
    51.02912
  ],
  "VINNYTSIA-CITY": [
    28.46871,
    49.2322
  ],
  "HAISYN-CITY": [
    29.37917,
    48.81294
  ],
  "ZHMERYNKA-CITY": [
    28.11405,
    49.03523
  ],
  "MOHYLIV-PODILSKYI-CITY": [
    27.79975,
    48.44278
  ],
  "TULCHYN-CITY": [
    28.86848,
    48.67397
  ],
  "HMILNIK-CITY": [
    27.95682,
    49.5581
  ],
  "ZVENIGORODKA-CITY": [
    30.96074,
    49.07765
  ],
  "VATUTINE-CITY": [
    31.04659,
    49.01198
  ],
  "ZOLOTONOSHA-CITY": [
    32.03637,
    49.66926
  ],
  "UMAN-CITY": [
    30.21944,
    48.7501
  ],
  "ZHASHKIV-CITY": [
    30.09888,
    49.2459
  ],
  "CHERKASY-CITY": [
    32.05738,
    49.44452
  ],
  "KORSUN-CITY": [
    31.25174,
    49.41822
  ],
  "KANIV-CITY": [
    31.47003,
    49.75187
  ],
  "SMILA-CITY": [
    31.88427,
    49.23295
  ],
  "KREMENCHUK-CITY": [
    33.40484,
    49.06253
  ],
  "HORISHNI-PLAVNI-CITY": [
    33.62926,
    49.00835
  ],
  "GREBINKA-CITY": [
    32.42966,
    50.12017
  ],
  "PIRYATIN-CITY": [
    32.5203,
    50.24388
  ],
  "HOROL-CITY": [
    33.27184,
    49.78286
  ],
  "LUBNY-CITY": [
    32.99975,
    50.01413
  ],
  "MIRGOROD-CITY": [
    33.60861,
    49.96464
  ],
  "POLTAVA-CITY": [
    34.55367,
    49.58925
  ],
  "KARLOVKA-CITY": [
    35.13493,
    49.45548
  ],
  "GOLOVANIVSK-CITY": [
    30.45947,
    48.3874
  ],
  "KROPYVNYTSKYOI-CITY": [
    32.26618,
    48.50834
  ],
  "NOVOUKRAYINSK-CITY": [
    31.522047,
    48.3250616
  ],
  "OLEKSANDRIIA-CITY": [
    33.11761,
    48.67466
  ],
  "SVITLOVODSK-CITY": [
    33.2458,
    49.06287
  ],
  "DNIPRO-CITY": [
    35.04066,
    48.46664
  ],
  "VERHIVCEVE-CITY": [
    34.24003,
    48.48127
  ],
  "VILNOGIRSK-CITY": [
    34.01708,
    48.48416
  ],
  "KAMIANSKE-CITY": [
    34.60617,
    48.51716
  ],
  "APOSTOLOVE-CITY": [
    33.71952,
    47.65983
  ],
  "VELIKA-KOSTROMKA-CITY": [
    33.71976,
    47.53364
  ],
  "ZELENODOLSK-CITY": [
    33.65905,
    47.55498
  ],
  "KRYVYOI-RIH-CITY": [
    33.38044,
    47.90966
  ],
  "MAR-YANSKE-CITY": [
    33.9235739,
    47.5522624
  ],
  "NIKOPOL-CITY": [
    34.39126,
    47.56826
  ],
  "MARHANETS-CITY": [
    34.6245,
    47.63088
  ],
  "POKROV-CITY": [
    34.11488,
    47.65361
  ],
  "NOVOMOSKOVSK-CITY": [
    35.2589,
    48.62893
  ],
  "PAVLOHRAD-CITY": [
    35.86878,
    48.53214
  ],
  "PERSHOTRAVNENSK-CITY": [
    36.39637,
    48.3479
  ],
  "SINELNIKOVO-CITY": [
    35.52612,
    48.32362
  ],
  "BEREZIVKA-CITY": [
    30.90943,
    47.20037
  ],
  "SERGIYIVKA-CITY": [
    30.37273,
    46.02756
  ],
  "BILHOROD-DNISTROVSKYOI-CITY": [
    30.34827,
    46.19484
  ],
  "KILIYA-CITY": [
    29.26396,
    45.44445
  ],
  "IZMAIL-CITY": [
    28.83751,
    45.35058
  ],
  "BILYAYIVKA-CITY": [
    30.2120913,
    46.4844245
  ],
  "CHORNOMORSK-CITY": [
    30.65529,
    46.29914
  ],
  "BOLHRAD-CITY": [
    28.61811,
    45.67786
  ],
  "PODILSK-CITY": [
    29.53074,
    47.74988
  ],
  "LIMANSKE-CITY": [
    29.97231,
    46.67952
  ],
  "ROZDILNA-CITY": [
    30.07091,
    46.85479
  ],
  "NOVIJ-BUG-CITY": [
    32.51214,
    47.69057
  ],
  "BASHTANKA-CITY": [
    32.43444,
    47.40528
  ],
  "VOZNESENSK-CITY": [
    31.33602,
    47.56218
  ],
  "YELANEC-CITY": [
    31.85222,
    47.69521
  ],
  "MYKOLAIV-CITY": [
    31.9939666,
    46.9758615
  ],
  "KUTSURUB-CITY": [
    31.61825,
    46.65277
  ],
  "OCHAKIV-CITY": [
    31.54505,
    46.61472
  ],
  "ARBUZINKA-CITY": [
    31.31701,
    47.90791
  ],
  "KRIVE-OZERO-CITY": [
    30.34701,
    47.94763
  ],
  "PERVOMAOISK-CITY": [
    30.8475997,
    48.045745
  ],
  "BERISLAV-CITY": [
    33.42664,
    46.83851
  ],
  "GENICHESK-CITY": [
    34.80861,
    46.16824
  ],
  "KAHOVKA-CITY": [
    33.47862,
    46.81601
  ],
  "NOVA-KAKHOVKA-CITY": [
    33.35591,
    46.75966
  ],
  "CHAPLINKA-CITY": [
    33.54087,
    46.36454
  ],
  "TAVRIJSK-CITY": [
    33.41665,
    46.75432
  ],
  "SKADOVSK-CITY": [
    32.90978,
    46.11313
  ],
  "OLESHKI-CITY": [
    32.72426,
    46.62553
  ],
  "CHORNOBAYIVKA-CITY": [
    32.54507,
    46.69641
  ],
  "OLEKSANDRIVKA-CITY": [
    32.1118946,
    46.6139617
  ],
  "BILOZERKA-CITY": [
    32.44447,
    46.62651
  ],
  "KHERSON-CITY": [
    32.61458,
    46.63695
  ],
  "BERDIANSK-CITY": [
    36.78815,
    46.75578
  ],
  "ENERHODAR-CITY": [
    34.66199,
    47.49048
  ],
  "ZAPORIZHZHIA-CITY": [
    35.11714,
    47.85167
  ],
  "MELITOPOL-CITY": [
    35.38196,
    46.84735
  ],
  "GULYAJPOLE-CITY": [
    36.2656849,
    47.6655382
  ],
  "KAM-YANKA-CITY": [
    36.65108,
    47.3624
  ],
  "ORIHIV-CITY": [
    35.78333,
    47.57613
  ],
  "TOKMAK-CITY": [
    35.70836,
    47.25554
  ],
  "POLOGI-CITY": [
    36.25463,
    47.47865
  ],
  "BAKHCHYSARAI-CITY": [
    33.85782,
    44.75525
  ],
  "BILOHIRSK-CITY": [
    34.60386,
    45.05679
  ],
  "YEVPATORIIA-CITY": [
    33.36655,
    45.20091
  ],
  "KURMAN-CITY": [
    34.30134,
    45.50271
  ],
  "YANY-KAPU-CITY": [
    33.79261,
    45.95547
  ],
  "SIMFEROPOL-CITY": [
    34.11079,
    44.95719
  ],
  "FEODOSIIA-CITY": [
    35.38153,
    45.03199
  ],
  "DZHANKOJ-CITY": [
    34.39273,
    45.7131
  ],
  "KERCH-CITY": [
    36.47542,
    45.35675
  ],
  "YALTA-CITY": [
    34.16624,
    44.50218
  ],
  "BOGODUHIV-CITY": [
    35.52367,
    50.16147
  ],
  "ZOLOCHIV-CITY": [
    35.9824347,
    50.2790531
  ],
  "BALAKLIYA-CITY": [
    36.8397826,
    49.4521336
  ],
  "IZIUM-CITY": [
    37.27679,
    49.20697
  ],
  "KRASNOGRAD-CITY": [
    35.44485,
    49.3776
  ],
  "KUP-YANSK-CITY": [
    37.61581,
    49.71003
  ],
  "PERVOMAJSKIJ-CITY": [
    36.21848,
    49.37646
  ],
  "LOZOVA-KHARKIVSKA-CITY": [
    36.31412,
    48.89066
  ],
  "DERGACHI-CITY": [
    36.1209,
    50.10789
  ],
  "KHARKIV-CITY": [
    36.25475,
    49.98177
  ],
  "MEREFA-CITY": [
    36.0567,
    49.82107
  ],
  "PISOCHINO-CITY": [
    36.10262,
    49.9516
  ],
  "CIRKUNI-CITY": [
    36.38724,
    50.08438
  ],
  "KOZACHA-LOPAN-CITY": [
    36.19823,
    50.33212
  ],
  "LIPCI-CITY": [
    36.42086,
    50.20919
  ],
  "VOVCHANSK-CITY": [
    36.94108,
    50.29078
  ],
  "KOROBOCHKINE-CITY": [
    36.81286,
    49.77626
  ],
  "BILIJ-KOLODYAZ-CITY": [
    37.11265,
    50.20412
  ],
  "CHUGUYIV-CITY": [
    36.6865,
    49.83538
  ],
  "BAKHMUT-CITY": [
    37.99886,
    48.59419
  ],
  "SVITLODARSK-CITY": [
    38.22331,
    48.43374
  ],
  "TORECK-CITY": [
    37.8478,
    48.39477
  ],
  "CHASIV-YAR-CITY": [
    37.83409,
    48.58768
  ],
  "SOLEDAR-CITY": [
    38.07098,
    48.6921
  ],
  "VELIKA-NOVOSILKA-CITY": [
    36.83627,
    47.84281
  ],
  "VUGLEDAR-CITY": [
    37.24999,
    47.77973
  ],
  "HORLIVKA-CITY": [
    38.01709,
    48.29986
  ],
  "SNIZHNE-CITY": [
    38.76205,
    48.02328
  ],
  "SHAKHTARSK-CITY": [
    38.43826,
    48.05657
  ],
  "IENAKIIEVE-CITY": [
    38.20403,
    48.23857
  ],
  "DONETSK-CITY": [
    37.80224,
    48.023
  ],
  "KHARTSYZK-CITY": [
    38.14025,
    48.04277
  ],
  "MAKIIVKA-CITY": [
    37.92576,
    48.04782
  ],
  "KALMIUSKE-CITY": [
    37.7925,
    47.242
  ],
  "LIMAN-CITY": [
    37.80843,
    48.99012
  ],
  "KRAMATORSK-CITY": [
    37.56779,
    48.73106
  ],
  "KOSTIANTYNIVKA-CITY": [
    37.6923755,
    48.5348985
  ],
  "DRUZHKIVKA-CITY": [
    37.52537,
    48.61995
  ],
  "SVYATOGIRSK-CITY": [
    37.57194,
    49.04101
  ],
  "SLOVIANSK-CITY": [
    37.59739,
    48.84974
  ],
  "MARIUPOL-CITY": [
    37.54131,
    47.09514
  ],
  "AVDIYIVKA-CITY": [
    37.75008,
    48.14019
  ],
  "DOBROPILLYA-CITY": [
    37.04866,
    48.42115
  ],
  "KURAHOVE-CITY": [
    37.28069,
    47.9847
  ],
  "MAR-YINKA-CITY": [
    37.50544,
    47.94527
  ],
  "MYRNOHRAD-CITY": [
    37.26513,
    48.3099
  ],
  "POKROVSK-CITY": [
    37.17706,
    48.28014
  ],
  "BRIANKA-CITY": [
    38.67222,
    48.511
  ],
  "KADIIVKA-CITY": [
    38.64352,
    48.56818
  ],
  "ALCHEVSK-CITY": [
    38.79744,
    48.46906
  ],
  "DOVZHANSK-CITY": [
    39.64744,
    48.07615
  ],
  "LUHANSK-CITY": [
    39.30553,
    48.56814
  ],
  "ROVENKY-CITY": [
    39.37696,
    48.08277
  ],
  "KHRUSTALNYOI-CITY": [
    38.92369,
    48.14241
  ],
  "ANTRATSYT-CITY": [
    39.08863,
    48.11638
  ],
  "RUBIZHNE-CITY": [
    38.37972,
    49.00849
  ],
  "SIEVIERODONETSK-CITY": [
    38.48754,
    48.94414
  ],
  "LYSYCHANSK-CITY": [
    38.42088,
    48.91211
  ],
  "ZOLOTE-CITY": [
    38.51512,
    48.69516
  ],
  "STAROBILSK-CITY": [
    38.9075,
    49.27881
  ],
  "NOVOAIDAR-CITY": [
    39.00376,
    48.96288
  ],
  "SEVASTOPOL-CITY": [
    33.52134,
    44.60795
  ],
  "SLAVUTICH-CITY": [
    30.71806,
    51.5225
  ],
  "POKROVSKE": [
    36.23446,
    47.98126
  ],
  "KROLEVETS-CITY": [
    33.38044,
    51.55181
  ],
  "BOIARKA-CITY": [
    30.2847595,
    50.3356709
  ],
  "BOHUSLAV-CITY": [
    30.87407,
    49.54637
  ],
  "ANTONIVKA-CITY": [
    32.73061,
    46.67666
  ],
  "NOVOPAVLIVKA-CITY": [
    34.43376,
    47.57563
  ],
  "MEZHOVA-CITY": [
    36.73178,
    48.25418
  ],
  "KOMISHUVAHA-CITY": [
    35.52405,
    47.71491
  ],
  "VILNIANSK-CITY": [
    35.44034,
    47.94768
  ],
  "BOROVA-CITY": [
    37.6253381,
    49.3799491
  ],
  "TAVRIISKE-CITY": [
    35.69733,
    47.652512
  ],
  "BILENKE-CITY": [
    35.030251,
    47.621609
  ],
  "NETISHYN-CITY": [
    26.64872,
    50.32863
  ],
  "BOBROVYTSIA-СITY": [
    31.38205,
    50.74559
  ],
  "HADIACH-CITY": [
    33.9950534,
    50.3701299
  ],
  "MENA-CITY": [
    32.21364,
    51.52205
  ],
  "OVIDIOPOL-CITY": [
    30.43746,
    46.24721
  ],
  "VYLKOVE-CITY": [
    29.5869,
    45.40279
  ],
  "TATARBUNARY-CITY": [
    29.61123,
    45.83861
  ],
  "TUZLY-CITY": [
    30.09773,
    45.86504
  ],
  "SARATA-CITY": [
    29.66444,
    46.02056
  ],
  "ARTSYZ-CITY": [
    29.43286,
    45.98526
  ],
  "SNIHURIVKA-CITY": [
    32.8197,
    47.07651
  ],
  "KOROP-CITY": [
    32.95217,
    51.56666
  ],
  "SOSNYTSIA-CITY": [
    32.49985,
    51.52387
  ],
  "SNOVSK-CITY": [
    31.94245,
    51.81674
  ],
  "KOZELETS-CITY": [
    31.11664,
    50.91211
  ],
  "BATURYN-CITY": [
    32.87981,
    51.34261
  ],
  "ANDRUSHIVKA-CITY": [
    29.01883,
    50.01922
  ],
  "KOROSTYSHIV-CITY": [
    29.05774,
    50.31686
  ],
  "CHERNIAKHIV-CITY": [
    28.66717,
    50.45412
  ],
  "RUZHYN-CITY": [
    29.21874,
    49.72175
  ],
  "MALYN-CITY": [
    29.24225,
    50.76756
  ],
  "LADYZHYN-CITY": [
    29.23636,
    48.68437
  ],
  "KOZIATYN-CITY": [
    28.8354279,
    49.7195867
  ],
  "POHREBYSHCHE-CITY": [
    29.25988,
    49.48508
  ],
  "KRASYLIV-CITY": [
    26.97211,
    49.65376
  ],
  "ADAMPIL-CITY": [
    27.65652,
    49.66791
  ],
  "POLONNE-CITY": [
    27.50856,
    50.11944
  ],
  "HNIVAN-CITY": [
    28.33785,
    49.0939
  ],
  "LOKHVYTSIA-CITY": [
    33.27153,
    50.36444
  ],
  "KOBELIAKY-CITY": [
    34.20193,
    49.14936
  ],
  "RESHETYLVKA-CITY": [
    34.07896,
    49.563
  ],
  "NOVISANZHARY-CITY": [
    34.31496,
    49.33379
  ],
  "HLOBYNE-CITY": [
    33.27555,
    49.37894
  ],
  "OSTROH-CITY": [
    26.52113,
    50.32897
  ],
  "ZDOLBUNIV-CITY": [
    26.24823,
    50.52205
  ],
  "KOSTOPIL-CITY": [
    26.44797,
    50.87732
  ],
  "ROKYTNE-CITY": [
    27.21705,
    51.27891
  ],
  "DUBROVYTSIA-CITY": [
    26.56369,
    51.57076
  ],
  "HOLOBY-CITY": [
    25.00882,
    51.08798
  ],
  "TURIISTK-CITY": [
    24.5262,
    51.08724
  ],
  "LIUBESHIV-CITY": [
    25.51317,
    51.76505
  ],
  "LOKACHI-CITY": [
    24.64872,
    50.73898
  ],
  "VOLODYMYR-CITY": [
    24.32119,
    50.85033
  ],
  "BIBRKA-CITY": [
    24.29369,
    49.63921
  ],
  "BUSK-CITY": [
    24.61227,
    49.96548
  ],
  "ZBARAZH-CITY": [
    25.77925,
    49.66157
  ],
  "BEREZHANY-CITY": [
    24.93686,
    49.44578
  ],
  "KOZOVA-CITY": [
    25.14547,
    49.43206
  ],
  "KREMENETS-CITY": [
    25.72787,
    50.09864
  ],
  "BURSHTYN-CITY": [
    24.63339,
    49.25193
  ],
  "HALYCH-CITY": [
    24.72748,
    49.12374
  ],
  "BOBRYNETS-CITY": [
    32.1655,
    48.05674
  ],
  "DOLYNSKA-CITY": [
    32.77691,
    48.11725
  ],
  "ONUFRIIVKA-CITY": [
    33.44954,
    48.89917
  ],
  "ZNAMIANKA-CITY": [
    32.6659476,
    48.7199609
  ],
  "RZHYSHCHIV-CITY": [
    31.0424,
    49.96934
  ],
  "VORZEL-CITY": [
    30.15305,
    50.5444
  ],
  "DYMER-CITY": [
    30.30357,
    50.78579
  ],
  "NOVOVORONTSOVKA-CITY": [
    33.92317,
    47.50499
  ],
  "OSOKORIVKA-CITY": [
    33.923,
    47.432
  ],
  "IRSHANSK-CITY": [
    28.72119,
    50.75317
  ],
  "HORODNIA-CITY": [
    31.59632,
    51.89129
  ],
  "LIUBAR-CITY": [
    27.75108,
    49.92322
  ],
  "OZERNE-CITY": [
    28.73384,
    50.17816
  ],
  "ILLINTSI-CITY": [
    29.20589,
    49.10544
  ],
  "LYPOVETS-CITY": [
    29.05669,
    49.22776
  ],
  "LITYN-CITY": [
    28.08698,
    49.32711
  ],
  "NEMYRIV-CITY": [
    28.83781,
    48.97002
  ],
  "ORATIV-CITY": [
    29.52889,
    49.18594
  ],
  "TYVRIV-CITY": [
    28.50044,
    49.01206
  ],
  "BERSHAD-CITY": [
    29.51463,
    48.36354
  ],
  "TEPLYK-CITY": [
    29.74482,
    48.66538
  ],
  "TROSTIANETS-CITY": [
    29.2226589,
    48.51227
  ],
  "CHECHELNYK-CITY": [
    29.36469,
    48.21558
  ],
  "BAR-CITY": [
    27.67404,
    49.07362
  ],
  "SHARHOROD-CITY": [
    28.08459,
    48.73562
  ],
  "MURAVANIKURYLIVTSI-CITY": [
    27.53084,
    48.71813
  ],
  "CHERNIVTSI-VIN-CITY": [
    28.1221153,
    48.5406973
  ],
  "YAMPIL-CITY": [
    28.28141,
    48.24056
  ],
  "KRYZHOPIL-CITY": [
    28.86766,
    48.3821
  ],
  "PISHCHANKA-CITY": [
    28.88056,
    48.21249
  ],
  "TOMASHPIL-CITY": [
    28.51295,
    48.53695
  ],
  "KALYNIVKA-CITY": [
    28.51541,
    49.46129
  ],
  "IVANYCHI-CITY": [
    24.35634,
    50.63592
  ],
  "MANEVYCHI-CITY": [
    25.53063,
    51.29385
  ],
  "LIUBOML-CITY": [
    24.03225,
    51.22536
  ],
  "RATNE-CITY": [
    24.52644,
    51.66919
  ],
  "STARA-VYZHIVKA-CITY": [
    24.43958,
    51.43661
  ],
  "SHATSK-CITY": [
    23.93589,
    51.49929
  ],
  "HOROKHIV-CITY": [
    24.75681,
    50.50224
  ],
  "KIVERTSI-CITY": [
    25.45596,
    50.83516
  ],
  "ROZHYSHCHE-CITY": [
    25.27121,
    50.91632
  ],
  "PETRYKIVKA-CITY": [
    34.61901,
    48.7264
  ],
  "SOLONE-CITY": [
    34.87585,
    48.20907
  ],
  "TSARYCHANKA-CITY": [
    34.48601,
    48.94186
  ],
  "VERKHNIODNIPROVSK-CITY": [
    34.3262,
    48.65557
  ],
  "KRYNYCHKY-CITY": [
    34.46202,
    48.37438
  ],
  "PIATYKHATKY-CITY": [
    33.7056731,
    48.4124572
  ],
  "SOFIIVKA-CITY": [
    33.8668627,
    48.0482032
  ],
  "SHYROKE-CITY": [
    33.26147,
    47.6855
  ],
  "TOMAKIVKA-CITY": [
    34.74324,
    47.81081
  ],
  "MAHDALYNIVKA-CITY": [
    34.91395,
    48.91204
  ],
  "YURIIVKA-CITY": [
    36.015,
    48.73556
  ],
  "VASYLKIVKA-CITY": [
    36.02214,
    48.20824
  ],
  "PETROPAVLIVKA-CITY": [
    36.43061,
    48.46353
  ],
  "VARVA-CITY": [
    32.72274,
    50.49858
  ],
  "SRIBNE-CITY": [
    32.91906,
    50.66314
  ],
  "KULYKIVKA-CITY": [
    31.64604,
    51.3729
  ],
  "RIPKY-CITY": [
    31.08578,
    51.80165
  ],
  "PUTYLA-CITY": [
    25.08757,
    47.99343
  ],
  "SOKYRIANY-CITY": [
    27.411193,
    48.4460307
  ],
  "KHOTYN-CITY": [
    26.48978,
    48.50555
  ],
  "HERTSA-CITY": [
    26.26186,
    48.14752
  ],
  "LYPOVA-DOLYNA-CITY": [
    33.79154,
    50.56292
  ],
  "YAMPILS-SUM-CITY": [
    33.778454,
    51.9481126
  ],
  "KHOLMY-CITY": [
    32.59733,
    51.87141
  ],
  "BRUSYLIV-CITY": [
    29.52008,
    50.28226
  ],
  "POPILNIA-CITY": [
    29.45265,
    49.9532
  ],
  "PULYNY-CITY": [
    28.27,
    50.46745
  ],
  "RADOMYSHL-CITY": [
    29.23003,
    50.4962
  ],
  "ROMANIV-CITY": [
    27.9314,
    50.14733
  ],
  "CHUDNIV-CITY": [
    28.12058,
    50.05255
  ],
  "KHOROSHIV-CITY": [
    28.44489,
    50.59484
  ],
  "LUHYNY-CITY": [
    28.39876,
    51.07899
  ],
  "NARODYCHI-CITY": [
    29.08341,
    51.20304
  ],
  "OLEVSK-CITY": [
    27.65228,
    51.22482
  ],
  "BARANIVKA-CITY": [
    27.6622,
    50.29691
  ],
  "YEMILCHYNE-CITY": [
    27.80198,
    50.87185
  ],
  "VYNOHRADIV-CITY": [
    23.03623,
    48.14126
  ],
  "VOLOVETS-CITY": [
    23.1851,
    48.7109
  ],
  "SVALIAVA-CITY": [
    22.98673,
    48.54735
  ],
  "VELYKYI-BEREZNYI-CITY": [
    22.46121,
    48.8934
  ],
  "PERECHYN-CITY": [
    22.47718,
    48.73494
  ],
  "IRSHAVA-CITY": [
    23.04065,
    48.31227
  ],
  "MIZHHIRIA-CITY": [
    23.5009289,
    48.5281184
  ],
  "PRYMORSK-CITY": [
    36.34599,
    46.73415
  ],
  "CHERNIHIVKA-CITY": [
    36.21648,
    47.19451
  ],
  "VELYKA-BILOZERKA-CITY": [
    34.68457,
    47.27572
  ],
  "KAMIANKA-DNIPROVSKA-CITY": [
    34.41026,
    47.49629
  ],
  "MYKHAILIVKA-CITY": [
    35.2217134,
    47.2657187
  ],
  "NOVOMYKHAILIVKA-CITY": [
    35.529781,
    47.838589
  ],
  "VESELE-CITY": [
    34.91843,
    47.00973
  ],
  "PRYAZOVSKE-CITY": [
    35.64082,
    46.73123
  ],
  "YAKYMIVKA-CITY": [
    35.16334,
    46.7011
  ],
  "BILMAK-CITY": [
    36.65331,
    47.35914
  ],
  "ROZIVKA-CITY": [
    37.07078,
    47.3954
  ],
  "BOHORODCHANY-CITY": [
    24.53728,
    48.80812
  ],
  "ROHATYN-CITY": [
    24.61103,
    49.41043
  ],
  "TLUMACH-CITY": [
    25.00385,
    48.86519
  ],
  "DOLYNA-CITY": [
    23.96558,
    48.97158
  ],
  "ROZHNIATIV-CITY": [
    24.15627,
    48.93975
  ],
  "HORODENKA-CITY": [
    25.5033,
    48.669
  ],
  "SNIATYN-CITY": [
    25.55994,
    48.44883
  ],
  "YAREMCHE-CITY": [
    24.55335,
    48.44886
  ],
  "CHORNOMORSKE-CITY": [
    30.9334115,
    46.5849122
  ],
  "USATOVE-CITY": [
    30.64951,
    46.52893
  ],
  "VOLODARKA-CITY": [
    29.91023,
    49.52501
  ],
  "STAVYSCHE-CITY": [
    30.19102,
    49.3915
  ],
  "TARASHCHA-CITY": [
    30.49615,
    49.55719
  ],
  "TETIIV-CITY": [
    29.66933,
    49.37019
  ],
  "BARYSHIVKA-CITY": [
    31.32005,
    50.35925
  ],
  "IVANKIV-CITY": [
    29.90205,
    50.93953
  ],
  "POLISKE-CITY": [
    29.38896,
    51.240486
  ],
  "DOBROTVIR-CITY": [
    24.3835,
    50.20526
  ],
  "CHAPLYNE-CITY": [
    36.23007,
    48.12827
  ],
  "NOVODONETSKE-CITY": [
    36.98276,
    48.63512
  ],
  "LIUBECH-CITY": [
    30.66018,
    51.70219
  ],
  "BLAHOVISHCHENSKE-CITY": [
    30.23619,
    48.32822
  ],
  "VILSHANKA-CITY": [
    30.87285,
    48.23421
  ],
  "HAIVORON-CITY": [
    29.8593204,
    48.3406905
  ],
  "NOVOARKHANHELSK-CITY": [
    30.80705,
    48.66187
  ],
  "KOMPANIIVKA-CITY": [
    32.20138,
    48.25022
  ],
  "NOVHORODKA-CITY": [
    32.65469,
    48.36089
  ],
  "OLEKSANDRIVKA-K-CITY": [
    32.23968,
    48.968
  ],
  "USTYNIVKA-CITY": [
    32.53938,
    47.95619
  ],
  "DOBROVELYCHKIVKA-CITY": [
    31.18039,
    48.38939
  ],
  "MALAVYSKA-CITY": [
    31.63231,
    48.64694
  ],
  "NOVOMYRHOROD-CITY": [
    31.64904,
    48.79345
  ],
  "PETROVE-CITY": [
    33.2653,
    48.33809
  ],
  "LANIVTSI-CITY": [
    26.09052,
    49.86103
  ],
  "SHUMSK-CITY": [
    26.11792,
    50.11775
  ],
  "ZBORIV-CITY": [
    25.14019,
    49.66493
  ],
  "PIDVOLOCHYSK-CITY": [
    26.14401,
    49.53131
  ],
  "PIDHAITSI-CITY": [
    25.1361578,
    49.2680238
  ],
  "TEREBOVLIA-CITY": [
    25.68886,
    49.29967
  ],
  "BORSHCHIV-CITY": [
    26.03171,
    48.80319
  ],
  "BUCHACH-CITY": [
    25.39496,
    49.06234
  ],
  "HUSIATYN-CITY": [
    26.20464,
    49.07123
  ],
  "ZALISHCHYKY-CITY": [
    25.7317,
    48.64098
  ],
  "MONASTYRYSKA-CITY": [
    25.17149,
    49.09063
  ],
  "SIVERSK-CITY": [
    38.09683,
    48.86476
  ],
  "VERKHNIASYROVATKA-CITY": [
    34.95861,
    50.82902
  ],
  "RAIOLEKSANDRIVKA-CITY": [
    37.8512,
    48.81041
  ],
  "PRYMORSKE-CITY": [
    35.29074,
    47.6449
  ],
  "MALOKATERYNIVKA-CITY": [
    35.25733,
    47.6557
  ],
  "KUSHUHUM-CITY": [
    35.21644,
    47.70963
  ],
  "BALABYNE-CITY": [
    35.21361,
    47.73686
  ],
  "HORODOK-CITY": [
    23.6465626,
    49.784596
  ],
  "KALYNIVKA-FASTIVSKIY-CITY": [
    30.2261781,
    50.2257254
  ],
  "KHOTIV-CITY": [
    30.46836,
    50.33069
  ],
  "CHABANY-CITY": [
    30.42856,
    50.34128
  ],
  "ZAZYMIA-CITY": [
    30.67319,
    50.56923
  ],
  "DMYTRIVKA-CITY": [
    31.740156,
    46.631561
  ],
  "MYKOLAIVKA-CITY": [
    37.76835,
    48.86193
  ],
  "STETSKIVKA-CITY": [
    34.78849,
    51.01307
  ],
  "MAIAKY-CITY": [
    30.2750575,
    46.416632
  ],
  "DOBROSLAV-CITY": [
    30.94518,
    46.82095
  ],
  "KOLODIAZNE-CITY": [
    37.688599,
    50.007702
  ],
  "SUKHANOVE-CITY": [
    33.53626,
    47.12841
  ],
  "HATNE-CITY": [
    30.37497,
    50.35444
  ],
  "DACHNE-CITY": [
    30.54747,
    46.58226
  ],
  "BOLHARKA-CITY": [
    30.46148,
    46.6912
  ],
  "DALNYK-CITY": [
    30.52982,
    46.22569
  ],
  "VELYKACHERNECHCHYNA-CITY": [
    34.92359,
    50.95458
  ],
  "DNIPROVSKE-CITY": [
    31.8741042,
    46.6358818
  ],
  "BYLBASIVKA-CITY": [
    37.50185,
    48.83929
  ],
  "LIUBASHIVKA-CITY": [
    30.25209,
    47.83387
  ],
  "NOVOMYKOLAIVKA-CITY": [
    35.89886,
    47.97146
  ],
  "VILSHANY-CITY": [
    35.88233,
    50.0544
  ],
  "UROZHAINE-CITY": [
    33.381176,
    46.968994
  ],
  "BEREZNEHUVATE-CITY": [
    32.85098,
    47.30872
  ],
  "LYMANKA-CITY": [
    30.67736,
    46.38564
  ],
  "BARABOI-CITY": [
    30.51368,
    46.28769
  ],
  "SANZHEIKA-CITY": [
    30.60897,
    46.22882
  ],
  "HRYBIVKA-CITY": [
    30.5606,
    46.20933
  ],
  "ROKSOLANY-CITY": [
    30.4568,
    46.17608
  ],
  "SHABO-CITY": [
    30.38567,
    46.12657
  ],
  "KAROLINOBUHAZ-CITY": [
    30.53068,
    46.14439
  ],
  "OLEKSANDRIVKA-OD-CITY": [
    30.6312513,
    46.3279486
  ],
  "MOLODIZHNE-CITY": [
    30.6094472,
    46.3314744
  ],
  "VELYKODOLYNSKE-CITY": [
    30.57902,
    46.34642
  ],
  "VELYKYIDALNYK-CITY": [
    30.56285,
    46.47212
  ],
  "VELYKYIBURLUK-CITY": [
    37.38358,
    50.06135
  ],
  "LIUBOTYN-CITY": [
    35.92907,
    49.94691
  ],
  "SLOBOZHANSKE-CITY": [
    36.52172,
    49.59054
  ],
  "ZMIIV-CITY": [
    36.36207,
    49.69689
  ],
  "NOVAVODOLAHA-CITY": [
    35.8601,
    49.71875
  ],
  "BARVINKOVE-CITY": [
    37.02257,
    48.9052
  ],
  "VALKY-CITY": [
    35.61393,
    49.83701
  ],
  "ZINKIV-CITY": [
    34.35952,
    50.20987
  ],
  "ZAVODSKE-CITY": [
    33.40118,
    50.40065
  ],
  "SOLONYTSIVKA-CITY": [
    36.03464,
    49.99682
  ],
  "KOTELVA-CITY": [
    34.74697,
    50.06849
  ],
  "MASHIVKA-CITY": [
    34.87157,
    49.44407
  ],
  "CHUTOVE-CITY": [
    35.15747,
    49.71414
  ],
  "SKOROKHODOVE-CITY": [
    35.07407,
    49.77437
  ],
  "ROMODAN-CITY": [
    33.32626,
    49.99135
  ],
  "HRADYZK-CITY": [
    33.13941,
    49.23943
  ],
  "KOMYSHNIA-CITY": [
    33.6831,
    50.18643
  ],
  "NALYVAIKIVKA-CITY": [
    29.72067,
    50.48491
  ],
  "KHODORIV-CITY": [
    24.31294,
    49.40738
  ],
  "CHYHYRYN-CITY": [
    32.66082,
    49.08045
  ],
  "ZHOVTIVODY-CITY": [
    33.49743,
    48.34518
  ],
  "BLYZNIUKY-CITY": [
    36.55368,
    48.85632
  ],
  "UKRAINKA-CITY": [
    30.74349,
    50.15309
  ],
  "ORZHYTSIA-CITY": [
    32.39398,
    50.10826
  ],
  "SOLONCHAKY-CITY": [
    31.81824,
    46.64388
  ],
  "ESKHAR-CITY": [
    36.59025,
    49.79736
  ],
  "TERNUVATE-CITY": [
    36.12973,
    47.82995
  ],
  "VYHODA-CITY": [
    30.40325,
    46.61662
  ],
  "YEHORIVKA-CITY": [
    30.4029,
    46.72059
  ],
  "HAVRYLIVKA-CITY": [
    30.206909,
    50.674782
  ],
  "PECHENIHY-CITY": [
    36.9386,
    49.86931
  ],
  "ARKHANHELSKE-CITY": [
    33.40506,
    47.43329
  ],
  "FONTANKA-CITY": [
    30.85916,
    46.56864
  ],
  "KOBLEVE-CITY": [
    31.20804,
    46.66499
  ],
  "ROZUMIVKA-CITY": [
    35.13938,
    47.75392
  ],
  "PROSIANA-CITY": [
    36.37175,
    48.11368
  ],
  "VELYKAOLEKSANDRIVKA-CITY": [
    33.29059,
    47.31888
  ],
  "STARYISALTIV-CITY": [
    36.78508,
    50.07155
  ],
  "BOZHEDARIVKA-CITY": [
    34.11207,
    48.35687
  ],
  "NOVOOLEKSANDRIVKA-CITY": [
    35.36739,
    47.751041
  ],
  "STEPNOHIRSK-CITY": [
    35.36399,
    47.59015
  ],
  "RICHNE-CITY": [
    35.31986,
    47.67406
  ],
  "SLATYNE-CITY": [
    36.15376,
    50.21041
  ],
  "PRUDIANKA-CITY": [
    36.16835,
    50.23606
  ],
  "ZNOB-NOVGORODSKE-CITY": [
    33.6016,
    52.26291
  ],
  "YUZHNE-CITY": [
    31.10182,
    46.62472
  ],
  "YUZHNOUKRAYINSK-CITY": [
    31.17513,
    47.82879
  ],
  "CHYSTIAKOVE-CITY": [
    38.59685,
    48.03876
  ],
  "MIHOVE-CITY": [
    25.37574,
    48.15612
  ],
  "CHABANKA-CITY": [
    30.706,
    46.575
  ],
  "KIYEW": [
    30.5234,
    50.4501
  ],
  "ODESKA": [
    30.74383,
    46.48572
  ],
  "KIYEWSKAYA": [
    30.5234,
    50.4501
  ],
  "SUMSKA": [
    34.79906,
    50.91741
  ],
  "LVIVKA": [
    24.02324,
    49.83826
  ],
  "VOLYNSKA": [
    25.35024,
    50.75784
  ],
  "TERNOPILSKA": [
    25.59067,
    49.55404
  ],
  "RIVENSKA": [
    26.23695,
    50.62036
  ],
  "ZAKARPATSKA": [
    22.2947,
    48.6242
  ],
  "IVANOFRANKIWSKA": [
    24.71248,
    48.92312
  ],
  "HMELNYCKA": [
    26.97936,
    49.41835
  ],
  "CHERNIVETSKA": [
    25.93241,
    48.29045
  ],
  "ZHYTOMYRSKA": [
    28.67913,
    50.26235
  ],
  "CHERNIGIWSKA": [
    31.28656,
    51.50541
  ],
  "VINNYTSA": [
    28.46871,
    49.2322
  ],
  "POLTASKA": [
    34.55367,
    49.58925
  ],
  "KIROWOGRADSKA": [
    32.26618,
    48.50834
  ],
  "DNIPROPETROVSKAYA": [
    35.04066,
    48.46664
  ],
  "MYKOLAYIV": [
    24.97731,
    50.34135
  ],
  "HERSONSKA": [
    32.61458,
    46.63695
  ],
  "KRIMEA": [
    34.11079,
    44.95719
  ],
  "HARKIVSKA": [
    36.25475,
    49.98177
  ],
  "DONETSKAYA": [
    37.80224,
    48.023
  ],
  "LUGANSKA": [
    39.30553,
    48.56814
  ],
  "CHERKASKA": [
    32.05738,
    49.44452
  ],
  "ZAPORIZKA": [
    35.11714,
    47.85167
  ],
  "CHERVONOHRYHORIVKA-CITY": [
    34.52453,
    47.62161
  ],
  "VELYKADYMERKA-CITY": [
    30.9016229,
    50.5913563
  ],
  "ROKYTNE-KYIV-CITY": [
    30.473034,
    49.6867282
  ],
  "BEREZANKA-CITY": [
    31.3874915,
    46.8544054
  ],
  "RYBAKIVKA-CITY": [
    31.3511191,
    46.6195586
  ],
  "BILIARI-CITY": [
    31.031178,
    46.6227
  ],
  "TERNY-CITY": [
    33.98346,
    50.99407
  ],
  "RICHKY-CITY": [
    34.4951996,
    51.1202488
  ],
  "STEPANIVKA-CITY": [
    34.6422099,
    50.9417042
  ],
  "TOKARI-CITY": [
    34.902016,
    50.920043
  ],
  "PRYKOLOTNE-CITY": [
    37.3498729,
    50.160627
  ],
  "ZELENIVKA-CITY": [
    32.6496911,
    46.7175203
  ],
  "MUZYKIVKA-CITY": [
    32.5640748,
    46.7536821
  ],
  "BOBROVYTSIA-CITY": [
    31.3860852,
    50.7415033
  ],
  "BOROZNA-CITY": [
    32.4263156,
    51.2534475
  ]
}

CITY_POINTS_BY_NAME = {
  "одеса": [
    30.74383,
    46.48572
  ],
  "odesa": [
    30.74383,
    46.48572
  ],
  "суми": [
    34.79906,
    50.91741
  ],
  "sumy": [
    34.79906,
    50.91741
  ],
  "білопілля": [
    34.31079,
    51.14747
  ],
  "bilopillia": [
    34.31079,
    51.14747
  ],
  "затока": [
    30.46265,
    46.07016
  ],
  "zatoka": [
    30.46265,
    46.07016
  ],
  "дрогобич": [
    23.51121,
    49.35196
  ],
  "drogobych": [
    23.51121,
    49.35196
  ],
  "самбір": [
    23.20133,
    49.51624
  ],
  "sambir": [
    23.20133,
    49.51624
  ],
  "zolochiv": [
    24.90376,
    49.8074
  ],
  "стрий": [
    23.84845,
    49.26103
  ],
  "striy": [
    23.84845,
    49.26103
  ],
  "львів": [
    24.02324,
    49.83826
  ],
  "lviv": [
    24.02324,
    49.83826
  ],
  "шептицький": [
    24.23935,
    50.39403
  ],
  "sheptytskyi": [
    24.23935,
    50.39403
  ],
  "яворів": [
    23.38355,
    49.93774
  ],
  "yavoriv": [
    23.38355,
    49.93774
  ],
  "нововолинськ": [
    24.15976,
    50.72949
  ],
  "novovolinsk": [
    24.15976,
    50.72949
  ],
  "камінь-каширський": [
    24.96276,
    51.62514
  ],
  "kamin-kashirskiy": [
    24.96276,
    51.62514
  ],
  "ковель": [
    24.70077,
    51.21548
  ],
  "kovel": [
    24.70077,
    51.21548
  ],
  "луцьк": [
    25.35024,
    50.75784
  ],
  "lutsk": [
    25.35024,
    50.75784
  ],
  "тернопіль": [
    25.59067,
    49.55404
  ],
  "ternopil": [
    25.59067,
    49.55404
  ],
  "чортків": [
    25.79808,
    49.01701
  ],
  "chortkiv": [
    25.79808,
    49.01701
  ],
  "вараш": [
    25.85547,
    51.34038
  ],
  "varash": [
    25.85547,
    51.34038
  ],
  "дубно": [
    25.7624,
    50.40752
  ],
  "dubno": [
    25.7624,
    50.40752
  ],
  "рівне": [
    26.23695,
    50.62036
  ],
  "rivne": [
    26.23695,
    50.62036
  ],
  "березне": [
    26.74618,
    51.00343
  ],
  "berezne": [
    26.74618,
    51.00343
  ],
  "корець": [
    27.15795,
    50.61921
  ],
  "korets": [
    27.15795,
    50.61921
  ],
  "сарни": [
    26.60693,
    51.33898
  ],
  "sarny": [
    26.60693,
    51.33898
  ],
  "берегове": [
    22.64453,
    48.20514
  ],
  "beregove": [
    22.64453,
    48.20514
  ],
  "мукачево": [
    22.718,
    48.44248
  ],
  "mukachevo": [
    22.718,
    48.44248
  ],
  "рахів": [
    24.20314,
    48.05472
  ],
  "rahiv": [
    24.20314,
    48.05472
  ],
  "тячів": [
    23.57168,
    48.01092
  ],
  "tyachiv": [
    23.57168,
    48.01092
  ],
  "ужгород": [
    22.2947,
    48.6242
  ],
  "uzhhorod": [
    22.2947,
    48.6242
  ],
  "хуст": [
    23.29791,
    48.17193
  ],
  "hust": [
    23.29791,
    48.17193
  ],
  "верховина": [
    24.82986,
    48.15536
  ],
  "verkhovyna": [
    24.82986,
    48.15536
  ],
  "івано-франківськ": [
    24.71248,
    48.92312
  ],
  "ivano-frankivsk": [
    24.71248,
    48.92312
  ],
  "калуш": [
    24.37206,
    49.02398
  ],
  "kalush": [
    24.37206,
    49.02398
  ],
  "коломия": [
    25.03712,
    48.52496
  ],
  "kolomyya": [
    25.03712,
    48.52496
  ],
  "косів": [
    25.09109,
    48.32051
  ],
  "kosiv": [
    25.09109,
    48.32051
  ],
  "надвірна": [
    24.5714,
    48.63659
  ],
  "nadvirna": [
    24.5714,
    48.63659
  ],
  "кам'янець-подільський": [
    26.58516,
    48.67882
  ],
  "kamianets-podilskyi": [
    26.58516,
    48.67882
  ],
  "теофіполь": [
    26.4204,
    49.83892
  ],
  "teofipol": [
    26.4204,
    49.83892
  ],
  "старокостянтинів": [
    27.21229,
    49.75522
  ],
  "starokostiantyniv": [
    27.21229,
    49.75522
  ],
  "волочиськ": [
    26.20681,
    49.53606
  ],
  "volochisk": [
    26.20681,
    49.53606
  ],
  "хмельницький": [
    26.97936,
    49.41835
  ],
  "khmelnytskyi": [
    26.97936,
    49.41835
  ],
  "шепетівка": [
    27.06517,
    50.18118
  ],
  "shepetivka": [
    27.06517,
    50.18118
  ],
  "славута": [
    26.86613,
    50.29609
  ],
  "slavuta": [
    26.86613,
    50.29609
  ],
  "вижниця": [
    25.18112,
    48.24482
  ],
  "vyzhnytsya": [
    25.18112,
    48.24482
  ],
  "кельменці": [
    26.83277,
    48.4664
  ],
  "kelmenci": [
    26.83277,
    48.4664
  ],
  "chernivtsi": [
    25.93241,
    48.29045
  ],
  "бердичів": [
    28.58236,
    49.89421
  ],
  "berdichiv": [
    28.58236,
    49.89421
  ],
  "житомир": [
    28.67913,
    50.26235
  ],
  "zhytomyr": [
    28.67913,
    50.26235
  ],
  "овруч": [
    28.80165,
    51.3274
  ],
  "ovruch": [
    28.80165,
    51.3274
  ],
  "коростень": [
    28.63859,
    50.9512
  ],
  "korosten": [
    28.63859,
    50.9512
  ],
  "звягель": [
    27.60884,
    50.59141
  ],
  "zvyagel": [
    27.60884,
    50.59141
  ],
  "узин": [
    30.42487,
    49.82482
  ],
  "uzin": [
    30.42487,
    49.82482
  ],
  "сквира": [
    29.66353,
    49.73401
  ],
  "skvira": [
    29.66353,
    49.73401
  ],
  "біла церква": [
    30.1165,
    49.7994
  ],
  "bila tserkva": [
    30.1165,
    49.7994
  ],
  "бориспіль": [
    30.95263,
    50.35051
  ],
  "boryspil": [
    30.95263,
    50.35051
  ],
  "яготин": [
    31.76343,
    50.27535
  ],
  "yagotin": [
    31.76343,
    50.27535
  ],
  "переяслав": [
    31.44969,
    50.06739
  ],
  "pereyaslav": [
    31.44969,
    50.06739
  ],
  "бровари": [
    30.79106,
    50.51097
  ],
  "brovary": [
    30.79106,
    50.51097
  ],
  "семиполки": [
    30.93441,
    50.72627
  ],
  "semipolki": [
    30.93441,
    50.72627
  ],
  "згурівка": [
    31.77687,
    50.50193
  ],
  "zgurivka": [
    31.77687,
    50.50193
  ],
  "білогородка": [
    30.22726,
    50.3898
  ],
  "bilogorodka": [
    30.22726,
    50.3898
  ],
  "бородянка": [
    29.92329,
    50.64306
  ],
  "borodyanka": [
    29.92329,
    50.64306
  ],
  "вишневе": [
    30.36809,
    50.38834
  ],
  "vishneve": [
    30.36809,
    50.38834
  ],
  "гостомель": [
    30.2651,
    50.56841
  ],
  "gostomel": [
    30.2651,
    50.56841
  ],
  "ірпінь": [
    30.24037,
    50.52201
  ],
  "irpin": [
    30.24037,
    50.52201
  ],
  "макарів": [
    29.81455,
    50.45735
  ],
  "makariv": [
    29.81455,
    50.45735
  ],
  "буча": [
    30.20879,
    50.54741
  ],
  "bucha": [
    30.20879,
    50.54741
  ],
  "вишгород": [
    30.48566,
    50.58312
  ],
  "vishgorod": [
    30.48566,
    50.58312
  ],
  "обухів": [
    30.63329,
    50.11632
  ],
  "obuhiv": [
    30.63329,
    50.11632
  ],
  "кагарлик": [
    30.82327,
    49.859
  ],
  "kagarlik": [
    30.82327,
    49.859
  ],
  "миронівка": [
    30.98225,
    49.66007
  ],
  "mironivka": [
    30.98225,
    49.66007
  ],
  "васильків": [
    30.31189,
    50.18023
  ],
  "vasilkiv": [
    30.31189,
    50.18023
  ],
  "фастів": [
    29.91963,
    50.07796
  ],
  "fastiv": [
    29.91963,
    50.07796
  ],
  "корюківка": [
    32.24747,
    51.7746
  ],
  "koryukivka": [
    32.24747,
    51.7746
  ],
  "бахмач": [
    32.83463,
    51.18144
  ],
  "bahmach": [
    32.83463,
    51.18144
  ],
  "ніжин": [
    31.88844,
    51.04772
  ],
  "nizhyn": [
    31.88844,
    51.04772
  ],
  "носівка": [
    31.58031,
    50.93799
  ],
  "nosivka": [
    31.58031,
    50.93799
  ],
  "борзна": [
    32.4269,
    51.25343
  ],
  "borzna": [
    32.4269,
    51.25343
  ],
  "семенівка": [
    32.57755,
    52.17853
  ],
  "semenivka": [
    33.17943,
    49.59655
  ],
  "новгород-сіверський": [
    33.2634,
    52.00684
  ],
  "novhorod-siverskyi": [
    33.2634,
    52.00684
  ],
  "прилуки": [
    32.38382,
    50.59525
  ],
  "pryluky": [
    32.38382,
    50.59525
  ],
  "талалаївка": [
    33.14173,
    50.84287
  ],
  "talalayivka": [
    33.14173,
    50.84287
  ],
  "ічня": [
    32.39129,
    50.85908
  ],
  "ichnya": [
    32.39129,
    50.85908
  ],
  "гончарівське": [
    30.91984,
    51.29892
  ],
  "goncharivske": [
    30.91984,
    51.29892
  ],
  "десна": [
    30.76678,
    50.92744
  ],
  "desna": [
    30.76678,
    50.92744
  ],
  "остер": [
    30.87735,
    50.94966
  ],
  "oster": [
    30.87735,
    50.94966
  ],
  "чернігів": [
    31.28656,
    51.50541
  ],
  "chernihiv": [
    31.28656,
    51.50541
  ],
  "буринь": [
    33.83338,
    51.19936
  ],
  "burin": [
    33.83338,
    51.19936
  ],
  "нова слобода": [
    34.12868,
    51.37492
  ],
  "nova sloboda": [
    34.12868,
    51.37492
  ],
  "путивль": [
    33.86885,
    51.33529
  ],
  "putivl": [
    33.86885,
    51.33529
  ],
  "конотоп": [
    33.2004,
    51.23251
  ],
  "konotop": [
    33.2004,
    51.23251
  ],
  "охтирка": [
    34.89468,
    50.30852
  ],
  "okhtyrka": [
    34.89468,
    50.30852
  ],
  "велика писарівка": [
    35.48299,
    50.42335
  ],
  "velyka pysarivka": [
    35.48299,
    50.42335
  ],
  "trostianets": [
    24.26033,
    48.16779
  ],
  "недригайлів": [
    33.87848,
    50.83587
  ],
  "nedryhailiv": [
    33.87848,
    50.83587
  ],
  "ромни": [
    33.4952,
    50.74025
  ],
  "romny": [
    33.4952,
    50.74025
  ],
  "шостка": [
    33.47283,
    51.86434
  ],
  "shostka": [
    33.47283,
    51.86434
  ],
  "вороніж": [
    33.45944,
    51.77572
  ],
  "voronizh": [
    33.45944,
    51.77572
  ],
  "середина-буда": [
    34.03613,
    52.18886
  ],
  "seredyna-buda": [
    34.03613,
    52.18886
  ],
  "глухів": [
    33.91682,
    51.67982
  ],
  "hlukhiv": [
    33.91682,
    51.67982
  ],
  "свеса": [
    33.93383,
    51.95131
  ],
  "svesa": [
    33.93383,
    51.95131
  ],
  "шалигине": [
    34.12507,
    51.56988
  ],
  "shalyhyne": [
    34.12507,
    51.56988
  ],
  "есмань": [
    34.06517,
    51.76966
  ],
  "esman": [
    34.06517,
    51.76966
  ],
  "павлівка": [
    34.5162883,
    51.224559
  ],
  "pavlivka": [
    28.4645,
    49.44291
  ],
  "атинське": [
    34.26888,
    51.21882
  ],
  "atyns'ke": [
    34.26888,
    51.21882
  ],
  "ободи": [
    34.62745,
    51.22236
  ],
  "obody": [
    34.62745,
    51.22236
  ],
  "рижівка": [
    34.24895,
    51.25268
  ],
  "rizhivka": [
    34.24895,
    51.25268
  ],
  "катеринівка": [
    34.244041,
    50.734859
  ],
  "katerynivka": [
    39.18277,
    48.55586
  ],
  "будки": [
    34.3338341,
    51.2343624
  ],
  "budky": [
    25.73965,
    51.2245
  ],
  "іскрисківщина": [
    34.38395,
    51.23877
  ],
  "iskryskivshchyna": [
    34.38395,
    51.23877
  ],
  "волфине": [
    34.46169,
    51.24139
  ],
  "volfyne": [
    34.46169,
    51.24139
  ],
  "ворожба": [
    34.22665,
    51.17316
  ],
  "vorozhba": [
    34.22665,
    51.17316
  ],
  "краснопілля": [
    35.2563391,
    50.7712539
  ],
  "krasnopillia": [
    38.11237,
    47.53927
  ],
  "миропілля": [
    35.24517,
    51.0244
  ],
  "myropillya": [
    35.24517,
    51.0244
  ],
  "мезенівка": [
    35.3134,
    50.63486
  ],
  "mezenivka": [
    35.3134,
    50.63486
  ],
  "угроїди": [
    35.27823,
    50.86293
  ],
  "uhroidy": [
    35.27823,
    50.86293
  ],
  "лебедин": [
    34.48258,
    50.58228
  ],
  "lebedyn": [
    34.48258,
    50.58228
  ],
  "хотінь": [
    34.77302,
    51.07997
  ],
  "khotin": [
    34.77302,
    51.07997
  ],
  "кіндратівка": [
    34.77343,
    51.14326
  ],
  "kindrativka": [
    34.77343,
    51.14326
  ],
  "юнаківка": [
    35.0385,
    51.12262
  ],
  "yunakivka": [
    35.0385,
    51.12262
  ],
  "басівка": [
    35.087929,
    51.181141
  ],
  "basivka": [
    23.91667,
    49.78333
  ],
  "mykolaiivka": [
    37.76835,
    48.86193
  ],
  "могриця": [
    35.11312,
    51.02912
  ],
  "mohrytsya": [
    35.11312,
    51.02912
  ],
  "вінниця": [
    28.46871,
    49.2322
  ],
  "vinnytsia": [
    28.46871,
    49.2322
  ],
  "гайсин": [
    29.37917,
    48.81294
  ],
  "gaysin": [
    29.37917,
    48.81294
  ],
  "жмеринка": [
    28.11405,
    49.03523
  ],
  "zhmerynka": [
    28.11405,
    49.03523
  ],
  "могилів-подільський": [
    27.79975,
    48.44278
  ],
  "mohyliv-podil's'kyi": [
    27.79975,
    48.44278
  ],
  "тульчин": [
    28.86848,
    48.67397
  ],
  "tulchin": [
    28.86848,
    48.67397
  ],
  "хмільник": [
    27.95682,
    49.5581
  ],
  "khmilnyk": [
    27.95682,
    49.5581
  ],
  "звенигородка": [
    30.96074,
    49.07765
  ],
  "zvenyhorodka": [
    30.96074,
    49.07765
  ],
  "багачеве": [
    31.04659,
    49.01198
  ],
  "bagacheve": [
    31.04659,
    49.01198
  ],
  "золотоноша": [
    32.03637,
    49.66926
  ],
  "zolotonosha": [
    32.03637,
    49.66926
  ],
  "умань": [
    30.21944,
    48.7501
  ],
  "uman": [
    30.21944,
    48.7501
  ],
  "жашків": [
    30.09888,
    49.2459
  ],
  "zhashkiv": [
    30.09888,
    49.2459
  ],
  "черкаси": [
    32.05738,
    49.44452
  ],
  "cherkasy": [
    32.05738,
    49.44452
  ],
  "корсунь-шевченківський": [
    31.25174,
    49.41822
  ],
  "korsun-shevchenkivskiy": [
    31.25174,
    49.41822
  ],
  "канів": [
    31.47003,
    49.75187
  ],
  "kaniv": [
    31.47003,
    49.75187
  ],
  "сміла": [
    31.88427,
    49.23295
  ],
  "smila": [
    31.88427,
    49.23295
  ],
  "кременчук": [
    33.40484,
    49.06253
  ],
  "kremenchuk": [
    33.40484,
    49.06253
  ],
  "горішні плавні": [
    33.62926,
    49.00835
  ],
  "horishni plavni": [
    33.62926,
    49.00835
  ],
  "гребінка": [
    32.42966,
    50.12017
  ],
  "grebinka": [
    32.42966,
    50.12017
  ],
  "пирятин": [
    32.5203,
    50.24388
  ],
  "pyryatyn": [
    32.5203,
    50.24388
  ],
  "хорол": [
    33.27184,
    49.78286
  ],
  "horol": [
    33.27184,
    49.78286
  ],
  "лубни": [
    32.99975,
    50.01413
  ],
  "lubny": [
    32.99975,
    50.01413
  ],
  "миргород": [
    33.60861,
    49.96464
  ],
  "mirgorod": [
    33.60861,
    49.96464
  ],
  "полтава": [
    34.55367,
    49.58925
  ],
  "poltava": [
    34.55367,
    49.58925
  ],
  "карлівка": [
    35.13493,
    49.45548
  ],
  "karlivka": [
    35.13493,
    49.45548
  ],
  "голованівськ": [
    30.45947,
    48.3874
  ],
  "golovanivsk": [
    30.45947,
    48.3874
  ],
  "кропивницький": [
    32.26618,
    48.50834
  ],
  "kropivnitskiy": [
    32.26618,
    48.50834
  ],
  "новоукраїнка": [
    31.522047,
    48.3250616
  ],
  "novoukrainka": [
    30.29026,
    46.81513
  ],
  "олександрія": [
    33.11761,
    48.67466
  ],
  "oleksandriia": [
    33.11761,
    48.67466
  ],
  "світловодськ": [
    33.2458,
    49.06287
  ],
  "svitlovodsk": [
    33.2458,
    49.06287
  ],
  "дніпро": [
    35.04066,
    48.46664
  ],
  "dnipro": [
    35.04066,
    48.46664
  ],
  "верхівцеве": [
    34.24003,
    48.48127
  ],
  "verhivceve": [
    34.24003,
    48.48127
  ],
  "вільногірськ": [
    34.01708,
    48.48416
  ],
  "vilnogirsk": [
    34.01708,
    48.48416
  ],
  "кам'янське": [
    34.60617,
    48.51716
  ],
  "kam'yanske": [
    34.60617,
    48.51716
  ],
  "апостолове": [
    33.71952,
    47.65983
  ],
  "apostolove": [
    33.71952,
    47.65983
  ],
  "велика долина": [
    33.71976,
    47.53364
  ],
  "velika dolina": [
    33.71976,
    47.53364
  ],
  "зеленодольськ": [
    33.65905,
    47.55498
  ],
  "zelenodolsk": [
    33.65905,
    47.55498
  ],
  "кривий ріг": [
    33.38044,
    47.90966
  ],
  "kriviy rih": [
    33.38044,
    47.90966
  ],
  "мар'янське": [
    33.9235739,
    47.5522624
  ],
  "mar'yanske": [
    33.70943,
    49.90864
  ],
  "нікополь": [
    34.39126,
    47.56826
  ],
  "nikopol": [
    34.39126,
    47.56826
  ],
  "марганець": [
    34.6245,
    47.63088
  ],
  "marganec": [
    34.6245,
    47.63088
  ],
  "покров": [
    34.11488,
    47.65361
  ],
  "pokrov": [
    34.11488,
    47.65361
  ],
  "самар": [
    35.2589,
    48.62893
  ],
  "samar": [
    35.2589,
    48.62893
  ],
  "павлоград": [
    35.86878,
    48.53214
  ],
  "pavlograd": [
    35.86878,
    48.53214
  ],
  "шахтарське": [
    36.39637,
    48.3479
  ],
  "shahtarske": [
    36.39637,
    48.3479
  ],
  "синельникове": [
    35.52612,
    48.32362
  ],
  "synel'nykove": [
    35.52612,
    48.32362
  ],
  "березівка": [
    30.90943,
    47.20037
  ],
  "berezivka": [
    30.90943,
    47.20037
  ],
  "сергіївка": [
    30.37273,
    46.02756
  ],
  "serhiivka": [
    33.75423,
    50.40154
  ],
  "білгород-дністровський": [
    30.34827,
    46.19484
  ],
  "bilhorod-dnistrovskyi": [
    30.34827,
    46.19484
  ],
  "кілія": [
    29.26396,
    45.44445
  ],
  "kiliya": [
    29.26396,
    45.44445
  ],
  "ізмаїл": [
    28.83751,
    45.35058
  ],
  "izmail": [
    28.83751,
    45.35058
  ],
  "біляївка": [
    30.2120913,
    46.4844245
  ],
  "bilyaivka": [
    35.44131,
    47.97614
  ],
  "чорноморськ": [
    30.65529,
    46.29914
  ],
  "chornomorsk": [
    30.65529,
    46.29914
  ],
  "болград": [
    28.61811,
    45.67786
  ],
  "bolgrad": [
    28.61811,
    45.67786
  ],
  "подільськ": [
    29.53074,
    47.74988
  ],
  "podilsk": [
    29.53074,
    47.74988
  ],
  "лиманське": [
    29.97231,
    46.67952
  ],
  "limanske": [
    29.97231,
    46.67952
  ],
  "роздільна": [
    30.07091,
    46.85479
  ],
  "rozdilna": [
    30.07091,
    46.85479
  ],
  "новий буг": [
    32.51214,
    47.69057
  ],
  "noviy buh": [
    32.51214,
    47.69057
  ],
  "баштанка": [
    32.43444,
    47.40528
  ],
  "bashtanka": [
    32.43444,
    47.40528
  ],
  "вознесенськ": [
    31.33602,
    47.56218
  ],
  "voznesensk": [
    31.33602,
    47.56218
  ],
  "єланець": [
    31.85222,
    47.69521
  ],
  "ielanec": [
    31.85222,
    47.69521
  ],
  "миколаїв": [
    31.9939666,
    46.9758615
  ],
  "mykolaiv": [
    24.97731,
    50.34135
  ],
  "куцуруб": [
    31.61825,
    46.65277
  ],
  "kucurub": [
    31.61825,
    46.65277
  ],
  "очаків": [
    31.54505,
    46.61472
  ],
  "ochakiv": [
    31.54505,
    46.61472
  ],
  "арбузинка": [
    31.31701,
    47.90791
  ],
  "arbuzinka": [
    31.31701,
    47.90791
  ],
  "криве озеро": [
    30.34701,
    47.94763
  ],
  "kryve ozero": [
    30.34701,
    47.94763
  ],
  "первомайськ": [
    30.8475997,
    48.045745
  ],
  "pervomaysk": [
    37.65408,
    47.11121
  ],
  "берислав": [
    33.42664,
    46.83851
  ],
  "beryslav": [
    33.42664,
    46.83851
  ],
  "генічеськ": [
    34.80861,
    46.16824
  ],
  "henichesk": [
    34.80861,
    46.16824
  ],
  "каховка": [
    33.47862,
    46.81601
  ],
  "kakhovka": [
    33.47862,
    46.81601
  ],
  "нова каховка": [
    33.35591,
    46.75966
  ],
  "nova kakhovka": [
    33.35591,
    46.75966
  ],
  "чаплинка": [
    33.54087,
    46.36454
  ],
  "chaplynka": [
    33.54087,
    46.36454
  ],
  "таврійськ": [
    33.41665,
    46.75432
  ],
  "tavriisk": [
    33.41665,
    46.75432
  ],
  "скадовськ": [
    32.90978,
    46.11313
  ],
  "skadovsk": [
    32.90978,
    46.11313
  ],
  "олешки": [
    32.72426,
    46.62553
  ],
  "oleshky": [
    32.72426,
    46.62553
  ],
  "чорнобаївка": [
    32.54507,
    46.69641
  ],
  "chornobaivka": [
    32.54507,
    46.69641
  ],
  "oleksandrivka": [
    32.23968,
    48.968
  ],
  "білозерка": [
    32.44447,
    46.62651
  ],
  "bilozerka": [
    32.44447,
    46.62651
  ],
  "херсон": [
    32.61458,
    46.63695
  ],
  "kherson": [
    32.61458,
    46.63695
  ],
  "бердянськ": [
    36.78815,
    46.75578
  ],
  "berdiansk": [
    36.78815,
    46.75578
  ],
  "енергодар": [
    34.66199,
    47.49048
  ],
  "energodar": [
    34.66199,
    47.49048
  ],
  "запоріжжя": [
    35.11714,
    47.85167
  ],
  "zaporizhzhia": [
    35.11714,
    47.85167
  ],
  "мелітополь": [
    35.38196,
    46.84735
  ],
  "melitopol": [
    35.38196,
    46.84735
  ],
  "гуляйполе": [
    36.2656849,
    47.6655382
  ],
  "gulyaypole": [
    30.96401,
    48.85747
  ],
  "кам'янка": [
    36.65108,
    47.3624
  ],
  "kam'yanka": [
    39.38667,
    48.24447
  ],
  "оріхів": [
    35.78333,
    47.57613
  ],
  "orihiv": [
    35.78333,
    47.57613
  ],
  "токмак": [
    35.70836,
    47.25554
  ],
  "tokmak": [
    35.70836,
    47.25554
  ],
  "пологи": [
    36.25463,
    47.47865
  ],
  "polohy": [
    36.25463,
    47.47865
  ],
  "бахчисарай": [
    33.85782,
    44.75525
  ],
  "bakhchysarai": [
    33.85782,
    44.75525
  ],
  "білогірськ": [
    34.60386,
    45.05679
  ],
  "bilogirsk": [
    34.60386,
    45.05679
  ],
  "євпаторія": [
    33.36655,
    45.20091
  ],
  "yevpatoriya": [
    33.36655,
    45.20091
  ],
  "курман": [
    34.30134,
    45.50271
  ],
  "kurman": [
    34.30134,
    45.50271
  ],
  "яни капу": [
    33.79261,
    45.95547
  ],
  "yani kapu": [
    33.79261,
    45.95547
  ],
  "сімферополь": [
    34.11079,
    44.95719
  ],
  "simferopol": [
    34.11079,
    44.95719
  ],
  "феодосія": [
    35.38153,
    45.03199
  ],
  "feodosiia": [
    35.38153,
    45.03199
  ],
  "джанкой": [
    34.39273,
    45.7131
  ],
  "dzhankoj": [
    34.39273,
    45.7131
  ],
  "керч": [
    36.47542,
    45.35675
  ],
  "kerch": [
    36.47542,
    45.35675
  ],
  "ялта": [
    34.16624,
    44.50218
  ],
  "yalta": [
    34.16624,
    44.50218
  ],
  "богодухів": [
    35.52367,
    50.16147
  ],
  "bogoduhiv": [
    35.52367,
    50.16147
  ],
  "балаклія": [
    36.8397826,
    49.4521336
  ],
  "balakliya": [
    33.75428,
    49.61376
  ],
  "ізюм": [
    37.27679,
    49.20697
  ],
  "izyum": [
    37.27679,
    49.20697
  ],
  "берестин": [
    35.44485,
    49.3776
  ],
  "berestyn": [
    35.44485,
    49.3776
  ],
  "куп'янськ": [
    37.61581,
    49.71003
  ],
  "kup'yansk": [
    37.61581,
    49.71003
  ],
  "златопіль": [
    36.21848,
    49.37646
  ],
  "zlatopil": [
    36.21848,
    49.37646
  ],
  "лозова": [
    36.31412,
    48.89066
  ],
  "lozova": [
    36.31412,
    48.89066
  ],
  "дергачі": [
    36.1209,
    50.10789
  ],
  "dergachi": [
    36.1209,
    50.10789
  ],
  "харків": [
    36.25475,
    49.98177
  ],
  "kharkiv": [
    36.25475,
    49.98177
  ],
  "мерефа": [
    36.0567,
    49.82107
  ],
  "merefa": [
    36.0567,
    49.82107
  ],
  "пісочин": [
    36.10262,
    49.9516
  ],
  "pisochyn": [
    36.10262,
    49.9516
  ],
  "циркуни": [
    36.38724,
    50.08438
  ],
  "tsyrkuny": [
    36.38724,
    50.08438
  ],
  "козача лопань": [
    36.19823,
    50.33212
  ],
  "kozacha lopan": [
    36.19823,
    50.33212
  ],
  "липці": [
    36.42086,
    50.20919
  ],
  "lyptsi": [
    36.42086,
    50.20919
  ],
  "вовчанськ": [
    36.94108,
    50.29078
  ],
  "vovchansk": [
    36.94108,
    50.29078
  ],
  "коробочкине": [
    36.81286,
    49.77626
  ],
  "korobochkine": [
    36.81286,
    49.77626
  ],
  "білий колодязь": [
    37.11265,
    50.20412
  ],
  "bilyi kolodyaz": [
    37.11265,
    50.20412
  ],
  "чугуїв": [
    36.6865,
    49.83538
  ],
  "chuhuiv": [
    36.6865,
    49.83538
  ],
  "бахмут": [
    37.99886,
    48.59419
  ],
  "bakhmut": [
    37.99886,
    48.59419
  ],
  "світлодарськ": [
    38.22331,
    48.43374
  ],
  "svitlodarsk": [
    38.22331,
    48.43374
  ],
  "торецьк": [
    37.8478,
    48.39477
  ],
  "toretsk": [
    37.8478,
    48.39477
  ],
  "часів яр": [
    37.83409,
    48.58768
  ],
  "chasiv yar": [
    37.83409,
    48.58768
  ],
  "соледар": [
    38.07098,
    48.6921
  ],
  "soledar": [
    38.07098,
    48.6921
  ],
  "велика новосілка": [
    36.83627,
    47.84281
  ],
  "velyka novosilka": [
    36.83627,
    47.84281
  ],
  "вугледар": [
    37.24999,
    47.77973
  ],
  "vugledar": [
    37.24999,
    47.77973
  ],
  "горлівка": [
    38.01709,
    48.29986
  ],
  "horlivka": [
    38.01709,
    48.29986
  ],
  "сніжне": [
    38.76205,
    48.02328
  ],
  "snizhne": [
    38.76205,
    48.02328
  ],
  "шахтарськ": [
    38.43826,
    48.05657
  ],
  "shahtarsk": [
    38.43826,
    48.05657
  ],
  "єнакієве": [
    38.20403,
    48.23857
  ],
  "yenakiieve": [
    38.20403,
    48.23857
  ],
  "донецьк": [
    37.80224,
    48.023
  ],
  "donetsk": [
    37.80224,
    48.023
  ],
  "харцизьк": [
    38.14025,
    48.04277
  ],
  "harcizk": [
    38.14025,
    48.04277
  ],
  "макіївка": [
    37.92576,
    48.04782
  ],
  "makiyivka": [
    37.92576,
    48.04782
  ],
  "кальміуське": [
    37.7925,
    47.242
  ],
  "kalmiuske": [
    37.7925,
    47.242
  ],
  "лиман": [
    37.80843,
    48.99012
  ],
  "lyman": [
    37.80843,
    48.99012
  ],
  "краматорськ": [
    37.56779,
    48.73106
  ],
  "kramatorsk": [
    37.56779,
    48.73106
  ],
  "костянтинівка": [
    37.6923755,
    48.5348985
  ],
  "kostyantinivka": [
    34.11774,
    47.15183
  ],
  "дружківка": [
    37.52537,
    48.61995
  ],
  "druzhkivka": [
    37.52537,
    48.61995
  ],
  "святогірськ": [
    37.57194,
    49.04101
  ],
  "svyatogirsk": [
    37.57194,
    49.04101
  ],
  "слов'янськ": [
    37.59739,
    48.84974
  ],
  "slov'yansk": [
    37.59739,
    48.84974
  ],
  "маріуполь": [
    37.54131,
    47.09514
  ],
  "mariupol": [
    37.54131,
    47.09514
  ],
  "авдіївка": [
    37.75008,
    48.14019
  ],
  "avdiivka": [
    37.75008,
    48.14019
  ],
  "добропілля": [
    37.04866,
    48.42115
  ],
  "dobropillia": [
    37.04866,
    48.42115
  ],
  "курахове": [
    37.28069,
    47.9847
  ],
  "kurahove": [
    37.28069,
    47.9847
  ],
  "мар'їнка": [
    37.50544,
    47.94527
  ],
  "mar'yinka": [
    37.50544,
    47.94527
  ],
  "мирноград": [
    37.26513,
    48.3099
  ],
  "mirnograd": [
    37.26513,
    48.3099
  ],
  "покровськ": [
    37.17706,
    48.28014
  ],
  "pokrovsk": [
    37.17706,
    48.28014
  ],
  "брянка": [
    38.67222,
    48.511
  ],
  "brianka": [
    38.67222,
    48.511
  ],
  "кадіївка": [
    38.64352,
    48.56818
  ],
  "kadiivka": [
    38.64352,
    48.56818
  ],
  "алчевськ": [
    38.79744,
    48.46906
  ],
  "alchevsk": [
    38.79744,
    48.46906
  ],
  "довжанськ": [
    39.64744,
    48.07615
  ],
  "dovzhansk": [
    39.64744,
    48.07615
  ],
  "луганськ": [
    39.30553,
    48.56814
  ],
  "lugansk": [
    39.30553,
    48.56814
  ],
  "ровеньки": [
    39.37696,
    48.08277
  ],
  "rovenky": [
    39.37696,
    48.08277
  ],
  "хрустальний": [
    38.92369,
    48.14241
  ],
  "hrustalniy": [
    38.92369,
    48.14241
  ],
  "антрацит": [
    39.08863,
    48.11638
  ],
  "antracyt": [
    39.08863,
    48.11638
  ],
  "рубіжне": [
    38.37972,
    49.00849
  ],
  "rubizhne": [
    38.37972,
    49.00849
  ],
  "сіверськодонецьк": [
    38.48754,
    48.94414
  ],
  "siverskodonetsk": [
    38.48754,
    48.94414
  ],
  "лисичанськ": [
    38.42088,
    48.91211
  ],
  "lisichansk": [
    38.42088,
    48.91211
  ],
  "золоте": [
    38.51512,
    48.69516
  ],
  "zolote": [
    38.51512,
    48.69516
  ],
  "старобільськ": [
    38.9075,
    49.27881
  ],
  "starobilsk": [
    38.9075,
    49.27881
  ],
  "новоайдар": [
    39.00376,
    48.96288
  ],
  "novoaidar": [
    39.00376,
    48.96288
  ],
  "севастополь": [
    33.52134,
    44.60795
  ],
  "sevastopol": [
    33.52134,
    44.60795
  ],
  "славутич": [
    30.71806,
    51.5225
  ],
  "slavutych": [
    30.71806,
    51.5225
  ],
  "покровське": [
    36.23446,
    47.98126
  ],
  "pokrovske": [
    36.23446,
    47.98126
  ],
  "кролевець": [
    33.38044,
    51.55181
  ],
  "krolevets": [
    33.38044,
    51.55181
  ],
  "боярка": [
    30.2847595,
    50.3356709
  ],
  "boyarka": [
    30.68736,
    49.327
  ],
  "богуслав": [
    30.87407,
    49.54637
  ],
  "boguslav": [
    30.87407,
    49.54637
  ],
  "антонівка": [
    32.73061,
    46.67666
  ],
  "antonivka": [
    32.73061,
    46.67666
  ],
  "новопавлівка": [
    34.43376,
    47.57563
  ],
  "novopavlivka": [
    34.43376,
    47.57563
  ],
  "межова": [
    36.73178,
    48.25418
  ],
  "mezhova": [
    36.73178,
    48.25418
  ],
  "комишуваха": [
    35.52405,
    47.71491
  ],
  "komishuvaha": [
    35.52405,
    47.71491
  ],
  "вільнянськ": [
    35.44034,
    47.94768
  ],
  "vilniansk": [
    35.44034,
    47.94768
  ],
  "борова": [
    37.6253381,
    49.3799491
  ],
  "borova": [
    30.10429,
    50.17625
  ],
  "таврійське": [
    35.69733,
    47.652512
  ],
  "tavriiske": [
    32.56239,
    46.37324
  ],
  "біленьке": [
    35.030251,
    47.621609
  ],
  "bilenke": [
    37.63309,
    48.76589
  ],
  "нетішин": [
    26.64872,
    50.32863
  ],
  "netishyn": [
    26.64872,
    50.32863
  ],
  "бобровиця": [
    31.3860852,
    50.7415033
  ],
  "bobrovytsia": [
    31.38205,
    50.74559
  ],
  "гадяч": [
    33.9950534,
    50.3701299
  ],
  "hadiach": [
    35.40338,
    49.28774
  ],
  "мена": [
    32.21364,
    51.52205
  ],
  "mena": [
    32.21364,
    51.52205
  ],
  "овідіополь": [
    30.43746,
    46.24721
  ],
  "ovidiopol": [
    30.43746,
    46.24721
  ],
  "вилкове": [
    29.5869,
    45.40279
  ],
  "vylkove": [
    29.5869,
    45.40279
  ],
  "татарбунари": [
    29.61123,
    45.83861
  ],
  "tatarbunary": [
    29.61123,
    45.83861
  ],
  "тузли": [
    30.09773,
    45.86504
  ],
  "tuzly": [
    30.09773,
    45.86504
  ],
  "сарата": [
    29.66444,
    46.02056
  ],
  "sarata": [
    29.66444,
    46.02056
  ],
  "арциз": [
    29.43286,
    45.98526
  ],
  "artsyz": [
    29.43286,
    45.98526
  ],
  "снігурівка": [
    32.8197,
    47.07651
  ],
  "snihurivka": [
    32.8197,
    47.07651
  ],
  "короп": [
    32.95217,
    51.56666
  ],
  "korop": [
    32.95217,
    51.56666
  ],
  "сосниця": [
    32.49985,
    51.52387
  ],
  "sosnytsia": [
    32.49985,
    51.52387
  ],
  "сновськ": [
    31.94245,
    51.81674
  ],
  "snovsk": [
    31.94245,
    51.81674
  ],
  "козелець": [
    31.11664,
    50.91211
  ],
  "kozelets": [
    31.11664,
    50.91211
  ],
  "батурин": [
    32.87981,
    51.34261
  ],
  "baturyn": [
    32.87981,
    51.34261
  ],
  "андрушівка": [
    29.01883,
    50.01922
  ],
  "andrushivka": [
    29.01883,
    50.01922
  ],
  "коростишів": [
    29.05774,
    50.31686
  ],
  "korostyshiv": [
    29.05774,
    50.31686
  ],
  "черняхів": [
    28.66717,
    50.45412
  ],
  "cherniakhiv": [
    28.66717,
    50.45412
  ],
  "ружин": [
    29.21874,
    49.72175
  ],
  "ruzhyn": [
    29.21874,
    49.72175
  ],
  "малин": [
    29.24225,
    50.76756
  ],
  "malyn": [
    29.24225,
    50.76756
  ],
  "ладижин": [
    29.23636,
    48.68437
  ],
  "ladyzhyn": [
    29.23636,
    48.68437
  ],
  "козятин": [
    28.8354279,
    49.7195867
  ],
  "koziatyn": [
    24.66437,
    50.57789
  ],
  "погребище": [
    29.25988,
    49.48508
  ],
  "pohrebyshche": [
    29.25988,
    49.48508
  ],
  "красилів": [
    26.97211,
    49.65376
  ],
  "krasyliv": [
    26.97211,
    49.65376
  ],
  "адампіль": [
    27.65652,
    49.66791
  ],
  "adampil": [
    27.65652,
    49.66791
  ],
  "полонне": [
    27.50856,
    50.11944
  ],
  "polonne": [
    27.50856,
    50.11944
  ],
  "гнівань": [
    28.33785,
    49.0939
  ],
  "hnivan": [
    28.33785,
    49.0939
  ],
  "лохвиця": [
    33.27153,
    50.36444
  ],
  "lokhvytsia": [
    33.27153,
    50.36444
  ],
  "кобеляки": [
    34.20193,
    49.14936
  ],
  "kobeliaky": [
    34.20193,
    49.14936
  ],
  "решетилівка": [
    34.07896,
    49.563
  ],
  "reshetylivka": [
    34.07896,
    49.563
  ],
  "нові санжари": [
    34.31496,
    49.33379
  ],
  "novi sanzhary": [
    34.31496,
    49.33379
  ],
  "глобине": [
    33.27555,
    49.37894
  ],
  "hlobyne": [
    33.27555,
    49.37894
  ],
  "острог": [
    26.52113,
    50.32897
  ],
  "ostroh": [
    26.52113,
    50.32897
  ],
  "здолбунів": [
    26.24823,
    50.52205
  ],
  "zdolbuniv": [
    26.24823,
    50.52205
  ],
  "костопіль": [
    26.44797,
    50.87732
  ],
  "kostopil": [
    26.44797,
    50.87732
  ],
  "rokytne": [
    27.21705,
    51.27891
  ],
  "дубровиця": [
    26.56369,
    51.57076
  ],
  "dubrovytsia": [
    26.56369,
    51.57076
  ],
  "голоби": [
    25.00882,
    51.08798
  ],
  "holoby": [
    25.00882,
    51.08798
  ],
  "турійськ": [
    24.5262,
    51.08724
  ],
  "turiisk": [
    24.5262,
    51.08724
  ],
  "любешів": [
    25.51317,
    51.76505
  ],
  "liubeshiv": [
    25.51317,
    51.76505
  ],
  "локачі": [
    24.64872,
    50.73898
  ],
  "lokachi": [
    24.64872,
    50.73898
  ],
  "володимир": [
    24.32119,
    50.85033
  ],
  "volodymyr": [
    24.32119,
    50.85033
  ],
  "бібрка": [
    24.29369,
    49.63921
  ],
  "bibrka": [
    24.29369,
    49.63921
  ],
  "буськ": [
    24.61227,
    49.96548
  ],
  "busk": [
    24.61227,
    49.96548
  ],
  "збараж": [
    25.77925,
    49.66157
  ],
  "zbarazh": [
    25.77925,
    49.66157
  ],
  "бережани": [
    24.93686,
    49.44578
  ],
  "berezhany": [
    24.93686,
    49.44578
  ],
  "козова": [
    25.14547,
    49.43206
  ],
  "kozova": [
    25.14547,
    49.43206
  ],
  "кременець": [
    25.72787,
    50.09864
  ],
  "kremenets": [
    25.72787,
    50.09864
  ],
  "бурштин": [
    24.63339,
    49.25193
  ],
  "burshtyn": [
    24.63339,
    49.25193
  ],
  "галич": [
    24.72748,
    49.12374
  ],
  "halych": [
    24.72748,
    49.12374
  ],
  "бобринець": [
    32.1655,
    48.05674
  ],
  "bobrynets": [
    32.1655,
    48.05674
  ],
  "долинська": [
    32.77691,
    48.11725
  ],
  "dolynska": [
    32.77691,
    48.11725
  ],
  "онуфріївка": [
    33.44954,
    48.89917
  ],
  "onufriivka": [
    33.44954,
    48.89917
  ],
  "знам'янка": [
    32.6659476,
    48.7199609
  ],
  "znamianka": [
    34.35201,
    45.5429
  ],
  "ржищів": [
    31.0424,
    49.96934
  ],
  "rzhyshchiv": [
    31.0424,
    49.96934
  ],
  "ворзель": [
    30.15305,
    50.5444
  ],
  "vorzel": [
    30.15305,
    50.5444
  ],
  "димер": [
    30.30357,
    50.78579
  ],
  "dymer": [
    30.30357,
    50.78579
  ],
  "нововоронцовка": [
    33.92317,
    47.50499
  ],
  "novovorontsovka": [
    33.92317,
    47.50499
  ],
  "осокорівка": [
    33.923,
    47.432
  ],
  "osokorivka": [
    33.923,
    47.432
  ],
  "іршанськ": [
    28.72119,
    50.75317
  ],
  "irshansk": [
    28.72119,
    50.75317
  ],
  "городня": [
    31.59632,
    51.89129
  ],
  "horodnia": [
    31.59632,
    51.89129
  ],
  "любар": [
    27.75108,
    49.92322
  ],
  "liubar": [
    27.75108,
    49.92322
  ],
  "озерне": [
    28.73384,
    50.17816
  ],
  "ozerne": [
    28.73384,
    50.17816
  ],
  "іллінці": [
    29.20589,
    49.10544
  ],
  "illintsi": [
    29.20589,
    49.10544
  ],
  "липовець": [
    29.05669,
    49.22776
  ],
  "lypovets": [
    29.05669,
    49.22776
  ],
  "літин": [
    28.08698,
    49.32711
  ],
  "lityn": [
    28.08698,
    49.32711
  ],
  "немирів": [
    28.83781,
    48.97002
  ],
  "nemyriv": [
    28.83781,
    48.97002
  ],
  "оратів": [
    29.52889,
    49.18594
  ],
  "orativ": [
    29.52889,
    49.18594
  ],
  "тиврів": [
    28.50044,
    49.01206
  ],
  "tyvriv": [
    28.50044,
    49.01206
  ],
  "бершадь": [
    29.51463,
    48.36354
  ],
  "bershad": [
    29.51463,
    48.36354
  ],
  "теплик": [
    29.74482,
    48.66538
  ],
  "teplyk": [
    29.74482,
    48.66538
  ],
  "чечельник": [
    29.36469,
    48.21558
  ],
  "chechelnyk": [
    29.36469,
    48.21558
  ],
  "бар": [
    27.67404,
    49.07362
  ],
  "bar": [
    27.67404,
    49.07362
  ],
  "шаргород": [
    28.08459,
    48.73562
  ],
  "sharhorod": [
    28.08459,
    48.73562
  ],
  "муровані курилівці": [
    27.53084,
    48.71813
  ],
  "murovani kurylivtsi": [
    27.53084,
    48.71813
  ],
  "yampil": [
    28.28141,
    48.24056
  ],
  "крижопіль": [
    28.86766,
    48.3821
  ],
  "kryzhopil": [
    28.86766,
    48.3821
  ],
  "піщанка": [
    28.88056,
    48.21249
  ],
  "pishchanka": [
    28.88056,
    48.21249
  ],
  "томашпіль": [
    28.51295,
    48.53695
  ],
  "tomashpil": [
    28.51295,
    48.53695
  ],
  "kalynivka": [
    28.51541,
    49.46129
  ],
  "іваничі": [
    24.35634,
    50.63592
  ],
  "ivanychi": [
    24.35634,
    50.63592
  ],
  "маневичі": [
    25.53063,
    51.29385
  ],
  "manevychi": [
    25.53063,
    51.29385
  ],
  "любомль": [
    24.03225,
    51.22536
  ],
  "liuboml": [
    24.03225,
    51.22536
  ],
  "ратне": [
    24.52644,
    51.66919
  ],
  "ratne": [
    24.52644,
    51.66919
  ],
  "стара вижівка": [
    24.43958,
    51.43661
  ],
  "stara vyzhivka": [
    24.43958,
    51.43661
  ],
  "шацьк": [
    23.93589,
    51.49929
  ],
  "shatsk": [
    23.93589,
    51.49929
  ],
  "горохів": [
    24.75681,
    50.50224
  ],
  "horokhiv": [
    24.75681,
    50.50224
  ],
  "ківерці": [
    25.45596,
    50.83516
  ],
  "kivertsi": [
    25.45596,
    50.83516
  ],
  "рожище": [
    25.27121,
    50.91632
  ],
  "rozhyshche": [
    25.27121,
    50.91632
  ],
  "петриківка": [
    34.61901,
    48.7264
  ],
  "petrykivka": [
    34.61901,
    48.7264
  ],
  "солоне": [
    34.87585,
    48.20907
  ],
  "solone": [
    34.87585,
    48.20907
  ],
  "царичанка": [
    34.48601,
    48.94186
  ],
  "tsarychanka": [
    34.48601,
    48.94186
  ],
  "верхньодніпровськ": [
    34.3262,
    48.65557
  ],
  "verkhniodniprovsk": [
    34.3262,
    48.65557
  ],
  "кринички": [
    34.46202,
    48.37438
  ],
  "krynychky": [
    34.46202,
    48.37438
  ],
  "п'ятихатки": [
    33.7056731,
    48.4124572
  ],
  "piatykhatky": [
    33.49625,
    49.15266
  ],
  "софіївка": [
    33.8668627,
    48.0482032
  ],
  "sofiivka": [
    34.00133,
    45.09456
  ],
  "широке": [
    33.26147,
    47.6855
  ],
  "shyroke": [
    33.26147,
    47.6855
  ],
  "томаківка": [
    34.74324,
    47.81081
  ],
  "tomakivka": [
    34.74324,
    47.81081
  ],
  "магдалинівка": [
    34.91395,
    48.91204
  ],
  "mahdalynivka": [
    34.91395,
    48.91204
  ],
  "юріївка": [
    36.015,
    48.73556
  ],
  "yuriivka": [
    36.015,
    48.73556
  ],
  "васильківка": [
    36.02214,
    48.20824
  ],
  "vasylkivka": [
    36.02214,
    48.20824
  ],
  "петропавлівка": [
    36.43061,
    48.46353
  ],
  "petropavlivka": [
    36.43061,
    48.46353
  ],
  "варва": [
    32.72274,
    50.49858
  ],
  "varva": [
    32.72274,
    50.49858
  ],
  "срібне": [
    32.91906,
    50.66314
  ],
  "sribne": [
    32.91906,
    50.66314
  ],
  "куликівка": [
    31.64604,
    51.3729
  ],
  "kulykivka": [
    31.64604,
    51.3729
  ],
  "ріпки": [
    31.08578,
    51.80165
  ],
  "ripky": [
    31.08578,
    51.80165
  ],
  "путила": [
    25.08757,
    47.99343
  ],
  "putyla": [
    25.08757,
    47.99343
  ],
  "сокиряни": [
    27.411193,
    48.4460307
  ],
  "sokyriany": [
    29.79168,
    48.58017
  ],
  "хотин": [
    26.48978,
    48.50555
  ],
  "khotyn": [
    26.48978,
    48.50555
  ],
  "герца": [
    26.26186,
    48.14752
  ],
  "hertsa": [
    26.26186,
    48.14752
  ],
  "липова долина": [
    33.79154,
    50.56292
  ],
  "lypova dolyna": [
    33.79154,
    50.56292
  ],
  "холми": [
    32.59733,
    51.87141
  ],
  "kholmy": [
    32.59733,
    51.87141
  ],
  "брусилів": [
    29.52008,
    50.28226
  ],
  "brusyliv": [
    29.52008,
    50.28226
  ],
  "попільня": [
    29.45265,
    49.9532
  ],
  "popilnia": [
    29.45265,
    49.9532
  ],
  "пулини": [
    28.27,
    50.46745
  ],
  "pulyny": [
    28.27,
    50.46745
  ],
  "радомишль": [
    29.23003,
    50.4962
  ],
  "radomyshl": [
    29.23003,
    50.4962
  ],
  "романів": [
    27.9314,
    50.14733
  ],
  "romaniv": [
    27.9314,
    50.14733
  ],
  "чуднів": [
    28.12058,
    50.05255
  ],
  "chudniv": [
    28.12058,
    50.05255
  ],
  "хорошів": [
    28.44489,
    50.59484
  ],
  "khoroshiv": [
    28.44489,
    50.59484
  ],
  "лугини": [
    28.39876,
    51.07899
  ],
  "luhyny": [
    28.39876,
    51.07899
  ],
  "народичі": [
    29.08341,
    51.20304
  ],
  "narodychi": [
    29.08341,
    51.20304
  ],
  "олевськ": [
    27.65228,
    51.22482
  ],
  "olevsk": [
    27.65228,
    51.22482
  ],
  "баранівка": [
    27.6622,
    50.29691
  ],
  "baranivka": [
    27.6622,
    50.29691
  ],
  "ємільчине": [
    27.80198,
    50.87185
  ],
  "yemilchyne": [
    27.80198,
    50.87185
  ],
  "виноградів": [
    23.03623,
    48.14126
  ],
  "vynohradiv": [
    23.03623,
    48.14126
  ],
  "воловець": [
    23.1851,
    48.7109
  ],
  "volovets": [
    23.1851,
    48.7109
  ],
  "свалява": [
    22.98673,
    48.54735
  ],
  "svaliava": [
    22.98673,
    48.54735
  ],
  "великий березний": [
    22.46121,
    48.8934
  ],
  "velykyi bereznyi": [
    22.46121,
    48.8934
  ],
  "перечин": [
    22.47718,
    48.73494
  ],
  "perechyn": [
    22.47718,
    48.73494
  ],
  "іршава": [
    23.04065,
    48.31227
  ],
  "irshava": [
    23.04065,
    48.31227
  ],
  "міжгір'я": [
    23.5009289,
    48.5281184
  ],
  "mizhhiria": [
    34.21238,
    49.78409
  ],
  "приморськ": [
    36.34599,
    46.73415
  ],
  "prymorsk": [
    36.34599,
    46.73415
  ],
  "чернігівка": [
    36.21648,
    47.19451
  ],
  "chernihivka": [
    36.21648,
    47.19451
  ],
  "велика білозерка": [
    34.68457,
    47.27572
  ],
  "velyka bilozerka": [
    34.68457,
    47.27572
  ],
  "кам'янка-дніпровська": [
    34.41026,
    47.49629
  ],
  "kamianka-dniprovska": [
    34.41026,
    47.49629
  ],
  "михайлівка": [
    35.2217134,
    47.2657187
  ],
  "mykhailivka": [
    38.90043,
    48.4976
  ],
  "новомихайлівка": [
    35.529781,
    47.838589
  ],
  "novomykhailivka": [
    32.73645,
    47.74502
  ],
  "веселе": [
    34.91843,
    47.00973
  ],
  "vesele": [
    34.91843,
    47.00973
  ],
  "приазовське": [
    35.64082,
    46.73123
  ],
  "pryazovske": [
    35.64082,
    46.73123
  ],
  "якимівка": [
    35.16334,
    46.7011
  ],
  "yakymivka": [
    35.16334,
    46.7011
  ],
  "більмак": [
    36.65331,
    47.35914
  ],
  "bilmak": [
    36.65331,
    47.35914
  ],
  "розівка": [
    37.07078,
    47.3954
  ],
  "rozivka": [
    37.07078,
    47.3954
  ],
  "богородчани": [
    24.53728,
    48.80812
  ],
  "bohorodchany": [
    24.53728,
    48.80812
  ],
  "рогатин": [
    24.61103,
    49.41043
  ],
  "rohatyn": [
    24.61103,
    49.41043
  ],
  "тлумач": [
    25.00385,
    48.86519
  ],
  "tlumach": [
    25.00385,
    48.86519
  ],
  "долина": [
    23.96558,
    48.97158
  ],
  "dolyna": [
    23.96558,
    48.97158
  ],
  "рожнятів": [
    24.15627,
    48.93975
  ],
  "rozhniativ": [
    24.15627,
    48.93975
  ],
  "городенка": [
    25.5033,
    48.669
  ],
  "horodenka": [
    25.5033,
    48.669
  ],
  "снятин": [
    25.55994,
    48.44883
  ],
  "sniatyn": [
    25.55994,
    48.44883
  ],
  "яремче": [
    24.55335,
    48.44886
  ],
  "yaremche": [
    24.55335,
    48.44886
  ],
  "чорноморське": [
    30.9334115,
    46.5849122
  ],
  "chornomorske": [
    32.69776,
    45.50657
  ],
  "усатове": [
    30.64951,
    46.52893
  ],
  "usatove": [
    30.64951,
    46.52893
  ],
  "володарка": [
    29.91023,
    49.52501
  ],
  "volodarka": [
    29.91023,
    49.52501
  ],
  "ставище": [
    30.19102,
    49.3915
  ],
  "stavysche": [
    30.19102,
    49.3915
  ],
  "тараща": [
    30.49615,
    49.55719
  ],
  "tarashcha": [
    30.49615,
    49.55719
  ],
  "тетіїв": [
    29.66933,
    49.37019
  ],
  "tetiiv": [
    29.66933,
    49.37019
  ],
  "баришівка": [
    31.32005,
    50.35925
  ],
  "baryshivka": [
    31.32005,
    50.35925
  ],
  "іванків": [
    29.90205,
    50.93953
  ],
  "ivankiv": [
    29.90205,
    50.93953
  ],
  "поліське": [
    29.38896,
    51.240486
  ],
  "poliske": [
    28.53761,
    50.9044
  ],
  "добротвір": [
    24.3835,
    50.20526
  ],
  "dobrotvir": [
    24.3835,
    50.20526
  ],
  "чаплине": [
    36.23007,
    48.12827
  ],
  "chaplyne": [
    36.23007,
    48.12827
  ],
  "новодонецьке": [
    36.98276,
    48.63512
  ],
  "novodonetske": [
    36.98276,
    48.63512
  ],
  "любеч": [
    30.66018,
    51.70219
  ],
  "liubech": [
    30.66018,
    51.70219
  ],
  "благовіщенське": [
    30.23619,
    48.32822
  ],
  "blahovishchenske": [
    30.23619,
    48.32822
  ],
  "вільшанка": [
    30.87285,
    48.23421
  ],
  "vilshanka": [
    30.87285,
    48.23421
  ],
  "гайворон": [
    29.8593204,
    48.3406905
  ],
  "haivoron": [
    29.83323,
    49.5739
  ],
  "новоархангельськ": [
    30.80705,
    48.66187
  ],
  "novoarkhanhelsk": [
    30.80705,
    48.66187
  ],
  "компаніївка": [
    32.20138,
    48.25022
  ],
  "kompaniivka": [
    32.20138,
    48.25022
  ],
  "новгородка": [
    32.65469,
    48.36089
  ],
  "novhorodka": [
    32.65469,
    48.36089
  ],
  "устинівка": [
    32.53938,
    47.95619
  ],
  "ustynivka": [
    32.53938,
    47.95619
  ],
  "добровеличківка": [
    31.18039,
    48.38939
  ],
  "dobrovelychkivka": [
    31.18039,
    48.38939
  ],
  "мала виска": [
    31.63231,
    48.64694
  ],
  "mala vyska": [
    31.63231,
    48.64694
  ],
  "новомиргород": [
    31.64904,
    48.79345
  ],
  "novomyrhorod": [
    31.64904,
    48.79345
  ],
  "петрове": [
    33.2653,
    48.33809
  ],
  "petrove": [
    33.2653,
    48.33809
  ],
  "ланівці": [
    26.09052,
    49.86103
  ],
  "lanivtsi": [
    26.09052,
    49.86103
  ],
  "шумськ": [
    26.11792,
    50.11775
  ],
  "shumsk": [
    26.11792,
    50.11775
  ],
  "зборів": [
    25.14019,
    49.66493
  ],
  "zboriv": [
    25.14019,
    49.66493
  ],
  "підволочиськ": [
    26.14401,
    49.53131
  ],
  "pidvolochysk": [
    26.14401,
    49.53131
  ],
  "підгайці": [
    25.1361578,
    49.2680238
  ],
  "pidhaitsi": [
    25.4037,
    50.71312
  ],
  "теребовля": [
    25.68886,
    49.29967
  ],
  "terebovlia": [
    25.68886,
    49.29967
  ],
  "борщів": [
    26.03171,
    48.80319
  ],
  "borshchiv": [
    26.03171,
    48.80319
  ],
  "бучач": [
    25.39496,
    49.06234
  ],
  "buchach": [
    25.39496,
    49.06234
  ],
  "гусятин": [
    26.20464,
    49.07123
  ],
  "husiatyn": [
    26.20464,
    49.07123
  ],
  "заліщики": [
    25.7317,
    48.64098
  ],
  "zalishchyky": [
    25.7317,
    48.64098
  ],
  "монастириська": [
    25.17149,
    49.09063
  ],
  "monastyryska": [
    25.17149,
    49.09063
  ],
  "сіверськ": [
    38.09683,
    48.86476
  ],
  "siversk": [
    38.09683,
    48.86476
  ],
  "верхня сироватка": [
    34.95861,
    50.82902
  ],
  "verkhnia syrovatka": [
    34.95861,
    50.82902
  ],
  "рай-олександрівка": [
    37.8512,
    48.81041
  ],
  "rai-oleksandrivka": [
    37.8512,
    48.81041
  ],
  "приморське": [
    35.29074,
    47.6449
  ],
  "prymorske": [
    35.29074,
    47.6449
  ],
  "малокатеринівка": [
    35.25733,
    47.6557
  ],
  "malokaterynivka": [
    35.25733,
    47.6557
  ],
  "кушугум": [
    35.21644,
    47.70963
  ],
  "kushuhum": [
    35.21644,
    47.70963
  ],
  "балабине": [
    35.21361,
    47.73686
  ],
  "balabyne": [
    35.21361,
    47.73686
  ],
  "городок": [
    23.6465626,
    49.784596
  ],
  "horodok": [
    26.56357,
    49.17209
  ],
  "хотів": [
    30.46836,
    50.33069
  ],
  "khotiv": [
    30.46836,
    50.33069
  ],
  "чабани": [
    30.42856,
    50.34128
  ],
  "chabany": [
    30.42856,
    50.34128
  ],
  "зазим'я": [
    30.67319,
    50.56923
  ],
  "zazymia": [
    30.67319,
    50.56923
  ],
  "дмитрівка": [
    31.740156,
    46.631561
  ],
  "dmytrivka": [
    28.98849,
    45.96904
  ],
  "mykolaivka": [
    37.76835,
    48.86193
  ],
  "стецьківка": [
    34.78849,
    51.01307
  ],
  "stetskivka": [
    34.78849,
    51.01307
  ],
  "маяки": [
    30.2750575,
    46.416632
  ],
  "maiaky": [
    37.6204,
    48.94685
  ],
  "доброслав": [
    30.94518,
    46.82095
  ],
  "dobroslav": [
    30.94518,
    46.82095
  ],
  "колодязне": [
    37.688599,
    50.007702
  ],
  "kolodiazne": [
    26.88333,
    50.91667
  ],
  "суханове": [
    33.53626,
    47.12841
  ],
  "sukhanove": [
    33.53626,
    47.12841
  ],
  "гатне": [
    30.37497,
    50.35444
  ],
  "hatne": [
    30.37497,
    50.35444
  ],
  "дачне": [
    30.54747,
    46.58226
  ],
  "dachne": [
    30.54747,
    46.58226
  ],
  "болгарка": [
    30.46148,
    46.6912
  ],
  "bolharka": [
    30.46148,
    46.6912
  ],
  "дальник": [
    30.52982,
    46.22569
  ],
  "dalnyk": [
    30.52982,
    46.22569
  ],
  "велика чернеччина": [
    34.92359,
    50.95458
  ],
  "velyka chernechchyna": [
    34.92359,
    50.95458
  ],
  "дніпровське": [
    31.8741042,
    46.6358818
  ],
  "dniprovske": [
    34.41394,
    48.59042
  ],
  "билбасівка": [
    37.50185,
    48.83929
  ],
  "bylbasivka": [
    37.50185,
    48.83929
  ],
  "любашівка": [
    30.25209,
    47.83387
  ],
  "liubashivka": [
    30.25209,
    47.83387
  ],
  "новомиколаївка": [
    35.89886,
    47.97146
  ],
  "novomykolaivka": [
    32.73427,
    46.229
  ],
  "вільшани": [
    35.88233,
    50.0544
  ],
  "vilshany": [
    35.88233,
    50.0544
  ],
  "урожайне": [
    33.381176,
    46.968994
  ],
  "urozhaine": [
    36.81876,
    47.75143
  ],
  "березнегувате": [
    32.85098,
    47.30872
  ],
  "bereznehuvate": [
    32.85098,
    47.30872
  ],
  "лиманка": [
    30.67736,
    46.38564
  ],
  "lymanka": [
    30.67736,
    46.38564
  ],
  "барабой": [
    30.51368,
    46.28769
  ],
  "baraboi": [
    30.51368,
    46.28769
  ],
  "санжійка": [
    30.60897,
    46.22882
  ],
  "sanzhiika": [
    30.60897,
    46.22882
  ],
  "грибівка": [
    30.5606,
    46.20933
  ],
  "hrybivka": [
    30.5606,
    46.20933
  ],
  "роксолани": [
    30.4568,
    46.17608
  ],
  "roksolany": [
    30.4568,
    46.17608
  ],
  "шабо": [
    30.38567,
    46.12657
  ],
  "shabo": [
    30.38567,
    46.12657
  ],
  "кароліно-бугаз": [
    30.53068,
    46.14439
  ],
  "karolino-buhaz": [
    30.53068,
    46.14439
  ],
  "молодіжне": [
    30.6094472,
    46.3314744
  ],
  "molodizhne": [
    33.4305,
    49.1504
  ],
  "великодолинське": [
    30.57902,
    46.34642
  ],
  "velykodolynske": [
    30.57902,
    46.34642
  ],
  "великий дальник": [
    30.56285,
    46.47212
  ],
  "velykyi dalnyk": [
    30.56285,
    46.47212
  ],
  "великий бурлук": [
    37.38358,
    50.06135
  ],
  "velykyi burluk": [
    37.38358,
    50.06135
  ],
  "люботин": [
    35.92907,
    49.94691
  ],
  "liubotyn": [
    35.92907,
    49.94691
  ],
  "слобожанське": [
    36.52172,
    49.59054
  ],
  "slobozhanske": [
    36.52172,
    49.59054
  ],
  "зміїв": [
    36.36207,
    49.69689
  ],
  "zmiiv": [
    36.36207,
    49.69689
  ],
  "нова водолага": [
    35.8601,
    49.71875
  ],
  "nova vodolaha": [
    35.8601,
    49.71875
  ],
  "барвінкове": [
    37.02257,
    48.9052
  ],
  "barvinkove": [
    37.02257,
    48.9052
  ],
  "валки": [
    35.61393,
    49.83701
  ],
  "valky": [
    35.61393,
    49.83701
  ],
  "зіньків": [
    34.35952,
    50.20987
  ],
  "zinkiv": [
    34.35952,
    50.20987
  ],
  "заводське": [
    33.40118,
    50.40065
  ],
  "zavodske": [
    33.40118,
    50.40065
  ],
  "солоницівка": [
    36.03464,
    49.99682
  ],
  "solonytsivka": [
    36.03464,
    49.99682
  ],
  "котельва": [
    34.74697,
    50.06849
  ],
  "kotelva": [
    34.74697,
    50.06849
  ],
  "машівка": [
    34.87157,
    49.44407
  ],
  "mashivka": [
    34.87157,
    49.44407
  ],
  "чутове": [
    35.15747,
    49.71414
  ],
  "chutove": [
    35.15747,
    49.71414
  ],
  "скороходове": [
    35.07407,
    49.77437
  ],
  "skorokhodove": [
    35.07407,
    49.77437
  ],
  "ромодан": [
    33.32626,
    49.99135
  ],
  "romodan": [
    33.32626,
    49.99135
  ],
  "градизьк": [
    33.13941,
    49.23943
  ],
  "hradyzk": [
    33.13941,
    49.23943
  ],
  "комишня": [
    33.6831,
    50.18643
  ],
  "komyshnia": [
    33.6831,
    50.18643
  ],
  "наливайківка": [
    29.72067,
    50.48491
  ],
  "nalyvaikivka": [
    29.72067,
    50.48491
  ],
  "ходорів": [
    24.31294,
    49.40738
  ],
  "khodoriv": [
    24.31294,
    49.40738
  ],
  "чигирин": [
    32.66082,
    49.08045
  ],
  "chyhyryn": [
    32.66082,
    49.08045
  ],
  "жовті води": [
    33.49743,
    48.34518
  ],
  "zhovti vody": [
    33.49743,
    48.34518
  ],
  "близнюки": [
    36.55368,
    48.85632
  ],
  "blyzniuky": [
    36.55368,
    48.85632
  ],
  "українка": [
    30.74349,
    50.15309
  ],
  "ukrainka": [
    30.74349,
    50.15309
  ],
  "оржиця": [
    32.39398,
    50.10826
  ],
  "orzhytsia": [
    32.39398,
    50.10826
  ],
  "солончаки": [
    31.81824,
    46.64388
  ],
  "solonchaky": [
    31.81824,
    46.64388
  ],
  "есхар": [
    36.59025,
    49.79736
  ],
  "eskhar": [
    36.59025,
    49.79736
  ],
  "тернувате": [
    36.12973,
    47.82995
  ],
  "ternuvate": [
    36.12973,
    47.82995
  ],
  "вигода": [
    30.40325,
    46.61662
  ],
  "vyhoda": [
    30.40325,
    46.61662
  ],
  "єгорівка": [
    30.4029,
    46.72059
  ],
  "yehorivka": [
    30.4029,
    46.72059
  ],
  "гаврилівка": [
    30.206909,
    50.674782
  ],
  "havrylivka": [
    34.70785,
    47.07117
  ],
  "печеніги": [
    36.9386,
    49.86931
  ],
  "pechenihy": [
    36.9386,
    49.86931
  ],
  "архангельське": [
    33.40506,
    47.43329
  ],
  "arkhanhelske": [
    33.40506,
    47.43329
  ],
  "фонтанка": [
    30.85916,
    46.56864
  ],
  "fontanka": [
    30.85916,
    46.56864
  ],
  "коблеве": [
    31.20804,
    46.66499
  ],
  "kobleve": [
    31.20804,
    46.66499
  ],
  "розумівка": [
    35.13938,
    47.75392
  ],
  "rozumivka": [
    35.13938,
    47.75392
  ],
  "просяна": [
    36.37175,
    48.11368
  ],
  "prosiana": [
    36.37175,
    48.11368
  ],
  "велика олександрівка": [
    33.29059,
    47.31888
  ],
  "velyka oleksandrivka": [
    33.29059,
    47.31888
  ],
  "старий салтів": [
    36.78508,
    50.07155
  ],
  "staryi saltiv": [
    36.78508,
    50.07155
  ],
  "божедарівка": [
    34.11207,
    48.35687
  ],
  "bozhedarivka": [
    34.11207,
    48.35687
  ],
  "новоолександрівка": [
    35.36739,
    47.751041
  ],
  "novooleksandrivka": [
    39.63714,
    48.26194
  ],
  "степногірськ": [
    35.36399,
    47.59015
  ],
  "stepnohirsk": [
    35.36399,
    47.59015
  ],
  "річне": [
    35.31986,
    47.67406
  ],
  "richne": [
    35.31986,
    47.67406
  ],
  "слатине": [
    36.15376,
    50.21041
  ],
  "slatyne": [
    36.15376,
    50.21041
  ],
  "прудянка": [
    36.16835,
    50.23606
  ],
  "prudianka": [
    36.16835,
    50.23606
  ],
  "зноб-новгородське": [
    33.6016,
    52.26291
  ],
  "znob-novgorodske": [
    33.6016,
    52.26291
  ],
  "південне (южне)": [
    31.10182,
    46.62472
  ],
  "pivdenne (yuzhne)": [
    31.10182,
    46.62472
  ],
  "південноукраїнськ (южноукраїнськ)": [
    31.17513,
    47.82879
  ],
  "pivdennoukrayinsk (yuzhnoukrayinsk)": [
    31.17513,
    47.82879
  ],
  "чистякове": [
    38.59685,
    48.03876
  ],
  "chistyakove": [
    38.59685,
    48.03876
  ],
  "мігове": [
    25.37574,
    48.15612
  ],
  "mihove": [
    25.37574,
    48.15612
  ],
  "чабанка": [
    30.706,
    46.575
  ],
  "chabanka": [
    30.706,
    46.575
  ],
  "українка київська": [
    30.74349,
    50.15309
  ],
  "ukrainka kyiv": [
    30.74349,
    50.15309
  ],
  "українка крим": [
    34.1407,
    44.8865
  ],
  "ukrainka crimea": [
    34.1407,
    44.8865
  ],
  "івано-франківськ івано-франківська": [
    24.71248,
    48.92312
  ],
  "богородчани івано-франківська": [
    24.53728,
    48.80812
  ],
  "бурштин івано-франківська": [
    24.63339,
    49.25193
  ],
  "галич івано-франківська": [
    24.72748,
    49.12374
  ],
  "рогатин івано-франківська": [
    24.61103,
    49.41043
  ],
  "тлумач івано-франківська": [
    25.00385,
    48.86519
  ],
  "верховина івано-франківська": [
    24.82986,
    48.15536
  ],
  "долина івано-франківська": [
    23.96558,
    48.97158
  ],
  "калуш івано-франківська": [
    24.37206,
    49.02398
  ],
  "рожнятів івано-франківська": [
    24.15627,
    48.93975
  ],
  "городенка івано-франківська": [
    25.5033,
    48.669
  ],
  "коломия івано-франківська": [
    25.03712,
    48.52496
  ],
  "снятин івано-франківська": [
    25.55994,
    48.44883
  ],
  "косів івано-франківська": [
    25.09109,
    48.32051
  ],
  "надвірна івано-франківська": [
    24.5714,
    48.63659
  ],
  "яремче івано-франківська": [
    24.55335,
    48.44886
  ],
  "іваничі волинська": [
    24.35634,
    50.63592
  ],
  "володимир волинська": [
    24.32119,
    50.85033
  ],
  "локачі волинська": [
    24.64872,
    50.73898
  ],
  "нововолинськ волинська": [
    24.15976,
    50.72949
  ],
  "камінь-каширський волинська": [
    24.96276,
    51.62514
  ],
  "любешів волинська": [
    25.51317,
    51.76505
  ],
  "маневичі волинська": [
    25.53063,
    51.29385
  ],
  "голоби волинська": [
    25.00882,
    51.08798
  ],
  "ковель волинська": [
    24.70077,
    51.21548
  ],
  "любомль волинська": [
    24.03225,
    51.22536
  ],
  "ратне волинська": [
    24.52644,
    51.66919
  ],
  "стара вижівка волинська": [
    24.43958,
    51.43661
  ],
  "турійськ волинська": [
    24.5262,
    51.08724
  ],
  "шацьк волинська": [
    23.93589,
    51.49929
  ],
  "горохів волинська": [
    24.75681,
    50.50224
  ],
  "ківерці волинська": [
    25.45596,
    50.83516
  ],
  "луцьк волинська": [
    25.35024,
    50.75784
  ],
  "рожище волинська": [
    25.27121,
    50.91632
  ],
  "іллінці вінницька": [
    29.20589,
    49.10544
  ],
  "вінниця вінницька": [
    28.46871,
    49.2322
  ],
  "гнівань вінницька": [
    28.33785,
    49.0939
  ],
  "липовець вінницька": [
    29.05669,
    49.22776
  ],
  "літин вінницька": [
    28.08698,
    49.32711
  ],
  "немирів вінницька": [
    28.83781,
    48.97002
  ],
  "оратів вінницька": [
    29.52889,
    49.18594
  ],
  "погребище вінницька": [
    29.25988,
    49.48508
  ],
  "тиврів вінницька": [
    28.50044,
    49.01206
  ],
  "бершадь вінницька": [
    29.51463,
    48.36354
  ],
  "гайсин вінницька": [
    29.37917,
    48.81294
  ],
  "ладижин вінницька": [
    29.23636,
    48.68437
  ],
  "теплик вінницька": [
    29.74482,
    48.66538
  ],
  "тростянець вінницька": [
    29.2226589,
    48.51227
  ],
  "чечельник вінницька": [
    29.36469,
    48.21558
  ],
  "бар вінницька": [
    27.67404,
    49.07362
  ],
  "жмеринка вінницька": [
    28.11405,
    49.03523
  ],
  "шаргород вінницька": [
    28.08459,
    48.73562
  ],
  "могилів-подільський вінницька": [
    27.79975,
    48.44278
  ],
  "муровані курилівці вінницька": [
    27.53084,
    48.71813
  ],
  "чернівці вінницька": [
    28.1221153,
    48.5406973
  ],
  "ямпіль вінницька": [
    28.28141,
    48.24056
  ],
  "крижопіль вінницька": [
    28.86766,
    48.3821
  ],
  "піщанка вінницька": [
    28.88056,
    48.21249
  ],
  "томашпіль вінницька": [
    28.51295,
    48.53695
  ],
  "тульчин вінницька": [
    28.86848,
    48.67397
  ],
  "калинівка вінницька": [
    28.51541,
    49.46129
  ],
  "козятин вінницька": [
    28.8354279,
    49.7195867
  ],
  "хмільник вінницька": [
    27.95682,
    49.5581
  ],
  "дніпро дніпропетровська": [
    35.04066,
    48.46664
  ],
  "петриківка дніпропетровська": [
    34.61901,
    48.7264
  ],
  "солоне дніпропетровська": [
    34.87585,
    48.20907
  ],
  "царичанка дніпропетровська": [
    34.48601,
    48.94186
  ],
  "божедарівка дніпропетровська": [
    34.11207,
    48.35687
  ],
  "верхньодніпровськ дніпропетровська": [
    34.3262,
    48.65557
  ],
  "верхівцеве дніпропетровська": [
    34.24003,
    48.48127
  ],
  "вільногірськ дніпропетровська": [
    34.01708,
    48.48416
  ],
  "жовті води дніпропетровська": [
    33.49743,
    48.34518
  ],
  "кам'янське дніпропетровська": [
    34.60617,
    48.51716
  ],
  "кринички дніпропетровська": [
    34.46202,
    48.37438
  ],
  "п'ятихатки дніпропетровська": [
    33.7056731,
    48.4124572
  ],
  "апостолове дніпропетровська": [
    33.71952,
    47.65983
  ],
  "велика долина дніпропетровська": [
    33.71976,
    47.53364
  ],
  "зеленодольськ дніпропетровська": [
    33.65905,
    47.55498
  ],
  "кривий ріг дніпропетровська": [
    33.38044,
    47.90966
  ],
  "мар'янське дніпропетровська": [
    33.9235739,
    47.5522624
  ],
  "софіївка дніпропетровська": [
    33.8668627,
    48.0482032
  ],
  "широке дніпропетровська": [
    33.26147,
    47.6855
  ],
  "марганець дніпропетровська": [
    34.6245,
    47.63088
  ],
  "нікополь дніпропетровська": [
    34.39126,
    47.56826
  ],
  "покров дніпропетровська": [
    34.11488,
    47.65361
  ],
  "томаківка дніпропетровська": [
    34.74324,
    47.81081
  ],
  "червоногригорівка дніпропетровська": [
    34.52453,
    47.62161
  ],
  "червоногригорівка": [
    34.52453,
    47.62161
  ],
  "васильківка дніпропетровська": [
    36.02214,
    48.20824
  ],
  "павлоград дніпропетровська": [
    35.86878,
    48.53214
  ],
  "юріївка дніпропетровська": [
    36.015,
    48.73556
  ],
  "магдалинівка дніпропетровська": [
    34.91395,
    48.91204
  ],
  "самар дніпропетровська": [
    35.2589,
    48.62893
  ],
  "межова дніпропетровська": [
    36.73178,
    48.25418
  ],
  "новопавлівка дніпропетровська": [
    34.43376,
    47.57563
  ],
  "петропавлівка дніпропетровська": [
    36.43061,
    48.46353
  ],
  "покровське дніпропетровська": [
    36.23446,
    47.98126
  ],
  "просяна дніпропетровська": [
    36.37175,
    48.11368
  ],
  "синельникове дніпропетровська": [
    35.52612,
    48.32362
  ],
  "чаплине дніпропетровська": [
    36.23007,
    48.12827
  ],
  "шахтарське дніпропетровська": [
    36.39637,
    48.3479
  ],
  "бахмут донецька": [
    37.99886,
    48.59419
  ],
  "світлодарськ донецька": [
    38.22331,
    48.43374
  ],
  "соледар донецька": [
    38.07098,
    48.6921
  ],
  "сіверськ донецька": [
    38.09683,
    48.86476
  ],
  "торецьк донецька": [
    37.8478,
    48.39477
  ],
  "часів яр донецька": [
    37.83409,
    48.58768
  ],
  "велика новосілка донецька": [
    36.83627,
    47.84281
  ],
  "вугледар донецька": [
    37.24999,
    47.77973
  ],
  "єнакієве донецька": [
    38.20403,
    48.23857
  ],
  "горлівка донецька": [
    38.01709,
    48.29986
  ],
  "сніжне донецька": [
    38.76205,
    48.02328
  ],
  "чистякове донецька": [
    38.59685,
    48.03876
  ],
  "шахтарськ донецька": [
    38.43826,
    48.05657
  ],
  "донецьк донецька": [
    37.80224,
    48.023
  ],
  "макіївка донецька": [
    37.92576,
    48.04782
  ],
  "харцизьк донецька": [
    38.14025,
    48.04277
  ],
  "кальміуське донецька": [
    37.7925,
    47.242
  ],
  "билбасівка донецька": [
    37.50185,
    48.83929
  ],
  "дружківка донецька": [
    37.52537,
    48.61995
  ],
  "костянтинівка донецька": [
    37.6923755,
    48.5348985
  ],
  "краматорськ донецька": [
    37.56779,
    48.73106
  ],
  "лиман донецька": [
    37.80843,
    48.99012
  ],
  "миколаївка донецька": [
    37.76835,
    48.86193
  ],
  "новодонецьке донецька": [
    36.98276,
    48.63512
  ],
  "рай-олександрівка донецька": [
    37.8512,
    48.81041
  ],
  "святогірськ донецька": [
    37.57194,
    49.04101
  ],
  "слов'янськ донецька": [
    37.59739,
    48.84974
  ],
  "маріуполь донецька": [
    37.54131,
    47.09514
  ],
  "авдіївка донецька": [
    37.75008,
    48.14019
  ],
  "добропілля донецька": [
    37.04866,
    48.42115
  ],
  "курахове донецька": [
    37.28069,
    47.9847
  ],
  "мар'їнка донецька": [
    37.50544,
    47.94527
  ],
  "мирноград донецька": [
    37.26513,
    48.3099
  ],
  "покровськ донецька": [
    37.17706,
    48.28014
  ],
  "андрушівка житомирська": [
    29.01883,
    50.01922
  ],
  "бердичів житомирська": [
    28.58236,
    49.89421
  ],
  "ружин житомирська": [
    29.21874,
    49.72175
  ],
  "брусилів житомирська": [
    29.52008,
    50.28226
  ],
  "житомир житомирська": [
    28.67913,
    50.26235
  ],
  "коростишів житомирська": [
    29.05774,
    50.31686
  ],
  "любар житомирська": [
    27.75108,
    49.92322
  ],
  "озерне житомирська": [
    28.73384,
    50.17816
  ],
  "попільня житомирська": [
    29.45265,
    49.9532
  ],
  "пулини житомирська": [
    28.27,
    50.46745
  ],
  "радомишль житомирська": [
    29.23003,
    50.4962
  ],
  "романів житомирська": [
    27.9314,
    50.14733
  ],
  "хорошів житомирська": [
    28.44489,
    50.59484
  ],
  "черняхів житомирська": [
    28.66717,
    50.45412
  ],
  "чуднів житомирська": [
    28.12058,
    50.05255
  ],
  "ємільчине житомирська": [
    27.80198,
    50.87185
  ],
  "баранівка житомирська": [
    27.6622,
    50.29691
  ],
  "звягель житомирська": [
    27.60884,
    50.59141
  ],
  "іршанськ житомирська": [
    28.72119,
    50.75317
  ],
  "коростень житомирська": [
    28.63859,
    50.9512
  ],
  "лугини житомирська": [
    28.39876,
    51.07899
  ],
  "малин житомирська": [
    29.24225,
    50.76756
  ],
  "народичі житомирська": [
    29.08341,
    51.20304
  ],
  "овруч житомирська": [
    28.80165,
    51.3274
  ],
  "олевськ житомирська": [
    27.65228,
    51.22482
  ],
  "берегове закарпатська": [
    22.64453,
    48.20514
  ],
  "виноградів закарпатська": [
    23.03623,
    48.14126
  ],
  "воловець закарпатська": [
    23.1851,
    48.7109
  ],
  "мукачево закарпатська": [
    22.718,
    48.44248
  ],
  "свалява закарпатська": [
    22.98673,
    48.54735
  ],
  "рахів закарпатська": [
    24.20314,
    48.05472
  ],
  "тячів закарпатська": [
    23.57168,
    48.01092
  ],
  "великий березний закарпатська": [
    22.46121,
    48.8934
  ],
  "перечин закарпатська": [
    22.47718,
    48.73494
  ],
  "ужгород закарпатська": [
    22.2947,
    48.6242
  ],
  "іршава закарпатська": [
    23.04065,
    48.31227
  ],
  "міжгір'я закарпатська": [
    23.5009289,
    48.5281184
  ],
  "хуст закарпатська": [
    23.29791,
    48.17193
  ],
  "бердянськ запорізька": [
    36.78815,
    46.75578
  ],
  "приморськ запорізька": [
    36.34599,
    46.73415
  ],
  "чернігівка запорізька": [
    36.21648,
    47.19451
  ],
  "велика білозерка запорізька": [
    34.68457,
    47.27572
  ],
  "енергодар запорізька": [
    34.66199,
    47.49048
  ],
  "кам'янка-дніпровська запорізька": [
    34.41026,
    47.49629
  ],
  "малокатеринівка запорізька": [
    35.25733,
    47.6557
  ],
  "михайлівка запорізька": [
    35.2217134,
    47.2657187
  ],
  "приморське запорізька": [
    35.29074,
    47.6449
  ],
  "степногірськ запорізька": [
    35.36399,
    47.59015
  ],
  "балабине запорізька": [
    35.21361,
    47.73686
  ],
  "біленьке запорізька": [
    35.030251,
    47.621609
  ],
  "вільнянськ запорізька": [
    35.44034,
    47.94768
  ],
  "запоріжжя запорізька": [
    35.11714,
    47.85167
  ],
  "комишуваха запорізька": [
    35.52405,
    47.71491
  ],
  "кушугум запорізька": [
    35.21644,
    47.70963
  ],
  "новомиколаївка запорізька": [
    35.89886,
    47.97146
  ],
  "новомихайлівка запорізька": [
    35.529781,
    47.838589
  ],
  "новоолександрівка запорізька": [
    35.36739,
    47.751041
  ],
  "розумівка запорізька": [
    35.13938,
    47.75392
  ],
  "річне запорізька": [
    35.31986,
    47.67406
  ],
  "таврійське запорізька": [
    35.69733,
    47.652512
  ],
  "тернувате запорізька": [
    36.12973,
    47.82995
  ],
  "веселе запорізька": [
    34.91843,
    47.00973
  ],
  "мелітополь запорізька": [
    35.38196,
    46.84735
  ],
  "приазовське запорізька": [
    35.64082,
    46.73123
  ],
  "якимівка запорізька": [
    35.16334,
    46.7011
  ],
  "більмак запорізька": [
    36.65331,
    47.35914
  ],
  "гуляйполе запорізька": [
    36.2656849,
    47.6655382
  ],
  "кам'янка запорізька": [
    36.65108,
    47.3624
  ],
  "оріхів запорізька": [
    35.78333,
    47.57613
  ],
  "пологи запорізька": [
    36.25463,
    47.47865
  ],
  "розівка запорізька": [
    37.07078,
    47.3954
  ],
  "токмак запорізька": [
    35.70836,
    47.25554
  ],
  "бориспіль київська": [
    30.95263,
    50.35051
  ],
  "переяслав київська": [
    31.44969,
    50.06739
  ],
  "яготин київська": [
    31.76343,
    50.27535
  ],
  "баришівка київська": [
    31.32005,
    50.35925
  ],
  "бровари київська": [
    30.79106,
    50.51097
  ],
  "велика димерка київська": [
    30.9016229,
    50.5913563
  ],
  "велика димерка": [
    30.9016229,
    50.5913563
  ],
  "зазим'я київська": [
    30.67319,
    50.56923
  ],
  "згурівка київська": [
    31.77687,
    50.50193
  ],
  "семиполки київська": [
    30.93441,
    50.72627
  ],
  "ірпінь київська": [
    30.24037,
    50.52201
  ],
  "бородянка київська": [
    29.92329,
    50.64306
  ],
  "буча київська": [
    30.20879,
    50.54741
  ],
  "білогородка київська": [
    30.22726,
    50.3898
  ],
  "вишневе київська": [
    30.36809,
    50.38834
  ],
  "ворзель київська": [
    30.15305,
    50.5444
  ],
  "гаврилівка київська": [
    30.206909,
    50.674782
  ],
  "гостомель київська": [
    30.2651,
    50.56841
  ],
  "макарів київська": [
    29.81455,
    50.45735
  ],
  "наливайківка київська": [
    29.72067,
    50.48491
  ],
  "біла церква київська": [
    30.1165,
    49.7994
  ],
  "володарка київська": [
    29.91023,
    49.52501
  ],
  "рокитне київська": [
    30.473034,
    49.6867282
  ],
  "сквира київська": [
    29.66353,
    49.73401
  ],
  "ставище київська": [
    30.19102,
    49.3915
  ],
  "тараща київська": [
    30.49615,
    49.55719
  ],
  "тетіїв київська": [
    29.66933,
    49.37019
  ],
  "узин київська": [
    30.42487,
    49.82482
  ],
  "іванків київська": [
    29.90205,
    50.93953
  ],
  "вишгород київська": [
    30.48566,
    50.58312
  ],
  "димер київська": [
    30.30357,
    50.78579
  ],
  "поліське київська": [
    29.38896,
    51.240486
  ],
  "славутич київська": [
    30.71806,
    51.5225
  ],
  "богуслав київська": [
    30.87407,
    49.54637
  ],
  "васильків київська": [
    30.31189,
    50.18023
  ],
  "кагарлик київська": [
    30.82327,
    49.859
  ],
  "миронівка київська": [
    30.98225,
    49.66007
  ],
  "обухів київська": [
    30.63329,
    50.11632
  ],
  "ржищів київська": [
    31.0424,
    49.96934
  ],
  "хотів київська": [
    30.46836,
    50.33069
  ],
  "боярка київська": [
    30.2847595,
    50.3356709
  ],
  "гатне київська": [
    30.37497,
    50.35444
  ],
  "калинівка київська": [
    30.2261781,
    50.2257254
  ],
  "фастів київська": [
    29.91963,
    50.07796
  ],
  "чабани київська": [
    30.42856,
    50.34128
  ],
  "євпаторія крим": [
    33.36655,
    45.20091
  ],
  "бахчисарай крим": [
    33.85782,
    44.75525
  ],
  "білогірськ крим": [
    34.60386,
    45.05679
  ],
  "джанкой крим": [
    34.39273,
    45.7131
  ],
  "керч крим": [
    36.47542,
    45.35675
  ],
  "севастополь крим": [
    33.52134,
    44.60795
  ],
  "курман крим": [
    34.30134,
    45.50271
  ],
  "яни капу крим": [
    33.79261,
    45.95547
  ],
  "сімферополь крим": [
    34.11079,
    44.95719
  ],
  "феодосія крим": [
    35.38153,
    45.03199
  ],
  "ялта крим": [
    34.16624,
    44.50218
  ],
  "благовіщенське кіровоградська": [
    30.23619,
    48.32822
  ],
  "вільшанка кіровоградська": [
    30.87285,
    48.23421
  ],
  "гайворон кіровоградська": [
    29.8593204,
    48.3406905
  ],
  "голованівськ кіровоградська": [
    30.45947,
    48.3874
  ],
  "новоархангельськ кіровоградська": [
    30.80705,
    48.66187
  ],
  "бобринець кіровоградська": [
    32.1655,
    48.05674
  ],
  "долинська кіровоградська": [
    32.77691,
    48.11725
  ],
  "знам'янка кіровоградська": [
    32.6659476,
    48.7199609
  ],
  "компаніївка кіровоградська": [
    32.20138,
    48.25022
  ],
  "кропивницький кіровоградська": [
    32.26618,
    48.50834
  ],
  "новгородка кіровоградська": [
    32.65469,
    48.36089
  ],
  "олександрівка кіровоградська": [
    32.23968,
    48.968
  ],
  "устинівка кіровоградська": [
    32.53938,
    47.95619
  ],
  "добровеличківка кіровоградська": [
    31.18039,
    48.38939
  ],
  "мала виска кіровоградська": [
    31.63231,
    48.64694
  ],
  "новомиргород кіровоградська": [
    31.64904,
    48.79345
  ],
  "новоукраїнка кіровоградська": [
    31.522047,
    48.3250616
  ],
  "олександрія кіровоградська": [
    33.11761,
    48.67466
  ],
  "онуфріївка кіровоградська": [
    33.44954,
    48.89917
  ],
  "петрове кіровоградська": [
    33.2653,
    48.33809
  ],
  "світловодськ кіровоградська": [
    33.2458,
    49.06287
  ],
  "алчевськ луганська": [
    38.79744,
    48.46906
  ],
  "брянка луганська": [
    38.67222,
    48.511
  ],
  "кадіївка луганська": [
    38.64352,
    48.56818
  ],
  "довжанськ луганська": [
    39.64744,
    48.07615
  ],
  "луганськ луганська": [
    39.30553,
    48.56814
  ],
  "антрацит луганська": [
    39.08863,
    48.11638
  ],
  "ровеньки луганська": [
    39.37696,
    48.08277
  ],
  "хрустальний луганська": [
    38.92369,
    48.14241
  ],
  "рубіжне луганська": [
    38.37972,
    49.00849
  ],
  "старобільськ луганська": [
    38.9075,
    49.27881
  ],
  "золоте луганська": [
    38.51512,
    48.69516
  ],
  "лисичанськ луганська": [
    38.42088,
    48.91211
  ],
  "сіверськодонецьк луганська": [
    38.48754,
    48.94414
  ],
  "новоайдар луганська": [
    39.00376,
    48.96288
  ],
  "дрогобич львівська": [
    23.51121,
    49.35196
  ],
  "буськ львівська": [
    24.61227,
    49.96548
  ],
  "золочів львівська": [
    24.90376,
    49.8074
  ],
  "бібрка львівська": [
    24.29369,
    49.63921
  ],
  "городок львівська": [
    23.6465626,
    49.784596
  ],
  "львів львівська": [
    24.02324,
    49.83826
  ],
  "самбір львівська": [
    23.20133,
    49.51624
  ],
  "стрий львівська": [
    23.84845,
    49.26103
  ],
  "ходорів львівська": [
    24.31294,
    49.40738
  ],
  "добротвір львівська": [
    24.3835,
    50.20526
  ],
  "шептицький львівська": [
    24.23935,
    50.39403
  ],
  "яворів львівська": [
    23.38355,
    49.93774
  ],
  "баштанка миколаївська": [
    32.43444,
    47.40528
  ],
  "березнегувате миколаївська": [
    32.85098,
    47.30872
  ],
  "новий буг миколаївська": [
    32.51214,
    47.69057
  ],
  "снігурівка миколаївська": [
    32.8197,
    47.07651
  ],
  "єланець миколаївська": [
    31.85222,
    47.69521
  ],
  "вознесенськ миколаївська": [
    31.33602,
    47.56218
  ],
  "південноукраїнськ (южноукраїнськ) миколаївська": [
    31.17513,
    47.82879
  ],
  "березанка миколаївська": [
    31.3874915,
    46.8544054
  ],
  "березанка": [
    31.3874915,
    46.8544054
  ],
  "дмитрівка миколаївська": [
    31.740156,
    46.631561
  ],
  "дніпровське миколаївська": [
    31.8741042,
    46.6358818
  ],
  "коблеве миколаївська": [
    31.20804,
    46.66499
  ],
  "куцуруб миколаївська": [
    31.61825,
    46.65277
  ],
  "миколаїв миколаївська": [
    31.9939666,
    46.9758615
  ],
  "очаків миколаївська": [
    31.54505,
    46.61472
  ],
  "рибаківка миколаївська": [
    31.3511191,
    46.6195586
  ],
  "рибаківка": [
    31.3511191,
    46.6195586
  ],
  "солончаки миколаївська": [
    31.81824,
    46.64388
  ],
  "арбузинка миколаївська": [
    31.31701,
    47.90791
  ],
  "криве озеро миколаївська": [
    30.34701,
    47.94763
  ],
  "первомайськ миколаївська": [
    30.8475997,
    48.045745
  ],
  "ізмаїл одеська": [
    28.83751,
    45.35058
  ],
  "вилкове одеська": [
    29.5869,
    45.40279
  ],
  "кілія одеська": [
    29.26396,
    45.44445
  ],
  "березівка одеська": [
    30.90943,
    47.20037
  ],
  "арциз одеська": [
    29.43286,
    45.98526
  ],
  "болград одеська": [
    28.61811,
    45.67786
  ],
  "білгород-дністровський одеська": [
    30.34827,
    46.19484
  ],
  "затока одеська": [
    30.46265,
    46.07016
  ],
  "кароліно-бугаз одеська": [
    30.53068,
    46.14439
  ],
  "сарата одеська": [
    29.66444,
    46.02056
  ],
  "сергіївка одеська": [
    30.37273,
    46.02756
  ],
  "татарбунари одеська": [
    29.61123,
    45.83861
  ],
  "тузли одеська": [
    30.09773,
    45.86504
  ],
  "шабо одеська": [
    30.38567,
    46.12657
  ],
  "єгорівка одеська": [
    30.4029,
    46.72059
  ],
  "барабой одеська": [
    30.51368,
    46.28769
  ],
  "болгарка одеська": [
    30.46148,
    46.6912
  ],
  "білярі одеська": [
    31.031178,
    46.6227
  ],
  "білярі": [
    31.031178,
    46.6227
  ],
  "біляївка одеська": [
    30.2120913,
    46.4844245
  ],
  "великий дальник одеська": [
    30.56285,
    46.47212
  ],
  "великодолинське одеська": [
    30.57902,
    46.34642
  ],
  "вигода одеська": [
    30.40325,
    46.61662
  ],
  "грибівка одеська": [
    30.5606,
    46.20933
  ],
  "дальник одеська": [
    30.52982,
    46.22569
  ],
  "дачне одеська": [
    30.54747,
    46.58226
  ],
  "доброслав одеська": [
    30.94518,
    46.82095
  ],
  "лиманка одеська": [
    30.67736,
    46.38564
  ],
  "маяки одеська": [
    30.2750575,
    46.416632
  ],
  "молодіжне одеська": [
    30.6094472,
    46.3314744
  ],
  "овідіополь одеська": [
    30.43746,
    46.24721
  ],
  "одеса одеська": [
    30.74383,
    46.48572
  ],
  "олександрівка одеська": [
    30.6312513,
    46.3279486
  ],
  "південне (южне) одеська": [
    31.10182,
    46.62472
  ],
  "роксолани одеська": [
    30.4568,
    46.17608
  ],
  "санжійка одеська": [
    30.60897,
    46.22882
  ],
  "усатове одеська": [
    30.64951,
    46.52893
  ],
  "фонтанка одеська": [
    30.85916,
    46.56864
  ],
  "чабанка одеська": [
    30.706,
    46.575
  ],
  "чорноморськ одеська": [
    30.65529,
    46.29914
  ],
  "чорноморське одеська": [
    30.9334115,
    46.5849122
  ],
  "любашівка одеська": [
    30.25209,
    47.83387
  ],
  "подільськ одеська": [
    29.53074,
    47.74988
  ],
  "лиманське одеська": [
    29.97231,
    46.67952
  ],
  "роздільна одеська": [
    30.07091,
    46.85479
  ],
  "глобине полтавська": [
    33.27555,
    49.37894
  ],
  "горішні плавні полтавська": [
    33.62926,
    49.00835
  ],
  "градизьк полтавська": [
    33.13941,
    49.23943
  ],
  "кременчук полтавська": [
    33.40484,
    49.06253
  ],
  "гребінка полтавська": [
    32.42966,
    50.12017
  ],
  "лубни полтавська": [
    32.99975,
    50.01413
  ],
  "оржиця полтавська": [
    32.39398,
    50.10826
  ],
  "пирятин полтавська": [
    32.5203,
    50.24388
  ],
  "хорол полтавська": [
    33.27184,
    49.78286
  ],
  "гадяч полтавська": [
    33.9950534,
    50.3701299
  ],
  "заводське полтавська": [
    33.40118,
    50.40065
  ],
  "комишня полтавська": [
    33.6831,
    50.18643
  ],
  "лохвиця полтавська": [
    33.27153,
    50.36444
  ],
  "миргород полтавська": [
    33.60861,
    49.96464
  ],
  "ромодан полтавська": [
    33.32626,
    49.99135
  ],
  "зіньків полтавська": [
    34.35952,
    50.20987
  ],
  "карлівка полтавська": [
    35.13493,
    49.45548
  ],
  "кобеляки полтавська": [
    34.20193,
    49.14936
  ],
  "котельва полтавська": [
    34.74697,
    50.06849
  ],
  "машівка полтавська": [
    34.87157,
    49.44407
  ],
  "нові санжари полтавська": [
    34.31496,
    49.33379
  ],
  "полтава полтавська": [
    34.55367,
    49.58925
  ],
  "решетилівка полтавська": [
    34.07896,
    49.563
  ],
  "скороходове полтавська": [
    35.07407,
    49.77437
  ],
  "чутове полтавська": [
    35.15747,
    49.71414
  ],
  "вараш рівненська": [
    25.85547,
    51.34038
  ],
  "дубно рівненська": [
    25.7624,
    50.40752
  ],
  "березне рівненська": [
    26.74618,
    51.00343
  ],
  "здолбунів рівненська": [
    26.24823,
    50.52205
  ],
  "корець рівненська": [
    27.15795,
    50.61921
  ],
  "костопіль рівненська": [
    26.44797,
    50.87732
  ],
  "острог рівненська": [
    26.52113,
    50.32897
  ],
  "рівне рівненська": [
    26.23695,
    50.62036
  ],
  "дубровиця рівненська": [
    26.56369,
    51.57076
  ],
  "рокитне рівненська": [
    27.21705,
    51.27891
  ],
  "сарни рівненська": [
    26.60693,
    51.33898
  ],
  "буринь сумська": [
    33.83338,
    51.19936
  ],
  "конотоп сумська": [
    33.2004,
    51.23251
  ],
  "кролевець сумська": [
    33.38044,
    51.55181
  ],
  "нова слобода сумська": [
    34.12868,
    51.37492
  ],
  "путивль сумська": [
    33.86885,
    51.33529
  ],
  "велика писарівка сумська": [
    35.48299,
    50.42335
  ],
  "охтирка сумська": [
    34.89468,
    50.30852
  ],
  "тростянець сумська": [
    34.96467,
    50.48046
  ],
  "липова долина сумська": [
    33.79154,
    50.56292
  ],
  "недригайлів сумська": [
    33.87848,
    50.83587
  ],
  "ромни сумська": [
    33.4952,
    50.74025
  ],
  "терни сумська": [
    33.98346,
    50.99407
  ],
  "терни": [
    33.98346,
    50.99407
  ],
  "іскрисківщина сумська": [
    34.38395,
    51.23877
  ],
  "атинське сумська": [
    34.26888,
    51.21882
  ],
  "басівка сумська": [
    35.087929,
    51.181141
  ],
  "будки сумська": [
    34.3338341,
    51.2343624
  ],
  "білопілля сумська": [
    34.31079,
    51.14747
  ],
  "велика чернеччина сумська": [
    34.92359,
    50.95458
  ],
  "верхня сироватка сумська": [
    34.95861,
    50.82902
  ],
  "волфине сумська": [
    34.46169,
    51.24139
  ],
  "ворожба сумська": [
    34.22665,
    51.17316
  ],
  "катеринівка сумська": [
    34.244041,
    50.734859
  ],
  "краснопілля сумська": [
    35.2563391,
    50.7712539
  ],
  "кіндратівка сумська": [
    34.77343,
    51.14326
  ],
  "лебедин сумська": [
    34.48258,
    50.58228
  ],
  "мезенівка сумська": [
    35.3134,
    50.63486
  ],
  "миколаївка сумська": [
    34.3729195,
    50.9395138
  ],
  "миропілля сумська": [
    35.24517,
    51.0244
  ],
  "могриця сумська": [
    35.11312,
    51.02912
  ],
  "ободи сумська": [
    34.62745,
    51.22236
  ],
  "павлівка сумська": [
    34.5162883,
    51.224559
  ],
  "рижівка сумська": [
    34.24895,
    51.25268
  ],
  "річки сумська": [
    34.4951996,
    51.1202488
  ],
  "річки": [
    34.4951996,
    51.1202488
  ],
  "степанівка сумська": [
    34.6422099,
    50.9417042
  ],
  "степанівка": [
    34.6422099,
    50.9417042
  ],
  "стецьківка сумська": [
    34.78849,
    51.01307
  ],
  "суми сумська": [
    34.79906,
    50.91741
  ],
  "токарі сумська": [
    34.902016,
    50.920043
  ],
  "токарі": [
    34.902016,
    50.920043
  ],
  "угроїди сумська": [
    35.27823,
    50.86293
  ],
  "хотінь сумська": [
    34.77302,
    51.07997
  ],
  "юнаківка сумська": [
    35.0385,
    51.12262
  ],
  "вороніж сумська": [
    33.45944,
    51.77572
  ],
  "глухів сумська": [
    33.91682,
    51.67982
  ],
  "есмань сумська": [
    34.06517,
    51.76966
  ],
  "зноб-новгородське сумська": [
    33.6016,
    52.26291
  ],
  "свеса сумська": [
    33.93383,
    51.95131
  ],
  "середина-буда сумська": [
    34.03613,
    52.18886
  ],
  "шалигине сумська": [
    34.12507,
    51.56988
  ],
  "шостка сумська": [
    33.47283,
    51.86434
  ],
  "ямпіль сумська": [
    33.778454,
    51.9481126
  ],
  "кременець тернопільська": [
    25.72787,
    50.09864
  ],
  "ланівці тернопільська": [
    26.09052,
    49.86103
  ],
  "шумськ тернопільська": [
    26.11792,
    50.11775
  ],
  "бережани тернопільська": [
    24.93686,
    49.44578
  ],
  "збараж тернопільська": [
    25.77925,
    49.66157
  ],
  "зборів тернопільська": [
    25.14019,
    49.66493
  ],
  "козова тернопільська": [
    25.14547,
    49.43206
  ],
  "підволочиськ тернопільська": [
    26.14401,
    49.53131
  ],
  "підгайці тернопільська": [
    25.1361578,
    49.2680238
  ],
  "теребовля тернопільська": [
    25.68886,
    49.29967
  ],
  "тернопіль тернопільська": [
    25.59067,
    49.55404
  ],
  "борщів тернопільська": [
    26.03171,
    48.80319
  ],
  "бучач тернопільська": [
    25.39496,
    49.06234
  ],
  "гусятин тернопільська": [
    26.20464,
    49.07123
  ],
  "заліщики тернопільська": [
    25.7317,
    48.64098
  ],
  "монастириська тернопільська": [
    25.17149,
    49.09063
  ],
  "чортків тернопільська": [
    25.79808,
    49.01701
  ],
  "ізюм харківська": [
    37.27679,
    49.20697
  ],
  "балаклія харківська": [
    36.8397826,
    49.4521336
  ],
  "барвінкове харківська": [
    37.02257,
    48.9052
  ],
  "борова харківська": [
    37.6253381,
    49.3799491
  ],
  "берестин харківська": [
    35.44485,
    49.3776
  ],
  "богодухів харківська": [
    35.52367,
    50.16147
  ],
  "валки харківська": [
    35.61393,
    49.83701
  ],
  "золочів харківська": [
    35.9824347,
    50.2790531
  ],
  "великий бурлук харківська": [
    37.38358,
    50.06135
  ],
  "колодязне харківська": [
    37.688599,
    50.007702
  ],
  "куп'янськ харківська": [
    37.61581,
    49.71003
  ],
  "приколотне харківська": [
    37.3498729,
    50.160627
  ],
  "приколотне": [
    37.3498729,
    50.160627
  ],
  "близнюки харківська": [
    36.55368,
    48.85632
  ],
  "златопіль харківська": [
    36.21848,
    49.37646
  ],
  "лозова харківська": [
    36.31412,
    48.89066
  ],
  "вільшани харківська": [
    35.88233,
    50.0544
  ],
  "дергачі харківська": [
    36.1209,
    50.10789
  ],
  "козача лопань харківська": [
    36.19823,
    50.33212
  ],
  "липці харківська": [
    36.42086,
    50.20919
  ],
  "люботин харківська": [
    35.92907,
    49.94691
  ],
  "мерефа харківська": [
    36.0567,
    49.82107
  ],
  "нова водолага харківська": [
    35.8601,
    49.71875
  ],
  "прудянка харківська": [
    36.16835,
    50.23606
  ],
  "пісочин харківська": [
    36.10262,
    49.9516
  ],
  "слатине харківська": [
    36.15376,
    50.21041
  ],
  "солоницівка харківська": [
    36.03464,
    49.99682
  ],
  "харків харківська": [
    36.25475,
    49.98177
  ],
  "циркуни харківська": [
    36.38724,
    50.08438
  ],
  "білий колодязь харківська": [
    37.11265,
    50.20412
  ],
  "вовчанськ харківська": [
    36.94108,
    50.29078
  ],
  "есхар харківська": [
    36.59025,
    49.79736
  ],
  "зміїв харківська": [
    36.36207,
    49.69689
  ],
  "коробочкине харківська": [
    36.81286,
    49.77626
  ],
  "печеніги харківська": [
    36.9386,
    49.86931
  ],
  "слобожанське харківська": [
    36.52172,
    49.59054
  ],
  "старий салтів харківська": [
    36.78508,
    50.07155
  ],
  "чугуїв харківська": [
    36.6865,
    49.83538
  ],
  "архангельське херсонська": [
    33.40506,
    47.43329
  ],
  "берислав херсонська": [
    33.42664,
    46.83851
  ],
  "велика олександрівка херсонська": [
    33.29059,
    47.31888
  ],
  "нововоронцовка херсонська": [
    33.92317,
    47.50499
  ],
  "осокорівка херсонська": [
    33.923,
    47.432
  ],
  "суханове херсонська": [
    33.53626,
    47.12841
  ],
  "урожайне херсонська": [
    33.381176,
    46.968994
  ],
  "генічеськ херсонська": [
    34.80861,
    46.16824
  ],
  "каховка херсонська": [
    33.47862,
    46.81601
  ],
  "нова каховка херсонська": [
    33.35591,
    46.75966
  ],
  "таврійськ херсонська": [
    33.41665,
    46.75432
  ],
  "чаплинка херсонська": [
    33.54087,
    46.36454
  ],
  "скадовськ херсонська": [
    32.90978,
    46.11313
  ],
  "антонівка херсонська": [
    32.73061,
    46.67666
  ],
  "білозерка херсонська": [
    32.44447,
    46.62651
  ],
  "зеленівка херсонська": [
    32.6496911,
    46.7175203
  ],
  "зеленівка": [
    32.6496911,
    46.7175203
  ],
  "музиківка херсонська": [
    32.5640748,
    46.7536821
  ],
  "музиківка": [
    32.5640748,
    46.7536821
  ],
  "олександрівка херсонська": [
    32.1118946,
    46.6139617
  ],
  "олешки херсонська": [
    32.72426,
    46.62553
  ],
  "херсон херсонська": [
    32.61458,
    46.63695
  ],
  "чорнобаївка херсонська": [
    32.54507,
    46.69641
  ],
  "кам'янець-подільський хмельницька": [
    26.58516,
    48.67882
  ],
  "адампіль хмельницька": [
    27.65652,
    49.66791
  ],
  "волочиськ хмельницька": [
    26.20681,
    49.53606
  ],
  "красилів хмельницька": [
    26.97211,
    49.65376
  ],
  "старокостянтинів хмельницька": [
    27.21229,
    49.75522
  ],
  "теофіполь хмельницька": [
    26.4204,
    49.83892
  ],
  "хмельницький хмельницька": [
    26.97936,
    49.41835
  ],
  "нетішин хмельницька": [
    26.64872,
    50.32863
  ],
  "полонне хмельницька": [
    27.50856,
    50.11944
  ],
  "славута хмельницька": [
    26.86613,
    50.29609
  ],
  "шепетівка хмельницька": [
    27.06517,
    50.18118
  ],
  "багачеве черкаська": [
    31.04659,
    49.01198
  ],
  "звенигородка черкаська": [
    30.96074,
    49.07765
  ],
  "золотоноша черкаська": [
    32.03637,
    49.66926
  ],
  "жашків черкаська": [
    30.09888,
    49.2459
  ],
  "умань черкаська": [
    30.21944,
    48.7501
  ],
  "канів черкаська": [
    31.47003,
    49.75187
  ],
  "корсунь-шевченківський черкаська": [
    31.25174,
    49.41822
  ],
  "сміла черкаська": [
    31.88427,
    49.23295
  ],
  "черкаси черкаська": [
    32.05738,
    49.44452
  ],
  "чигирин черкаська": [
    32.66082,
    49.08045
  ],
  "вижниця чернівецька": [
    25.18112,
    48.24482
  ],
  "мігове чернівецька": [
    25.37574,
    48.15612
  ],
  "путила чернівецька": [
    25.08757,
    47.99343
  ],
  "кельменці чернівецька": [
    26.83277,
    48.4664
  ],
  "сокиряни чернівецька": [
    27.411193,
    48.4460307
  ],
  "хотин чернівецька": [
    26.48978,
    48.50555
  ],
  "герца чернівецька": [
    26.26186,
    48.14752
  ],
  "чернівці чернівецька": [
    25.93241,
    48.29045
  ],
  "корюківка чернігівська": [
    32.24747,
    51.7746
  ],
  "мена чернігівська": [
    32.21364,
    51.52205
  ],
  "сновськ чернігівська": [
    31.94245,
    51.81674
  ],
  "сосниця чернігівська": [
    32.49985,
    51.52387
  ],
  "холми чернігівська": [
    32.59733,
    51.87141
  ],
  "короп чернігівська": [
    32.95217,
    51.56666
  ],
  "новгород-сіверський чернігівська": [
    33.2634,
    52.00684
  ],
  "семенівка чернігівська": [
    32.57755,
    52.17853
  ],
  "батурин чернігівська": [
    32.87981,
    51.34261
  ],
  "бахмач чернігівська": [
    32.83463,
    51.18144
  ],
  "бобровиця чернігівська": [
    31.3860852,
    50.7415033
  ],
  "борзна чернігівська": [
    32.4269,
    51.25343
  ],
  "носівка чернігівська": [
    31.58031,
    50.93799
  ],
  "ніжин чернігівська": [
    31.88844,
    51.04772
  ],
  "ічня чернігівська": [
    32.39129,
    50.85908
  ],
  "варва чернігівська": [
    32.72274,
    50.49858
  ],
  "прилуки чернігівська": [
    32.38382,
    50.59525
  ],
  "срібне чернігівська": [
    32.91906,
    50.66314
  ],
  "талалаївка чернігівська": [
    33.14173,
    50.84287
  ],
  "гончарівське чернігівська": [
    30.91984,
    51.29892
  ],
  "городня чернігівська": [
    31.59632,
    51.89129
  ],
  "десна чернігівська": [
    30.76678,
    50.92744
  ],
  "козелець чернігівська": [
    31.11664,
    50.91211
  ],
  "куликівка чернігівська": [
    31.64604,
    51.3729
  ],
  "любеч чернігівська": [
    30.66018,
    51.70219
  ],
  "остер чернігівська": [
    30.87735,
    50.94966
  ],
  "ріпки чернігівська": [
    31.08578,
    51.80165
  ],
  "чернігів чернігівська": [
    31.28656,
    51.50541
  ],
  "борозна чернігівська": [
    32.4263156,
    51.2534475
  ],
  "борозна": [
    32.4263156,
    51.2534475
  ]
}

CITY_POINTS = CITY_POINTS_BY_SLUG
