from setuptools import setup

package_name = 'live_detection'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tjkim',
    maintainer_email='tjkim@rcv.sejong.ac.kr',
    description='ROS2 Package for live detection using Tensorflow',
    license='MIT License',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'live_detector = live_detection.live_detector:main',
        ],
    },
)