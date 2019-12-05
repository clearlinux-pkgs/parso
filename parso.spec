#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : parso
Version  : 0.5.1
Release  : 32
URL      : https://files.pythonhosted.org/packages/21/40/615957db4d178b7504c87b1a5b85fa5945b0b4fa5f5a845e31fc7aad6018/parso-0.5.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/21/40/615957db4d178b7504c87b1a5b85fa5945b0b4fa5f5a845e31fc7aad6018/parso-0.5.1.tar.gz
Summary  : A Python Parser
Group    : Development/Tools
License  : BSD-3-Clause MIT Python-2.0
Requires: parso-license = %{version}-%{release}
Requires: parso-python = %{version}-%{release}
Requires: parso-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
###################################################################
parso - A Python Parser
###################################################################

%package license
Summary: license components for the parso package.
Group: Default

%description license
license components for the parso package.


%package python
Summary: python components for the parso package.
Group: Default
Requires: parso-python3 = %{version}-%{release}

%description python
python components for the parso package.


%package python3
Summary: python3 components for the parso package.
Group: Default
Requires: python3-core

%description python3
python3 components for the parso package.


%prep
%setup -q -n parso-0.5.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1563049174
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/parso
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/parso/LICENSE.txt
cp docs/_themes/flask/LICENSE %{buildroot}/usr/share/package-licenses/parso/docs__themes_flask_LICENSE
cp test/normalizer_issue_files/LICENSE %{buildroot}/usr/share/package-licenses/parso/test_normalizer_issue_files_LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/parso/LICENSE.txt
/usr/share/package-licenses/parso/docs__themes_flask_LICENSE
/usr/share/package-licenses/parso/test_normalizer_issue_files_LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
