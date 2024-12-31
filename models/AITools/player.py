class Player:
    
    def __init__(self, team, resources = {"gold":0,"wood":0,"food":0}):
        self.team = team
        self.resources = resources

    def add_resources(self, resources):

        for resource, amount in resources.items():
            if resource in self.resources and isinstance(amount, (int, float)): # the isinstance is just to prevent undefined behavior ( if happend)
                self.resources[resource] += amount
    
    def remove_resources(self, resources):

        for resource, amount in resources.items():
            if resource in self.resources and isinstance(amount, (int, float )):
                self.resources[resource] = max(0, self.resources[resource] - amount) # in case something not usual happen so the currency doesnt drop to neg numbers, it is not going to happen but who knows
    