Summary:	xbiff application - mailbox flag for X
Summary(pl.UTF-8):	Aplikacja xbiff - flaga skrzynki pocztowej dla X
Name:		xorg-app-xbiff
Version:	1.0.4
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/xbiff-%{version}.tar.bz2
# Source0-md5:	66dd3ebd6351b1911b831b89b2dba8ec
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-data-xbitmaps
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-util-util-macros >= 1.8
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
