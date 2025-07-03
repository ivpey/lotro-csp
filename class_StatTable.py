import pandas

class Stat_Table:

    def __init__(self):

        char_stat_derivations = pandas.read_html('https://lotro-wiki.com/wiki/Character_Stat_Derivations')[0]
        char_stat_derivations.columns = [
            'Main stat', 'Derived stat', 'Beorning', 'Brawler', 'Burglar', 'Captain', 'Champion', 'Guardian',
            'Hunter', 'Lore-master', 'Mariner', 'Minstrel', 'Rune-keeper', 'Warden'
        ]

        self.__full_table = char_stat_derivations.dropna()

    def getFullTable(self):
        return self.__full_table

    def listMainStats(self):
        return list(self.__full_table['Main stat'].unique())

    def listDerivedStats(self):
        return list(self.__full_table['Derived stat'].unique())
    
    def listAllStats(self):
        ms = list(self.__full_table['Main stat'].unique())
        ds = list(self.__full_table['Derived stat'].unique())
        ms.extend(ds)
        return ms