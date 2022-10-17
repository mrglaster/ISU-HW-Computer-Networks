import os


powers = {}

def process_key(value):
    """Обновляет данные по степеням вершин"""
    if value not in powers.keys():
        powers[value] = 1
    else:
        powers[value] += 1

def write_powers(filename):
    """Пишет данные о степенях вершин в текстовый файл"""
    if len(powers.keys()) == 0 or len(powers.values()) == 0:
        raise ValueError("Something is wrong with dict")
    print(f"Detected vertexs: {len(powers.keys())}")
    filename_new = filename[:len(filename)-4]+"_results.txt"
    with open(filename_new, "w") as f:
        for i in powers.values():
            f.write(str(i)+'\n')
    powers.clear()


def parse_graph(input_file):
    """Обрабатывает текстовый файл с данными формта vertex_a vertex_b и обновляет данные по степеням вершин"""
    if not os.path.exists(input_file):
        raise FileExistsError(f"File not found: {input_file} ")
    with open(input_file) as f:
        for line in f:
            inner_list = [elt.strip() for elt in line.split(' ')]
            process_key(inner_list[0])
            process_key(inner_list[1])
    write_powers(input_file)


def main():
    parse_graph('test1.txt')
    parse_graph('test2.txt')

if __name__ == '__main__':
    main()