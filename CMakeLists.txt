project(kubeplayer)
cmake_minimum_required(VERSION 2.6)

find_package(KDE4 REQUIRED)
include(KDE4Defaults)
add_subdirectory(lib)
add_subdirectory(data)

configure_file(main.rb main.rb)

install(DIRECTORY lib DESTINATION ${DATA_INSTALL_DIR}/kubeplayer
  FILES_MATCHING PATTERN "*.rb")

install(FILES ${PROJECT_BINARY_DIR}/main.rb
        DESTINATION ${BIN_INSTALL_DIR}
        PERMISSIONS OWNER_READ OWNER_EXECUTE GROUP_EXECUTE WORLD_READ WORLD_EXECUTE
        RENAME kubeplayer)