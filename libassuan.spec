#specfile originally created for Fedora, modified for Moblin Linux

Name:    libassuan
Summary: GnuPG IPC library
Version: 1.0.5
Release: 5.3.moblin2

License: LGPLv2+
Source0: ftp://ftp.gnupg.org/gcrypt/libassuan/libassuan-%{version}.tar.bz2
Source1: ftp://ftp.gnupg.org/gcrypt/libassuan/libassuan-%{version}.tar.bz2.sig
URL:     http://www.gnupg.org/
Group:   System/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Patch1:  libassuan-1.0.5-multilib.patch

# -debuginfo useless for (only) static libs
%define debug_package   %{nil}

BuildRequires: gawk
BuildRequires: pth-devel

%description
This is the IPC library used by GnuPG 2, GPGME and a few other
packages.

%package devel 
Summary: GnuPG IPC library 
Group: Development/Libraries
Requires: pth-devel
Requires(post): /sbin/install-info
Requires(postun): /sbin/install-info
Obsoletes: %{name}-static < %{version}-%{release}
Provides:  %{name}-static = %{version}-%{release}
%description devel 
This is the IPC static library used by GnuPG 2, GPGME and a few other
packages.

This package contains files needed to develop applications using %{name}.


%prep
%setup -q

%patch1 -p1 -b .multilib


%build
#ifarch x86_64
export CFLAGS="%{optflags} -fPIC"
#endif
%configure

make %{?_smp_mflags}


%install
rm -rf %{buildroot}

make install DESTDIR=%{buildroot}

## Unpackaged files
rm -f %{buildroot}%{_infodir}/dir


%check
make check


%post devel 
[ -e %{_infodir}/assuan.info ] && /sbin/install-info %{_infodir}/assuan.info %{_infodir}/dir &>/dev/null || :

%postun devel 
if [ $1 -eq 0 ]; then
  [ -e %{_infodir}/assuan.info ] && /sbin/install-info --delete %{_infodir}/assuan.info %{_infodir}/dir &>/dev/null || :
fi


%clean
rm -rf %{buildroot}


%files devel 
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING.LIB NEWS README THANKS TODO
%{_bindir}/libassuan-config
%{_includedir}/*
%{_libdir}/lib*.a
%{_datadir}/aclocal/*
%doc %{_infodir}/assuan.info*

