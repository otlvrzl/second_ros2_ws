from launch import LaunchDescription
from launch.actions import ExecuteProcess
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    return LaunchDescription([
        ExecuteProcess(
            cmd=['gz', 'sim', 'sensor_tutorial.sdf'],
            output='screen',
        ),
        ExecuteProcess(
            cmd=['./build/lidar_node'],
            output='screen',
        ),
    ])