from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
    # Serial reader node
    Node(
        package='serial_mpu_reader'
