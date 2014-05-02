Summary:	Well designed C++ sqlite 3.x wrapper library
Name:		libvsqlitepp
Version:	0.3.13
Release:	1
License:	BSD
Group:		Development/Libraries
Source0:	http://evilissimo.fedorapeople.org/releases/vsqlite--/%{version}/vsqlite++-%{version}.tar.xz
# Source0-md5:	f0616fd2680e0c78e50f78f6b869c0ba
URL:		https://github.com/vinzenz/vsqlite--
BuildRequires:	boost-devel >= 1.33
BuildRequires:	doxygen
BuildRequires:	graphviz
BuildRequires:	libtool
BuildRequires:	premake
BuildRequires:	sqlite3-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VSQLite++ is a C++ wrapper for sqlite3 using the C++ standard library
and boost. VSQLite++ is designed to be easy to use and focuses on
simplicity.

%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains development files for %{name}.

%package doc
Summary:	Development documentation for %{name}
Group:		Development/Libraries
# noarch subpackages only when building with rpm5
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc
This package contains development documentation files for %{name}.

%prep
%setup -q -n vsqlite++-%{version}

%build
%configure \
	--disable-static
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
%doc ChangeLog README COPYING
%{_libdir}/libvsqlitepp.so.*.*.*
%ghost %{_libdir}/libvsqlitepp.so.3

%files devel
%defattr(644,root,root,755)
%doc examples/sqlite_wrapper.cpp
%{_libdir}/libvsqlitepp.so
%{_includedir}/sqlite

%files doc
%defattr(644,root,root,755)
%doc html/*
