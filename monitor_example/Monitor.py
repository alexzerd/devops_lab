import psutil
import datetime
import time
import json
import os
from configparser import SafeConfigParser


class Monitor:

    def __init__(self):

        parser = SafeConfigParser()
        parser.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'time.conf'))
        self.interval = int(parser.get('common', 'interval'))
        self.output = parser.get('common', 'output')

    def snapshot(self):

        cpu_percent = psutil.cpu_percent()
        cache_amount = psutil.virtual_memory()[8]
        memory_percent = psutil.virtual_memory()[2]
        disk_percent = psutil.disk_usage('/')[3]
        iotime = psutil.disk_io_counters()[8]
        net_info = self.get_network()

        print("Hit CTRL-C to stop")

        while True:

            if self.output == 'txt':

                line = 40 * "-"

                with open("output.txt", "a+") as text_file:

                    text_file.write(line)
                    text_file.write('\nSNAPSHOT AT {0}\n'.format(datetime.now()))
                    text_file.write(line + '\n')

                    text_file.write('Current disk utili is {0} percent\n'.format(disk_percent))
                    text_file.write('Total io time is {0} ms\n'.format(iotime))
                    text_file.write('Current CPU utilization is {0} percent\n'.format(cpu_percent))
                    text_file.write('Current mem util is {0} percent\n'.format(memory_percent))
                    text_file.write('Current virt mem amount is {0} bytes\n'.format(cache_amount))

                    columns = ['IP', 'Interface', 'Sent', 'Received']
                    text_file.write('{:<20s}{:>10s}{:>10s}{:>10s}\n'.format(
                        columns[0], columns[1], columns[2], columns[3]))

                    for i in range(len(net_info)):
                        text_file.write('{:<20s}{:>10s}{:^10s}{:>10s}\n'.format(
                            net_info[i]['ip'], net_info[i]['iface'],
                            net_info[i]['sent'], net_info[i]['recv']))

            else:
                out = {}

                out['date'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                out['disk_percent'] = disk_percent
                out['io_time'] = iotime
                out['cpu'] = cpu_percent
                out['memory_utilization'] = memory_percent
                out['virt_memory'] = cache_amount
                out['network'] = net_info

                with open('output.json', 'a+') as fp:
                    json.dump(out, fp, indent=4)

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
