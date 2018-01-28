
@nrp.MapSpikeSink("output_neuron", nrp.brain.neurons[1], nrp.leaky_integrator_alpha)
@nrp.Neuron2Robot(Topic('/robot/hollie_real_left_arm_2_joint/cmd_pos', std_msgs.msg.Float64))
# Example TF: get output neuron voltage and actuate the arm with the current simulation time. You could do something with the voltage here and command the robot accordingly.
def swing(t, output_neuron):
    pos = t * (-1)
    if t > 1:
        pos = t * 4
    if t > 2:
        pos = 0
    voltage=output_neuron.voltage
    return std_msgs.msg.Float64(pos)
