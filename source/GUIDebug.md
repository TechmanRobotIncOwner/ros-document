## __9. GUI Debug__
The GUI displays tm_driver connection status, sct, sta, svr messages and robot status. Easily judge the message between the driver and the robot through the GUI display. If the connection fails, the user can also try to send a reconnect command on this GUI for debugging.


### &sect; GUI Debugging description
> * If the user forgets to run the TM ROS driver, the user will see all the controlled label items of the GUI are displayed as "NaN".<br/>
> * The user can click "``Quit_GUI``" button or click the "``x``" close button in the upper right corner to close this GUI.<br/>
> * If "``Ethernet``" and "``Listen Node``" connection display are "on", it means that ROS SvrClient and SctClient are successfully connected.<br/>
> * If "``Ethernet``" connection display is is "off", the user should check whether the TM Robot has been started or whether the network settings are correct.<br/>
> * If "``Listen Node``" connection is "off", the user should check whether the task project is running.<br/>
> :bulb: If "``Listen Node``" connection is interrupted as "``Project_Run``" is stopped, the "``Listen Node``" connection will be "off". <br/>

> <table><tr><td bgcolor=bisque> <font color=black> Note :</font><br/> If <font color=red>"Listen Node"</font> connection is interrupted as <font color=red>"Project_Run"</font> is stopped, the <font color=red>"Listen Node"</font> connection will be "off". </td></tr></table><br/>

> * If both "``Ethernet``" and "``Listen Node``" connection display  are "on", but the "``Robot_Link``" is false or "``Robot_Error``" is true; this means the robot is working abnormally, or maybe the ESTOP button was pressed or or some kind of protection or error <sup>1</sup> occurred. Therefore, when the user sends a move script command at this time, it will not work.<br/> 
> <sup>1</sup> For more detailed information, please refer to the TM Robot User Guide.<br/> 
> * The user can use the self-developed script to read/write project data through communication protocols to control the TM Robot. If it does not work properly, the user can quickly determine whether there is a communication error code by viewing the "``Response ROS Node Status``" display.<br/>
> * When the user sends a command or clicks DO0 Ctrl "``H/L``" button of Control_Box, the user also can see the response message <sup>2</sup> embedded in the "``Robot Response``" item view.<br/>
> <sup>2</sup> For details of this item, please refer to __SctResponse.msg__, __StaResponse.msg__ and __SvrResponse.msg__ of TM ROS driver code.<br/>
> * The user can click "``clear``" button to clear the old response message.<br/>

> <table><tr><td bgcolor=bisque> <font color=black> Note :</font><br/> If <font color=red>"Ethernet"</font> connection is interrupted, the display of most controlled label items in the GUI will be displayed as "NaN" and the robot feedback state will remain the last state and become invalid. </td></tr></table><br/>

### &sect; Usage with GUI debugging in ROS1
> Note: If the user have even successfully built a specific code(tmr_ros1), the user only need to change to the TM driver workspace path  ``cd ~/tmdriver_ws`` , and then directly refer to steps 5~7 below. <br/>
> 1. Type to create a root workspace directory by starting a terminal: For example,  ``tmdriver_ws`` or ``catkin_ws``, then type to change current directory into the workspace directory path.<br/>
``mkdir ~/tmdriver_ws``<br/>
``cd ~/tmdriver_ws``<br/>
> 2. Clone the the TM driver of git repository into the current directory by typing<br/>
``git clone https://github.com/TechmanRobotInc/tmr_ros1.git -b noetic``<br/>
> 3. After the download done, rename the download folder ``tmr_ros1``(or ``tmr_ros1-noetic``) to ``src`` by typing<br/>
``mv tmr_ros1 src``<br/>  (or right-click on the download folder, select "Rename...")<br/>
> 4. At the workspace directory to build the download packages and source 'setup.bash' in this workspace to make the worksapce visible to ROS of this terminal 1.<br/>
Note: Do you set``source /opt/ros/noetic/setup.bash`` ready? Make sure to obtain the correct setup file according to your workspace hierarchy, and then type the following below to compile.<br/>
``catkin_make``<br/>
``source ./devel/setup.bash``<br/>
> 5. Terminal 1: Startup ROS core  and type<br/>
``roscore``<br/>
> 6. In a new terminal 2: Source setup.bash in the workspace path and run the driver to connect to TM Robot by typing<br/>
``source ./devel/setup.bash``<br/>
``rosrun tm_driver tm_driver <robot_ip_address>``<br/>
The <robot_ip_address> is the IP address of the TM Robot, the user can get it through TM Flow, for example 192.168.10.2<br/>
> 7. In another new terminal 3: Source setup.bash in the workspace path and start GUI debug by typing<br/>
``source ./devel/setup.bash``<br/>
``rosrun ui_for_debug_and_demo robot_ui``<br/>

### &sect; Usage with GUI debugging in ROS2
> Note: If the user have even successfully built a specific code(tmr_ros2), the user only need to change to the TM driver workspace path  ``cd ~/tmdriver_ws`` , and then directly refer to steps 5~6 below. <br/>
> 1. Type to create a root workspace directory by starting a terminal: For example,  ``tmdriver_ws`` or ``catkin_ws``, then type to change current directory into the workspace directory path.<br/>
``mkdir ~/tmdriver_ws``<br/>
``cd ~/tmdriver_ws``<br/>
> 2. Clone the the TM driver of git repository into the current directory by typing<br/>
``git clone https://github.com/TechmanRobotInc/tmr_ros2.git``<br/>
> 3. After the download done, rename the download folder ``tmr_ros2``(or ``tmr_ros2-master``) to ``src`` by typing<br/>
``mv tmr_ros2 src``<br/>  (or right-click on the download folder, select "Rename...")<br/>
> 4. At the workspace directory to build the download packages and source 'setup.bash' in this workspace to make the worksapce visible to ROS.<br/>
Note: Do you set ``source /opt/ros/foxy/setup.bash`` ready? Make sure to obtain the correct setup file according to your workspace hierarchy, and then type the following below to compile.<br/>
``colcon build``<br/>
``source ./install/setup.bash``<br/>
> 5. In a new terminal: Source setup.bash in the workspace path and run the driver to connect to TM Robot by typing<br/>
``source ./install/setup.bash``<br/>
``ros2 run tm_driver tm_driver <robot_ip_address>``<br/>
The <robot_ip_address> is the IP address of the TM Robot, the user can get it through TM Flow, for example 192.168.10.2<br/>
> 6. In another new terminal: Source setup.bash in the workspace path and start GUI debug by typing<br/>
``source ./install/setup.bash``<br/>
``ros2 run ui_for_debug_and_demo robot_ui``<br/>
