from markdown import markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape
import os
import argparse
import json

HTML_ARTICLE_DIR = './site/articles/'
INDEX_PAGE_LOC = './site/index.html'


def parse_args():
    parser = argparse.ArgumentParser(description='The script creates a static encyclopedia website from json config '
                                                 'file and a folder ./articles with Jinja2 template engine.')
    parser.add_argument('config', help='Path to JSON config file.')
    return parser.parse_args()


def check_dir(dir_path):
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)


def get_templates():
    env = Environment(
        loader=FileSystemLoader('templates'),
        autoescape=['xml', 'html']
    )
    return env.get_template('article_template.html'), env.get_template('index_template.html')


def make_html_path(source_path):
    html_path = '{}{}.html'.format(HTML_ARTICLE_DIR, source_path.split('.')[0])
    return html_path


def get_html_from_markdown(path):
    with open(path, 'r', encoding='utf-8') as md_handler:
        return markdown(md_handler.read(), extensions=['codehilite', 'fenced_code'])


def make_dir_path(path):
    dirs = path.split('/')[:-1]
    return '/'.join(dirs)


def generate_html_articles(template, config):

    for article in config['articles']:
        article_path = './articles/{}'.format(article['source'])
        html_path = make_html_path(article['source'])
        dir_path = make_dir_path(html_path)
        check_dir(dir_path)
        article_html = get_html_from_markdown(article_path)
        data = {
            'name': article['title'],
            'topic': article['topic'],
            'index_path': INDEX_PAGE_LOC,
            'html': article_html,
        }
        with open(html_path, mode='w', encoding='utf-8') as html_source:
            html_source.write(template.render(data))


def generate_index_file(template, config):
    template.globals['make_html_path'] = make_html_path
    data = {
        'name': 'Содержание',
        'topics': config['topics'],
        'index_path': INDEX_PAGE_LOC,
        'articles': config['articles'],
    }
    with open(INDEX_PAGE_LOC, mode='w', encoding='utf-8') as html_source:
        html_source.write(template.render(data))


def load_config(config_file_path):
    with open(config_file_path) as json_handler:
        return json.load(json_handler)


if __name__=='__main__':

    args = parse_args()
    article_template, index_template = get_templates()
    config_json = load_config(args.config)
    generate_html_articles(article_template, config_json)
    generate_index_file(index_template, config_json)

