from cards import Card
from location import Location
from character import Character

global locations
locations = [
    Location('Le Refuge de l\'hermite', 3),
    Location('La Porte de l\'Outremonde', 5),
    Location('Le Monastère', 6),
    Location('Le Cimetière', 8),
    Location('La Forêt hantée', 9),
    Location('Le Sanctuaire ancien', 10)
]

global vision_cards
vision_cards = [
    Card('Vision mortifère', 'Je pense que tu es Hunter. Si c\'est le cas subis 1 Blessure!'),
    Card('Vision divine', 'Je pense que tu es Hunter. Si c\'est le cas soigne 1 Blessure.'),
    Card('Vision foudroyante', 'Je pense que tu es Shadow. Si c\'est le cas subis 1 Blessure!'),
    Card('Vision lugubre', 'Je pense que tu es Shadow. Si c\'est le cas soigne 1 Blessure.')
]

global emi
emi = Character('Emi', 10, 'Hunters')
global franklin
franklin = Character('Franklin', 12, 'Hunters')
global george
george = Character('George', 14, 'Hunters')
global metamorphe
metamorphe = Character('Métamorphe', 11, 'Shadow')
global vampire
vampire = Character('Vampire', 13, 'Shadow')
global werewolf
werewolf = Character('Loup-Garou', 14, 'Shadow')
global allie
allie = Character('Allie', 8, 'Neutres')
global bob
bob = Character('Bob', 10, 'Neutres')
global charles
charles = Character('Charles', 11, 'Neutres')
global daniel
daniel = Character('Daniel', 13, 'Neutres')
