import qtrf.units

prefix_map = qtrf.units.prefix_map.copy()
del(prefix_map['f'])
del(prefix_map['p'])
del(prefix_map['n'])
del(prefix_map['m'])

units = 'Hz'
