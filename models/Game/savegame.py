import json

class Savegame:
    def __init__(self, game_state, filename='savegame.json'):
        self.game_state = game_state
        self.filename = filename

    def save_game(self):
        data = {
            "map": self._save_map(),
            "entities": self._save_entities()
        }
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)
        print("Game saved successfully.")

    def load_game(self):
        with open(self.filename, 'r') as file:
            data = json.load(file)

        self._load_map(data["map"])
        self._load_entities(data["entities"])
        print("Game loaded successfully.")

    def _save_map(self):
        return {
            "nb_CellX": self.game_state.map.nb_CellX,
            "nb_CellY": self.game_state.map.nb_CellY
        }

    def _save_entities(self):
        entities = []
        for entity_id, entity in self.game_state.map.entity_id_dict.items():
            entities.append({
                "id": entity.id,
                "type": type(entity).__name__,
                "x": entity.cell_X,
                "y": entity.cell_Y,
                "hp": entity.hp
            })
        return entities

    def _load_map(self, map_data):
        self.game_state.map.nb_CellX = map_data["nb_CellX"]
        self.game_state.map.nb_CellY = map_data["nb_CellY"]

    def _load_entities(self, entities_data):
        for entity_data in entities_data:
            entity_type = entity_data["type"]
            x, y, hp = entity_data["x"], entity_data["y"], entity_data["hp"]
            if entity_type == "Archer":
                entity = Archer(y, x, PVector2(0, 0), 1)
            elif entity_type == "Villager":
                entity = Villager(y, x, PVector2(0, 0), 2)

            entity.hp = hp
            self.game_state.map.add_entity(entity)
