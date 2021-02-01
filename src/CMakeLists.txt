### Sets QT_INSTALL_QML to the directory where QML Plugins should be installed
function(FindQtInstallQml)
    execute_process(
        COMMAND qmake -query QT_INSTALL_QML
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
    Qt5::Core
    Qt5::Qml 
    Qt5::Quick)

FindQtInstallQml()

install(FILES qmldir DESTINATION ${QT_INSTALL_QML}/org/nemomobile/settings/)
install(TARGETS nemosettings DESTINATION ${QT_INSTALL_QML}/org/nemomobile/settings/)