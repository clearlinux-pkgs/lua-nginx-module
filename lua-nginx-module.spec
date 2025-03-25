#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: nginx
# autospec version: v18
# autospec commit: f35655a
#
Name     : lua-nginx-module
Version  : 0.10.27
Release  : 82
URL      : https://github.com/openresty/lua-nginx-module/archive/v0.10.27/lua-nginx-module-0.10.27.tar.gz
Source0  : https://github.com/openresty/lua-nginx-module/archive/v0.10.27/lua-nginx-module-0.10.27.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: lua-nginx-module-lib = %{version}-%{release}
BuildRequires : buildreq-nginx
BuildRequires : openssl-dev
BuildRequires : pkgconfig(luajit)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Name
====
ngx_http_lua_module - Embed the power of Lua into Nginx HTTP Servers.
This module is a core component of [OpenResty](https://openresty.org). If you are using this module,
then you are essentially using OpenResty :)

%package lib
Summary: lib components for the lua-nginx-module package.
Group: Libraries

%description lib
lib components for the lua-nginx-module package.


%prep
%setup -q -n lua-nginx-module-0.10.27
cd %{_builddir}/lua-nginx-module-0.10.27
pushd ..
cp -a lua-nginx-module-0.10.27 buildavx2
popd

%build
## build_prepend content
export LUAJIT_LIB=`pkg-config --variable libdir luajit`
export LUAJIT_INC=`pkg-config --variable includedir luajit`
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
nginx-module configure
nginx-module build

%install
nginx-module install %{buildroot}

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/nginx-mainline/ngx_http_lua_module.so
