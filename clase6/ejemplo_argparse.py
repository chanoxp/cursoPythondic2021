import argparse
import sys
import os


mi_parser = argparse.ArgumentParser(prog= 'ejemplo_argparse.py',
                                    description= 'Listado del contenido del direcorio',
                                    epilog= 'Muchas gracias')

mi_parser.add_argument('path',
                        metavar= 'Ruta',
                        type= str,
                        help='La ruta al directorio')                                    

args = mi_parser.parse_args()
dir_ruta = args.path

if not os.path.isdir(dir_ruta):
    print('Este directorio no existe')
    sys.exit()

print('\n'.join(os.listdir(dir_ruta)))



