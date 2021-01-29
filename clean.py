import os


def remove_file(file):
    os.system(f'rm {file}')

def main():
    with open('generate_list.txt') as f:
        lines = f.read().splitlines()
    for line in lines:
        remove_file(line)


if __name__ == '__main__':
    main()
