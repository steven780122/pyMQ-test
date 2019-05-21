import pymqi


# queue_manager = "OPSJXCTIQMST"
# # channel = "OPSJXCTIQMST.INF.C1"
# host = "10.20.20.23"
# port = "1603"
# queue_name = "CSC.OPS.INF.LEGD.TEST"
# message = "Hello from Python!"
# my_str_as_bytes = str.encode(message)


queue_manager = "QM1"
# channel = "OPSJXCTIQMST.CTI.C1"
channel = ""
host = "10.20.20.23"
port = "1414"
queue_name = "TEST.IAS.LQ1"


conn_info = "%s(%s)".format(host, port)

qmgr = pymqi.connect(queue_manager, channel, conn_info)
queue = pymqi.Queue(qmgr, queue_name)
message = queue.get()

print(message)
queue.close()

qmgr.disconnect()




