# Copyright (c) 2022-2025, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

from isaaclab.utils import configclass

import leapfeels.envs.inhand_env_cfg as inhand_env_cfg

##
# Pre-defined configs
##
from leapfeels.assets.leap_hand.leaphand import LEAP_HAND_CFG  # isort: skip


@configclass
class LeapHandCubeEnvCfg(inhand_env_cfg.InHandObjectEnvCfg):
    def __post_init__(self):
        # post init of parent
        super().__post_init__()

        # switch robot to leap hand
        self.scene.robot = LEAP_HAND_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot")


@configclass
class LeapHandCubeEnvCfg_PLAY(LeapHandCubeEnvCfg):
    def __post_init__(self):
        # post init of parent
        super().__post_init__()
        # make a smaller scene for play
        self.scene.num_envs = 50
        # disable randomization for play
        self.observations.policy.enable_corruption = False
        # remove termination due to timeouts
        self.terminations.time_out = None


##
# Environment configuration with no velocity observations.
##


@configclass
class LeapHandCubeNoVelObsEnvCfg(LeapHandCubeEnvCfg):
    def __post_init__(self):
        # post init of parent
        super().__post_init__()

        # switch observation group to no velocity group
        self.observations.policy = inhand_env_cfg.ObservationsCfg.NoVelocityKinematicObsGroupCfg()


@configclass
class LeapHandCubeNoVelObsEnvCfg_PLAY(LeapHandCubeNoVelObsEnvCfg):
    def __post_init__(self):
        # post init of parent
        super().__post_init__()
        # make a smaller scene for play
        self.scene.num_envs = 50
        # disable randomization for play
        self.observations.policy.enable_corruption = False
        # remove termination due to timeouts
        self.terminations.time_out = None
