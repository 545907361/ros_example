# generated from catkin/cmake/template/pkg.context.pc.in
CATKIN_PACKAGE_PREFIX = ""
PROJECT_PKG_CONFIG_INCLUDE_DIRS = "${prefix}/include".split(';') if "${prefix}/include" != "" else []
PROJECT_CATKIN_DEPENDS = "roscpp;pluginlib;nodelet;ecl_threads;dynamic_reconfigure;geometry_msgs;nav_msgs".replace(';', ' ')
PKG_CONFIG_LIBRARIES_WITH_PREFIX = "-lfollower_velocity_smoother_nodelet".split(';') if "-lfollower_velocity_smoother_nodelet" != "" else []
PROJECT_NAME = "follower_velocity_smoother"
PROJECT_SPACE_DIR = "/home/feng/catkin_ws/install"
PROJECT_VERSION = "0.6.4"
