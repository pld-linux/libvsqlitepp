#
# Conditional build:
%bcond_without	static_libs	# static library build
#
Summary:	Well designed C++ sqlite 3.x wrapper library
Summary(pl.UTF-8):	Dobrze zaprojektowana biblioteka obudowująca C++ dla sqlite 3.x
Name:		libvsqlitepp
Version:	0.3.13
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://evilissimo.fedorapeople.org/releases/vsqlite--/%{version}/vsqlite++-%{version}.tar.xz
# Source0-md5:	f0616fd2680e0c78e50f78f6b869c0ba
URL:		https://github.com/vinzenz/vsqlite--
BuildRequires:	boost-devel >= 1.33
BuildRequires:	doxygen
BuildRequires:	graphviz
BuildRequires:	libstdc++-devel
BuildRequires:	sqlite3-devel >= 3
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VSQLite++ is a C++ wrapper for sqlite3 using the C++ standard library
and Boost. VSQLite++ is designed to be easy to use and focuses on
simplicity.

%description -l pl.UTF-8
VSQLite++ to obudowanie C++ dla sqlite3 przy użyciu biblioteki
standardowej C++ oraz Boosta. Jest zaprojektowane z myślą o łatwym
użyciu, skupia się na prostocie.

%package devel
Summary:	Development files for VSQLite++ library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki VSQLite++
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	boost-devel >= 1.33
Requires:	libstdc++-devel

%description devel
This package contains development files for VSQLite++ library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki programistyczne biblioteki VSQLite++.

%package static
Summary:	Static VSQLite++ library
Summary(pl.UTF-8):	Statyczna biblioteka VSQLite++
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static VSQLite++ library.

%description static -l pl.UTF-8
Statyczna biblioteka VSQLite++.

%package doc
Summary:	Development documentation for VSQLite++ library
Summary(pl.UTF-8):	Dokumentacja programisty do biblioteki VSQLite++
Group:		Documentation
# noarch subpackages only when building with rpm5
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc
This package contains development documentation files for VSQLite++.

%description doc -l pl.UTF-8
Ten pakiet zawiera dokumentację programisty do biblioteki VSQLite++.

%prep
%setup -q -n vsqlite++-%{version}

%build
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}
doxygen Doxyfile

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libvsqlitepp.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README TODO
%attr(755,root,root) %{_libdir}/libvsqlitepp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvsqlitepp.so.3

%files devel
%defattr(644,root,root,755)
%doc examples/sqlite_wrapper.cpp
%attr(755,root,root) %{_libdir}/libvsqlitepp.so
%{_includedir}/sqlite

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libvsqlitepp.a
%endif

%files doc
%defattr(644,root,root,755)
%doc html/*
