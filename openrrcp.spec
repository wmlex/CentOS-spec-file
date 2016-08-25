Name:           openrrcp
Version:        0.2.1
Release:        1%{?dist}
Summary:        Open-source cross-platform RRCP(Realtek Remote Configuration Protocol)-based tool.

Group:          Networking/Other
License:        GNU
URL:            http://sourceforge.net/projects/openrrcp
Source0:        http://ufpr.dl.sourceforge.net/project/openrrcp/openrrcp/0.2.1/%{name}-%{version}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#BuildRequires:
#Requires:

%description
Open-source cross-platform RRCP(Realtek Remote Configuration Protocol)-based tool, that is able to configure
and fetch status from L2 ethernet switches based on some Realtek's chips.
Linux, FreeBSD and RTL8316BP/RTL8324P/RTL8326/RTL8326S are support

%prep
%setup


%build
make %{?_smp_mflags} EXTRA_CFLAGS="$RPM_OPT_FLAGS"


%install
rm -rf %{buildroot}
make install -C src DESTDIR=%{buildroot}/usr

%files
%{_bindir}/*


%changelog
* Wed Oct 31 2012 Aleksandr Chernyshev <wmlex@yandex.ru> 0.2.1-1
- first build
