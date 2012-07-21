# Created by pyp2rpm-0.4.2
%global pypi_name jsonschema

Name:           python-%{pypi_name}
Version:        0.2
Release:        2%{?dist}
Summary:        An implementation of JSON Schema validation for Python

License:        MIT
URL:            http://pypi.python.org/pypi/jsonschema/0.2
Source0:        http://pypi.python.org/packages/source/j/jsonschema/jsonschema-0.2.tar.gz
BuildArch:      noarch

BuildRequires:  python-devel


%description
jsonschema is JSON Schema validator currently based on
http://tools.ietf.org/html/draft-zyp-json-schema-03

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%{__python} setup.py build


%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}


%files
%doc README.rst COPYING
%{python_sitelib}/%{pypi_name}.*
%{python_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info


%changelog
* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 23 2012 Pádraig Brady <P@draigBrady.com> - 0.2-1
- Initial package.
