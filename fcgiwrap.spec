%global commit 99c942c90063c73734e56bacaa65f947772d9186
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20150530

Name:           fcgiwrap
Version:        1.1.0
Release:        2.%{date}git%{shortcommit}%{?dist}
Summary:        Simple FastCGI wrapper for CGI scripts
License:        MIT
URL:            https://nginx.localdomain.pl/wiki/FcgiWrap
Source0:        https://github.com/gnosek/fcgiwrap/archive/%{commit}/%{name}-%{commit}.tar.gz

Patch0:		run_user.patch

BuildRequires:    autoconf
BuildRequires:    automake
BuildRequires:    fcgi-devel
BuildRequires:    systemd
BuildRequires:    systemd-devel

Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

%description
fcgiwrap is a simple server for running CGI applications over FastCGI.
It hopes to provide clean CGI support to Nginx (and other web servers
that may need it).


%prep
%setup -q -n %{name}-%{commit}
%patch0 -p1

%build
autoreconf -i
%configure --prefix="" --with-systemd
make %{?_smp_mflags}


%install
%make_install

%post
%systemd_post fcgiwrap.service
%systemd_post fcgiwrap.socket

%preun
%systemd_preun fcgiwrap.service
%systemd_preun fcgiwrap.socket

%postun
%systemd_postun_with_restart fcgiwrap.service
%systemd_postun_with_restart fcgiwrap.socket

%files
%doc README.rst
%{_sbindir}/fcgiwrap
%{_mandir}/man8/fcgiwrap.8*
%{_unitdir}/fcgiwrap.service
%{_unitdir}/fcgiwrap.socket

%changelog
* Wed Sep 28 2016 Aleksandr Chernyshev <wmlex@yandex.ru> - 1.1.0-2.20150530git99c942c
- Add run_user.patch

* Sat May 30 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.1.0-2.20150530git99c942c
- Update to commit 99c942c

* Fri Feb 08 2013 Hiroaki Nakamura <hnakamur@gmail.com> - 1.1.0-1
- new upstream release.

* Fri Jan 11 2013 Hiroaki Nakamura <hnakamur@gmail.com> - 1.0.3.20120908-1
- Change version to increase monotonously.

* Wed Jan  9 2013 Hiroaki Nakamura <hnakamur@gmail.com> - 1.0.3-3.gitb9f03e6377
- Make the rpm relocatable.

* Tue Dec 25 2012 Hiroaki Nakamura <hnakamur@gmail.com> - 1.0.3-2.gitb9f03e6377

* Tue Jan 31 2012 Craig Barnes <cr@igbarn.es> - 1.0.3-1.git1328862
- Initial package
