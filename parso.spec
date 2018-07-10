#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : parso
Version  : 0.3.0
Release  : 19
URL      : http://pypi.debian.net/parso/parso-0.3.0.tar.gz
Source0  : http://pypi.debian.net/parso/parso-0.3.0.tar.gz
Summary  : A Python Parser
Group    : Development/Tools
License  : BSD-3-Clause MIT Python-2.0
Requires: parso-python3
Requires: parso-license
Requires: parso-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

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
Requires: parso-python3

%description python
python components for the parso package.


%package python3
Summary: python3 components for the parso package.
Group: Default
Requires: python3-core

%description python3
python3 components for the parso package.


%prep
%setup -q -n parso-0.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530400026
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/parso
cp LICENSE.txt %{buildroot}/usr/share/doc/parso/LICENSE.txt
cp test/normalizer_issue_files/LICENSE %{buildroot}/usr/share/doc/parso/test_normalizer_issue_files_LICENSE
cp docs/_themes/flask/LICENSE %{buildroot}/usr/share/doc/parso/docs__themes_flask_LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/parso/LICENSE.txt
/usr/share/doc/parso/docs__themes_flask_LICENSE
/usr/share/doc/parso/test_normalizer_issue_files_LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
