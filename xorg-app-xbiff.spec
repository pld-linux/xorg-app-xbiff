# $Rev: 3371 $, $Date: 2005-08-27 17:42:47 $
#
Summary:	xbiff application
Summary(pl):	Aplikacja xbiff
Name:		xorg-app-xbiff
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/app/xbiff-%{version}.tar.bz2
# Source0-md5:	36e2d36ab6160220afed85d0c0d4a314
Patch0:		xbiff-man.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-data-xbitmaps
BuildRoot:	%{tmpdir}/xbiff-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
xbiff application.

%description -l pl
Aplikacja xbiff


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
%attr(755,root,wheel) %{_bindir}/*
%{_mandir}/man1/*.1*
