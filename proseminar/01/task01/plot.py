import pandas as pd
import matplotlib.pyplot as plt

def read_data_df(file):
    with open(file) as f:
        raw = f.read()
    data = [[x.split(' ')[0], float(x.split(' ')[-1])] for x in raw.splitlines()[2:]]
    df = pd.DataFrame(data)
    df.set_index(0, inplace=True)
    return df

bw = read_data_df('./bandwidth.log')
lat = read_data_df('./latency.log')

fig, axs = plt.subplots(ncols=2, nrows=1, figsize=(13,6))

bw.plot(ax=axs[0], legend=False, grid=True)
lat.plot(ax=axs[1], legend=False, grid=True)

# Set xticks for both subplots
axs[0].set_title('Bandwidth (MB/s)')
axs[0].set_xticks(range(len(bw.index)))
axs[0].set_xticklabels(bw.index, rotation=45)
axs[0].set_xlabel('MB/s')
axs[0].set_ylabel('Size')

axs[1].set_title('Latency (us)')
axs[1].set_xticks(range(len(lat.index)))
axs[1].set_xticklabels(lat.index, rotation=45)
axs[0].set_xlabel('us')
axs[0].set_ylabel('Size')

plt.savefig('plot.jpg')
