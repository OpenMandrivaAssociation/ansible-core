Summary:	SSH-based configuration management, deployment, and task execution system
Name:		ansible-core
Version:	2.14.0
Release:	1
License:	GPLv3
Group:		Development/Python
Url:		https://www.ansible.com/
Source0:	https://pypi.io/packages/source/a/%{name}/%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(pip)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(wheel)
# tests
#BuildRequires:	python3dist(botocore)
BuildRequires:	python3dist(jinja2)
BuildRequires:	python3dist(pyyaml)
BuildRequires:	python3dist(cryptography)
#BuildRequires:	python3dist(curses)
BuildRequires:	python3dist(packaging)
BuildRequires:	python3dist(pytest)
BuildRequires:	python3dist(pytz)
#BuildRequires:	python3dist(resolvelib) < 0.9.0

Requires:	python3dist(jinja2)
Requires:	python3dist(pyyaml)
Requires:	python3dist(cryptography)
Requires:	python3dist(packaging)
#Requires:	python3dist(resolvelib)

BuildArch:	noarch

%description
Ansible is a radically simple IT automation system. It handles
configuration management, application deployment, cloud provisioning,
ad-hoc task execution, network automation, and multi-node orchestration
Ansible makes complex changes like zero-downtime rolling updates with
load balancers easy.

Design Principles:
  *  Have an extremely simple setup process with a minimal learning curve.
  *  Manage machines quickly and in parallel.
  *  Avoid custom-agents and additional open ports, be agentless by leveraging the existing SSH daemon.
  *  Describe infrastructure in a language that is both machine and human friendly.
  *  Focus on security and easy auditability/review/rewriting of content.
  *  Manage new remote machines instantly, without bootstrapping any software.
  *  Allow module development in any dynamic language, not just Python.
  *  Be usable as non-root.
  *  Be the easiest IT automation system to use, ever.

%files
%license COPYING
%doc README.rst PKG-INFO porting_guide_?.rst CHANGELOG-v?.rst
%{_bindir}/ansible-community
%config(noreplace) %{_sysconfdir}/ansible
%{py_sitedir}/ansible_collections
%{py_sitedir}/ansible-%{uversion}-py%{python3_version}.egg-info
%doc %{_mandir}/man1/ansible*
%doc examples/playbooks

#--------------------------------------------------------------------

%prep
%autosetup -p1

%build
%py_build

%install
%py_install

mkdir -p %{buildroot}%{_sysconfdir}/ansible/
cp examples/hosts %{buildroot}%{_sysconfdir}/ansible/
cp examples/ansible.cfg %{buildroot}%{_sysconfdir}/ansible/
mkdir -p %{buildroot}/%{_mandir}/man1/
cp -v docs/man/man1/*.1 %{buildroot}/%{_mandir}/man1/
mkdir -p %{buildroot}/%{_datadir}/ansible
cp -va library/* %{buildroot}/%{_datadir}/ansible/

#mkdir -p $RPM_BUILD_ROOT/%{_mandir}/{man1,man3}/
#cp -va library/* $RPM_BUILD_ROOT/%{_datadir}/ansible/
#rm -f $RPM_BUILD_ROOT%{_datadir}/ansible/utilities/fireball $RPM_BUILD_ROOT%{_mandir}/man3/ansible.fireball*

#cp -pr docs/docsite/rst .

