Summary:	xbiff application - mailbox flag for X
Summary(pl.UTF-8):	Aplikacja xbiff - flaga skrzynki pocztowej dla X
Name:		xorg-app-xbiff
Version:	1.0.2
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xbiff-%{version}.tar.bz2
# Source0-md5:	1d4ad06725f9dc4b877ecd210b7b1607
Patch0:		%{name}-maildir.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-data-xbitmaps
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-util-util-macros >= 1.3
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
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/xbiff
%{_mandir}/man1/xbiff.1x*
