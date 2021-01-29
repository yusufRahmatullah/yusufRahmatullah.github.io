import os

from jinja2 import Environment, FileSystemLoader


def url_for(folder, filename=''):
    return os.path.join(folder, filename)


def generate_html(env, root, template_name):
    template = env.get_template('index.html')

    filename = os.path.join(root, 'index.html')
    with open(filename, 'w') as f:
        f.write(template.render())


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(root, 'templates')
    env = Environment(loader=FileSystemLoader(templates_dir))
    env.globals.update({
        'url_for': url_for,
    })
    with open('generate_list.txt') as f:
        lines = f.read().splitlines()
    for line in lines:
        generate_html(env, root, lines)


if __name__ == '__main__':
    main()
