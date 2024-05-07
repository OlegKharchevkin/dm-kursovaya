cmake_minimum_required(VERSION 3.5)
project(hamiltonian_cycles)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/..)

add_library(graph ./source/graph.cpp)
add_library("path" ./source/path.cpp)
add_library(hamiltonianCycles ./source/hamiltonianCycles.cpp)
add_library(interface SHARED ./source/interface.cpp)

target_link_libraries(hamiltonianCycles graph "path")
target_link_libraries(interface hamiltonianCycles )