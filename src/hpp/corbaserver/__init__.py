import omniORB
omniORB.updateModule("hpp.corbaserver")

import robot_idl
import common_idl
import obstacle_idl
import problem_idl
import server_idl_idl

from .client import Client
from .robot import Robot
Transform = common_idl._0_hpp.Transform
from .problem_solver import ProblemSolver, newProblem, loadServerPlugin
from .benchmark import Benchmark
