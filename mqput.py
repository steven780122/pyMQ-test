import pymqi

queue_manager = "OPSJXCTIQMST"
channel = ""
host = "10.20.20.23"
port = "1603"
queue_name = "CSC.OPS.INF.LEGO.TEST"

#
# queue_manager = "QM1"
# channel = ""
# host = "10.20.20.23"
# port = "1414"
# queue_name = "TEST.IAS.LQ1"
message = "Hello from Python!"
my_str_as_bytes = str.encode(message)

conn_info = "%s(%s)".format(host, port)

qmgr = pymqi.connect(queue_manager, channel, conn_info)
queue = pymqi.Queue(qmgr, queue_name)
queue.put(my_str_as_bytes)
queue.close()

qmgr.disconnect()


