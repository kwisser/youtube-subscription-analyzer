import matplotlib.pyplot as plt

# Daten für die Kanäle und ihre Themenbereiche
channels = [
    ('Jasmin Kosubek', 'Interviews'),
    ('STRG_F', 'Dokumentationen'),
    ('Y-Kollektiv', 'Dokumentationen'),
    ('Coding Crashkurse', 'Informatik'),
    ('Stephan Pütz', 'Sport und Ernährung'),
    ('Informatik mit Prof. Sebastian', 'Informatik'),
    ('m4xFPS', 'Informatik'),
    ('Fireship', 'Informatik'),
    ('LiveOverflow', 'Informatik'),
    ('CodeAesthetic', 'Informatik'),
    ('Simplicissimus', 'Kritische Analyse'),
    ('Dennis Ivy', 'Informatik'),
    ('Sumit Kumar', 'Informatik'),
    ('Beyond Fireship', 'Informatik'),
    ('Sebastian Hahner - skate702', 'Informatik'),
    ('Script Raccoon', 'Informatik'),
    ('Joseph DeChangeman', 'Dokumentationen'),
    ('Reluctant Anarchist', 'Informatik'),
    ('Dinge Erklärt – Kurzgesagt', 'Wissenschaft'),
    ('Juxtopposed', 'Informatik'),
    ('Ultralativ', 'Wissen und Kultur'),
    ('GreenConnection', 'Cannabis'),
    ('Unleashed Design', 'Informatik'),
    ('SEOTADEO', 'Wissenschaft'),
    ('Der Dunkle Parabelritter', 'Kultur und Kritik'),
    ('Hubertus Koch', 'Politik'),
    ('Pauls gsunde Küche', 'Kochen'),
    ('Ben Awad', 'Informatik'),
    ('Das ist Berlin Bitch', 'Unterhaltung'),
    ('Manuel Haase', 'Philosophie'),
    ('Florian Woelki', 'Informatik'),
    ('TheCodex', 'Informatik'),
    ('FÄTTE', 'Unterhaltung'),
    ('Coding with Lewis', 'Informatik'),
    ('CodingEntrepreneurs', 'Informatik'),
    ('Yakuza112 Inc.', 'Informatik'),
    ('KLEMDMA', 'Musik'),
    ('RobBubble', 'Unterhaltung'),
    ('Niklas Christl', 'Unterhaltung'),
    ('struthless', 'Persönlichkeitsentwicklung'),
    ('René Pickhardt', 'Informatik'),
    ('DJ Jordan', 'Musik'),
    ('Defog Tech', 'Informatik'),
    ('Pfennigfuchser', 'Finanzen'),
    ('Animakers Show DE', 'Animationen'),
    ('STEPHAN BODZIN', 'Musik'),
    ('Biscuit', 'Musik'),
    ('Hallden', 'Informatik'),
    ('Wende', 'Unterhaltung'),
    ('MNML4U', 'Musik'),
    ('Polymita', 'Unterhaltung'),
    ('3Blue1Brown', 'Mathematik'),
    ('Der Kapitalist', 'Wirtschaft'),
    ('Jet0JLHSupport', 'Informatik'),
    ('GreenGermany', 'Cannabis'),
    ('sens cuisine', 'Kochen'),
    ('ThinMatrix', 'Informatik'),
    ('Hacker Shack', 'Informatik'),
    ('Hex Murder', 'Informatik'),
    ('DerMicha', 'Cannabis'),
    ('Ignobilium _', 'Musik'),
    ('Benjamin Jaworskyj - Zweitkanal', 'Fotografie')
]

# Extrahiere die Themenbereiche
topics = [channel[1] for channel in channels]

# Zähle die Anzahl der Kanäle pro Themenbereich
topic_counts = {}
for topic in topics:
    if topic in topic_counts:
        topic_counts[topic] += 1
    else:
        topic_counts[topic] = 1

# Erstelle das Pie Chart
plt.figure(figsize=(8, 8))
plt.pie(list(topic_counts.values()), labels=list(topic_counts.keys()), autopct='%1.1f%%', startangle=90)

# Füge einen Kreis in der Mitte hinzu, um ein Donut-Chart zu erstellen
circle = plt.Circle((0, 0), 0.7, color='white')
plt.gca().add_artist(circle)

# Füge einen Titel hinzu
plt.title('YouTube-Kanäle nach Themenbereich')

# Zeige das Diagramm an
plt.tight_layout()
plt.show()
