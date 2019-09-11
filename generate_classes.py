#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import json
from re import compile
from six.moves.urllib.request import urlopen

github_user = 'Palakis'
github_repo = 'obs-websocket'
github_branch = '4.x-current'
github_path = 'docs/generated/comments.json'

caps = compile('(?<![A-Z])([A-Z])')


def clean_var(string):
    """
    Converts a string to a suitable variable name by using snake case and
    replacing - by _.
    """
    return caps.sub(r'_\1', string).lower().lstrip('_').replace('-', '_')


def generate_classes():
    """Generates the necessary classes."""
    import_url = 'https://raw.githubusercontent.com/{}/{}/{}/{}'.format(
        github_user, github_repo, github_branch, github_path)
    print("Downloading {} for last API version.".format(import_url))
    data = json.loads(urlopen(import_url).read().decode('utf-8'))
    print("Download OK. Generating python files...")

    for kinds in ['requests', 'events']:
        if kinds not in data:
            raise Exception("Missing {} in data.".format(kinds))
        kind = kinds.rstrip('s').title()
        with open('pyobs/{}.py'.format(kinds), 'w') as f:

            f.write("#!/usr/bin/env python\n")
            f.write("# -*- coding: utf-8 -*-\n")
            f.write("\n")
            f.write("# THIS FILE WAS GENERATED BY generate_classes.py - "
                    "DO NOT EDIT #\n")
            f.write("# (Generated on {}) #\n".format(
                datetime.now().isoformat(" ")))
            f.write("\n")
            f.write("from .base_classes import Base{}\n".format(kind))
            f.write("\n\n")
            for sec in sorted(data[kinds]):
                for i in data[kinds][sec]:
                    f.write("class {}(Base{}):\n".format(i['name'], kind))
                    f.write("    \"\"\"\n")
                    f.write("    {}\n".format(
                        i['description'].replace('\n', '\n    ')))

                    if (
                            ('returns' in i) and (len(i['returns']) > 0)
                    ) or (
                            ('params' in i) and (len(i['params']) > 0)
                    ):
                        f.write("\n")

                    arguments_default = []
                    arguments = []
                    try:
                        if len(i['params']) > 0:
                            f.write("    :Arguments:\n")
                            for a in i['params']:
                                f.write("       *{}*\n".format(
                                    clean_var(a['name'])))
                                f.write("            type: {}\n".format(
                                    a['type']))
                                f.write("            {}\n".format(
                                    a['description']))
                                if '.' in a['name']:
                                    # If the name contains a . it is
                                    # describing a field of an object, we do
                                    # not need to create variables, storage
                                    # or accessors, just document it
                                    continue
                                if '[]' in a['name']:
                                    # If the name contains a [] it is
                                    # describing the items of an array, we do
                                    # not need to create variables, storage
                                    # or accessors, just document it
                                    continue
                                if 'optional' in a['type']:
                                    arguments_default.append(a['name'])
                                else:
                                    arguments.append(a['name'])
                    except KeyError:
                        pass

                    returns = []
                    try:
                        if len(i['returns']) > 0:
                            f.write("    :Returns:\n")
                            for r in i['returns']:
                                f.write("       *{}*\n".format(
                                    clean_var(r['name'])))
                                f.write("            type: {}\n".format(
                                    r['type']))
                                f.write("            {}\n".format(
                                    r['description']))
                                if '.' in r['name']:
                                    # If the name contains a . it is
                                    # describing a field of an object, we do
                                    # not need to create variables, storage
                                    # or accessors, just document it
                                    continue
                                # .*. are used to describe arrays that are
                                # already being captured by the above filter
                                returns.append(r['name'])
                    except KeyError:
                        pass

                    f.write("    \"\"\"\n")
                    f.write("    def __init__({}):\n".format(
                        ", ".join(
                            ["self"] +
                            [clean_var(a) for a in arguments] +
                            [clean_var(a) + "=None" for a in arguments_default]
                        )
                    ))
                    f.write("        Base{}.__init__(self)\n".format(kind))
                    f.write("        self._name = '{}'\n".format(i['name']))
                    for r in returns:
                        f.write("        self._returns['{}'] = None\n".format(
                            r))
                    for a in arguments:
                        f.write("        self._params['{}'] = {}\n".format(
                            a, clean_var(a)))
                    for a in arguments_default:
                        f.write("        self._params['{}'] = {}\n".format(
                            a, clean_var(a)))
                    f.write("\n")
                    for r in returns:
                        f.write("    @property\n")
                        f.write("    def {}(self):\n".format(clean_var(r)))
                        f.write("        return self._returns['{}']\n".format(
                            r))
                        f.write("\n")
                    f.write("\n")

    print("API classes have been generated.")


if __name__ == '__main__':
    generate_classes()
