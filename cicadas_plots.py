import matplotlib.pyplot as plt
# from sys import argv

# filename = argv[1]


# dataf = open(filename, 'r')
dataf = open('Hybrid Theory\Results\Experiment 7 - 12\Spreadsheet\cicadas-hybrid Experiment 12.csv', 'r')
data = dataf.readlines()

data = data[17][2:-1].split('","')

result_hist = []

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
        plt.savefig('Hybrid Theory\Results\Experiment 7 - 12\Plots\Experiment 12 - ' + str(i + 1) + '.png')
        result_hist.append(plot_data)
    except ValueError:
        plt.clf()
        plt.savefig('Hybrid Theory\Results\Experiment 7 - 12\Plots\Experiment 12 - ' + str(i + 1) + '.png')


result_hist = map((lambda x: list(set(x))), result_hist)
result_hist = [x[0] for x in result_hist if len(x) == 1]

n = len(result_hist)

plt.clf()
plt.hist(result_hist)
plt.title('Experiment 12')
plt.suptitle('n =' + str(n), fontsize=12)
plt.xlabel('Lifecycle duration (years)')
plt.ylabel('Frequency')
plt.savefig('Hybrid Theory\Results\Experiment 7 - 12\Plots\Experiment 12.png')


dataf.close()
