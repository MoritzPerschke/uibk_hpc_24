import os
import pandas as pd
import matplotlib.pyplot as plt

def read_data_df(file):
    with open(f'{file}.log') as f:
        raw = f.read()
    data = [[x.split(' ')[0], float(x.split(' ')[-1])] for x in raw.splitlines()[2:]]
    df = pd.DataFrame(data)
    df.set_index(0, inplace=True)
    return df

cl = read_data_df('./latency/cores')
sl = read_data_df('./latency/sockets')
nl = read_data_df('./latency/nodes')

cb = read_data_df('./bandwidth/cores')
sb = read_data_df('./bandwidth/sockets')
nb = read_data_df('./bandwidth/nodes')

fig, axs = plt.subplots(ncols=3, nrows=2, figsize=(12,5))

# axs[0].set_xticks(range(len(bw.index)))
# axs[0].set_xticklabels(bw.index, rotation=45)
cl.plot(ax=axs[0][0], legend=False, grid=True)
axs[0][0].set_title('Cores')
axs[0][0].set_ylabel('Latency')
axs[0][0].set_ylim(top=int(nl.max().max())+10)
axs[0][0].set_xticks(range(len(nl.index)))
axs[0][0].set_xlabel('')

sl.plot(ax=axs[0][1], legend=False, grid=True)
axs[0][1].set_xticks(range(len(nl.index)))
axs[0][1].set_title('Sockets')
axs[0][1].set_xlabel('')
axs[0][1].set_ylim(top=int(nl.max().max())+10)

nl.plot(ax=axs[0][2], legend=False, grid=True)
axs[0][2].set_xticks(range(len(nl.index)))
axs[0][2].set_title('Nodes')
axs[0][2].set_xlabel('')
axs[0][2].set_ylim(top=int(nl.max().max())+10)

cb.plot(ax=axs[1][0], legend=False, grid=True)
axs[1][0].set_xticks(range(len(nb.index)))
axs[1][0].set_ylabel('Bandwidth')
axs[1][0].set_xlabel('')

sb.plot(ax=axs[1][1], legend=False, grid=True)
axs[1][1].set_xticks(range(len(nb.index)))
axs[1][1].set_xlabel('')

nb.plot(ax=axs[1][2], legend=False, grid=True)
axs[1][2].set_xticks(range(len(nb.index)))
axs[1][2].set_xlabel('')

plt.savefig('plot.jpg')
