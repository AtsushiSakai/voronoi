cmake_minimum_required(VERSION 3.15)
project(voronoi C)

set(CMAKE_C_STANDARD 99)

add_executable(voronoi test/assert_test.c test/invalid_data.h)
target_include_directories(voronoi PUBLIC "src")
