import qbs

Project{
    property string version: "0.1"

    DynamicLibrary {
        name: "nemosettings"
        files: [
            "src/plugin.cpp",
            "src/settings.cpp",
            "src/settings.h",
        ]
        Depends {
            name: "cpp"
        }
        Depends {
            name: "Qt.quick"
        }

        Group {
            qbs.install: true
            qbs.installDir: "/usr/lib/qt5/qml/org/nemomobile/settings/"
            fileTagsFilter: "dynamiclibrary"
        }

        Group{
            qbs.install: true
            qbs.installDir: "/usr/lib/qt5/qml/org/nemomobile/settings/"
            files: [
                "src/qmldir"
            ]
        }
    }
}
