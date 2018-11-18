#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x579C160D4C9E23E8 (jelmer@fsfe.org)
#
Name     : fastimport
Version  : 0.9.8
Release  : 1
URL      : https://files.pythonhosted.org/packages/aa/65/47a579aae80fbd8b89cfbdffcde8dff68d57e3148b99da6a326673021455/fastimport-0.9.8.tar.gz
Source0  : https://files.pythonhosted.org/packages/aa/65/47a579aae80fbd8b89cfbdffcde8dff68d57e3148b99da6a326673021455/fastimport-0.9.8.tar.gz
Source99 : https://files.pythonhosted.org/packages/aa/65/47a579aae80fbd8b89cfbdffcde8dff68d57e3148b99da6a326673021455/fastimport-0.9.8.tar.gz.asc
Summary  : VCS fastimport/fastexport parser
Group    : Development/Tools
License  : GPL-2.0
Requires: fastimport-bin = %{version}-%{release}
Requires: fastimport-license = %{version}-%{release}
Requires: fastimport-python = %{version}-%{release}
Requires: fastimport-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
[![Build Status](https://travis-ci.org/jelmer/python-fastimport.png?branch=master)](https://travis-ci.org/jelmer/python-fastimport)

%package bin
Summary: bin components for the fastimport package.
Group: Binaries
Requires: fastimport-license = %{version}-%{release}

%description bin
bin components for the fastimport package.


%package license
Summary: license components for the fastimport package.
Group: Default

%description license
license components for the fastimport package.


%package python
Summary: python components for the fastimport package.
Group: Default
Requires: fastimport-python3 = %{version}-%{release}

%description python
python components for the fastimport package.


%package python3
Summary: python3 components for the fastimport package.
Group: Default
Requires: python3-core

%description python3
python3 components for the fastimport package.


%prep
%setup -q -n fastimport-0.9.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542512216
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/fastimport
cp COPYING %{buildroot}/usr/share/package-licenses/fastimport/COPYING
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/fast-import-filter
/usr/bin/fast-import-info
/usr/bin/fast-import-query

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/fastimport/COPYING

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
