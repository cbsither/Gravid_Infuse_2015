import numpy as np
from scipy import stats
import csv

"""
This code was written during the first few months of learning Python. I have organized the other parts of this project
but am leaving this bit of code as is, since it would be too tedious and induce more errors than it's worth.
"""

gravid_trap_data = '../data/MosqColGravidTrap_JohnSither_Final2.csv'

# returns hhs_oak , hhs_grass , dev_oak , dev_grass , church_oak , church_grass --- species by site by date
def Infusion_Comparison_By_Date_Species_Site( gravid_trap_data , species_name ):
	hhs_oak , hhs_grass , dev_oak , dev_grass , church_oak , church_grass = [],[],[],[],[],[]
	date_collection = []
	with open( gravid_trap_data , newline = '') as ff:
		gravid_data = csv.reader( ff , delimiter = ',' )
		for _position_ , _row_ in enumerate( gravid_data ):
			if _position_ == 0:
				pass
			else:
				if _row_[2] not in date_collection:
					date_collection.append( _row_[2] )
		ff.seek(0)
		for _date_ in date_collection:
			hhs_oak_day , hhs_grass_day , dev_oak_day , dev_grass_day , church_oak_day , church_grass_day = 0,0,0,0,0,0
			for _position_ , _row_ in enumerate( gravid_data ):
				if _position_ == 0:
					pass
				else:
					if _row_[2] == _date_:
						if _row_[6] == species_name:
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
			hhs_oak.append( hhs_oak_day )
			hhs_grass.append( hhs_grass_day )
			dev_oak.append( dev_oak_day )
			dev_grass.append( dev_grass_day )
			church_oak.append( church_oak_day )
			church_grass.append( church_grass_day )
	return hhs_oak , hhs_grass , dev_oak , dev_grass , church_oak , church_grass

def FindRange(x, axis=0):
    return np.max(x, axis=axis) - np.min(x, axis=axis)

