Summary:	Pan-o-matic - a tool that automates the creation of control points in Hugin
Summary(pl.UTF-8):	Pan-o-matic - narzędzie automatycznie tworzące punkty kontrolne dla Hugina
Name:		panomatic
Version:	0.9.4
Release:	0.1
License:	GPL v2+
Group:		X11/Applications/Graphics
Source0:	http://aorlinsk2.free.fr/panomatic/bin/%{name}-%{version}-src.tar.bz2 
# Source0-md5:	0b08a4f7e1b4ecaf6ae364779a01da07
Patch0:		%{name}-system-libs.patch
URL:		http://aorlinsk2.free.fr/panomatic/
BuildRequires:	ZThread-devel >= 2.3.1
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	boost-devel >= 1.35.0
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libpng-devel >= 1.2.16
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel >= 3.8.2
# modified vigra 1.5.0 is included
#BuildRequires:	vigra-devel >= 1.5.0
BuildRequires:	zlib-devel >= 1.2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pan-o-matic is a tool that automates the creation of control points in
Hugin.

%description -l pl.UTF-8
Pan-o-matic to narzędzie automatycznie tworzące punkty kontrolne dla
Hugina.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal} -I m4 -I zthread/share
%{__autoconf}
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
%doc AUTHORS
%attr(755,root,root) %{_bindir}/panomatic
