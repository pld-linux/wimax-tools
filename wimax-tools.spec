%define	snap	20090320
Summary:	Low level user space tools for the Linux WiMAX stack
Name:		wimax-tools
Version:	1.4.1
Release:	0.%{snap}.1
License:	BSD
Group:		Networking/Admin
Source0:	%{name}-20090320.tar.bz2
# Source0-md5:	fd05043b611359dee2e75ce41343c9f9
URL:		http://www.linuxwimax.org/
BuildRequires:	doxygen
BuildRequires:	libnl-devel
BuildRequires:	linux-libc-headers >= 7:2.6.29
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Low level user space tools for the Linux WiMAX stack.

%package -n libwimaxll
Summary:	WiMAX library
Group:		Libraries

%description -n libwimaxll
WiMAX library.

%package -n libwimaxll-devel
Summary:	WiMAX library (development files)
Group:		Development/Libraries
Requires:	libwimaxll = %{epoch}:%{version}-%{release}

%description -n libwimaxll-devel
WiMAX library (development files).

%package -n libwimaxll-static
Summary:	WiMAX library (static library)
Group:		Development/Libraries
Requires:	libwimaxll-devel = %{epoch}:%{version}-%{release}

%description -n libwimaxll-static
WiMAX library (static library).

%prep
%setup -q -n %{name}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n libwimaxll -p /sbin/ldconfig
%postun	-n libwimaxll -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc READ* INSTA*
%attr(755,root,root) %{_bindir}/*

%files -n libwimaxll
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwimaxll.so.*

%files -n libwimaxll-devel
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}/html
%attr(755,root,root) %{_libdir}/libwimaxll.so
%{_includedir}/*.h
%{_libdir}/libwimaxll.la
%{_pkgconfigdir}/libwimaxll*.pc

%files -n libwimaxll-static
%defattr(644,root,root,755)
%{_libdir}/libwimaxll.a
