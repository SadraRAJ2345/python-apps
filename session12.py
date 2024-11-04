# __init__ = magic method - special method - dunder

class Tv:
    def __init__(self, year, company, model):
        self.model = model
        self.company = company
        self.year = year
        self.is_on = False
        self.volume = 98

    def __str__(self) -> str:
        return "Tv({},{},{})".format(self.year,self.model,self.company)

    def change_state(self):
        self.is_on = not self.is_on
        return "Done"

    def increase_volume(self):
        if self.volume < 100:
            self.volume += 1
            return "Done"
        else:
            return "Maximum"

    def decrease(self):
        self.volume -=1
        return "Done"


o1 = Tv(2017, "LG", "T110")
o1.increase_volume()
print(o1.increase_volume())

print(o1.increase_volume())
print(o1.increase_volume())

