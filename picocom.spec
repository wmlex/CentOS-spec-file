Name:           picocom
Version:        2.1
Release:        1%{?dist}
Summary:        Minimal serial communications program

Group:          Applications/Communications
License:        GPLv2+
URL:            https://github.com/npat-efault/picocom
Source0:	https://github.com/npat-efault/picocom/archive/%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
As its name suggests, picocom is a minimal dumb-terminal emulation program.
It is, in principle, very much like minicom, only it's "pico" instead of "mini"!
It was designed to serve as a simple, manual, modem configuration, testing, and
debugging tool. It has also served (quite well) as a low-tech serial communications
program to allow access to all types of devices that provide serial consoles.
It could also prove useful in many other similar tasks.
It is ideal for embedded systems since its memory footprint is minimal
(approximately 30K, when stripped). Apart from being a handy little tool, picocom's
source distribution includes a simple, easy to use, and thoroughly documented
terminal-management library, which could serve other projects as well. 

%prep
%setup -q

%build
make CC="%{__cc}" CFLAGS="$RPM_OPT_FLAGS" %{_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m 755 picocom $RPM_BUILD_ROOT%{_bindir}/
install -m 644 picocom.1 $RPM_BUILD_ROOT%{_mandir}/man1/

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc CONTRIBUTORS LICENSE.txt TODO README.md pcasc pcxm pcym pczm
%{_bindir}/picocom
%{_mandir}/man1/*

%changelog
* Wed Jan 27 2016 Aleksandr Chernyshev <wmlex@yandex.ru> - 2.1-1
- Initial RPM spec file.
