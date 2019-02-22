#!/usr/bin/env python3

import pandas
import numpy

nodes = pandas.read_csv('nodes.csv')
ga = pandas.read_csv('ga.csv')

ga = ga.merge(nodes, how='left', left_on='Page', right_on='Path')
ga = ga.merge(nodes, how='left', left_on='Page', right_on='Path - NID')

for column in nodes:
  ga[column] = ga[column+'_x'].combine(ga[column+'_y'], lambda a, b: a if isinstance(a, str) or not numpy.isnan(a) else b, None)
  ga = ga.drop(columns=[
    column + '_x',
    column + '_y'
  ])

ga.to_csv('out.csv')