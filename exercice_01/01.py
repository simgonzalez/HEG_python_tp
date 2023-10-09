class Camion():
    chargement_max: int = 5000
    chargement_init: float = (35 * 54.5) + (40 * 35)
    charge_restante: float = chargement_max - chargement_init

    def add_chargement(self, to_add: float):
        if (self.charge_restante - to_add) > 0:
            self.charge_restante -= to_add
        else:
            print(f"The left weight is {self.charge_restante}")

    def get_charge_restante(self):
        return self.charge_restante


camion1: Camion = Camion()
print(camion1.get_charge_restante())

camion1.add_chargement(150*5)
print(camion1.get_charge_restante())

camion1.add_chargement(29*12.5)
print(camion1.get_charge_restante())
