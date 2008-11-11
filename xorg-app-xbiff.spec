Summary:	xbiff application
Summary(pl.UTF-8):	Aplikacja xbiff
Name:		xorg-app-xbiff
Version:	1.0.1
Release:	4
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xbiff-%{version}.tar.bz2
# Source0-md5:	404f5add4537d22dd109c33e518a5190
Patch0:		%{name}-maildir.patch
Patch1:		%{name}-xaw.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-data-xbitmaps
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xbiff application.

%description -l pl.UTF-8
Aplikacja xbiff.

%prep
%setup -q -n xbiff-%{version}
%patch0 -p1
%patch1 -p1

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
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/xbiff
%{_mandir}/man1/xbiff.1x*
