from time import sleep
from threading import Thread

tasks = []
for i in range(10):
    tasks.append(f"movie{i}")

def download(movie):
    """

    :param movie:
    :return:
    """
    print(f"start downloadwing {movie}")
    sleep(4)
    print(f"finished downloading {movie}")


if __name__ == '__main__':
    a = 'https'
    print(a[0:4])