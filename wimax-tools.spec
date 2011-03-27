Summary:	Low level user space tools for the Linux WiMAX stack
Name:		wimax-tools
Version:	1.4.4
Release:	2
License:	BSD
Group:		Networking/Admin
# http://www.linuxwimax.org/Download
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	6acd0e6971952a761c98e9b4c65e6b4e
URL:		http://www.linuxwimax.org/
BuildRequires:	doxygen
BuildRequires:	glib2-devel >= 1:2.14.0
BuildRequires:	libnl-devel
BuildRequires:	linux-libc-headers >= 7:2.6.29
BuildRequires:	pkgconfig
Requires:	libwimaxll = %{version}-%{release}
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
Requires:	libnl-devel
Requires:	libwimaxll = %{version}-%{release}

%description -n libwimaxll-devel
WiMAX library (development files).

%package -n libwimaxll-static
Summary:	WiMAX library (static library)
Group:		Development/Libraries
Requires:	libwimaxll-devel = %{version}-%{release}

%description -n libwimaxll-static
WiMAX library (static library).

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/wimax-tools/plugins/*.{a,la}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n libwimaxll -p /sbin/ldconfig
%postun	-n libwimaxll -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc READ* INSTA*
%attr(755,root,root) %{_bindir}/wimax-tools-version
%attr(755,root,root) %{_bindir}/wimaxll
%attr(755,root,root) %{_bindir}/wimaxll-reset
%attr(755,root,root) %{_bindir}/wimaxll-rfkill
%attr(755,root,root) %{_bindir}/wimaxll-wait-for-state-change
%dir %{_libdir}/wimax-tools
%dir %{_libdir}/wimax-tools/plugins
%attr(755,root,root) %{_libdir}/wimax-tools/plugins/wimaxll-pl-reset.so
%attr(755,root,root) %{_libdir}/wimax-tools/plugins/wimaxll-pl-rfkill.so
%attr(755,root,root) %{_libdir}/wimax-tools/plugins/wimaxll-pl-state-get.so
%attr(755,root,root) %{_libdir}/wimax-tools/plugins/wimaxll-pl-wfsc.so
%dir %{_libdir}/wimax-tools/test
%attr(755,root,root) %{_libdir}/wimax-tools/test/test-dump-pipe
%attr(755,root,root) %{_libdir}/wimax-tools/test/test-rfkill

%files -n libwimaxll
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwimaxll.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwimaxll.so.0
%attr(755,root,root) %{_libdir}/libwimaxll-i2400m.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwimaxll-i2400m.so.0

%files -n libwimaxll-devel
%defattr(644,root,root,755)
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/html
%attr(755,root,root) %{_libdir}/libwimaxll.so
%attr(755,root,root) %{_libdir}/libwimaxll-i2400m.so
%{_includedir}/wimaxll
%{_includedir}/*.h
%{_pkgconfigdir}/libwimaxll-0.pc
%{_pkgconfigdir}/libwimaxll-i2400m-0.pc
%{_pkgconfigdir}/wimaxll-cmd-0.pc

%files -n libwimaxll-static
%defattr(644,root,root,755)
%{_libdir}/libwimaxll.a
%{_libdir}/libwimaxll-i2400m.a
