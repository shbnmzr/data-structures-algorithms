import time


def find_nemo(array):
    for i in array:
        if i == 'nemo':
            print('Found NEMO!')
    return


def measure_performance(func, *args):
    start = time.time()
    func(*args)
    end = time.time()
    print(f'Duration: {end - start}')


def main():
    nemo = [1000000000 * 'someone', 'nemo']
    measure_performance(find_nemo, nemo)


if __name__ == '__main__':
    main()
