import pymqi

queue_manager = "QM1"
channel = ""
host = "10.20.99.120"
port = "1414"
queue_name = "LQ1"
message = "Hello from Python2!"
my_str_as_bytes = str.encode(message)


conn_info = "%s(%s)".format(host, port)

qmgr = pymqi.connect(queue_manager, channel, conn_info)
queue = pymqi.Queue(qmgr, queue_name)
queue.put(my_str_as_bytes)
queue.close()

qmgr.disconnect()


