#
# Conditional build:
#
%define		_state		stable
%define		orgname		krfb
%define		qtver		4.8.3

Summary:	Virtual Desktops
Summary(pl.UTF-8):	Wirtualne biurka
Name:		kde4-krfb
Version:	4.14.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	c130cf8ad2551de14f8dd9a6a32121d9
URL:		http://www.kde.org/
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtOpenGL-devel >= %{qtver}
BuildRequires:	QtScript-devel >= %{qtver}
BuildRequires:	QtSql-devel >= %{qtver}
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	QtTest-devel >= %{qtver}
BuildRequires:	QtWebKit-devel >= %{qtver}
BuildRequires:	alsa-lib-devel
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	boost-devel
BuildRequires:	cmake >= 2.8.0
BuildRequires:	giflib-devel
BuildRequires:	gmp-devel
BuildRequires:	gpgme-devel
BuildRequires:	jasper-devel
BuildRequires:	kde4-kdebase-devel >= %{version}
BuildRequires:	kde4-kdebase-workspace-devel >= 4.11.4
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-kdepimlibs-devel >= %{version}
BuildRequires:	libgadu-devel >= 1.8.0
BuildRequires:	libidn-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libktorrent-devel >= 1.0.2
BuildRequires:	libmms-devel
BuildRequires:	libmsn-devel >= 4.1
BuildRequires:	libotr-devel >= 4.0.0
BuildRequires:	libv4l-devel >= 0.5.8
BuildRequires:	libvncserver-devel
BuildRequires:	libxml2-progs
BuildRequires:	libxslt-devel >= 1.0.7
BuildRequires:	meanwhile-devel >= 1.0.1
BuildRequires:	mediastreamer-devel >= 2.3.0
BuildRequires:	msilbc-devel >= 2.0.1
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	ortp-devel >= 0.16.1-3
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig
BuildRequires:	qca-devel >= 2.0
BuildRequires:	qimageblitz-devel >= 0.0.6
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	shared-desktop-ontologies-devel >= 0.5
BuildRequires:	soprano-devel >= 2.4.64
BuildRequires:	speex-devel
BuildRequires:	sqlite3-devel
BuildRequires:	strigi-devel >= 0.7.2
BuildRequires:	telepathy-qt4-devel >= 0.9.0
BuildRequires:	xmms-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXtst-devel
Requires:	kde4-kdebase >= %{version}
# needed for /usr/share/telepathy
Requires:	telepathy-mission-control
Suggests:	rdesktop
Obsoletes:	kde4-kdenetwork-%{orgname}
Obsoletes:	kdenetwork4
Conflicts:	kdenetwork4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Remote Desktop Connection is a client application that allows you to
view or even control the desktop session on another machine that is
running a compatible (VNC) server. You would typically use Remote
Desktop Connection with the KDE VNC server, which is Desktop Sharing
(also provided in this package), since it closely matches the special
features of Remote Desktop Connection.

%description -l pl.UTF-8
Remote Desktop Connection to aplikacja kliencka umożliwiająca
oglądanie a nawet sterowanie sesją na innej maszynie z działającym
kompatybilnym serwerem (VNC). Zwykle używa się Remote Desktop
Connection z użyciem serwera KDE VNC, czyli "dzielenia pulpitu" (także
dostarczanego przez ten pakiet), jako że najlepiej pasuje do
specjalnych możliwości Remote Desktop Connection.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	-DMOZPLUGIN_INSTALL_DIR=%{_browserpluginsdir} \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/krfb
%attr(755,root,root) %{_libdir}/libkrfbprivate.so.*.*.*
%attr(755,root,root) %{_libdir}/kde4/krfb_framebuffer_qt.so
%attr(755,root,root) %{_libdir}/kde4/krfb_framebuffer_x11.so
%{_datadir}/apps/krfb
%{_datadir}/kde4/services/krfb_framebuffer_qt.desktop
%{_datadir}/kde4/services/krfb_framebuffer_x11.desktop
%{_datadir}/kde4/servicetypes/krfb-framebuffer.desktop
%{_desktopdir}/kde4/krfb.desktop
%{_kdedocdir}/en/krfb
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.kr*.service
%{_datadir}/telepathy/clients/kr*.client
