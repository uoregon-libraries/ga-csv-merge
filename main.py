#!/usr/bin/env python3

import pandas
import numpy

# Configure which columns need to be summed and collapsed when finding duplicate rows
columns_to_sum = [
  'Pageviews',
  'Unique Pageviews',
]

nodes = pandas.read_csv('nodes.csv')
ga = pandas.read_csv('ga.csv')

# Merge Drupal and GA data
ga = ga.merge(nodes, how='left', left_on='Page', right_on='Path')
ga = ga.merge(nodes, how='left', left_on='Page', right_on='Path - NID')

# Collapse _x and _y columns via data presence heuristic
for column in nodes:
  ga[column] = ga[column+'_x'].combine(ga[column+'_y'], lambda a, b: a if isinstance(a, str) or not numpy.isnan(a) else b, None)
  ga = ga.drop(columns=[
    column + '_x',
    column + '_y'
  ])

# Find rows in GA data that are actually duplicates
for index, row in nodes.iterrows():
  rows = ga.loc[ga['Path - NID'] == row['Path - NID']]
  # Look for rows in GA that are for /node/<nid> but actually have an alias
  if rows.shape[0] > 1 and not row['Path'].startswith('/node/'):
    path_index = ga.loc[ga['Page'] == row['Path']].index
    node_index = ga.loc[ga['Page'] == row['Path - NID']].index
    total = rows.sum()
    # Insert the summed data for the to-sum columns
    for column in columns_to_sum:
      ga.loc[path_index, column] = total[column]
    # Drop the duplicate, unaliased row
    ga = ga.drop(node_index)

# Dump to CSV
ga.to_csv('out.csv')
