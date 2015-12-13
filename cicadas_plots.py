import matplotlib.pyplot as plt

data = open('Simulation_Data\cicadas.csv', 'r').readlines()

data = data[15][2:-1].split('","')

for i in range(0, len(data)):
    plot_data = data[i][2:-2].split()

    if i == len(data) - 1:
        plot_data[-1] = plot_data[-1].replace(']', '')

    plot_data = map(int, plot_data)

    maxduration = max(plot_data)
    minduration = min(plot_data)

    plt.clf()
    plt.hist(plot_data, bins=maxduration)
    plt.xlabel('Lifecycle duration (years)')
    plt.ylabel('Number of Cicadas')
    plt.xticks(range(minduration, maxduration + 1))
    plt.savefig('Plots\\test' + str(i + 1) + '.png')

data.close()
