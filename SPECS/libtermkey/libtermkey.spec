Summary:        This library allows easy processing of keyboard entry from terminal-based programs.
Name:           libtermkey
Version:        0.22
Release:        1%{?dist}
License:        MIT
Group:          Development/Tools
Vendor:         Microsoft Corporation
Distribution:   Mariner
Url:            https://www.leonerd.org.uk/code/libtermkey/
Source0:        https://www.leonerd.org.uk/code/libtermkey/libtermkey-%{version}.tar.gz
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  unibilium-devel
Requires:       unibilium

%description
This library allows easy processing of keyboard entry from terminal-based programs.
It handles all the necessary logic to recognise special keys, UTF-8 combining, and so on, with a simple interface.

%package    devel
Summary:    Header and development files for unibilium
Requires:   %{name} = %{version}-%{release}
%description    devel
It contains the libraries and header files.

%prep
%setup -q

%build
make

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} PREFIX=%{_prefix} install
find %{buildroot} -type f -name "*.la" -delete -print

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%license LICENSE
%{_libdir}/libtermkey.so.*
%{_mandir}/man3/*.3*
%{_mandir}/man7/*.7*

%files devel
%{_includedir}/termkey.h
%{_libdir}/libtermkey.a
%{_libdir}/libtermkey.so
%{_libdir}/pkgconfig/termkey.pc

%changelog
* Thu Jun 08 2023 Andy Voltz <anvoltz@microsoft.com> - 0.22
- Initial version
