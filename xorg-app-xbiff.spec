Summary:	xbiff application - mailbox flag for X
Summary(pl.UTF-8):	Aplikacja xbiff - flaga skrzynki pocztowej dla X
Name:		xorg-app-xbiff
Version:	1.0.5
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/xbiff-%{version}.tar.xz
# Source0-md5:	0964f62fc603caf1bd0d88d648f2be9a
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-data-xbitmaps
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.1.0
BuildRequires:	xorg-proto-xproto-devel >= 7.0.25
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
Requires:	xorg-lib-libXt >= 1.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xbiff application provides graphical notification of new e-mail. It
only handles mail stored in a filesystem accessible file, not via
IMAP, POP or other remote access protocols.

%description -l pl.UTF-8
Aplikacja xbiff zapewnia graficzne powiadomienia o nowych
wiadomościach e-mail. Obsługuje wyłącznie pocztę zapisywaną w pliku
dostępnym poprzez system plików, nie przez IMAP, POP czy inne
protokoły zdalnego dostępu.

%prep
%setup -q -n xbiff-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-mailbox-directory=/var/mail

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_bindir}/xbiff
%{_mandir}/man1/xbiff.1*
