from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    use_rviz = LaunchConfiguration('rviz')

    return LaunchDescription([
        DeclareLaunchArgument(
            'rviz',
            default_value='true',
            description='Launch RViz2'
        ),

        Node(
            package='your_serial_package',
            executable='serial_reader_node',
            name='serial_reader',
            output='screen',
        ),

        Node(
            package='imu_filter_madgwick',
            executable='imu_filter_madgwick_node',
            name='imu_filter',
            output='screen',
            parameters=[{'use_mag': False}],
            remappings=[
                ('imu/data_raw', '/imu/raw'),
                ('imu/data', '/imu/data')
            ]
        ),

        ExecuteProcess(
            condition=IfCondition(use_rviz),
            cmd=['rviz2', '-d', '/absolute/path/to/imu_viz.rviz'],
            output='screen'
        )
    ])

