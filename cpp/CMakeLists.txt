cmake_minimum_required(VERSION 3.0.0)
project(Algorithm VERSION 0.1.0)

include(CTest)
enable_testing()

add_executable(Algorithm 0017电话号码的字母组合.cpp)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
