# Copyright 2021 pinorobotics
# 
# Website: https://github.com/pinorobotics/gripper-rollpawkit
# 
# This source file is a part of sainsmart-simulator project.
# Description for this  project can be found in readme file.
# 
# sainsmart-simulator is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# sainsmart-simulator is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public License
# along with sainsmart-simulator. If not, see <http://www.gnu.org/licenses/>.

from launch import LaunchDescription
from launch.substitutions import Command, LaunchConfiguration, PathJoinSubstitution, FindExecutable
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
 
def generate_launch_description():
  share_folder = FindPackageShare('gripper-rollpawkit')
  robot_description_content = Command(
      [
          PathJoinSubstitution([FindExecutable(name="xacro")]),
          " ",
          PathJoinSubstitution([share_folder, "urdf", "gripper-rollpawkit.urdf"]),
      ])
  robot_description = {"robot_description": robot_description_content}
  rviz_config_file = PathJoinSubstitution([share_folder, "rviz", "visualize.rviz"])
  return LaunchDescription([
      Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="both",
        parameters=[robot_description],
      ),
      Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', rviz_config_file]),
      Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui')])

