Name:    libassuan
Summary: GnuPG IPC library
Version: 2.5.5
Release: 1

License: LGPLv2+
Source0: libassuan-%{version}.tar.bz2
URL:     http://www.gnupg.org/software/libassuan

BuildRequires: gawk
BuildRequires: pkgconfig(npth)
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
This is the IPC library used by GnuPG 2, GPGME and a few other
packages.

%package devel 
Summary: GnuPG IPC library 
Requires: %{name} = %{version}-%{release}
Requires(post): /sbin/install-info
Requires(postun): /sbin/install-info
%description devel 
This is the IPC static library used by GnuPG 2, GPGME and a few other
packages.

This package contains files needed to develop applications using %{name}.


%prep
%autosetup -p1 -n %{name}-%{version}/upstream


%build
%reconfigure --enable-maintainer-mode
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install


%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post devel
if [ -f %{_infodir}/assuan.info.gz ]; then
    /sbin/install-info %{_infodir}/assuan.info.gz %{_infodir}/dir || :
fi

%preun devel
if [ $1 = 0 -a -f %{_infodir}/assuan.info.gz ]; then
   /sbin/install-info --delete %{_infodir}/assuan.info.gz %{_infodir}/dir || :
fi

%files
%defattr(-,root,root)
%{_libdir}/libassuan.so.*

%files devel 
%defattr(-,root,root,-)
%doc README
%{_bindir}/libassuan-config
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/*
%doc %{_infodir}/assuan.info*

