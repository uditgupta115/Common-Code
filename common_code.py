# decode json file from the content.

if 'json' in http.headers['content-type']:
    print http.headers
    print http.headers['host']
    print http.headers['content-type']
    print http.headers['content-encoding']
    if http.headers['content-encoding'] == 'gzip':
        dec_json = zlib.decompress(http_payload, 16 + zlib.MAX_WBITS)
        print dec_json
    elif http.headers['content-encoding'] == 'deflate':
        dec_json = zlib.decompress(http_payload)
        print dec_json
    print



# this will generate queries need to give only tablename and dict as parameters. 
def ins_query_maker(tablename, rowdict):
    keys = tuple(rowdict)
    dictsize = len(rowdict)
    sql = ''
    try:
        for i in range(dictsize):
            if type(rowdict[keys[i]]).__name__ == 'str':
                sql += '\"' + str(rowdict[keys[i]]).replace("'", "").replace('"', '') + '\"'
            else:
                sql += "\"" + str(rowdict[keys[i]]).replace("'", "").replace('"', '') + "\""
            if i < dictsize-1:
                sql += ', '
    except Exception as e:
        print e
    query = "insert ignore into " + str(tablename) + " " + "(" + ", ".join(keys) + ")" + " values (" + sql + ")"
    # print query
    return query  # in real code we do this


#  handler for new Handler in Database Queries!
def column_creater(error_msg, table_name, db_con):
    if 'Unknown column' in error_msg:
        sp_data = error_msg.split(' ')
        for i in sp_data:
            if i == 'column':
                col_name = sp_data[sp_data.index(i) + 1].replace(' ', "").replace("'", "").replace('"', "")
                sql_qry = 'ALTER TABLE %s ADD %s VARCHAR(250);' % (table_name, col_name)
                print sql_qry
                db_con.execute(sql_qry)



def datasaver():
    while 1:
        try:
            data = q.get()[1]
            eth = dpkt.ethernet.Ethernet(data)
            ip = eth.data
            tcp = ip.data
            payload = tcp.data
            if len(payload):
                if tcp.sport == 80:
                    compress(payload)
        except:
            pass


# way to use multithreading 
if __name__ == '__main__':
    thread1t = threading.Thread(target=datasaver)
    thread1t.daemon = True
    thread1t.start()
    try:
        while 1:
            q.put(p.next())
    except KeyboardInterrupt:
        print p.stats()
        print q.qsize()
        threading.Thread._Thread__stop(thread1t)
        print thread1t.isAlive()
# new

#old one updated is upper only!
def ins_query_maker(tablename, rowdict):
    keys = tuple(rowdict)
    dictsize = len(rowdict)
    sql = ''
    for i in range(dictsize):
        if type(rowdict[keys[i]]).__name__ == 'str':
            sql += '\'' + str(rowdict[keys[i]]) + '\''
        else:
            sql += str(rowdict[keys[i]])
        if i < dictsize-1:
            sql += ', '
    query = "insert into " + str(tablename) + " " + "(" + ", ".join(keys) + ")" + " values (" + sql + ")"
    print(query)  # for demo purposes we do this
    return query  # in real code we do this



# this one is to let you know how to use multiprocess module in python!

# -*- coding: utf-8 -*-
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
