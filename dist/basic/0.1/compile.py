import os
from distutils.dir_util import copy_tree
import yaml

def main(src: str):
    #
    # Compile src into dist
    #
    # Parameters:
    #    src (str): The src directory.
    #

    print('Compiling...')
    dist = os.getcwd()

    print('Moving dist to .compiled directory...')
    copy_tree(dist + '/src/', src + '/.compiled/')

    print('Copying src files to .compiled directory...')
    copy_tree(src + '/.compiled/', src + '/src/')

    print('Replacing placeholders...')
    app = yaml.load(src + 'config/app.yaml', Loader=yaml.FullLoader)

    print('Done.')


if __name__ == '__main__':
    main()
