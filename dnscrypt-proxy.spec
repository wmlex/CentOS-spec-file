Name:           dnscrypt-proxy
Version:        1.6.0
Release:        1%{?dist}
Summary:        A tool for securing communications between a client and a DNS resolver.
License:        ISC
URL:            http://dnscrypt.org/
Source:         http://download.dnscrypt.org/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:  libsodium-devel

%description
A tool for securing communications between a client and a DNS resolver
The DNSCrypt protocol is very similar to DNSCurve, but focuses on
securing communications between a client and its first-level resolver.
While not providing end-to-end security, it protects the local network
(which is often the weakest link in the chain) against
man-in-the-middle attacks. It also provides some confidentiality to
DNS queries.

The DNSCrypt daemon acts as a DNS proxy between a regular client, like
a DNS cache or an operating system stub resolver, and a DNSCrypt-aware
resolver.

%package devel
Summary:        Development files for dnscrypt-proxy
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development and header files for dnscrypt-proxy

%prep
%setup -q -n %{name}-%{version}

%build
./configure \
--enable-plugins \
--enable-plugins-root \
--libdir=%{_libdir} \
--prefix=%{_prefix}

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

mkdir -p %{buildroot}/etc/sysconfig
cat > %{buildroot}/etc/sysconfig/dnscrypt-proxy <<HERE
DNSCRYPT_LOCALIP=127.0.0.1
DNSCRYPT_LOCALPORT=53
DNSCRYPT_USER=nobody
DNSCRYPT_PROVIDER_NAME=2.dnscrypt-cert.opendns.com
DNSCRYPT_PROVIDER_KEY=B735:1140:206F:225D:3E2B:D822:D7FD:691E:A1C3:3CC8:D666:8D0C:BE04:BFAB:CA43:FB79
DNSCRYPT_RESOLVERIP=208.67.220.220
DNSCRYPT_RESOLVERPORT=443
DNSCRYPT_LOG=/var/log/dnscrypt-proxy.log
HERE

mkdir -p %{buildroot}/usr/lib/systemd/system/
cat > %{buildroot}/usr/lib/systemd/system/dnscrypt-proxy.service <<HERE
[Unit]
Description=A tool for securing communications between a client and a DNS resolver.
After=network.target

[Service]
EnvironmentFile=/etc/sysconfig/dnscrypt-proxy
ExecStart=/usr/sbin/dnscrypt-proxy \\
    --local-address=\${DNSCRYPT_LOCALIP}:\${DNSCRYPT_LOCALPORT} \\
    --resolver-address=\${DNSCRYPT_RESOLVERIP}:\${DNSCRYPT_RESOLVERPORT} \\
    --provider-name=\${DNSCRYPT_PROVIDER_NAME} \\
    --provider-key=\${DNSCRYPT_PROVIDER_KEY} \\
    --user=\${DNSCRYPT_USER} \\
    --logfile=\${DNSCRYPT_LOG}
Restart=on-abort

[Install]
WantedBy=multi-user.target
HERE

%files
%{_bindir}/hostip
%{_sbindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man8/*
%config /etc/sysconfig/dnscrypt-proxy
%config /usr/lib/systemd/system/dnscrypt-proxy.service

%files devel
%{_prefix}/include/dnscrypt
%{_libdir}/%{name}

%changelog
* Wed Dec 16 2015 Aleksandr Chernyshev <wmlex@yandex.ru>
- Update to 1.6.0 
* Thu Dec 4 2014 Josh Chia <joshchia@gmail.com>
- Added systemd service
* Sat Jul 26 2014 Ricky Elrod <relrod@redhat.com> - 1.4.0-1
- Initial packaging.
