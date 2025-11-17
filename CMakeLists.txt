cmake_minimum_required(VERSION 3.10)

project(n_queens_basic LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_executable(n_queens
    main.cpp
)
