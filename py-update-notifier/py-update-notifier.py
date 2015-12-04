#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import semver

from pipita.pipita import info
from termcolor import colored


def latest_version(pkg_name):
    version = info(pkg_name).latest_version
    return version


def compare(current, latest):
    return semver.compare(current, latest)


def notify(pkg_name, current, latest):
    line1 = ' Update available: ' + \
        colored(latest, 'green') + ' (current: ' + current + ')' + ' '
    line2 = ' Run ' + \
        colored('pip install --upgrade ' + pkg_name, 'blue') + ' to update. '
    width = max(len(line1), len(line2))
    line1rest = width - len(line1)
    line2rest = width - len(line2)
    top = colored('┌' + '─'*width + '┐', 'yellow')
    bottom = colored('└' + '─'*width + '┘', 'yellow')
    side = colored('│', 'yellow')

    message = '\n\n' + top + '\n' + side + line1 + ' '*line1rest + side + \
        '\n' + side + line2 + ' '*line2rest + side + '\n' + bottom + '\n'
    print message


def check(pkg_name, current_version):
    latest = latest_version(pkg_name)
    n = compare(current_version, latest)
    if n < 0:
        notify(pkg_name, current_version, latest)
