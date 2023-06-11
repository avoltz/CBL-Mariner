Summary:        hyperextensible Vim-based text editor
Name:           neovim
Version:        0.9.1
Release:        1%{?dist}
# zlib licenses comes from minizip/ source code
License:        Apache-2.0 and Vim
Vendor:         Microsoft Corporation
Distribution:   Mariner
Group:          Applications/Editors
URL:            https://neovim.io
#Source0:        https://github.com/%{name}/%{name}/archive/refs/tags/v%{version}.tar.gz
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gettext
#BuildRequires:  gperf
#BuildRequires:  less
#BuildRequires:  libacl
#BuildRequires:  libuv
#BuildRequires:  luajit
#BuildRequires:  lua
#BuildRequires:  msgpack
BuildRequires:  libacl-devel
BuildRequires:  libuv-devel
BuildRequires:  luajit-devel
BuildRequires:  lua-devel
BuildRequires:  msgpack-devel
#BuildRequires:  ninja-build
#BuildRequires:  nss_wrapper

%description
Neovim is a project that seeks to aggressively refactor Vim in order to:

- Simplify maintenance and encourage contributions
- Split the work between multiple developers
- Enable advanced UIs without modifications to the core
- Maximize extensibility

%prep
%setup -q -n neovim-stable

%build
make CMAKE_BUILD_TYPE=Release USE_BUNDLED=n

%install
%make_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README.md VERSION.txt


%changelog
* Sun Jun 11 2023 Andy Voltz <anvoltz@microsoft.com> 0.9.1
- Initial version
