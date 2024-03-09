import subprocess
import argparse

parser = argparse.ArgumentParser(description='You can change the mode of the interface',
                                 epilog='........................',
                                 prog='mod_changer.py',
                                 usage='%(prog)s [interface] [mode]')

parser.add_argument('-i', '--interface' ,
                    dest='interface',
                    help='The interface where you want to change the mode',
                    metavar='',
                    required=True,
                    type=str)
parser.add_argument('-m', '--mode' ,
                    dest='mode',
                    help='choose managed or monitor',
                    metavar='',
                    required=True,
                    type=str)

args = parser.parse_args()
interface = args.interface
mode = args.mode


try:
    subprocess.run(['service', 'NetworkManager', 'stop'],
                   capture_output=True,
                   text=True,
                   timeout=10,
                   check=True)
except subprocess.CalledProcessError as error:
    print(error.stderr)


try:
    subprocess.run(['ifconfig', interface, 'down'],
                   capture_output=True,
                   text=True,
                   timeout=10,
                   check=True)
except subprocess.CalledProcessError as error:
    print(error.stderr)


try:
    subprocess.run(['iwconfig', interface, 'mode', mode],
                   capture_output=True,
                   text=True,
                   timeout=10,
                   check=True)
except subprocess.CalledProcessError as error:
    print(error.stderr)


try:
    subprocess.run(['ifconfig', interface, 'up'],
                   capture_output=True,
                   text=True,
                   timeout=10,
                   check=True)

except subprocess.CalledProcessError as error:
    print(error.stderr)


