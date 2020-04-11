#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pprint import pprint

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}
Moskow = sites['Moscow']
London = sites['London']
Paris = sites['Paris']


# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = dict()

Moskow_London = ((Moskow[0] - London[0]) ** 2 + (Moskow[1] - London[1]) **2) ** .5
Moskow_Paris = ((Moskow[0] - Paris[0]) ** 2 + (Moskow[1] - Paris[1]) **2) ** .5
London_Paris = ((London[0] - Paris[0]) ** 2 + (London[1] - Paris[1]) **2) ** .5

distances['Moskow'] = {}
distances['Moskow']['London'] = Moskow_London
distances['Moskow']['Paris'] = Moskow_Paris

distances['London'] = {}
distances['London']['Moskow'] = Moskow_London
distances['London']['Paris'] = London_Paris

distances['Paris'] = {}
distances['Paris']['Moskow'] = Moskow_Paris
distances['Paris']['London'] = London_Paris


pprint(distances)




