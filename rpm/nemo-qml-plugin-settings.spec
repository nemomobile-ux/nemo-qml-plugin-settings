Name:       nemo-qml-plugin-settings

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}

Summary:    Nemo QML settings plugin
Version:    0.0.1
Release:    1
Group:      System/Libraries
License:    GPL
URL:        https://github.com/nemomobile-ux/nemo-qml-plugins-settings
Source:    %{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
%description
QML wrapper for QSettings class

%prep
%setup -q -n %{name}-%{version}

%build

%qtc_qmake5 VERSION=%{version}
%qtc_make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%qmake5_install

%files
%defattr(0644,root,root,-)
%{_libdir}/qt5/qml/org/nemomobile/settings/libnemosettings.so
%{_libdir}/qt5/qml/org/nemomobile/settings/qmldir
