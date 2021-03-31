import json
import sys


def main(argv):
    input_file = argv[1]
    output_file = argv[2]

    output_f = open(output_file, 'w')

    print('Extract hyracks jobs graph')
    data = json.load(open(input_file))
    for entry in data['connectors']:
        output_f.writelines('{} {}\n'.format(entry['in-operator-id'], entry['out-operator-id']))

    output_f.close()


if __name__ == '__main__':
    main(sys.argv)
