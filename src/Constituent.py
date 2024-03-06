import numpy as np
from src.Candidate import Candidate

class Constituent:
    def __init__(self, parties, bias=None):
        if bias is None:
            self.supports = np.random.choice(parties)
            self.leaning = np.random.normal()
        else:
            if len(bias) != len(parties):
                raise ValueError("The length of the bias list must be the same as the number of parties")
            self.supports = np.random.choice(parties, p=bias)
            self.leaning = np.random.normal()

    def set_leaning(self, leaning):
        self.leaning = leaning

    def get_support(self):
        return self.supports

    def get_leaning(self):
        return self.leaning    

    def set_support(self, party):
        self.supports = party
    
    def vote(self, candidates):
        closest_leaning_candidate = None
        most_popular_candidate = None
        for candidate in candidates:
            if closest_leaning_candidate is None:
                closest_leaning_candidate = candidate
            elif abs(candidate.leans - self.leaning) < abs(closest_leaning_candidate.leans - self.leaning):
                closest_leaning_candidate = candidate
            if most_popular_candidate is None:
                most_popular_candidate = candidate
            elif candidate.popularity > most_popular_candidate.popularity:
                most_popular_candidate = candidate
            if candidate.party == self.supports and self.supports != 'Independent':
                return candidate
        return np.random.choice([closest_leaning_candidate, most_popular_candidate])
        

