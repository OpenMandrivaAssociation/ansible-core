Summary:	SSH-based configuration management, deployment, and task execution system
Name:		ansible-core
Version:	2.18.5
Release:	1
License:	GPLv3
Group:		Development/Python
Url:		https://www.ansible.com/
Source0:	https://pypi.io/packages/source/a/%{name}/ansible_core-%{version}.tar.gz

BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
# tests
#BuildRequires:	python%{pyver}dist(botocore)
BuildRequires:	python%{pyver}dist(jinja2)
BuildRequires:	python%{pyver}dist(pyyaml)
BuildRequires:	python%{pyver}dist(cryptography)
#BuildRequires:	python%{pyver}dist(curses)
BuildRequires:	python%{pyver}dist(packaging)
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(pytz)
#BuildRequires:	python%{pyver}dist(resolvelib) < 0.9.0

Requires:	python%{pyver}dist(jinja2)
Requires:	python%{pyver}dist(pyyaml)
Requires:	python%{pyver}dist(cryptography)
Requires:	python%{pyver}dist(packaging)
#Requires:	python%{pyver}dist(resolvelib)

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
%{_bindir}/ansible
%{_bindir}/ansible-config
%{_bindir}/ansible-console
%{_bindir}/ansible-doc
%{_bindir}/ansible-galaxy
%{_bindir}/ansible-inventory
%{_bindir}/ansible-playbook
%{_bindir}/ansible-pull
%{_bindir}/ansible-test
%{_bindir}/ansible-vault
%config(noreplace) %{_sysconfdir}/ansible
%{py_sitedir}/ansible
%{py_sitedir}/ansible_test
%{py_sitedir}/ansible_core-%{version}*-info

#--------------------------------------------------------------------

%prep
%autosetup -p1 -n ansible_core-%{version}

%build
%py_build

%install
%py_install

mkdir -p %{buildroot}%{_sysconfdir}/ansible/
mkdir -p %{buildroot}/%{_mandir}/man1/
mkdir -p %{buildroot}/%{_datadir}/ansible

#mkdir -p $RPM_BUILD_ROOT/%{_mandir}/{man1,man3}/
#cp -va library/* $RPM_BUILD_ROOT/%{_datadir}/ansible/
#rm -f $RPM_BUILD_ROOT%{_datadir}/ansible/utilities/fireball $RPM_BUILD_ROOT%{_mandir}/man3/ansible.fireball*

#cp -pr docs/docsite/rst .

