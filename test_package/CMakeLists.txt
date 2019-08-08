cmake_minimum_required(VERSION 2.8.12)
project(PackageTest C CXX)

include(${CMAKE_BINARY_DIR}/conan_paths.cmake)

find_library(LIBBLAKE2B blake2b)
find_path(LIBBLAKE2_INCLUDE_DIR blake2/blake2.h)

if( NOT LIBBLAKE2B )
	message(FATAL_ERROR "Blake2b lib not found!")
elseif( NOT  LIBBLAKE2_INCLUDE_DIR )
	message(FATAL_ERROR "Blake2b includes not found!")
else()	
	message(STATUS "Blake2b lib found!")
endif()

include_directories(${LIBBLAKE2_INCLUDE_DIR})
add_executable(example example.cpp)
target_link_libraries(example ${LIBBLAKE2B})

