import argparse
import socket
import sys

try:
    import ipaddress
except ImportError:
    print("Couldn't find ipaddress module. Module requires python3.3+, you are using {}".format(sys.version.split(" ")[0]))
    sys.exit()

parser = argparse.ArgumentParser()
parser.add_argument("iprange", help="The range you want to find the reverse records for.")
parser.add_argument("--failures", "-f", help="Use this switch to capture failed lookups", action="store_true")
parser.add_argument("--outfile", "-o", help="Use this to save output to a file")
args = parser.parse_args()

try:
    ips = ipaddress.IPv4Network(args.iprange)
except:
    print("{} is not a valid subnet address.".format(args.iprange))
    sys.exit()

if args.outfile:
    rhino_out = open(args.outfile, 'wb')

for ip in ips:
    try:
        if args.outfile:
            rhino_out.write("{} - {}\n".format(str(ip), socket.gethostbyaddr(str(ip))[0]).encode())
        else:
            print("{} - {}".format(str(ip), socket.gethostbyaddr(str(ip))[0]))
    except socket.herror as e:
        if args.failures:
            if args.outfile:
                rhino_out.write("{} - none\n".format(str(ip)).encode())
            else:
                print("{} - none".format(str(ip)))
        else:
            pass
rhino_out.close()
