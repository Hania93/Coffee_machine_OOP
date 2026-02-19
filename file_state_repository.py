import json
import os

class FileStateRepository:
    def __init__(self, filename: str = "state.json"):
        self.filename = filename
        self.default_state = {
            "resources": {
                "coffee": 200,
                "water": 1000,
                "milk": 300
            },
            "coins": {
                10: 5,
                25: 5,
                50: 5,
                100: 5,
                500: 5
            },
            "profit": 0.0,
            "drinks_counter": 0
        }
        if not os.path.exists(self.filename):
            self.save(self.default_state)

    def save(self, state: dict) -> bool:
        try:
            with open(self.filename, "w") as f:
                json.dump(state, f, indent=4)            
            return True
        except Exception:
            return False

    def load(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)

            resources_raw = data.get("resources", self.default_state["resources"])
            if isinstance(resources_raw, dict):
                resources = {k: int(v) for k, v in resources_raw.items()}
            else:
                resources = self.default_state["resources"]

            coins_raw = data.get("coins", self.default_state["coins"])
            if isinstance(coins_raw, dict):
                coins = {int(k): int(v) for k, v in coins_raw.items()}
            else:
                coins = self.default_state["coins"]

            profit = float(data.get("profit", self.default_state["profit"]))
            drinks_counter = int(data.get("drinks_counter", self.default_state["drinks_counter"]))

            return True, resources, coins, profit, drinks_counter

        except (FileNotFoundError, json.JSONDecodeError, ValueError):
            
            self.save(self.default_state)
            return (
                False,
                self.default_state["resources"],
                self.default_state["coins"],
                self.default_state["profit"],
                self.default_state["drinks_counter"]
            )



