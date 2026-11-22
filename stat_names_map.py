"""
    A 3-way mapping of stat names:
        - root: display name for use in the UI
        - itemsdb: coming from https://github.com/LotroCompanion/lotro-items-db
        - calcstat: used in sqlite and for stat derivations via CalcStat package

    The stat list is incomplete on purpose because Power, ICMR / ICPR, etc. are irrelevant for me.
"""

stat_names_map = {
    'Might': {
        'itemsdb': 'MIGHT',
        'calcstat': 'Might'
    },
    'Agility': {
        'itemsdb': 'AGILITY',
        'calcstat': 'Agility'
    },
    'Vitality': {
        'itemsdb': 'VITALITY',
        'calcstat': 'Vitality'
    },
    'Will': {
        'itemsdb': 'WILL',
        'calcstat': 'Will'
    },
    'Fate': {
        'itemsdb': 'FATE',
        'calcstat': 'Fate'
    },
    'Critical Rating': {
        'itemsdb': 'CRITICAL_RATING',
        'calcstat': 'CritHit'
    },
    'Finesse Rating': {
        'itemsdb': 'FINESSE',
        'calcstat': 'Finesse'
    },
    'Physical Mastery Rating': {
        'itemsdb': 'PHYSICAL_MASTERY',
        'calcstat': 'PhyMas'
    },
    'Tactical Mastery Rating': {
        'itemsdb': 'TACTICAL_MASTERY',
        'calcstat': 'TacMas'
    },
    'Outgoing Healing Rating': {
        'itemsdb': 'OUTGOING_HEALING',
        'calcstat': 'OutHeal'
    },
    'Incoming Healing Rating': {
        'itemsdb': 'INCOMING_HEALING',
        'calcstat': 'InHeal'
    },
    'Resistance Rating': {
        'itemsdb': 'RESISTANCE',
        'calcstat': 'Resist'
    },
    'Block Rating': {
        'itemsdb': 'BLOCK',
        'calcstat': 'Block'
    },
    'Parry Rating': {
        'itemsdb': 'PARRY',
        'calcstat': 'Parry'
    },
    'Evade Rating': {
        'itemsdb': 'EVADE',
        'calcstat': 'Evade'
    },
    'Physical Mitigation': {
        'itemsdb': 'PHYSICAL_MITIGATION',
        'calcstat': 'PhyMit'
    },
    'Tactical Mitigation': {
        'itemsdb': 'TACTICAL_MITIGATION',
        'calcstat': 'TacMit'
    },
    'Critical Defense': {
        'itemsdb': 'CRITICAL_DEFENCE',
        'calcstat': 'CritDef'
    },
    'Maximum Morale': {
        'itemsdb': 'MORALE',
        'calcstat': 'Morale'
    }
}