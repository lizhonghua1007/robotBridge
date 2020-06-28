import roslibpy

rosClient = roslibpy.Ros(host='192.168.1.154',port=9090)
rosClient.run()
print(rosClient.is_connected)
rosClient.terminate()