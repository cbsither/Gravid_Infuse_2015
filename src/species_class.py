import csv
import numpy as np

# 'triseriatus sl', 'japonicus'

class Species:

    def __init__(self, file_path, species):
        self.csv_loc = file_path
        self.species = species

    def infusion_comparison_by_date_species_site(self):
        self.hhs_oak, self.hhs_grass, self.dev_oak, self.dev_grass, self.church_oak, self.church_grass = [], [], [], [], [], []
        self.date_collection = []
        with open(self.csv_loc, newline='') as ff:
            gravid_data = csv.reader(ff, delimiter=',')
            for _position_, _row_ in enumerate(gravid_data):
                if _position_ == 0:
                    pass
                else:
                    if _row_[2] not in self.date_collection:
                        self.date_collection.append(_row_[2])
            ff.seek(0)
            for _date_ in self.date_collection:
                hhs_oak_day, hhs_grass_day, dev_oak_day, dev_grass_day, church_oak_day, church_grass_day = 0, 0, 0, 0, 0, 0
                for _position_, _row_ in enumerate(gravid_data):
                    if _position_ == 0:
                        pass
                    else:
                        if _row_[2] == _date_:
                            if _row_[6] == self.species:
                                if _row_[4] == 'grass':
                                    if _row_[3] == 'Church':
                                        church_grass_day += 1
                                    elif _row_[3] == 'dev.cent.':
                                        dev_grass_day += 1
                                    elif _row_[3] == 'HHS':
                                        hhs_grass_day += 1
                                    else:
                                        pass
                                else:
                                    if _row_[3] == 'Church':
                                        church_oak_day += 1
                                    elif _row_[3] == 'dev.cent.':
                                        dev_oak_day += 1
                                    elif _row_[3] == 'HHS':
                                        hhs_oak_day += 1
                                    else:
                                        pass
                            else:
                                pass
                ff.seek(0)
                self.hhs_oak.append(hhs_oak_day)
                self.hhs_grass.append(hhs_grass_day)
                self.dev_oak.append(dev_oak_day)
                self.dev_grass.append(dev_grass_day)
                self.church_oak.append(church_oak_day)
                self.church_grass.append(church_grass_day)

    def summary_stats(self):
        self.total = sum(self.hhs_oak + self.hhs_grass + self.dev_oak + self.dev_grass + self.church_oak + self.church_grass)

    def oak(self):
        self.oak_data = self.church_oak + self.hhs_oak + self.dev_oak
        self.oak_total = sum(self.oak_data)
        self.oak_by_date = np.sum([self.church_oak, self.hhs_oak, self.dev_oak], axis=0)

    def grass(self):
        self.grass_data = self.church_grass + self.hhs_grass + self.dev_grass
        self.grass_total = sum(self.grass_data)
        self.grass_by_date = np.sum([self.church_grass, self.hhs_grass, self.dev_grass], axis=0)

    def sites(self):
        pass

    def extract(self):
        self.infusion_comparison_by_date_species_site()
        self.summary_stats()
        self.oak()
        self.grass()
        self.sites()
        self.time_val = len(self.date_collection)


