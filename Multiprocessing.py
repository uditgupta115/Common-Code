import threading
import os
import pcap
from multiprocessing import Process
# from cheapflightv1 import cheapflight_execution
# from cheapflightv1 import cheapflight_execution_json
# from tangov1 import tango_execution
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

p = pcap.pcapObject()
device = sys.argv[1]
p.open_live(device, 65536, 0, 0)
# p.open_offline("cheapfl.pcap")
# p.open_offline("location.pcap")


cwd = os.getcwd()
append_packet_data = []


if __name__ == '__main__':
    count = 0
    # thread1t = threading.Thread(target=datasaver)
    # thread1t.daemon = True
    # thread1t.start()
    while 1:
        try:
            packet = p.next()
            if packet:
                append_packet_data.append(packet)
                print count, "---", "\r",
                count += 1
                if len(append_packet_data) == 10000:
                    # pass
                    p1 = Process(target=tango_execution, args=(append_packet_data,))
                    p1.daemon = True
                    p1.start()

                    p2 = Process(target=cheapflight_execution, args=(append_packet_data,))
                    p2.daemon = True
                    p2.start()

                    p3 = Process(target=cheapflight_execution_json, args=(append_packet_data,))
                    p3.daemon = True
                    p3.start()
                    append_packet_data = []

        except KeyboardInterrupt:
            print p.stats()
            # threading.Thread._Thread__stop(thread1t)
            # print thread1t.isAlive()