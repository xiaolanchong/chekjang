# Script to create a page of links to text files
import os.path
import re
from collections import OrderedDict
from pathlib import Path
import urllib.parse


def encode_url(url):
    # preserve names
    url = url.replace(' ', '%20')
    url = url.replace('[', urllib.parse.quote_plus('['))
    url = url.replace(']', urllib.parse.quote_plus(']'))
    return url


def get_files_by_author(dir_name):
    authors = OrderedDict()
    for path in Path(dir_name).rglob('*.txt'):
        relpath = path.relative_to(dir_name)
        base, *rest = relpath.parts
        author_files = authors.setdefault(base, [])
        work = Path(relpath.stem).as_posix()
        url = encode_url(Path(relpath).as_posix())
        author_files.append((work, url))
    return authors


def get_file_links(files_by_author):
    template = '   <li><a href="{file_name}">{work_name}</a></li>\n'
    contents = ''
    for author, his_files in files_by_author.items():
        contents += '\n'
        contents += '<h2>{}</h2>\n'.format(author)
        contents += '<div><a href="">Wikipedia</a></div>\n'
        contents += '<ul>\n'

        for work_name, html_file_name in his_files:
            list_item = template.format(file_name=html_file_name, work_name=work_name)
            contents += list_item

        contents += '</ul>\n'
    return contents


author_dict = get_files_by_author(r'f:\wodetien\Korean\chekjang\foreign\classics')
contents = get_file_links(author_dict)
print(contents)
