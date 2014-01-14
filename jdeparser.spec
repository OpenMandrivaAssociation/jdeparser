%{?_javapackages_macros:%_javapackages_macros}
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jdeparser
Version:          1.0.0
Release:          2.0%{?dist}
Summary:          Source generator library for Java

# See README.md
License:          (CDDL or GPLv2 with exceptions) and MIT
URL:              https://github.com/jdeparser/jdeparser

# git clone git://github.com/jdeparser/jdeparser.git
# cd jdeparser && git archive --format=tar --prefix=jdeparser-1.0.0.Final/ 1.0.0.Final | xz > jdeparser-1.0.0.Final.tar.xz
Source0:          jdeparser-%{namedversion}.tar.xz
BuildArch:        noarch

BuildRequires:    maven-local

%description
This project is a fork of Sun's (now Oracle's) com.sun.codemodel project. We
decided to fork the project because by all evidence, the upstream project is
dead and not actively accepting outside contribution. All JBoss projects are
urged to use this project instead for source code generation.

%package javadoc
Summary:        Javadocs for %{name}


%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jdeparser-%{namedversion}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE-original.html
%doc README.md

%files javadoc -f .mfiles-javadoc
%doc LICENSE-original.html

%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 29 2013 Marek Goldmann <mgoldman@redhat.com> - 1.0.0-1
- Initial packaging

