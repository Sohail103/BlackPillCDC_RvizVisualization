from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'serial_mpu_reader'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools', 'pyserial'],
    zip_safe=True,
    maintainer='sohail',
    maintainer_email='sohailraj.satapathy@gmail.com',
    description='reads serial data on /dev/ttyACM0 and publishes it on ros topic /imu/data_raw',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'serial_reader = serial_mpu_reader.serial_reader:main',
        ],
    },
)
