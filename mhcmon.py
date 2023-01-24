import argparse
import os
from app import MHCMON

cwd = os.getcwd()
parser = argparse.ArgumentParser(
    prog="MHCMON",
    description="[ MHCMON ] DESCRIPTION : auto run bash and c# scripts",
    epilog="Ato Codes || MHCDA",
    add_help=True
)

parser.add_argument(
    'file',
    action='store',
    nargs=1,
    default=None,
    help="file name or path",
)

args = parser.parse_args()

[ file ] = args.file

file_dir = f'{cwd}/{file}'

if os.path.exists(file_dir):
    mhcmon = MHCMON(file_name=file)
    mhcmon.start()
else:
    print(file_dir)
    raise FileNotFoundError('File not found')
