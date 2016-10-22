%{?scl:%scl_package nodejs-normalize-git-url}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-normalize-git-url

%global npm_name normalize-git-url
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-normalize-git-url
Version:	3.0.1
Release:	2%{?dist}
Summary:	Normalizes Git URLs. For npm, but you can use it too.
Url:		https://github.com/npm/normalize-git-url
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	ISC

BuildArch:	noarch
ExclusiveArch:	%{ix86} x86_64 %{arm} noarch

BuildRequires:	%{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:	%{?scl_prefix}npm(tap)
%endif

%description
Normalizes Git URLs. For npm, but you can use it too.

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json normalize-git-url.js \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
tap test/*.js
%endif

%files
%{nodejs_sitelib}/normalize-git-url

%doc README.md
%doc LICENSE

%changelog
* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.0.1-2
- Rebuilt for rhel6

* Mon Nov 30 2015 Tomas Hrcka <thrcka@redhat.com> - 3.0.1-1
- New upstream release

* Fri Nov 27 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.1-3
- Enable SCL macros

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 22 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.1-1
- Rebuilt with new release containing license text

* Wed May 13 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.0-1
- Initial build
