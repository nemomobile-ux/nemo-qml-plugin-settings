Name:       nemo-qml-plugin-settings

Summary:    Nemo QML settings plugin
Version:    0.1.1
Release:    1
Group:      System/Libraries
License:    GPL
URL:        https://github.com/nemomobile-ux/nemo-qml-plugins-settings
Source:    %{name}-%{version}.tar.bz2
BuildRequires:  cmake
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)

%description
QML wrapper for QSettings class

%prep
%setup -q -n %{name}-%{version}

%build
mkdir build
cd build
cmake \
	-DCMAKE_BUILD_TYPE=Debug \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCMAKE_INSTALL_LBIDIR=%{_lib} \
	-DCMAKE_VERBOSE_MAKEFILE=ON \
	..
cmake --build .

%install
cd build
rm -rf %{buildroot}
DESTDIR=%{buildroot} cmake --build . --target install =

%files
%defattr(0644,root,root,-)
%{_libdir}/qt5/qml/org/nemomobile/settings/libnemosettings.so
%{_libdir}/qt5/qml/org/nemomobile/settings/qmldir
