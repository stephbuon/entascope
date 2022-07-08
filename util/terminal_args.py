def show_entity_labels():
    print("""
    PERSON:        People's names
    NORP:          Nationalities or religiouse or political groups.
    FAC:           Infrastructure such as buildings, airports, highways, bridges, etc.
    ORG:           Companies, agencies, institutions, etc.
    GPE:           Countries, cities, states.
    LOC:           Non-GPE locations, mountain ranges, bodies of water. 
    PRODUCT:       Objects, vehicles, foods, etc. (Not services.)
    EVENT:         Names of events. Natural disasters, battles, sports events, etc. Coronavirus strains like "omicron" are categorized as events.
    WORK_OF_ART:   Titles of books, songs, etc.
    LAW:           Names of documents made into laws.
    LANGUAGE:      Named languages.
    DATE:          Absolute or relative dates or periods.
    TIME:          Times smaller than a day.
    PERCENT:       Percentage, including "%".
    MONEY:         Monetary values.
    QUANTITY:      Measurements, as of weight or distance.
    ORDINAL:       Terms denoting order, such as "first" or "second."
    CARDINAL:      Numerals that do not fall under another time. 
    """)
