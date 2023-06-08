Summary:        Tree-sitter is a parser generator tool and incremental parsing library
Name:           tree-sitter
Version:        0.20.8
Release:        1%{?dist}
License:        MIT
Group:          Development/Tools
Vendor:         Microsoft Corporation
Distribution:   Mariner
Url:            https://tree-sitter.github.io
#Source0:        https://github.com/%{name}/%{name}/archive/refs/tags/v%{version}.tar.gz
Source0:        %{name}-v%{version}.tar.gz
BuildRequires:  make
BuildRequires:  gcc

%description
Tree-sitter is a parser generator tool and an incremental parsing library.
It can build a concrete syntax tree for a source file and efficiently update the syntax tree as the source file is edited.
Tree-sitter aims to be:

- **General** enough to parse any programming language
- **Fast** enough to parse on every keystroke in a text editor
- **Robust** enough to provide useful results even in the presence of syntax errors
- **Dependency-free** so that the runtime library (which is written in pure C) can be embedded in any application

%package    devel
Summary:    Header and development files for tree-sitter
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

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%license LICENSE
%{_libdir}/libtree-sitter.so.0*

%files devel
%dir %{_includedir}/tree_sitter
%{_includedir}/tree_sitter/*.h
%{_libdir}/libtree-sitter.a
%{_libdir}/libtree-sitter.so
%{_libdir}/pkgconfig/tree-sitter.pc

%changelog
* Wed Jun 07 2023 Andy Voltz <anvoltz@microsoft.com> - 0.20.8
- Initial version
