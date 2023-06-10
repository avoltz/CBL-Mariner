Summary:        This library makes libuv available to lua scripts.
Name:           luv
Version:        1.44.2
Release:        1%{?dist}
License:        Apache-2.0
Group:          Development/Tools
Vendor:         Microsoft Corporation
Distribution:   Mariner
Url:            https://luvit.io
Source0:        https://github.com/luvit/%{name}/releases/download/%{version}/%{name}-%{version}-1.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libuv-devel
BuildRequires:  luajit-devel
BuildRequires:  lua-compat-5.3-devel
Requires:       libuv

%description
This library makes libuv available to lua scripts.
It was made for the luvit project but should usable from nearly any lua project.

The library can be used by multiple threads at once.

%package    devel
Summary:    Header and development files for luv
Requires:   %{name} = %{version}-%{release}
%description    devel
It contains the libraries and header files.

%prep
%setup -q -n %{name}-%{version}-1

%build
mkdir build && cd build
%cmake .. -DWITH_SHARED_LIBUV=ON -DLUA_BUILD_TYPE=System -DWITH_LUA_ENGINE=LuaJIT -DLUA_COMPAT53_DIR=/usr/include/lua-compat-5.3/
%make_build

%install
%make_install -C build

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%license LICENSE.txt
%{_libdir}/libluv.so*
%{_libdir}/lua/5.1/luv.so

%files devel
%{_includedir}/luv/*.h
%{_libdir}/pkgconfig/*.pc

%changelog
* Fri Jun 09 2023 Andy Voltz <anvoltz@microsoft.com> - 1.44.2
- Initial version
