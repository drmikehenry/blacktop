#!/usr/bin/env python3

import black
from black import *
import re

__version__ = '0.1.0'


def _get_func_def(func_name):
    source = open(black.__file__).read()
    parts = re.split(r'^def\s+', source, flags=re.MULTILINE)
    matches = ['def ' + m for m in parts if m.startswith(func_name + '(')]
    if len(matches) == 1:
        return matches[0].strip() + '\n'
    raise RuntimeError('missing function {}'.format(func_name))


def main():
    func_name = 'normalize_string_quotes'
    old_text = """   orig_quote == '"':   """.strip()
    new_text = """   orig_quote == "'":   """.strip()
    exec(_get_func_def(func_name).replace(old_text, new_text))
    black.normalize_string_quotes = vars()[func_name]
    return black.main()
