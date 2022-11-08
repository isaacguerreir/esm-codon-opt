import pandas as pd
import numpy as np
import statistics

microarray_names = [
    'TBioassayData-1628.tsv',
    'TBioassayData-1629.tsv',
    'TBioassayData-1630.tsv',
    'TBioassayData-2063.tsv',
    'TBioassayData-2064.tsv',
    'TBioassayData-2065.tsv'
]

microarray_assays = []

for microarray_name in microarray_names:
  df = pd.read_csv(microarray_name, '\t')
  df.set_index("Reporter", inplace = True)
  microarray_assays.append(df)

assays_identifiers = pd.read_csv('assays-ids-k12.csv')

def getFromAssays(id):
  values = []
  for assay in microarray_assays:
    values.append(assay.loc[[id]].values[0][0])
  return(statistics.mean(values))
