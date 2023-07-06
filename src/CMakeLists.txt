### Sets QT_INSTALL_QML to the directory where QML Plugins should be installed
function(FindQtInstallQml)
    if (QT_VERSION_MAJOR EQUAL 5)
        find_program(QMAKE NAMES qmake-qt5 qmake)
    elseif (QT_VERSION_MAJOR EQUAL 6)
        find_program(QMAKE NAMES qmake-qt6 qmake6)
    else()
        message(FATAL_ERROR "incorrect QT_VERSION_MAJOR")
    endif ()

    if(NOT QMAKE)
        message(FATAL_ERROR "qmake not found")
    endif()
    execute_process(
        COMMAND ${QMAKE} -query QT_INSTALL_QML
        OUTPUT_VARIABLE PROC_RESULT
        OUTPUT_STRIP_TRAILING_WHITESPACE
    )
    set(QT_INSTALL_QML ${PROC_RESULT} PARENT_SCOPE)
endfunction()


set(SRC
    settings.cpp
    plugin.cpp)

set(HEADERS
    settings.h)

add_library(nemosettings SHARED ${SRC})

target_link_libraries(nemosettings
    Qt${QT_VERSION_MAJOR}::Core
    Qt${QT_VERSION_MAJOR}::Qml
    Qt${QT_VERSION_MAJOR}::Quick)

FindQtInstallQml()

install(FILES qmldir DESTINATION ${QT_INSTALL_QML}/org/nemomobile/settings/)
install(TARGETS nemosettings DESTINATION ${QT_INSTALL_QML}/org/nemomobile/settings/)
