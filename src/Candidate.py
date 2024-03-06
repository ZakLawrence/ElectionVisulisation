
class Candidate:
    def __init__(self,name, party, popularity, leans):
        self.name = name
        self.party = party
        self.popularity = popularity
        self.leans = leans
    
    def __str__(self):
        return "{}, Party: {}, Popularity: {}, Leans: {}".format(self.name, self.party, self.popularity, self.leans) 
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__ (self, other):
        return self.name == other.name and self.party == other.party and self.popularity == other.popularity and self.leans == other.leans
    
    