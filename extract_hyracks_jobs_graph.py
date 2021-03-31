import json


def main():
    output_f = open('edges.csv', 'w')

    print('Extract hyracks jobs graph')
    data = json.load(open('spatial_join_hyracks_jobs.json'))
    print(data['connectors'])
    for entry in data['connectors']:
        output_f.writelines('{} {}\n'.format(entry['in-operator-id'], entry['out-operator-id']))

    output_f.close()


if __name__ == '__main__':
    main()
