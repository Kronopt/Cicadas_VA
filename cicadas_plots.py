import matplotlib.pyplot as plt

# linha, no ficheiro csv, onde esta a informacao que se quer utilizar
l = 29

# o valor c vai correspondre ao numero do ficheiro. ver linha 9.
for c in [16]:
    # abre ficheiro csv, correspondentes aos resultados de um Experiment
    dataf = open('Hybrid + Predator\Results\Hybrid Theory\Spreadsheets\cicadas-hybrid-predators Experiment Hybrid ' + str(c) + '.csv', 'r')
    data = dataf.readlines()

    data = data[l-1][2:-1].split('","')

    result_hist = []

    # faz um grafico por run
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
            # guarda o grafico correspondente a esta run
            plt.savefig('Hybrid + Predator\Results\Hybrid Theory\Plots\cicadas-hybrid-predators Experiment Hybrid ' + str(c) + ' - ' + str(i + 1) + '.png')
            result_hist.append(plot_data)
        # Ja nao me lembro para que e que isto era. Mas acho que era para quando nao havia nenhumas cicadas no final da run -
        # quando isso acontece, uma das funcoes atira um ValueError. Nesses caso, crio um grafico vazio.
        except ValueError:
            plt.clf()
            plt.savefig('Hybrid + Predator\Results\Hybrid Theory\Plots\cicadas-hybrid-predators Experiment Hybrid ' + str(c) + ' - ' + str(i + 1) + '.png')

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
    # guarda o grafico que corresponde a sumarizacao de todas as runs
    plt.savefig('Hybrid + Predator\Results\Hybrid Theory\Plots\cicadas-hybrid-predators Experiment Hybrid ' + str(c) + '.png')

    dataf.close()
