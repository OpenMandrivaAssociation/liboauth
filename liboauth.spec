%define major 0
%define libname %mklibname oauth %{major}
%define develname %mklibname -d oauth

Summary:        OAuth library functions
Name:           liboauth
Version:        0.9.7
Release:        1
Group:          System/Libraries
License:        MIT
URL:            http://liboauth.sourceforge.net/
Source0:        http://liboauth.sourceforge.net/pool/liboauth-%{version}.tar.gz

BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(nss)

%description
liboauth is a collection of POSIX-c functions implementing the OAuth
Core RFC 5849 standard. liboauth provides functions to escape and
encode parameters according to OAuth specification and offers
high-level functionality to sign requests or verify OAuth signatures
as well as perform HTTP requests.

%package        -n %{libname}
Summary:        OAuth library functions
Group:          System/Libraries

%description    -n %{libname}
liboauth is a collection of POSIX-c functions implementing the OAuth
Core RFC 5849 standard. liboauth provides functions to escape and
encode parameters according to OAuth specification and offers
high-level functionality to sign requests or verify OAuth signatures
as well as perform HTTP requests.

%package        -n %{develname}
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{libname} = %{version}-%{release}
Provides:       %{name}-devel  = %{version}-%{release}

%description    -n %{develname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
autoreconf -fi
%configure2_5x \
	--disable-static \
	--enable-nss

%make

%install
%makeinstall_std
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%files -n %{libname}
%{_libdir}/liboauth.so.%{major}*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/oauth.pc
%{_mandir}/man3/oauth.*

