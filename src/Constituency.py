from src.Constituent import Constituent
import numpy as np

class Constituency:
    def __init__(self,name,onsid, population, candidates, parties, bias=None):
        self.name = name
        self.onsid = onsid
        self.population = population
        self.candidates = candidates
        self.voters = [Constituent(parties, bias) for _ in range(population)]

    def __str__(self):
        return "{}, Population: {}, Candidates: {}".format(self.name, self.population, self.candidates)
    
    def add_candidate(self, candidate):
        self.candidates.append(candidate)

    def remove_candidate(self, candidate):
        self.candidates.remove(candidate)

    def get_candidate(self, candidate):
        if candidate in self.candidates:
            return candidate
        else:
            return None
    
    def get_candidate_by_name(self, name):
        for candidate in self.candidates:
            if candidate.name == name:
                return candidate
        return None

    def get_candidates(self):
        return self.candidates

    def get_population(self):
        return self.population

    def get_name(self):
        return self.name

    def set_population(self, population):
        self.population = population
    
    def set_name(self, name):
        self.name = name

    def set_candidates(self, candidates):
        self.candidates = candidates

    def get_party_support(self):
        supporters = {}
        for voter in self.voters:
            if voter.get_support() in supporters.keys():
                supporters[voter.get_support()] += 1
            else:
                supporters[voter.get_support()] = 1
        return supporters

    def run_election(self, turnout, System):
        voters = np.random.choice(self.voters, int(self.population * turnout))
        result = System(voters, self.candidates)
        result['name'] = self.name
        result['ONS ID'] = self.onsid
        result['Electorate'] = self.population
        result['Turnout'] = turnout
        return result