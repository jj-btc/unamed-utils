from eth_utils.abi import fetch_abi
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('addr', type=str, help='Contract address')
parser.add_argument('-o', '--output', type=str, help="Path to the output JSON file", required=True)

if __name__ == "__main__":
    args = parser.parse_args()
    open(args.output, 'w').write(fetch_abi(args.addr))