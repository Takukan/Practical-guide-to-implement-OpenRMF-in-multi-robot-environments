from setuptools import find_packages, setup

package_name = 'project_tasks'

setup(
    name=package_name,
    version='2.0.3',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/'+package_name, [package_name+'/airport_docker_config.yaml']),
        ('share/'+package_name, [package_name+'/hotel_cleaner_config.yaml']),
    ],
    install_requires=['setuptools'],
    author='Grey',
    author_email='grey@openrobotics.org',
    zip_safe=True,
    maintainer='yadu',
    maintainer_email='yadunund@openrobotics.org',
    description='A package containing scripts for demos',
    license='Apache License Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
          'request_loop = project_tasks.request_loop:main',
          'request_lift = project_tasks.request_lift:main',
          'cancel_task = project_tasks.cancel_task:main',
          'dispatch_loop = project_tasks.dispatch_loop:main',
          'dispatch_action = project_tasks.dispatch_action:main',
          'dispatch_patrol = project_tasks.dispatch_patrol:main',
          'dispatch_delivery = project_tasks.dispatch_delivery:main',
          'dispatch_clean = project_tasks.dispatch_clean:main',
          'dispatch_go_to_place = project_tasks.dispatch_go_to_place:main',
          'mock_docker = project_tasks.mock_docker:main',
          'teleop_robot = project_tasks.teleop_robot:main',
        ],
    },
)
