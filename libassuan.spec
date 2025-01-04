#specfile originally created for Fedora, modified for Moblin Linux

Name:    libassuan
Summary: GnuPG IPC library
Version: 1.0.5
Release: 1

License: LGPLv2+
Source0: ftp://ftp.gnupg.org/gcrypt/libassuan/libassuan-%{version}.tar.bz2
Source1: ftp://ftp.gnupg.org/gcrypt/libassuan/libassuan-%{version}.tar.bz2.sig
URL:     http://www.gnupg.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Patch1:  libassuan-1.0.5-multilib.patch
Patch2:  libassuan-1.0.5-include-fix.patch

# -debuginfo useless for (only) static libs
%define debug_package   %{nil}

BuildRequires: gawk
BuildRequires: pth-devel

%description
This is the IPC library used by GnuPG 2, GPGME and a few other
packages.

%package devel
Summary: GnuPG IPC library
Requires: pth-devel
Obsoletes: %{name}-static < %{version}-%{release}
Provides:  %{name}-static = %{version}-%{release}

%description devel
This is the IPC static library used by GnuPG 2, GPGME and a few other
packages.

This package contains files needed to develop applications using %{name}.

%prep
%autosetup -p1

%build
#ifarch x86_64
export CFLAGS="%{optflags} -fPIC"
#endif
%configure --enable-static

%make_build

%install

%make_install

## Unpackaged files
rm -Rf %{buildroot}%{_infodir}

%check
%if ! 0%{?qemu_user_space_build}
make check
%endif

%files devel
%license COPYING.LIB
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%{_bindir}/libassuan-config
%{_includedir}/*
%{_libdir}/lib*.a
%{_datadir}/aclocal/*
