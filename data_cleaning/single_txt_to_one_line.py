import re



if __name__ == '__main__':
    corpus = ""

    with open(r"C:\Users\叫乌鸦的少年怪\Desktop\328.txt", 'r', encoding='utf-8') as f:
        data = f.read()
        corpus = re.sub('\n', "", data)
    print(corpus)