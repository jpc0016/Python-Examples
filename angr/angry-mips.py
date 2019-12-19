# Solving a MIPS binary
#
# angry-mips.py
#
# Load a shared embedded object /lib/ld-uClibc.so.0 with the MIPS 32-bit
# LSB binary

import angr
import sys
import monkeyhex

def main(argv):
    # initialize path to binary (string)
    path_to_binary = '/home/jpc0016/projects/rootme/cracking/ch27-elf-mips/ch27.bin'

    # create project object
    project = angr.Project(path_to_binary, use_sim_procedures=True)
    project.hook(addr, angr.SIM_PROCEDURES['libc']['atoi']())


    # tell angr where to start executing the binary
    initial_state = project.factory.entry_state()

    # create simulation manager initialized with initial state
    simulation = project.factory.simgr(initial_state)

    # explore the simulation to find victory address
    print_good_address = 0x4007c0
    simulation.explore(find=print_good_address)

    # if a solution is found, a list of possible solutions will be set to solution_state
    if simulation.found:
        solution_state = simulation.found[0]

        # print string to stdin
        print(solution_state.posix.dumps(sys.stdin.fileno()))
    else:
        # show message if no solution found
        raise Exception('Could not find the solution')

if __name__ == '__main__':
    main(sys.argv)
