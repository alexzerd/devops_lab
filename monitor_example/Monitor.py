import psutil
from datetime import datetime
import time
from configparser import SafeConfigParser


class Monitor:

    def __init__(self):

        parser = SafeConfigParser()
        parser.read('time.conf')
        self.interval = int(parser.get('common', 'interval'))

    def snapshot(self):

        cpu_percent = psutil.cpu_percent()
        cache_amount = psutil.virtual_memory()[8]
        memory_percent = psutil.virtual_memory()[2]
        disk_percent = psutil.disk_usage('/')[3]
        iotime = psutil.disk_io_counters()[8]
        net_info = self.get_network()

        while True:

            line = 40 * "-"
            print(line)
            print('SNAPSHOT AT', datetime.now())
            print(line)

            print('Current disk utilization is', disk_percent, 'percent')
            print('Total io time is', iotime, 'miliseconds')
            print('Current CPU utilization is', cpu_percent, 'percent')
            print('Current memory utilization is', memory_percent, 'percent')
            print('Current virtual memoty amount is', cache_amount, 'bytes')

            columns = ['IP', 'Interface', 'Sent', 'Received']
            print('{:<20s}{:>10s}{:>10s}{:>10s}'.format(
                columns[0], columns[1], columns[2], columns[3]))

            for i in range(len(net_info)):
                print('{:<20s}{:>10s}{:^10s}{:>10s}'.format(
                    net_info[i]['ip'], net_info[i]['iface'],
                    net_info[i]['sent'], net_info[i]['recv']))

            time.sleep(self.interval * 60)

    def get_network(self):

        network = psutil.net_io_counters(pernic=True)
        ifaces = psutil.net_if_addrs()
        networks = list()
        for k, v in ifaces.items():
            ip = v[0].address
            data = network[k]
            ifnet = dict()
            ifnet['ip'] = ip
            ifnet['iface'] = k
            ifnet['sent'] = '%.2fMB' % (data.bytes_sent / 1024 / 1024)
            ifnet['recv'] = '%.2fMB' % (data.bytes_recv / 1024 / 1024)
            networks.append(ifnet)
        return networks


if __name__ == "__main__":

    print("I'm inside __main__")
    m = Monitor()
    m.snapshot()
