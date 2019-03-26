# -*- coding: utf-8 -*-
from qtrf.units import prefix_map

units      = 'Ω'
prefix_map = prefix_map.copy()
del(prefix_map['M'])
del(prefix_map['G'])
del(prefix_map['T'])
