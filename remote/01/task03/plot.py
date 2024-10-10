import os
import pandas as pd
import matplotlib.pyplot as plt

def read_data_df(dir):
    files = os.listdir(dir)
    with open(f'{dir}/{files[0]}') as f:
        raw = f.read()
    data = [[x.split(' ')[0], float(x.split(' ')[-1])] for x in raw.splitlines()[2:]]
    df = pd.DataFrame(data)
    df.set_index(0, inplace=True)
    for i, file in enumerate(files[1:]):
        with open(f'{dir}/{file}') as f:
            raw = f.read()
        data = [float(x.split(' ')[-1]) for x in raw.splitlines()[2:]]
        df[i+2] = data
    return df

cl = read_data_df('./cores/latency')
sl = read_data_df('./sockets/latency/')
nl = read_data_df('./nodes/latency/')

cb = read_data_df('./cores/bandwidth')
sb = read_data_df('./sockets/bandwidth/')
nb = read_data_df('./nodes/bandwidth/')

fig, axs = plt.subplots(ncols=3, nrows=2, figsize=(11,5))

# axs[0].set_xticks(range(len(bw.index)))
# axs[0].set_xticklabels(bw.index, rotation=45)
cl.plot(ax=axs[0][0], legend=False)
axs[0][0].set_title('Cores')
axs[0][0].set_ylabel('Latency')
axs[0][0].set_ylim(top=int(nl.max().max())+10)

sl.plot(ax=axs[0][1], legend=False)
axs[0][1].set_title('Sockets')
axs[0][1].set_ylim(top=int(nl.max().max())+10)

nl.plot(ax=axs[0][2], legend=False)
axs[0][2].set_title('Nodes')
axs[0][2].set_ylim(top=int(nl.max().max())+10)

cb.plot(ax=axs[1][0], legend=False)
axs[1][0].set_ylabel('Bandwidth')
sb.plot(ax=axs[1][1], legend=False)
nb.plot(ax=axs[1][2], legend=False)

plt.savefig('consistency.jpg')
