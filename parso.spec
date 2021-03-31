#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : parso
Version  : 0.8.2
Release  : 49
URL      : https://files.pythonhosted.org/packages/5e/61/d119e2683138a934550e47fc8ec023eb7f11b194883e9085dca3af5d4951/parso-0.8.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/5e/61/d119e2683138a934550e47fc8ec023eb7f11b194883e9085dca3af5d4951/parso-0.8.2.tar.gz
Summary  : A Python Parser
Group    : Development/Tools
License  : BSD-3-Clause MIT Python-2.0
Requires: parso-license = %{version}-%{release}
Requires: parso-python = %{version}-%{release}
Requires: parso-python3 = %{version}-%{release}
Requires: flake8
Requires: mypy
BuildRequires : buildreq-distutils3
BuildRequires : flake8
BuildRequires : mypy

%description
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
Provides: pypi(parso)

%description python3
python3 components for the parso package.


%prep
%setup -q -n parso-0.8.2
cd %{_builddir}/parso-0.8.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1617214616
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/parso
cp %{_builddir}/parso-0.8.2/LICENSE.txt %{buildroot}/usr/share/package-licenses/parso/b1a7c6c0bf49fd5b62cca57a802166f291273c9a
cp %{_builddir}/parso-0.8.2/docs/_themes/flask/LICENSE %{buildroot}/usr/share/package-licenses/parso/d0eff60551064b040266867c393e035d747b0ae5
cp %{_builddir}/parso-0.8.2/test/normalizer_issue_files/LICENSE %{buildroot}/usr/share/package-licenses/parso/f71a77bff7a0853ddf32ea962ef8582fe808d9f6
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/parso/b1a7c6c0bf49fd5b62cca57a802166f291273c9a
/usr/share/package-licenses/parso/d0eff60551064b040266867c393e035d747b0ae5
/usr/share/package-licenses/parso/f71a77bff7a0853ddf32ea962ef8582fe808d9f6

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
