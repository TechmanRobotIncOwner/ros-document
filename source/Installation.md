## __2. Feature and Installation__



Note: The two current master branches are ROS1 Melodic and ROS2 Foxy.<br/>

### &sect; __ROS Driver Feaure__

The TM ROS driver connects to _TMflow Ethernet Slave_ to control _TMflow project_. Robot state is transmitted through this connection.  A working driver also connects to a _Listen node_ (running at a _TMflow project_) at the same time. To control the robot locomotion ,IO ,etc., the TM ROS driver sends robot script (_TM Robot Expression_) through this connection.
More information about _TM Robot Expression_ and _Ethernet Slave_, see [Expression Editor and Listen Node.pdf](https://assets.omron.eu/downloads/manual/en/v1/i848_tm_expression_editor_and_listen_node_reference_manual_en.pdf).
The TM ROS driver for ROS1 is a __single ROS node__ which creates a ROS interface such as topics and services:

> __Action Server__
>
> - An  action interface on _/follow_joint_trajectory_ for seamless integration with MoveIt
>
> __Topic Publisher__
>
> - publish feedback state on _/feedback_states_ 
feedback state include robot position, error code, io state, etc.
(see _tm_msgs/msg/FeedbackState.msg_) 
> - publish joint states on _/joint_states_ 
> - publish tool pose on _/tool_pose_
>
> __Service Server__
>
> - _/tm_driver/send_script_ (see _tm_msgs/srv/SendScript.srv_) : 
send robot script (_TM Robot Expression_) to _Listen node_ 
> - _/tm_driver/set_event_ (see _tm_msgs/srv/SetEvent.srv_) : 
send "Stop", "Pause" or "Resume" command to _Listen node_ 
> - _/tm_driver/set_io_ (see _tm_msgs/srv/SetIO.srv_) : 
send digital or analog output value to _Listen node_ 
> - _/tm_driver/set_position (see _tm_msgs/srv/SetPosition.srv_) : 
send motion command to _Listen node_, the motion type include PTP, LINE, CIRC ans PLINE, the position value is joint angle(__J__) or tool pose(__T__), see [[Expression Editor and Listen Node.pdf]]
>
>

### &sect; __ROS1 Melodic Installation__
Just clone the TM ROS driver of git repository into your working directory and then built it.<br/>
The user can directly refer to the chapters introduced in the following text: steps 1 to 4 of __&sect; Usage with demo code & driver__.<br/>

### &sect; __ROS1 Noetic Installation__
Just clone the TM ROS driver of git repository into your working directory and then built it.<br/>
The user can directly refer to the chapters introduced in the following text: steps 1 to 4 of __&sect; Usage with demo code & driver__.<br/>

### &sect; __ROS2 Dashing Installation__
Just clone the TM ROS driver of git repository into your working directory and then built it.<br/>
The user can directly refer to the chapters introduced in the following text: steps 1 to 4 of __&sect; Usage with demo code & driver__.<br/>

### &sect; __ROS2 Foxy Installation__
Just clone the TM ROS driver of git repository into your working directory and then built it.<br/>
The user can directly refer to the chapters introduced in the following text: steps 1 to 4 of __&sect; Usage with demo code & driver__.<br/>
