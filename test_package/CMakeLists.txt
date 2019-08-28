cmake_minimum_required(VERSION 2.8.12)
project(PackageTest C CXX)

set(CMAKE_BUILD_WITH_INSTALL_RPATH ON)

include(${CMAKE_BINARY_DIR}/conan_paths.cmake)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/bin)

if (APPLE)
    set(CMAKE_INSTALL_RPATH "@executable_path/")
else()
    set(CMAKE_INSTALL_RPATH "$ORIGIN/")
endif()

set(CMAKE_BUILD_WITH_INSTALL_RPATH ON)

find_package(blake2 REQUIRED COMPONENTS blake2b)

add_executable(example example.cpp)
target_link_libraries(example blake2::blake2b)

install(TARGETS example RUNTIME DESTINATION bin ARCHIVE DESTINATION lib LIBRARY DESTINATION lib)

