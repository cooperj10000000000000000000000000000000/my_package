from setuptools import setup

package_name = 'my_package'

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
    maintainer='Paolo',
    maintainer_email='pstegagno@uri.edu',
    description='Testing stuff',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_node = my_package.my_node:main',
            'talker = my_package.my_publisher:main',
            'listener = my_package.my_subscriber:main',
            'example_cmd_vel = my_package.example_cmd_vel:main',
            'example_read_lidar = my_package.example_read_lidar:main',
            'example_cmd_vel_lidar = my_package.example_cmd_vel_lidar:main',
            'example_feedbacklin_controller = my_package.example_feedbacklin_controller:main',
            'test_in_class = my_package.test_in_class:main',
            'hw09pub = my_package.hw09pub:main',
            'hw09sub = my_package.hw09sub:main',
            'class_251125 = my_package.class_251125:main',
        ],
    },
)
