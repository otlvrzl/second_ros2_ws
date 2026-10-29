cmake_minimum_required(VERSION 3.10.2 FATAL_ERROR)

project(avoid_wall)

# Find the Gazebo_Transport library
find_package(gz_transport_vendor REQUIRED)
find_package(gz-transport REQUIRED)

include_directories(${CMAKE_BINARY_DIR})

if(EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/lidar_node.cc")
add_executable(lidar_node lidar_node.cc)

target_link_libraries(lidar_node
PRIVATE
gz-transport::core
)
endif()