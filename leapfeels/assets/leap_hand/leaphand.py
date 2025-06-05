# Copyright (c) 2022-2025, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""Configuration for the Leap Hand robots from Wonik Robotics.

The following configurations are available:

* :obj:`LEAP_HAND_CFG`: Leap Hand with implicit actuator model.

Reference:

* https://www.wonikrobotics.com/robot-hand

"""


import math

import isaaclab.sim as sim_utils
from isaaclab.actuators.actuator_cfg import ImplicitActuatorCfg
from isaaclab.assets.articulation import ArticulationCfg
from isaaclab.utils.assets import ISAAC_NUCLEUS_DIR

from pathlib import Path

##
# Configuration
##
HERE = Path(__file__).resolve().parent                # /root/LEAP_Hand_Sim/neuralfeels/leapfeels/assets/leap_hand

# USDファイルへの相対パスを組み立て
usd_file = (HERE / "hand" / "robot" / "robot.usd").resolve()
            
LEAP_HAND_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        # usd_path=f"{ISAAC_NUCLEUS_DIR}/Robots/LeapHand/leap_hand_instanceable.usd",
        # usd_path=f"/home/initial/workspace/LEAP_Hand_Sim/assets/leap_hand/robot/robot.usd",
        usd_path=str(usd_file),
        activate_contact_sensors=False,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=True,
            retain_accelerations=False,
            enable_gyroscopic_forces=False,
            angular_damping=0.01,
            max_linear_velocity=1000.0,
            max_angular_velocity=64 / math.pi * 180.0,
            max_depenetration_velocity=1000.0,
            max_contact_impulse=1e32,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=True,
            solver_position_iteration_count=8,
            solver_velocity_iteration_count=0,
            sleep_threshold=0.005,
            stabilization_threshold=0.0005,
        ),
        # collision_props=sim_utils.CollisionPropertiesCfg(contact_offset=0.005, rest_offset=0.0),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        # pos=(0.0, 0.0, 0.5),
        # rot=(0.257551, 0.283045, 0.683330, -0.621782),
        pos=(-0.01754, -0.23918, 0.4758),
        rot=(-0.01416, -0.86568, 0.4998, -0.05),
        # joint_pos={
        #     # すべて 0.0 にして…
        #     **{str(i): 0.0 for i in range(16)},
        #     # …thumb の最初の関節（URDF の "12"）だけ 0.28 rad に
        #     "12": 0.28,
        # },
        joint_pos={
            # USD のプリム名 “a_0”～“a_15” に合わせる
            **{f"a_{i}": 0.0 for i in range(16)},
            # “a_12” のみ 0.28 rad に設定
            "a_12": 0.28,
        },
    ),
    actuators={
        "fingers": ImplicitActuatorCfg(
            # 数値名のジョイントすべてにアクチュエータを適用
            # joint_names_expr=[r"^[0-9]+$"],
            joint_names_expr=[r"^a_[0-9]+$"],
            effort_limit=0.5,
            velocity_limit=100.0,
            stiffness=3.0,
            damping=0.1,
            friction=0.01,
        ),
    },
    soft_joint_pos_limit_factor=1.0,
)
"""Configuration of Leap Hand robot."""
