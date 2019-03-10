try:
    from setuptools import setup
except ImportError:
    from disutils.core import setup

config = {
    'description': 'Forest Text-Based Adventure',
    'author': 'John Desmond',
    'url': 'https://github.com/yohn-dezmon/forest_game_v2',
    'download_url': 'https://github.com/yohn-dezmon/forest_game_v2',
    'author_email': 'johndesmond631@gmail.com',
    'version': '0.1',
    'install_requires': ['pytest'],
    'packages': ['Forest_Game_v2'],
    'scripts': ['bin/z_runner.py'],
    'name': 'ForestGame'
}

setup(**config)
