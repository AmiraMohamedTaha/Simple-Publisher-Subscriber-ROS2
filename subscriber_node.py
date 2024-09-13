import rclpy 
from rclpy.node import Node
from std_msgs.msg import Int32

class  subscriber_node(Node):
    def __init__(self):
        super().__init__("Sensor_reader")  
        self.subscriber_= self.create_subscription(Int32,'temperature',self.temp_subscriber,10)
        
       
    def temp_subscriber(self,msg):
        self.get_logger().info(f'Subscribing: {msg.data}')

def main(args=None):    
    rclpy.init(args=args)
    node=subscriber_node()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if _name_ == '_main_':
    main()