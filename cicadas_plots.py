import matplotlib.pyplot as plt
# from sys import argv

# filename = argv[1]

# dataf = open(filename, 'r')
dataf = open('Simulation_Data\cicadas-hybrid Experiment 2-spreadsheet 4', 'r')
data = dataf.readlines()

data = data[16][2:-1].split('","')

for i in range(0, len(data)):
    plot_data = data[i][2:-2].split()

    if i == len(data) - 1:
        plot_data[-1] = plot_data[-1].replace(']', '')

    plot_data = map(int, plot_data)

    try:
        maxduration = max(plot_data)
        minduration = min(plot_data)

        plt.clf()
        plt.hist(plot_data, bins=maxduration)
        plt.xlabel('Lifecycle duration (years)')
        plt.ylabel('Number of Cicadas')
        plt.xticks(range(minduration, maxduration + 1))
        plt.savefig('Plots\\Esperiencia 4' + str(i + 1) + '.png')
    except ValueError:
        plt.clf()
        plt.savefig('Plots\\Esperiencia 4' + str(i + 1) + '.png')

dataf.close()
