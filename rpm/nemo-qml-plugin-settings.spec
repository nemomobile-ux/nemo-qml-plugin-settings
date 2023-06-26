Name:       nemo-qml-plugin-settings

Summary:    Nemo QML settings plugin
Version:    0.1.1
Release:    1
Group:      System/Libraries
License:    GPL
URL:        https://github.com/nemomobile-ux/nemo-qml-plugins-settings
Source:     %{name}-%{version}.tar.bz2
BuildRequires:  cmake
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)

%description
QML wrapper for QSettings class

%prep
%setup -q -n %{name}-%{version}

%build
%cmake
%cmake_build

%install
rm -rf %{buildroot}
%cmake_install

%files
%defattr(0644,root,root,-)
%{_libdir}/qt5/qml/org/nemomobile/settings/libnemosettings.so
%{_libdir}/qt5/qml/org/nemomobile/settings/qmldir
%dir %{_libdir}/qt5/qml/org
%dir %{_libdir}/qt5/qml/org/nemomobile
%dir %{_libdir}/qt5/qml/org/nemomobile/settings
