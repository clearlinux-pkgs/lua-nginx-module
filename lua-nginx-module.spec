#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : lua-nginx-module
Version  : 0.10.19
Release  : 6
URL      : https://github.com/openresty/lua-nginx-module/archive/v0.10.19/lua-nginx-module-0.10.19.tar.gz
Source0  : https://github.com/openresty/lua-nginx-module/archive/v0.10.19/lua-nginx-module-0.10.19.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: lua-nginx-module-lib = %{version}-%{release}
BuildRequires : buildreq-nginx
BuildRequires : openssl-dev
BuildRequires : pkgconfig(luajit)

%description
<!---
Don't edit this file manually! Instead you should generate it by using:
wiki2markdown.pl doc/HttpLuaModule.wiki
-->

%package lib
Summary: lib components for the lua-nginx-module package.
Group: Libraries

%description lib
lib components for the lua-nginx-module package.


%prep
%setup -q -n lua-nginx-module-0.10.19
cd %{_builddir}/lua-nginx-module-0.10.19

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


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/nginx-mainline/ngx_http_lua_module.so
