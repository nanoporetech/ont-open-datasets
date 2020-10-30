from concurrent.futures import ProcessPoolExecutor

import pandas as pd

import aplanat.util
from aplanat import lines
from aplanat.layouts import facet_grid
from aplanat.report import HTMLReport


def read_data(args):
    caller, filename = args
    df = pd.read_csv(filename, sep='\t')
    xs, ys = aplanat.util.kernel_density_estimate(df['acc'], step=0.05)
    df = pd.DataFrame({'accuracy':xs, 'density':ys})
    df['caller'] = caller
    return df

data_sets = {
    'bonito': 'bonito.stats',
    'guppy': 'guppy.stats'}

with ProcessPoolExecutor() as executor:
    report = HTMLReport("Basecalling Accuracy Summary", "GM24385")
    dfs = list(executor.map(read_data, data_sets.items()))
plot = lines.line(
    [df['accuracy'] for df in dfs],
    [df['density'] for df in dfs],
    colors=['red', 'blue'],
    names=['bonito', 'guppy'],
    xlim=(85,100),
    x_axis_label='Alignment accuracy',
    y_axis_label='Density')
plot.legend.location = 'top_left'
report.plot(plot)
report.write("report.html")
