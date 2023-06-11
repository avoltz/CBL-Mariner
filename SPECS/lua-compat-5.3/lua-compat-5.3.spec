Summary:        Lua-5.3-style APIs for Lua 5.2 and 5.1.
Name:           lua-compat-5.3
Version:        0.9
Release:        1%{?dist}
License:        MIT
Group:          Development/Tools
Vendor:         Microsoft Corporation
Distribution:   Mariner
Url:            https://github.com/lunarmodules/lua-compat-5.3
# https://github.com/lunarmodules/lua-compat-5.3/archive/refs/tags/v%{version}.tar.gz
Source0:        %{name}-v%{version}.tar.gz
BuildArch:      noarch

%description
This is a small module that aims to make it easier to write code in a Lua-5.3-style that
is compatible with Lua 5.1, Lua 5.2, and Lua 5.3. This does not make Lua 5.2 (or even Lua
5.1) entirely compatible with Lua 5.3, but it brings the API closer to that of Lua 5.3.

%package    devel
Summary:    Header and development files for lua-compat53
Requires:   %{name} = %{version}-%{release}
%description    devel
It contains the libraries and header files.

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_prefix}/share/lua/5.1/compat53 %{buildroot}%{_prefix}/share/lua/5.2/compat53
cp -rv compat53/*.lua %{buildroot}%{_prefix}/share/lua/5.1/compat53/
ln -s ../../5.1/compat53/init.lua %{buildroot}%{_prefix}/share/lua/5.2/compat53/init.lua
ln -s ../../5.1/compat53/module.lua %{buildroot}%{_prefix}/share/lua/5.2/compat53/module.lua
mkdir -p %{buildroot}%{_prefix}/include/%{name}/c-api
cp -t %{buildroot}%{_prefix}/include/%{name}/c-api c-api/*

%check
rm -f debugsources.list debugfiles.list debuglinks.list

%files
%defattr(-, root, root)
%license LICENSE
%{_usr}/share/lua/5.1/compat53/*.lua
%{_usr}/share/lua/5.2/compat53/*.lua

%files devel
%{_includedir}/%{name}/c-api/*

%changelog
* Sat Jun 10 2023 Andy Voltz <anvoltz@microsoft.com> - 0.9
- Initial version
