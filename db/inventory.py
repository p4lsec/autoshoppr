import sqlite3

class RecipeInventory:
    def __init__(self):
        self.conn = sqlite3.connect('autoshoppr.db')
    
    def create_recipe_table(self):
        self.conn.execute("""CREATE TABLE recipe 
                            (recipe_id INTEGER PRIMARY KEY NOT NULL, 
                            recipe_name TEXT, 
                            recipe_url TEXT,
                            instructions_id INTEGER
                            ingredients_id INTEGER""")
        self.conn.execute("""CREATE TABLE instructions
                            (instructions_id INTEGER PRIMARY KEY NOT NULL,
                            instructions TEXT)""")
        self.conn.execute("""CREATE TABLE ingredients
                            (ingredient_id INTEGER PRIMARY KEY NOT NULL,
                            ingredient_name TEXT, 
                            ingredient_qty QTY, 
                            ingredient_url TEXT)""")
        self.conn.commit()
        
    def add_recipe(self, recipe):
        self.conn.execute("INSERT INTO recipes VALUES (?)", (recipe,))
        self.conn.commit()
    
    def get_recipes(self):
        return self.conn.execute("SELECT * FROM recipes")
    
    def get_recipe(self, recipe):
        return self.conn.execute("SELECT * FROM recipes WHERE recipe=?", (recipe,))
    
    def get_recipe_qty(self, recipe):
        return self.conn.execute("SELECT qty FROM recipes WHERE recipe=?", (recipe,))
    
    def get_recipe_qty_by_id(self, id):
        return self.conn.execute("SELECT qty FROM recipes WHERE id=?", (id,))
    
    def get_recipe_id(self, recipe):
        return self.conn.execute("SELECT id FROM recipes WHERE recipe=?", (recipe,))
    
    def get_recipe_id_by_qty(self, qty):
        return self.conn.execute("SELECT id FROM recipes WHERE qty=?", (qty,))
    

