class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self.update_item_quality(item)

    #NB:
    # un produit ne peut jamais voir sa qualité augmenter au-dessus de 50
    #La qualité (quality) d'un produit ne peut jamais être négative.
    def update_item_quality(self, item):
        if item.name == "Aged Brie":
            self.update_aged_brie(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            self.update_backstage_passes(item)
        elif item.name == "Sulfuras, Hand of Ragnaros":
            pass  # Sulfuras objet légendaire, n'a pas de date de péremption et ne perd jamais en qualité
        elif item.name.startswith("Conjured"):
            self.update_conjured_item(item)
        else:
            self.update_normal_item(item)

        if item.name != "Sulfuras, Hand of Ragnaros":
            #diminue le nombre de jours restant pour chaque produit sauf le produit "Sulfuras"
            item.sell_in -= 1

        if item.sell_in < 0:
            #Une fois que la date de péremption est passée, la qualité se dégrade deux fois plus rapidement.
            self.item_sellIn_expired(item)

    def update_aged_brie(self, item):
        #augmente sa qualité (quality) plus le temps passe 
        if item.quality < 50:
            item.quality += 1

    def update_backstage_passes(self, item):
        #augmente sa qualité (quality) plus le temps passe
        #La qualité augmente de 2 quand il reste 10 jours ou moins
        #La qualité augmente de 3 quand il reste 5 jours ou moins
        if item.quality < 50:
            item.quality += 1
            if item.sell_in < 11 and item.sell_in > 5:
                if item.quality < 50:
                    item.quality += 1
            if item.sell_in < 6:
                if item.quality < 50:
                    item.quality += 2

    def update_normal_item(self, item):
        if item.quality > 0:
            item.quality -= 1

    def update_conjured_item(self, item):
        #les éléments "Conjured" voient leur qualité se dégrader de deux fois plus vite que les objets normaux.
        #La qualité (quality) d'un produit ne peut jamais être négative.
        if item.quality > 0:
            item.quality -= 2
            if item.quality < 0:
                item.quality = 0

    def item_sellIn_expired(self, item):
        #Une fois que la date de péremption est passée, la qualité se dégrade deux fois plus rapidement.
        if item.name == "Aged Brie":
            if item.quality < 50:
                item.quality += 1
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            #la qualité tombe à 0 après le concert.
            item.quality = 0
        elif item.name.startswith("Conjured"):
            #qualité se dégrader de deux fois plus vite que les objets normaux.
            if item.quality > 1:
                item.quality -= 2
            else:
                item.quality = 0
        elif item.quality > 0 and item.name != "Sulfuras, Hand of Ragnaros":
            item.quality -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f"{self.name}, {self.sell_in}, {self.quality}"
