cmake_minimum_required(VERSION 3.1.0)

project(nemosettings
    VERSION 0.0.2
    DESCRIPTION "Provides QML features of class QSettings")

set(CMAKE_AUTOMOC ON)

set(CMAKE_INCLUDE_CURRENT_DIR ON)
include(FeatureSummary)
include(GNUInstallDirs)

set(QT_MIN_VERSION "5.6.0")

find_package(QT NAMES Qt6 Qt5 REQUIRED COMPONENTS Core)
find_package(Qt${QT_VERSION_MAJOR} REQUIRED COMPONENTS Core Qml Quick)
add_subdirectory(src)

feature_summary(WHAT PACKAGES_FOUND PACKAGES_NOT_FOUND FATAL_ON_MISSING_REQUIRED_PACKAGES)