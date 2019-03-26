from qtrf.units import prefix_map

units      = 'A'
prefix_map = prefix_map.copy()
del(prefix_map['K'])
del(prefix_map['M'])
del(prefix_map['G'])
del(prefix_map['T'])
