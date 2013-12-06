Summary:	Low level user space tools for the Linux WiMAX stack
Summary(pl.UTF-8):	Niskopoziomowe narzędzia przestrzeni użytkownika do stosu WiMAX Linuksa
Name:		wimax-tools
Version:	1.4.4
Release:	4
License:	BSD
Group:		Networking/Admin
# http://www.linuxwimax.org/Download
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	6acd0e6971952a761c98e9b4c65e6b4e
Patch0:		format-security.patch
URL:		http://www.linuxwimax.org/
BuildRequires:	doxygen
BuildRequires:	glib2-devel >= 1:2.14
BuildRequires:	libnl1-devel >= 1.0-0pre7
BuildRequires:	linux-libc-headers >= 7:2.6.31
BuildRequires:	pkgconfig
Requires:	glib2 >= 1:2.14
Requires:	libwimaxll = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Low level user space tools for the Linux WiMAX stack.

%description -l pl.UTF-8
Niskopoziomowe narzędzia przestrzeni użytkownika do stosu WiMAX
Linuksa.

%package -n libwimaxll
Summary:	WiMAX low-level library
Summary(pl.UTF-8):	Biblioteka niskopoziomowa WiMAX
Group:		Libraries
Requires:	libnl1 >= 1.0-0pre7

%description -n libwimaxll
WiMAX low-level library.

%description -n libwimaxll -l pl.UTF-8
Biblioteka niskopoziomowa WiMAX.

%package -n libwimaxll-devel
Summary:	Header files for WiMAX low-level library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki niskopoziomowej WiMAX
Group:		Development/Libraries
Requires:	libnl1-devel >= 1.0-0.pre7
Requires:	libwimaxll = %{version}-%{release}

%description -n libwimaxll-devel
Header files for WiMAX low-level library.

%description -n libwimaxll-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki niskopoziomowej WiMAX.

%package -n libwimaxll-static
Summary:	WiMAX low-level static library
Summary(pl.UTF-8):	Statyczna biblioteka niskopoziomowa WiMAX
Group:		Development/Libraries
Requires:	libwimaxll-devel = %{version}-%{release}

%description -n libwimaxll-static
WiMAX low-level static library.

%description -n libwimaxll-static -l pl.UTF-8
Statyczna biblioteka niskopoziomowa WiMAX.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/wimax-tools/plugins/*.{a,la}
# obsoleted by pkg-config 
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n libwimaxll -p /sbin/ldconfig
%postun	-n libwimaxll -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
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
%attr(755,root,root) %{_libdir}/libwimaxll.so
%attr(755,root,root) %{_libdir}/libwimaxll-i2400m.so
%{_includedir}/wimaxll
%{_includedir}/wimaxll*.h
%{_pkgconfigdir}/libwimaxll-0.pc
%{_pkgconfigdir}/libwimaxll-i2400m-0.pc
%{_pkgconfigdir}/wimaxll-cmd-0.pc
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/html

%files -n libwimaxll-static
%defattr(644,root,root,755)
%{_libdir}/libwimaxll.a
%{_libdir}/libwimaxll-i2400m.a
