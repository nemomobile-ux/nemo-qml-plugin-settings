TEMPLATE = lib
TARGET = nemosettings

QT += qml
CONFIG += qt plugin hide_symbols


# Input
SOURCES += \
    src/settings.cpp \
    src/plugin.cpp

HEADERS += \
    src/settings.h

DISTFILES = src/qmldir \
    rpm/nemo-qml-plugin-settings.spec \
    README.md

target.path = $$[QT_INSTALL_QML]/org/nemomobile/settings/
INSTALLS += target

qmldir.files += src/qmldir
qmldir.path +=  $$[QT_INSTALL_QML]/org/nemomobile/settings/
INSTALLS += qmldir
