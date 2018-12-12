"""
Project:     hqf
Homepage:    https://github.com/olivierpons/weechat_hqf/
Description: Sends quickly different states of current user.
License:     MIT (see below)

Copyright (c) 2019 by Olivier Pons <olivier.pons@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os
import re
import subprocess
import sys
import time


# Ensure that we are running under WeeChat.
try:
    import weechat
except ImportError:
    sys.exit('This script has to run under WeeChat (https://weechat.org/).')


# Name of the script.
SCRIPT_NAME = 'hqf'

# Author of the script.
SCRIPT_AUTHOR = 'olivierpons'

# Version of the script.
SCRIPT_VERSION = '0.1'

# License under which the script is distributed.
SCRIPT_LICENSE = 'MIT'

# Description of the script.
SCRIPT_DESC = 'Sends quickly different states of current user.'

# Name of a function to be called when the script is unloaded.
SCRIPT_SHUTDOWN_FUNC = ''

# Used character set (utf-8 by default).
SCRIPT_CHARSET = ''

# Script options.
OPTIONS = {
    'set_away': (
        'off',
        'Sets current user as away'
    ),
}

def add_default_value_to(description, default_value):
    """Adds the given default value to the given option description."""
    # All descriptions end with a period, so do not add another period.
    return '{} Default: {}.'.format(description,
                                    default_value if default_value else '""')


if __name__ == '__main__':
    # Registration.
    weechat.register(
        SCRIPT_NAME,
        SCRIPT_AUTHOR,
        SCRIPT_VERSION,
        SCRIPT_LICENSE,
        SCRIPT_DESC,
        SCRIPT_SHUTDOWN_FUNC,
        SCRIPT_CHARSET
    )

    # Initialization.
    for option, (default_value, description) in OPTIONS.items():
        description = add_default_value_to(description, default_value)
        weechat.config_set_desc_plugin(option, description)
        if not weechat.config_is_set_plugin(option):
            weechat.config_set_plugin(option, default_value)

    # Catch all messages on all buffers and strip colors from them before
    # passing them into the callback.
    weechat.hook_print('', '', '', 1, 'message_printed_callback', '')
