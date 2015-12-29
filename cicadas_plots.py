import matplotlib.pyplot as plt
# from sys import argv

# filename = argv[1]


# dataf = open(filename, 'r')

for c in range(13, 22):
    dataf = open('Hybrid Theory\Results\Experiments 13 - 15\Spreadsheets\cicadas-hybrid Experiment ' + str(c) + '.csv', 'r')
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
            plt.savefig('Hybrid Theory\Results\Experiments 13 - 15\Plots\Experiment ' + str(c) + ' - ' + str(i + 1) + '.png')
            result_hist.append(plot_data)
        except ValueError:
            plt.clf()
            plt.savefig('Hybrid Theory\Results\Experiments 13 - 15\Plots\Experiment ' + str(c) + ' - ' + str(i + 1) + '.png')

    result_hist = map((lambda x: list(set(x))), result_hist)
    result_hist = [x[0] for x in result_hist if len(x) == 1]

    n = len(result_hist)
    m = max(set(result_hist), key=result_hist.count)

    plt.clf()
    plt.hist(result_hist)
    plt.title('Experiment ' + str(c))
    plt.suptitle('n =' + str(n) + ' Winner =' + str(m), fontsize=12)
    plt.xlabel('Lifecycle duration (years)')
    plt.ylabel('Frequency')
    plt.savefig('Hybrid Theory\Results\Experiments 13 - 15\Plots\Experiment ' + str(c) + '.png')

    dataf.close()
