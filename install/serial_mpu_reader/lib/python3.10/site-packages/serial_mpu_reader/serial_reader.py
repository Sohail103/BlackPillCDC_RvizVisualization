import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
import serial

class SerialIMUReader(Node):
    def __init__(self):
        super().__init__('serial_imu_reader')
        self.publisher_ = self.create_publisher(Imu, 'imu/data_raw', 10)
        self.serial_port = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
        self.timer = self.create_timer(0.02, self.read_serial_data)  # 50Hz

    def read_serial_data(self):
        try:
            line = self.serial_port.readline().decode('utf-8').strip()
            if not line.startswith('AX:'):
                return
            
            line = line.split(',')
            
            msg = Imu()
            msg.header.stamp = self.get_clock().now().to_msg()
            msg.header.frame_id = "imu_link"

            msg.linear_acceleration.x = (float)(line[0].split(':')[1])
            msg.linear_acceleration.y = (float)(line[1].split(':')[1])
            msg.linear_acceleration.z = (float)(line[2].split(':')[1])

            msg.angular_velocity.x = (float)(line[3].split(':')[1])
            msg.angular_velocity.y = (float)(line[4].split(':')[1])
            msg.angular_velocity.z = (float)(line[5].split(':')[1])

            self.publisher_.publish(msg)
        except Exception as e:
            self.get_logger().warn(f"Serial read error: {e}")

def main(args=None):
    rclpy.init(args=args)
    node = SerialIMUReader()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