def SummaryStatsTable():
	with open('../tables/Summary_Stats_Table.csv', "w") as sum_stats:
		sum_stats.write(',,HHS,,,,,,Church,,,,,,devCent,,,,,,Species Total,,,,,,\n')
		sum_stats.write(',,Sum,Mean,Variance,Median,Mode,Range,Sum,Mean,Variance,Median,Mode,Range,Sum,Mean,Variance,Median,Mode,Range,Sum,Mean,Variance,Median,Mode,Range\n')
		# Aedes trisieratus
		hhs_oak , hhs_grass , dev_oak , dev_grass , church_oak , church_grass = Infusion_Comparison_By_Date_Species_Site( gravid_trap_data , 'triseriatus sl' )
		sum_stats.write(f'Aedes triseriatus,Site Total,{sum(hhs_oak+hhs_grass)},{np.mean(hhs_oak+hhs_grass)},{np.var(hhs_oak+hhs_grass)},{np.median(hhs_oak + hhs_grass)},{int(stats.mode(hhs_oak + hhs_grass)[0])},{FindRange(hhs_oak + hhs_grass)}, \
		{sum(church_oak + church_grass)},{np.mean(church_oak + church_grass)},{np.var(church_oak + church_grass)},{np.median(church_oak + church_grass)},{int(stats.mode(church_oak + church_grass)[0])},{FindRange(church_oak + church_grass)},\
		{sum(dev_oak + dev_grass)},{np.mean(dev_oak + dev_grass)},{np.var(dev_oak + dev_grass)},{np.median(dev_oak + dev_grass)},{int(stats.mode(dev_oak + dev_grass)[0])},{FindRange(dev_oak + dev_grass)},\
		{sum(hhs_oak + hhs_grass + dev_oak + dev_grass + church_oak + church_grass)},{np.mean(hhs_oak + hhs_grass + dev_oak + dev_grass + church_oak + church_grass)},{np.var(hhs_oak + hhs_grass + dev_oak + dev_grass + church_oak + church_grass)},\
		{np.median(hhs_oak + hhs_grass + dev_oak + dev_grass + church_oak + church_grass)},{int(stats.mode(hhs_oak + hhs_grass + dev_oak + dev_grass + church_oak + church_grass)[0])},\
		{FindRange(hhs_oak + hhs_grass + dev_oak + dev_grass + church_oak + church_grass)}\n')
		sum_stats.write(f',Oak,{sum(hhs_oak)},{np.mean(hhs_oak)},{np.var(hhs_oak)},{np.median(hhs_oak)},{int(stats.mode(hhs_oak)[0])},{FindRange(hhs_oak)}, \
		{sum(church_oak)},{np.mean(church_oak)},{np.var(church_oak)},{np.median(church_oak)},{int(stats.mode(church_oak)[0])},{FindRange(church_oak)},\
		{sum(dev_oak)},{np.mean(dev_oak)},{np.var(dev_oak)},{np.median(dev_oak)},{int(stats.mode(dev_oak)[0])},{FindRange(dev_oak)}\n')
		sum_stats.write(f',Grass,{sum(hhs_grass)},{np.mean(hhs_grass)},{np.var(hhs_grass)},{np.median(hhs_grass)},{int(stats.mode(hhs_grass)[0])},{FindRange(hhs_grass)}, \
		{sum(church_grass)},{np.mean(church_grass)},{np.var(church_grass)},{np.median(church_grass)},{int(stats.mode(church_grass)[0])},{FindRange(church_grass)},\
		{sum(dev_grass)},{np.mean(dev_grass)},{np.var(dev_grass)},{np.median(dev_grass)},{int(stats.mode(dev_grass)[0])},{FindRange(dev_grass)}\n')
		# Aedes japonicus
		hhs_oak , hhs_grass , dev_oak , dev_grass , church_oak , church_grass = Infusion_Comparison_By_Date_Species_Site( gravid_trap_data , 'japonicus' )
		sum_stats.write(f'Aedes japonicus,Site Total,{sum(hhs_oak + hhs_grass)},{np.mean(hhs_oak + hhs_grass)},{np.var(hhs_oak + hhs_grass)},{np.median(hhs_oak + hhs_grass)},{int(stats.mode(hhs_oak + hhs_grass)[0])},{FindRange(hhs_oak + hhs_grass)}, \
		{sum(church_oak + church_grass)},{np.mean(church_oak + church_grass)},{np.var(church_oak + church_grass)},{np.median(church_oak + church_grass)},{int(stats.mode(church_oak + church_grass)[0])},{FindRange(church_oak + church_grass)},\
		{sum(dev_oak + dev_grass)},{np.mean(dev_oak + dev_grass)},{np.var(dev_oak + dev_grass)},{np.median(dev_oak + dev_grass)},{int(stats.mode(dev_oak + dev_grass)[0])},{FindRange(dev_oak + dev_grass)},\
		{sum(hhs_oak + hhs_grass + dev_oak + dev_grass + church_oak + church_grass)},{np.mean(hhs_oak + hhs_grass + dev_oak + dev_grass + church_oak + church_grass)},{np.var(hhs_oak + hhs_grass + dev_oak + dev_grass + church_oak + church_grass)},\
		{np.median(hhs_oak + hhs_grass + dev_oak + dev_grass + church_oak + church_grass)},{int(stats.mode(hhs_oak + hhs_grass + dev_oak + dev_grass + church_oak + church_grass)[0])},\
		{FindRange(hhs_oak + hhs_grass + dev_oak + dev_grass + church_oak + church_grass)}\n')
		sum_stats.write(f',Oak,{sum(hhs_oak)},{np.mean(hhs_oak)},{np.var(hhs_oak)},{np.median(hhs_oak)},{int(stats.mode(hhs_oak)[0])},{FindRange(hhs_oak)}, \
		{sum(church_oak)},{np.mean(church_oak)},{np.var(church_oak)},{np.median(church_oak)},{int(stats.mode(church_oak)[0])},{FindRange(church_oak)},\
		{sum(dev_oak)},{np.mean(dev_oak)},{np.var(dev_oak)},{np.median(dev_oak)},{int(stats.mode(dev_oak)[0])},{FindRange(dev_oak)}\n')
		sum_stats.write(f',Grass,{sum(hhs_grass)},{np.mean(hhs_grass)},{np.var(hhs_grass)},{np.median(hhs_grass)},{int(stats.mode(hhs_grass)[0])},{FindRange(hhs_grass)}, \
		{sum(church_grass)},{np.mean(church_grass)},{np.var(church_grass)},{np.median(church_grass)},{int(stats.mode(church_grass)[0])},{FindRange(church_grass)},\
		{sum(dev_grass)},{np.mean(dev_grass)},{np.var(dev_grass)},{np.median(dev_grass)},{int(stats.mode(dev_grass)[0])},{FindRange(dev_grass)}\n')
		# Aedes albopictus
		hhs_oak , hhs_grass , dev_oak , dev_grass , church_oak , church_grass = Infusion_Comparison_By_Date_Species_Site( gravid_trap_data , 'albopictus' )
		sum_stats.write(f'Aedes albopictus,Site Total,{sum(hhs_oak + hhs_grass)},{np.mean(hhs_oak + hhs_grass)},{np.var(hhs_oak + hhs_grass)},{np.median(hhs_oak + hhs_grass)},{int(stats.mode(hhs_oak + hhs_grass)[0])},{FindRange(hhs_oak + hhs_grass)}, \
		{sum(church_oak + church_grass)},{np.mean(church_oak + church_grass)},{np.var(church_oak + church_grass)},{np.median(church_oak + church_grass)},{int(stats.mode(church_oak + church_grass)[0])},{FindRange(church_oak + church_grass)},\
		{sum(dev_oak + dev_grass)},{np.mean(dev_oak + dev_grass)},{np.var(dev_oak + dev_grass)},{np.median(dev_oak + dev_grass)},{int(stats.mode(dev_oak + dev_grass)[0])},{FindRange(dev_oak + dev_grass)},\
		{sum(hhs_oak + hhs_grass + dev_oak + dev_grass + church_oak + church_grass)},{np.mean(hhs_oak + hhs_grass + dev_oak + dev_grass + church_oak + church_grass)},{np.var(hhs_oak + hhs_grass + dev_oak + dev_grass + church_oak + church_grass)},\
		{np.median(hhs_oak + hhs_grass + dev_oak + dev_grass + church_oak + church_grass)},{int(stats.mode(hhs_oak + hhs_grass + dev_oak + dev_grass + church_oak + church_grass)[0])},\
		{FindRange(hhs_oak + hhs_grass + dev_oak + dev_grass + church_oak + church_grass)}\n')
		sum_stats.write(f',Oak,{sum(hhs_oak)},{np.mean(hhs_oak)},{np.var(hhs_oak)},{np.median(hhs_oak)},{int(stats.mode(hhs_oak)[0])},{FindRange(hhs_oak)}, \
		{sum(church_oak)},{np.mean(church_oak)},{np.var(church_oak)},{np.median(church_oak)},{int(stats.mode(church_oak)[0])},{FindRange(church_oak)},\
		{sum(dev_oak)},{np.mean(dev_oak)},{np.var(dev_oak)},{np.median(dev_oak)},{int(stats.mode(dev_oak)[0])},{FindRange(dev_oak)}\n')
		sum_stats.write(f',Grass,{sum(hhs_grass)},{np.mean(hhs_grass)},{np.var(hhs_grass)},{np.median(hhs_grass)},{int(stats.mode(hhs_grass)[0])},{FindRange(hhs_grass)}, \
		{sum(church_grass)},{np.mean(church_grass)},{np.var(church_grass)},{np.median(church_grass)},{int(stats.mode(church_grass)[0])},{FindRange(church_grass)},\
		{sum(dev_grass)},{np.mean(dev_grass)},{np.var(dev_grass)},{np.median(dev_grass)},{int(stats.mode(dev_grass)[0])},{FindRange(dev_grass)}\n')
		# Culex restuans
		hhs_oak , hhs_grass , dev_oak , dev_grass , church_oak , church_grass = Infusion_Comparison_By_Date_Species_Site( gravid_trap_data , 'restuans' )
		sum_stats.write(f'Culex restuans,Site Total,{sum(hhs_oak + hhs_grass)},{np.mean(hhs_oak + hhs_grass)},{np.var(hhs_oak + hhs_grass)},{np.median(hhs_oak + hhs_grass)},{int(stats.mode(hhs_oak + hhs_grass)[0])},{FindRange(hhs_oak + hhs_grass)}, \
		{sum(church_oak + church_grass)},{np.mean(church_oak + church_grass)},{np.var(church_oak + church_grass)},{np.median(church_oak + church_grass)},{int(stats.mode(church_oak + church_grass)[0])},{FindRange(church_oak + church_grass)},\
		{sum(dev_oak + dev_grass)},{np.mean(dev_oak + dev_grass)},{np.var(dev_oak + dev_grass)},{np.median(dev_oak + dev_grass)},{int(stats.mode(dev_oak + dev_grass)[0])},{FindRange(dev_oak + dev_grass)},\
		{sum(hhs_oak + hhs_grass + dev_oak + dev_grass + church_oak + church_grass)},{np.mean(hhs_oak + hhs_grass + dev_oak + dev_grass + church_oak + church_grass)},{np.var(hhs_oak + hhs_grass + dev_oak + dev_grass + church_oak + church_grass)},\
		{np.median(hhs_oak + hhs_grass + dev_oak + dev_grass + church_oak + church_grass)},{int(stats.mode(hhs_oak + hhs_grass + dev_oak + dev_grass + church_oak + church_grass)[0])},\
		{FindRange(hhs_oak + hhs_grass + dev_oak + dev_grass + church_oak + church_grass)}\n')
		sum_stats.write(f',Oak,{sum(hhs_oak)},{np.mean(hhs_oak)},{np.var(hhs_oak)},{np.median(hhs_oak)},{int(stats.mode(hhs_oak)[0])},{FindRange(hhs_oak)}, \
		{sum(church_oak)},{np.mean(church_oak)},{np.var(church_oak)},{np.median(church_oak)},{int(stats.mode(church_oak)[0])},{FindRange(church_oak)},\
		{sum(dev_oak)},{np.mean(dev_oak)},{np.var(dev_oak)},{np.median(dev_oak)},{int(stats.mode(dev_oak)[0])},{FindRange(dev_oak)}\n')
		sum_stats.write(f',Grass,{sum(hhs_grass)},{np.mean(hhs_grass)},{np.var(hhs_grass)},{np.median(hhs_grass)},{int(stats.mode(hhs_grass)[0])},{FindRange(hhs_grass)}, \
		{sum(church_grass)},{np.mean(church_grass)},{np.var(church_grass)},{np.median(church_grass)},{int(stats.mode(church_grass)[0])},{FindRange(church_grass)},\
		{sum(dev_grass)},{np.mean(dev_grass)},{np.var(dev_grass)},{np.median(dev_grass)},{int(stats.mode(dev_grass)[0])},{FindRange(dev_grass)}\n')
		# Culex territans
		hhs_oak , hhs_grass , dev_oak , dev_grass , church_oak , church_grass = Infusion_Comparison_By_Date_Species_Site( gravid_trap_data , 'territans' )
		sum_stats.write(f'Culex territans,Site Total,{sum(hhs_oak + hhs_grass)},{np.mean(hhs_oak + hhs_grass)},{np.var(hhs_oak + hhs_grass)},{np.median(hhs_oak + hhs_grass)},{int(stats.mode(hhs_oak + hhs_grass)[0])},{FindRange(hhs_oak + hhs_grass)}, \
		{sum(church_oak + church_grass)},{np.mean(church_oak + church_grass)},{np.var(church_oak + church_grass)},{np.median(church_oak + church_grass)},{int(stats.mode(church_oak + church_grass)[0])},{FindRange(church_oak + church_grass)},\
		{sum(dev_oak + dev_grass)},{np.mean(dev_oak + dev_grass)},{np.var(dev_oak + dev_grass)},{np.median(dev_oak + dev_grass)},{int(stats.mode(dev_oak + dev_grass)[0])},{FindRange(dev_oak + dev_grass)},\
		{sum(hhs_oak + hhs_grass + dev_oak + dev_grass + church_oak + church_grass)},{np.mean(hhs_oak + hhs_grass + dev_oak + dev_grass + church_oak + church_grass)},{np.var(hhs_oak + hhs_grass + dev_oak + dev_grass + church_oak + church_grass)},\
		{np.median(hhs_oak + hhs_grass + dev_oak + dev_grass + church_oak + church_grass)},{int(stats.mode(hhs_oak + hhs_grass + dev_oak + dev_grass + church_oak + church_grass)[0])},\
		{FindRange(hhs_oak + hhs_grass + dev_oak + dev_grass + church_oak + church_grass)}\n')
		sum_stats.write(f',Oak,{sum(hhs_oak)},{np.mean(hhs_oak)},{np.var(hhs_oak)},{np.median(hhs_oak)},{int(stats.mode(hhs_oak)[0])},{FindRange(hhs_oak)}, \
		{sum(church_oak)},{np.mean(church_oak)},{np.var(church_oak)},{np.median(church_oak)},{int(stats.mode(church_oak)[0])},{FindRange(church_oak)},\
		{sum(dev_oak)},{np.mean(dev_oak)},{np.var(dev_oak)},{np.median(dev_oak)},{int(stats.mode(dev_oak)[0])},{FindRange(dev_oak)}\n')
		sum_stats.write(f',Grass,{sum(hhs_grass)},{np.mean(hhs_grass)},{np.var(hhs_grass)},{np.median(hhs_grass)},{int(stats.mode(hhs_grass)[0])},{FindRange(hhs_grass)}, \
		{sum(church_grass)},{np.mean(church_grass)},{np.var(church_grass)},{np.median(church_grass)},{int(stats.mode(church_grass)[0])},{FindRange(church_grass)},\
		{sum(dev_grass)},{np.mean(dev_grass)},{np.var(dev_grass)},{np.median(dev_grass)},{int(stats.mode(dev_grass)[0])},{FindRange(dev_grass)}\n')
		sum_stats.close()

SummaryStatsTable()