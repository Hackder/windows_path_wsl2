#!/usr/bin/env python

from PyInquirer import prompt
from examples import custom_style_3
import os

environent_name = "WINDOWS_PATHS_WSL2_SETUP"
save_file_path = 'active_paths.txt'
save_file_windows = 'windows_paths.txt'

# Get absolute save path
current_dir = os.path.dirname(os.path.realpath(__file__))
save_file_path = os.path.join(current_dir, save_file_path)
save_file_windows = os.path.join(current_dir, save_file_windows)


def save_paths(filename, paths):
    with open(filename, 'w') as file:
        content = ':'.join(paths)
        file.write(content)


def read_paths(filename):
    if (not os.path.exists(filename)):
        return []
    with open(filename, 'r') as file:
        content = file.read()
        return list(map(lambda x: x.strip(), content.split(':')))


# Get paths
active_paths = read_paths(save_file_path)
windows_paths = read_paths(save_file_windows)

questions = [
    {
        'type': 'checkbox',
        'qmark': '?',
        'message': 'Select windows paths to apply',
        'name': 'windows_paths',
        'choices': [
            {
                'name': p,
                'checked': p in active_paths
            } for p in sorted(windows_paths)
        ]
    }
]
answer = prompt(questions, style=custom_style_3)
if not 'windows_paths' in answer:
    exit()
paths_to_apply = answer['windows_paths']
indices = {i: e for e, i in enumerate(windows_paths)}
paths_to_apply.sort(key=lambda e: indices[e])

# Save the paths
save_paths(save_file_path, paths_to_apply)
print("PATH updated! You need to reload your shell for this to take effect!")
