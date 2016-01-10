import matplotlib.pyplot as plt

# linha, no ficheiro csv, onde está a informação que se quer utilizar
n = 27


for c in [26, 27]:
    # abre ficheiro csv, correspondentes aos resultados de um Experiment
    dataf = open('Hybrid + Predator\Results\Experiments 26 - 27\Spreadsheets\cicadas-hybrid-predators Experiment ' + str(c) + '.csv', 'r')
    data = dataf.readlines()

    data = data[n-1][2:-1].split('","')

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
            print plot_data
            plt.hist(plot_data, bins=maxduration)
            plt.xlabel('Lifecycle duration (years)')
            plt.ylabel('Number of Cicadas')
            plt.xticks(range(minduration, maxduration + 1))
            # guarda o gráfico correspondente a esta run
            plt.savefig('Hybrid + Predator\Results\Experiments 26 - 27\Plots\Experiment ' + str(c) + ' - ' + str(i + 1) + '.png')
            result_hist.append(plot_data)
        except ValueError:
            plt.clf()
            plt.savefig('Hybrid + Predator\Results\Experiments 26 - 27\Plots\Experiment ' + str(c) + ' - ' + str(i + 1) + '.png')

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
    # guarda o gráfico que corresponde à sumarização de todas as runs
    plt.savefig('Hybrid + Predator\Results\Experiments 26 - 27\Plots\Experiment ' + str(c) + '.png')

    dataf.close()
