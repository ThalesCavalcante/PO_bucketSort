import timeit
from random import randint
import matplotlib.pyplot as plt
import sys
from random import shuffle

sys.setrecursionlimit(10 ** 6)


def desenhaGrafico(x, y, xl="Entradas", yl="Saidas", name="out"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label="Melhor Tempo")
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(name)


def geraLista(tam):
    lista = list(range(1, tam + 1))
    shuffle(lista)
    return lista


def bucketSort(list):
    largest = max(list)
    length = len(list)
    size = largest/length

    buckets = [[] for _ in range(length)]
    for i in range(length):
        j = int(list[i]/size)
        if j != length:
            buckets[j].append(list[i])
        else:
            buckets[length - 1].append(list[i])

    for i in range(length):
        insertion_sort(buckets[i])

    result = []
    for i in range(length): 
        result = result + buckets[i]

    return result


def insertion_sort(list):
    for i in range(1, len(list)):
        temp = list[i]
        j = i - 1
        while (j >= 0 and temp < list[j]):
            list[j + 1] = list[j]
            j = j - 1
        list[j + 1] = temp


size = [10000, 20000, 40000, 50000, 100000, 200000]
time = []

for s in size:
    lista = geraLista(s)
    time.append(timeit.timeit("bucketSort({})".format(lista),
                              setup="from __main__ import bucketSort", number=1))
    print(s)

desenhaGrafico(size, time, "Tamanho", "Tempo",
               "bucketSort.png")