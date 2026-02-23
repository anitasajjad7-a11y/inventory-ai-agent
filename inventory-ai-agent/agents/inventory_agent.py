import pandas as pd

class InventoryAgent:
    def __init__(self):
        self.df = pd.read_csv("inventory.csv")

    def answer(self, question):
        question = question.lower()

        # Low stock
        if "low" in question or "reorder" in question:
            low_stock = self.df[self.df["Stock"] < self.df["ReorderLevel"]]
            if low_stock.empty:
                return "All items are sufficiently stocked."
            result = ""
            for _, row in low_stock.iterrows():
                result += f"{row['Item']}: {row['Stock']} units (Reorder Level: {row['ReorderLevel']})\n"
            return result

        # Out of stock
        if "out of stock" in question:
            out = self.df[self.df["Stock"] == 0]
            if out.empty:
                return "No items are out of stock."
            return ", ".join(out["Item"]) + " is out of stock!"

        # Specific item query
        if "how many units" in question:
            words = question.split()
            for word in words:
                if word.upper() in self.df["Item"].values:
                    item = word.upper()
                    row = self.df[self.df["Item"] == item].iloc[0]
                    return f"{item} has {row['Stock']} units left. Reorder Level is {row['ReorderLevel']}."
            return "Item not found."

        # Show all stock
        if "all" in question or "current" in question:
            result = ""
            for _, row in self.df.iterrows():
                result += f"{row['Item']}: {row['Stock']} units\n"
            return result

        return "Sorry, I didn't understand your question."