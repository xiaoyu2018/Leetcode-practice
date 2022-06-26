cmake_minimum_required(VERSION 3.0.0)
project(Algorithm VERSION 0.1.0)

include(CTest)
enable_testing()

add_executable(Algorithm 1047删除字符串中所有相邻重复项.cpp)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
