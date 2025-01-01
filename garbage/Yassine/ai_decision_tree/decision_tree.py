class DecisionNode:
    def __init__(self, question, yes_action=None, no_action=None, priority=0):
        """
        Représente un noeud de décision dans l'arbre.
        """
        self.question = question
        self.yes_action = yes_action
        self.no_action = no_action
        self.priority = priority

    def decide(self, context):
        """
        Traverse l'arbre pour trouver les actions optimales en fonction des priorités.
        """
        actions = []

        # Vérifie la condition
        if self.question(context):
            if isinstance(self.yes_action, DecisionNode):
                actions.extend(self.yes_action.decide(context))
            else:
                actions.append((self.yes_action, self.priority))
        else:
            if isinstance(self.no_action, DecisionNode):
                actions.extend(self.no_action.decide(context))
            else:
                actions.append((self.no_action, self.priority))

        # Trie les actions par priorité (ordre décroissant)
        actions.sort(key=lambda x: x[1], reverse=True)

        # Exécute les actions et retourne leurs résultats
        results = []
        for action, _ in actions:
            if callable(action):
                results.append(action())
            else:
                results.append(action)

        return results
