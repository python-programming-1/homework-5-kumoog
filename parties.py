import csv
import pprint
import operator


def get_bar_party_data():
    """this function reads from a csv file and converts the data into a list of dictionaries.
     each item in the list is a dictionary of a specific location and the number of complaint calls
     it received in 2016"""

    bar_list = []
    with open('bar_locations.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            bar_dict = {'location_type': row[0],
                        'zip_code': row[1],
                        'city': row[2],
                        'borough': row[3],
                        'latitude': row[4],
                        'longitude': row[5],
                        'num_calls': row[6]}
            bar_list.append(bar_dict)
    return bar_list


def print_data(data):
    for entry in data:
        print(entry)
        pprint.pprint(entry)


def get_most_noisy_city_and_borough(data):
    """ fill in the Nones for the dictionary below using the bar party data """
    noisiest_city_and_borough = {'city': data[1].get('city'), 'borough': data[1].get('borough'),
                                 'num_city_calls': data[1].get('num_calls'),
                                 'num_borough_calls': data[1].get('num_calls')}
    b ={}
    h ={}

    for i in range(1,2441):
        if not data[i].get('city') in b:
           b.setdefault(data[i].get('city'), int(data[i].get('num_calls')))

           continue

        elif data[i].get('city') in b:
           y = (data[i].get('city'))
           t = int(b.get(data[i].get('city'))) + int(data[i].get('num_calls'))
           c = {y: t}
           b.update(c)
           continue



    for i in range(1,2441):
        if data[i].get('city') == max(b, key=lambda key: b[key]):
            if not data[i].get('borough') in h:
                h.setdefault(data[i].get('borough'),data[i].get('num_calls'))
                continue
            elif data[i].get('borough') in h:
                q = (data[i].get('borough'))
                w = int(h.get(data[i].get('borough'))) + int(data[i].get('num_calls'))
                j = {q: w}
                h.update(j)
                continue


    noisiest_city_and_borough = {'city': max(b, key=lambda key: b[key]), 'borough': max(h, key=lambda key: h[key]),
                                                                         'num_city_calls': max(b.values()),
                                                                         'num_borough_calls': max(h.values())}

    return noisiest_city_and_borough


def get_quietest_city_and_borough(data):
    """ fill in the Nones for the dictionary below using the bar party data """
    quietest_city_and_borough = {'city': data[1].get('city'), 'borough': data[1].get('borough'),
                                 'num_city_calls': data[1].get('num_calls'),
                                 'num_borough_calls': data[1].get('num_calls')}
    b ={}
    h ={}

    for i in range(1,2441):
        if not data[i].get('city') in b:
           b.setdefault(data[i].get('city'), int(data[i].get('num_calls')))

           continue

        elif data[i].get('city') in b:
           y = (data[i].get('city'))
           t = int(b.get(data[i].get('city'))) + int(data[i].get('num_calls'))
           c = {y: t}
           b.update(c)
           continue



    for i in range(1,2441):
        if data[i].get('city') == min(b, key=lambda key: b[key]):
            if not data[i].get('borough') in h:
                h.setdefault(data[i].get('borough'),data[i].get('num_calls'))
                continue
            elif data[i].get('borough') in h:
                q = (data[i].get('borough'))
                w = int(h.get(data[i].get('borough'))) + int(data[i].get('num_calls'))
                j = {q: w}
                h.update(j)
                continue


    quietest_city_and_borough = {'city': min(b, key=lambda key: b[key]), 'borough': min(h, key=lambda key: h[key]),
                                                                         'num_city_calls': min(b.values()),
                                                                         'num_borough_calls': min(h.values())}

    return quietest_city_and_borough


if __name__ == '__main__':
    bar_data = get_bar_party_data()

    # uncomment the line below to see what the data looks like
    # print_data(bar_data)

    noisy_metrics = get_most_noisy_city_and_borough(bar_data)

    quiet_metrics = get_quietest_city_and_borough(bar_data)

    print('Noisy Metrics: {}'.format(noisy_metrics))
    print('Quiet Metrics: {}'.format(quiet_metrics))
