import roslibpy
import time

rosClient = roslibpy.Ros(host='192.168.73.128',port=9090)
rosClient.run()
talker = roslibpy.Topic(rosClient, '/chatter', 'std_msgs/String')

while rosClient.is_connected:
    talker.publish(roslibpy.Message({'data': 'Hello World!'}))
    print('Sending message...')
    time.sleep(1)

talker.unadvertise()
rosClient.terminate()