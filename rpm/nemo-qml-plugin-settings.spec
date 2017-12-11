Name:       nemo-qml-plugin-settings
Summary:    Nemo QML settings plugin
Version:    0.0.1
Release:    1
Group:      System/Libraries
License:    GPL
URL:        https://github.com/nemomobile-ux/nemo-qml-plugin-settings
Source:    %{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  qbs
%description
QML wrapper for QSettings class

%prep
%setup -q -n %{name}-%{version}
qbs setup-toolchains --detect
qbs setup-qt --detect
qbs config defaultProfile qt-5-6-2

mkdir -p %{buildroot}
%build
qbs build

%install
rm -rf %{buildroot}
qbs install --install-root %{buildroot}

%files
%defattr(0644,root,root,-)
%{_libdir}/qt5/qml/org/nemomobile/settings/libnemosettings.so
%{_libdir}/qt5/qml/org/nemomobile/settings/qmldir
