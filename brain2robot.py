
@nrp.MapSpikeSink("output0", nrp.brain.actors[0], nrp.population_rate)
@nrp.MapSpikeSink("output1", nrp.brain.actors[1], nrp.population_rate)
@nrp.MapSpikeSink("output2", nrp.brain.actors[2], nrp.population_rate)
@nrp.MapSpikeSink("debug", nrp.brain.sensors, nrp.population_rate)
@nrp.MapRobotPublisher('arm_2_joint', Topic('/robot/hollie_real_left_arm_2_joint/cmd_pos', std_msgs.msg.Float64))
@nrp.MapRobotPublisher('arm_3_joint', Topic('/robot/hollie_real_left_arm_3_joint/cmd_pos', std_msgs.msg.Float64))
@nrp.MapRobotPublisher('arm_5_joint', Topic('/robot/hollie_real_left_arm_5_joint/cmd_pos', std_msgs.msg.Float64))
@nrp.Neuron2Robot()
# Example TF: get output neuron voltage and actuate the arm with the current simulation time. You could do something with the voltage here and command the robot accordingly.
def swing(t, debug, output0, output1, output2, arm_2_joint, arm_3_joint, arm_5_joint):
    clientLogger.info(debug.rate, [output0.rate, output1.rate, output2.rate])
    arm_2_joint.send_message(std_msgs.msg.Float64(min(-1.0 + output0.rate / 50.0, 1.0)))
    arm_3_joint.send_message(std_msgs.msg.Float64(min(-1.0 + output1.rate / 50.0, 1.0)))
    arm_5_joint.send_message(std_msgs.msg.Float64(min(-1.0 + output2.rate / 50.0, 1.0)))
