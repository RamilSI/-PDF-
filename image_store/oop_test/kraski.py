from __future__ import division


class Paint:
    dry_residue = 83

    def practical_consumption(self):
        tsp = 100
        fp = 30
        theoretical_consumption = tsp / (10 * self.dry_residue)
        practical = theoretical_consumption / (1 - fp / 100)
        return practical


# описание класса "материал"
"""
сухой остаток
цена
мин. толщина
макс. толщина

"""

grunt_1052 = Paint()

grunt_1052.dry_residue = 80
w = grunt_1052.practical_consumption()
print(w)
print(grunt_1052.__dict__)
print(Paint.__dict__)
