## __6. ROS2 Usage__

> __ROS2 driver usage__
> 
> After the user has set up the ROS2 environment and built the TM driver based on the specific workspace, please enter your workspace `<workspace>` by launching the terminal, and remember to make the workspace visible to ROS. 
>
>
> ```bash
> source /opt/ros/foxy/setup.bash
> cd <workspace>
> source ./install/setup.bash
> ```
> <table><tr><td bgcolor=Bisque> <font color=black> Note :</font><br/> Do you prepare the <b>TM Robot</b> ready ? Make sure that TM Robot's operating software (<b>TMflow</b>) network settings are ready and the <b>Listen node</b> project is running. </td></tr></table><br/>
> 
> Then, run the driver to maintain the connection with TM Robot by typing 
>
>```bash
> ros2 run tm_driver tm_driver <robot_ip_address>
>```
> Example :``ros2 run tm_driver tm_driver 192.168.10.2``, if the <robot_ip_address> is 192.168.10.2
>
> Now, the user can use a new terminal to run each ROS node or command, but don't forget to source the correct setup shell files as starting a new terminal.

> __Usage with MoveIt2 (Tentative)__ 
>
> See [Moveit2 tutorial](https://moveit.ros.org/install-moveit2/source/).<br/>
> 
> Assuming that the user is ready to build Moveit2, and the user wants to apply the MoveIt by TM Robot, please do'nt forget to source the MoveIt environment, or you can add  ``source <MoveIt_WS>/install/setup.bash`` to your .bashrc.<br/>
> The `<MoveIt_WS>` means the Moveit2 workspace, for example `COLCON_WS` .<br/>
> The `<TMDriver_WS>` means TM driver workspace, for example `tmdriver_ws` .<br/>
>
>
> Then to built the TM driver based on the <TMDriver_WS> workspace, please enter the specific workspace `tmdriver_ws` by launching the terminal, and remember to make the workspace visible to ROS..<br/>
>
>
> ```bash
> source /opt/ros/foxy/setup.bash
> source ~/COLCON_WS/install/setup.bash
> cd ~/tmdriver_ws 
> colcon build
> source ./install/setup.bash
> ```
>
> The demo launches the RViz GUI and demonstrates planning and execution of a simple collision-free motion plan with TM Robot.
> To bring up MoveIt2 demo environment in simulation mode with virtual TM Robot, by typing
>
> ```bash
> ros2 launch tmr_run_moveit_cpp_demo run_moveit_cpp.launch.py
> ```
>
> The user can also manipulate real TM Robot to run, by typing<br/>
> <table><tr><td bgcolor=Bisque> <font color=black> Note :</font><br/> Do you prepare the <b>TM Robot</b> ready ? Make sure that TM Robot's operating software (<b>TMflow</b>) network settings are ready and the <I>Listen task</I> project is running. </td></tr></table><br/>
>
> ```bash
> ros2 launch tmr_run_moveit_cpp_demo run_moveit_cpp.launch.py robot_ip:=<robot_ip_address>
> ```
>
> The parameter `<robot_ip_address>` means the IP address of the TM Robot.<br/>
> <table><tr><td bgcolor=Bisque> <font color=red> WARNING :</font> Some demos will let the TM Robot move, please be careful.</td></tr></table><br/>
><br/>
