## __4. ROS1 Usage__

> __ROS1 driver usage__
> 
> After the user has set up the ROS1 environment and built the TM driver based on the specific workspace, please enter your workspace `<workspace>` by launching the terminal, and remember to make the workspace visible to ROS.
>
>
> ```bash
> source /opt/ros/noetic/setup.bash
> cd <workspace>
> source ./devel/setup.bash
> ```
> <table><tr><td bgcolor=Bisque> <font color=black> Note :</font><br/> Do you prepare the <b>TM Robot</b> ready ? Make sure that TM Robot's operating software (<b>TMflow</b>) network settings are ready and the <b>Listen node</b> is running.</td></tr></table><br/>
> 
> Then, run the driver to maintain the connection with TM Robot by typing 
>
>```bash
> rosrun tm_driver tm_driver <robot_ip_address>
>```
> Example :``rosrun tm_driver tm_driver 192.168.10.2``, if the <robot_ip_address> is 192.168.10.2
>
> Now, the user can use a new terminal to run each ROS node or command, but don't forget to source the correct setup shell files as starting a new terminal.

> __Usage with MoveIt__ 
>
> See [Moveit tutorial](https://ros-planning.github.io/moveit_tutorials/).<br/>
>
> To bring up MoveIt environment in simulation mode with virtual TM Robot, by typing
>
>
> ```bash
> roslaunch tm5_900_moveit_config tm5_900_moveit_planning_execution.launch sim:=True
> ```
>
> The user can also manipulate TM Robot in the real world, by typing<br/>
> <table><tr><td bgcolor=Bisque> <font color=black> Note :</font><br/> Do you prepare the <b>TM Robot</b> ready ? Make sure that TM Robot's operating software (<b>TMflow</b>) network settings are ready and the <b>Listen node</b> is running.</td></tr></table><br/>
>
> ```bash
> roslaunch tm5_900_moveit_config tm5_900_moveit_planning_execution.launch sim:=False robot_ip:=<robot_ip_address>
> ```
>
> The parameter `<robot_ip_address>` means the IP address of the TM Robot.<br/>
> <table><tr><td bgcolor=Bisque> <font color=red> WARNING :</font> This demo will let the real TM Robot move, please be careful.</td></tr></table><br/>
