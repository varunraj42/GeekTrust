import pdb

class Routes:
    route1 = {'CHN': 0, 'SLM': 350, 'BLR': 550, 'KRN': 900, 'HYB': 1200, 'NGP': 1600, 'ITJ': 1900, 'BPL': 2000, 'AGA': 2500, 'NDL': 2700}

    route2 = {'TVC': 0, 'SRR': 300, 'MAQ': 600, 'MAO': 1000, 'PNE': 1400, 'HYB': 2000, 'NGP': 2400, 'ITJ': 2700, 'BPL': 2800, 'PTA': 3800, 'NJP': 4200, 'GHY': 4700}

    def __init__(self, source):
        self.source = source
        self.route = Routes.route1 if 'CHN' in self.source else Routes.route2
        self.first_junction = 'HYB'
        self.last_junction = 'BPL'

    def find_distance_to_dest(self, dest):
        if 'HYB' not in self.source:
            if 'CHN' in self.source:
                distance_till_bhopal = Routes.route1['BPL']
            elif 'TVC' in self.source:
                distance_till_bhopal = Routes.route2['BPL']

            if dest in Routes.route1:
                distance_from_bhopal = Routes.route1[dest] - Routes.route1['BPL']
                return distance_till_bhopal + distance_from_bhopal
            elif dest in Routes.route2:
                distance_from_bhopal = Routes.route2[dest] - Routes.route2['BPL']
                return distance_till_bhopal + distance_from_bhopal
        else:
            if dest in Routes.route1:
                distance_from_hyd = Routes.route1[dest] - Routes.route1['HYB']
                return distance_from_hyd
            elif dest in Routes.route2:
                distance_from_hyd = Routes.route2[dest] - Routes.route2['HYB']
                return distance_from_hyd

        return None


class Train:
    trains = []

    def __init__(self, source, deboard_boggies, extend_routes={}):
        self.deboard_boggies = deboard_boggies
        self.route_obj = Routes(source)
        for route in extend_routes:
            self.route_obj.route[route] = extend_routes[route]


    def sort_boggies(self):
        self.departed_boggies = list()
        self.stations_in_route = list(self.route_obj.route.keys())
        distance_to_dest = [[boggie, self.route_obj.find_distance_to_dest(dest=boggie)] for boggie in self.deboard_boggies]
        self.departed_boggies = [item for item in distance_to_dest if item[1]]
        self.departed_boggies = sorted(self.departed_boggies, key=lambda item: item[1], reverse=True)
        final_station_route = self.stations_in_route[-1]
        stations_till_bhopal = self.stations_in_route[:self.stations_in_route.index('BPL')+1]
        self.departed_boggies = [boggie[0] for boggie in self.departed_boggies if boggie[0] in final_station_route] + [boggie[0] for boggie in self.departed_boggies if boggie[0]!= final_station_route and boggie[0] not in stations_till_bhopal] + [boggie[0] for boggie in self.departed_boggies if boggie[0] in stations_till_bhopal]
        return self.departed_boggies

    def remove_boggie(self, boggies, boggie_to_remove):
        while boggies[-1] == boggie_to_remove:
            print(f"\tDetaching {boggie_to_remove}")
            boggies.remove(boggies[-1])

        return boggies

    def reach_first_junction(self):
        for station in self.stations_in_route:
            print(f"Came to {station}")
            if station == self.route_obj.first_junction:
                #print(f"Reached {station} from {self.route_obj.source} --> {self.departed_boggies}")
                return self.departed_boggies
            elif station == self.departed_boggies[-1]:
                self.departed_boggies = self.remove_boggie(self.departed_boggies, station)

            print(f"Leaving {station}")

        return self.departed_boggies


def main(instructions):
    merged_boggies = []
    output = []

    for ins in instructions:
        if ins:
            source_station = 'CHN' if 'TRAIN_A' in ins else 'TVC'
            deboard_stations = ins.split('ENGINE')[-1].split(' ')
            train_obj = Train(source_station, deboard_stations)
            Train.trains.append(train_obj)

    for train in Train.trains:
        boggies_sorted = train.sort_boggies()
        print(f"Started from {train.route_obj.source} as {boggies_sorted}")
        boggies = train.reach_first_junction()

        for boggie in boggies:
            merged_boggies.append(boggie)

        train_name = 'TRAIN_A' if train.route_obj.source == 'CHN' else 'TRAIN_B'
        output.append(f"ARRIVAL {train_name} ENGINE {' '.join(boggies)}")

    train_ab = Train('HYB', merged_boggies)
    for train in [train_ab]:
        boggies_sorted = train.sort_boggies()
        #print(f"Started from {train.route_obj.source} as {boggies_sorted}")
        train_name = 'TRAIN_AB' if train.route_obj.source == 'HYB' else 'TRAIN_AB'
        output.append(f"DEPARTURE {train_name} ENGINE {' '.join(boggies_sorted)}")

    return '\n'.join(output)

def read_file(file):
    with open(file, 'r') as input:
        data = input.read().split('\n')
    return data

if __name__ == '__main__':
    import sys
    file = sys.argv[1]
    instructions = read_file(file)
    print(main(instructions))
