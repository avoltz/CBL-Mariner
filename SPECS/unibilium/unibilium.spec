Summary:        Unibilium is a very basic terminfo library
Name:           unibilium
Version:        2.1.1
Release:        1%{?dist}
License:        LGPLv3+
Group:          Development/Tools
Vendor:         Microsoft Corporation
Distribution:   Mariner
Url:            https://github.com/neovim/unibilium
#Source0:        https://github.com/neovim/%{name}/archive/refs/tags/v%{version}.tar.gz
Source0:        %{name}-v%{version}.tar.gz
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libtool

%description
Unibilium is a very basic terminfo library. It can read and write
ncurses-style terminfo files, and it can interpret terminfo format strings.
It doesn't depend on curses or any other library. It also doesn't use global
variables, so it should be thread-safe.

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
%license LICENSE LGPLv3
%{_mandir}/man3/*.3*
%{_libdir}/libunibilium.so.*

%files devel
%{_includedir}/unibilium.h
%{_libdir}/libunibilium.a
%{_libdir}/libunibilium.so
%{_libdir}/pkgconfig/unibilium.pc

%changelog
* Thu Jun 08 2023 Andy Voltz <anvoltz@microsoft.com> - 2.1.1
- Initial version
