#!/usr/bin/env python
"""ROS node for the Wit.ai API"""

import roslib
roslib.load_manifest('wit_ros')

APIKEY ='VJ52BYRJMSLYAAHPBTKZ2RW2CTE2B3DZ'

import rospy
import requests

from wit_ros.srv import Interpret, InterpretResponse

def interpret(rosrequest):
    httpresponse = requests.get('https://api.wit.ai/message?q={sentence}'.format(sentence=rosrequest.sentence), 
        headers={"Authorization":"Bearer {key}".format(key=APIKEY)})
    data = httpresponse.json()
    
    return InterpretResponse(   msg_body    = str(data["msg_body"]),
                                msg_id      = str(data["msg_id"]),
                                outcome     = str(data["outcome"]))

if __name__ == "__main__":
    rospy.init_node("wit_ros")

    rospy.Service('wit/interpret', Interpret, interpret)

    rospy.spin()