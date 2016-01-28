# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "hri_navigation: 1 messages, 0 services")

set(MSG_I_FLAGS "-Ihri_navigation:/home/ted/catkin_ws/src/hri_navigation/msg;-Istd_msgs:/opt/ros/jade/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(hri_navigation_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/ted/catkin_ws/src/hri_navigation/msg/Goal.msg" NAME_WE)
add_custom_target(_hri_navigation_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "hri_navigation" "/home/ted/catkin_ws/src/hri_navigation/msg/Goal.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(hri_navigation
  "/home/ted/catkin_ws/src/hri_navigation/msg/Goal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/hri_navigation
)

### Generating Services

### Generating Module File
_generate_module_cpp(hri_navigation
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/hri_navigation
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(hri_navigation_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(hri_navigation_generate_messages hri_navigation_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ted/catkin_ws/src/hri_navigation/msg/Goal.msg" NAME_WE)
add_dependencies(hri_navigation_generate_messages_cpp _hri_navigation_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(hri_navigation_gencpp)
add_dependencies(hri_navigation_gencpp hri_navigation_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS hri_navigation_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(hri_navigation
  "/home/ted/catkin_ws/src/hri_navigation/msg/Goal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/hri_navigation
)

### Generating Services

### Generating Module File
_generate_module_eus(hri_navigation
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/hri_navigation
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(hri_navigation_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(hri_navigation_generate_messages hri_navigation_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ted/catkin_ws/src/hri_navigation/msg/Goal.msg" NAME_WE)
add_dependencies(hri_navigation_generate_messages_eus _hri_navigation_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(hri_navigation_geneus)
add_dependencies(hri_navigation_geneus hri_navigation_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS hri_navigation_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(hri_navigation
  "/home/ted/catkin_ws/src/hri_navigation/msg/Goal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/hri_navigation
)

### Generating Services

### Generating Module File
_generate_module_lisp(hri_navigation
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/hri_navigation
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(hri_navigation_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(hri_navigation_generate_messages hri_navigation_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ted/catkin_ws/src/hri_navigation/msg/Goal.msg" NAME_WE)
add_dependencies(hri_navigation_generate_messages_lisp _hri_navigation_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(hri_navigation_genlisp)
add_dependencies(hri_navigation_genlisp hri_navigation_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS hri_navigation_generate_messages_lisp)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(hri_navigation
  "/home/ted/catkin_ws/src/hri_navigation/msg/Goal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/hri_navigation
)

### Generating Services

### Generating Module File
_generate_module_py(hri_navigation
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/hri_navigation
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(hri_navigation_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(hri_navigation_generate_messages hri_navigation_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ted/catkin_ws/src/hri_navigation/msg/Goal.msg" NAME_WE)
add_dependencies(hri_navigation_generate_messages_py _hri_navigation_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(hri_navigation_genpy)
add_dependencies(hri_navigation_genpy hri_navigation_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS hri_navigation_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/hri_navigation)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/hri_navigation
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
add_dependencies(hri_navigation_generate_messages_cpp std_msgs_generate_messages_cpp)

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/hri_navigation)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/hri_navigation
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
add_dependencies(hri_navigation_generate_messages_eus std_msgs_generate_messages_eus)

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/hri_navigation)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/hri_navigation
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
add_dependencies(hri_navigation_generate_messages_lisp std_msgs_generate_messages_lisp)

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/hri_navigation)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/hri_navigation\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/hri_navigation
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
add_dependencies(hri_navigation_generate_messages_py std_msgs_generate_messages_py)
