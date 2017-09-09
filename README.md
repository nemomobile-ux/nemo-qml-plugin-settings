**Nemomobile qml wrapper for QSettings class**

Upsage:

    import QtQuick 2.0
    import org.nemomobile.settings 1.0

    Item{
            Settings{
                    id: mainSettings
            }

                Component.onComplited{
                        mainSettings.setValue("key","hello");
                        var value = mainSettings.value("key");
                }

                Connections{
                        target: mainSettings
                        onValueChange: {
                                console.log("key "+key+" changed! Current value is:"+value);
                        }
                }
    }
