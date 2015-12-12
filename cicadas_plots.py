import matplotlib.pyplot as plt

data = open('Simulation_Data\cicadas.csv', 'r').readlines()

data = data[15][2:-1].split('","')

for i in range(0, len(data)):
    plot_data = data[i][2:-2].split()

    if i == len(data) - 1:
        plot_data[-1] = plot_data[-1].replace(']', '')

    plot_data = map(int, plot_data)

    nbins = max(plot_data)

    plt.clf()
    plt.hist(plot_data, bins=nbins)
    plt.xlabel('Lifecycle duration (years)')
    plt.ylabel('Number of Cicadas')
    plt.xticks(range(1, nbins + 1))
    plt.savefig('Plots\\test' + str(i + 1) + '.png')
