%define major	0
%define libname %mklibname oauth %{major}
%define devname %mklibname -d oauth

Summary:	OAuth library functions
Name:		liboauth
Version:	1.0.0
Release:	3
Group:		System/Libraries
License:	MIT
Url:		http://liboauth.sourceforge.net/
Source0:	http://liboauth.sourceforge.net/pool/liboauth-%{version}.tar.gz
Patch0:		liboauth-automake-1.13.patch

BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(nss)

%track
prog %{name} = {
	url = http://liboauth.sourceforge.net/
	version = %{version}
	regex = %{name}-(__VER__)\.tar\.gz
}

%description
liboauth is a collection of POSIX-c functions implementing the OAuth
Core RFC 5849 standard. liboauth provides functions to escape and
encode parameters according to OAuth specification and offers
high-level functionality to sign requests or verify OAuth signatures
as well as perform HTTP requests.

%package        -n %{libname}
Summary:	OAuth library functions
Group:		System/Libraries

%description    -n %{libname}
liboauth is a collection of POSIX-c functions implementing the OAuth
Core RFC 5849 standard. liboauth provides functions to escape and
encode parameters according to OAuth specification and offers
high-level functionality to sign requests or verify OAuth signatures
as well as perform HTTP requests.

%package        -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel  = %{version}-%{release}

%description    -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%apply_patches
autoreconf -fi

%build
%configure2_5x \
	--disable-static \
	--enable-nss

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/liboauth.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/oauth.pc
%{_mandir}/man3/oauth.*

