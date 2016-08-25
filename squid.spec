Name:     squid
Version:  3.5.8
Release:  1%{?dist}
Summary:  The Squid proxy caching server
Epoch:    7
# See CREDITS for breakdown of non GPLv2+ code
License:  GPLv2+ and (LGPLv2+ and MIT and BSD and Public Domain)
Group:    System Environment/Daemons
URL:      http://www.squid-cache.org
Source0:  http://www.squid-cache.org/Versions/v3/3.5/squid-%{version}.tar.xz
Source1:  http://www.squid-cache.org/Versions/v3/3.5/squid-%{version}.tar.xz.asc
Source2:  squid.init
Source3:  squid.logrotate
Source4:  squid.sysconfig
Source5:  squid.pam
Source6:  squid.nm
Patch0:   pinger_off.patch
Patch1:   bug-4330-put_cipher_by_char-t1.patch

Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: bash >= 2.0
Requires(pre): shadow-utils
Requires: libtool-ltdl
# squid_ldap_auth and other LDAP helpers require OpenLDAP
BuildRequires: openldap-devel
# squid_pam_auth requires PAM development libs
BuildRequires: pam-devel
# SSL support requires OpenSSL
BuildRequires: openssl-devel
# squid_kerb_aut requires Kerberos development libs
BuildRequires: krb5-devel
# squid_session_auth requires DB4
BuildRequires: db4-devel
# ESI support requires Expat & libxml2
BuildRequires: expat-devel libxml2-devel
# TPROXY requires libcap, and also increases security somewhat
BuildRequires: libcap-devel
# eCAP and some other need libltdl
BuildRequires: libtool libtool-ltdl-devel
# Required to allow debug package auto creation
BuildRequires: redhat-rpm-config

# Required to validate auto requires AutoReqProv: no
## aaaAutoReqProv: no

%description
Squid is a high-performance proxy caching server for Web clients,
supporting FTP, gopher, and HTTP data objects. Unlike traditional
caching software, Squid handles all requests in a single,
non-blocking, I/O-driven process. Squid keeps meta data and especially
hot objects cached in RAM, caches DNS lookups, supports non-blocking
DNS lookups, and implements negative caching of failed requests.

Squid consists of a main server program squid, a Domain Name System
lookup program (dnsserver), a program for retrieving FTP data
(ftpget), and some management and client tools.

%prep
%setup -q
%patch0
%patch1

%package helpers
Group: System Environment/Daemons
Summary: SysV initscript for squid caching proxy
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires(preun): /sbin/service
Requires(postun): /sbin/service
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/service /sbin/chkconfig
Requires(postun): /sbin/service

%description helpers
The squid-helpers contains the external helpers.

%build
#was added due to new squid features that will be added soon
export CXXFLAGS="$RPM_OPT_FLAGS -fPIC"

%configure \
   --exec_prefix=/usr \
   --libexecdir=%{_libdir}/squid \
   --localstatedir=/var \
   --datadir=%{_datadir}/squid \
   --sysconfdir=%{_sysconfdir}/squid \
   --with-logdir='$(localstatedir)/log/squid' \
   --with-pidfile='$(localstatedir)/run/squid.pid' \
   --disable-dependency-tracking \
   --enable-follow-x-forwarded-for \
   --enable-auth \
   --enable-auth-basic="DB,LDAP,NCSA,NIS,PAM,POP3,RADIUS,SASL,SMB,getpwnam" \
   --enable-auth-ntlm="smb_lm,fake" \
   --enable-auth-digest="file,LDAP" \
   --enable-auth-negotiate="kerberos,wrapper" \
   --enable-external-acl-helpers="wbinfo_group,kerberos_ldap_group" \
   --enable-cache-digests \
   --enable-cachemgr-hostname=localhost \
   --enable-delay-pools \
   --enable-epoll \
   --enable-icap-client \
   --enable-ident-lookups \
   %ifnarch ppc64 ia64 x86_64 s390x
   --with-large-files \
   %endif
   --enable-linux-netfilter \
   --enable-removal-policies="heap,lru" \
   --enable-snmp \
   --enable-storeio="aufs,diskd,ufs,rock" \
   --enable-wccpv2 \
   --enable-esi \
   --enable-ssl-crtd  \
   --enable-icmp \
   --with-aio \
   --with-default-user="squid" \
   --with-filedescriptors=16384 \
   --with-dl \
   --with-openssl \
   --with-pthreads \
   --with-included-ltdl \
   --disable-arch-native \
   --without-nettle

make \
	DEFAULT_SWAP_DIR='$(localstatedir)/spool/squid' \
	%{?_smp_mflags}

#%install
%if %{?fedora}00%{?rhel} < 6
sed -i 's|password-auth|system-auth|' %{SOURCE5}
%endif
rm -rf $RPM_BUILD_ROOT
make \
	DESTDIR=$RPM_BUILD_ROOT \
	install

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pam.d
mkdir -p $RPM_BUILD_ROOT/usr/libexec/squid
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/NetworkManager/dispatcher.d
install -m 755 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/squid
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/squid
install -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/squid
install -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/squid

install -m 644 %{SOURCE6} $RPM_BUILD_ROOT%{_sysconfdir}/NetworkManager/dispatcher.d/20-squid
mkdir -p $RPM_BUILD_ROOT/var/log/squid
mkdir -p $RPM_BUILD_ROOT/var/spool/squid
chmod 644 contrib/url-normalizer.pl contrib/rredir.* contrib/user-agents.pl
iconv -f ISO88591 -t UTF8 ChangeLog -o ChangeLog.tmp
mv -f ChangeLog.tmp ChangeLog

# Move the MIB definition to the proper place (and name)
mkdir -p $RPM_BUILD_ROOT/usr/share/snmp/mibs
mv $RPM_BUILD_ROOT/usr/share/squid/mib.txt $RPM_BUILD_ROOT/usr/share/snmp/mibs/SQUID-MIB.txt

# squid.conf.documented is documentation. We ship that in doc/
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/squid/squid.conf.documented

# remove unpackaged files from the buildroot
rm -f $RPM_BUILD_ROOT%{_bindir}/{RunAccel,RunCache}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING README CREDITS ChangeLog QUICKSTART src/squid.conf.documented
%doc contrib/url-normalizer.pl contrib/rredir.* contrib/user-agents.pl

%attr(755,root,root) %dir %{_sysconfdir}/squid
%attr(755,root,root) %dir %{_libdir}/squid
%attr(750,squid,squid) %dir /var/log/squid
%attr(750,squid,squid) %dir /var/spool/squid

%config(noreplace) %attr(640,root,squid) %{_sysconfdir}/squid/squid.conf
%config(noreplace) %attr(644,root,squid) %{_sysconfdir}/squid/cachemgr.conf
%config(noreplace) %{_sysconfdir}/squid/mime.conf
%config(noreplace) %{_sysconfdir}/squid/errorpage.css
%config(noreplace) %{_sysconfdir}/sysconfig/squid
# These are not noreplace because they are just sample config files
%config %{_sysconfdir}/squid/squid.conf.default
%config %{_sysconfdir}/squid/mime.conf.default
%config %{_sysconfdir}/squid/errorpage.css.default
%config %{_sysconfdir}/squid/cachemgr.conf.default
%config(noreplace) %{_sysconfdir}/pam.d/squid
%config(noreplace) %{_sysconfdir}/logrotate.d/squid

%dir %{_datadir}/squid
%attr(-,root,root) %{_datadir}/squid/errors
%attr(755,root,root) %{_sysconfdir}/NetworkManager/dispatcher.d/20-squid
%{_datadir}/squid/icons
%{_sbindir}/squid
%{_bindir}/squidclient
%{_bindir}/purge
%{_mandir}/man8/*
%{_mandir}/man1/*
%{_libdir}/squid/diskd
%{_libdir}/squid/log_file_daemon
%{_libdir}/squid/unlinkd
%attr(4755,root,root) %{_libdir}/squid/pinger

%{_datadir}/snmp/mibs/SQUID-MIB.txt
%attr(755,root,root) %{_sysconfdir}/rc.d/init.d/squid

%files helpers
%{_libdir}/squid/basic_db_auth
%{_libdir}/squid/basic_getpwnam_auth
%{_libdir}/squid/basic_ldap_auth
%{_libdir}/squid/basic_ncsa_auth
%{_libdir}/squid/basic_nis_auth
%{_libdir}/squid/basic_pam_auth
%{_libdir}/squid/basic_pop3_auth
%{_libdir}/squid/basic_radius_auth
%{_libdir}/squid/basic_sasl_auth
%{_libdir}/squid/basic_smb_auth
%{_libdir}/squid/basic_smb_auth.sh
%{_libdir}/squid/cachemgr.cgi
%{_libdir}/squid/cert_tool
%{_libdir}/squid/cert_valid.pl
%{_libdir}/squid/digest_file_auth
%{_libdir}/squid/digest_ldap_auth
%{_libdir}/squid/ext_kerberos_ldap_group_acl
%{_libdir}/squid/ext_wbinfo_group_acl
%{_libdir}/squid/helper-mux.pl
%{_libdir}/squid/log_db_daemon
%{_libdir}/squid/negotiate_kerberos_auth
%{_libdir}/squid/negotiate_kerberos_auth_test
%{_libdir}/squid/negotiate_wrapper_auth
%{_libdir}/squid/ntlm_fake_auth
%{_libdir}/squid/ntlm_smb_lm_auth
%{_libdir}/squid/ssl_crtd
%{_libdir}/squid/storeid_file_rewrite
%{_libdir}/squid/url_fake_rewrite
%{_libdir}/squid/url_fake_rewrite.sh

%pre
if ! getent group squid >/dev/null 2>&1; then
  /usr/sbin/groupadd -g 23 squid
fi

if ! getent passwd squid >/dev/null 2>&1 ; then
  /usr/sbin/useradd -g 23 -u 23 -d /var/spool/squid -r -s /sbin/nologin squid >/dev/null 2>&1 || exit 1 
fi

for i in /var/log/squid /var/spool/squid ; do
        if [ -d $i ] ; then
                for adir in `find $i -maxdepth 0 \! -user squid`; do
                        chown -R squid:squid $adir
                done
        fi
done

exit 0

%post
echo "squid.conf.documented is at /usr/share/squid-%{version}/squid.conf.documented"
/sbin/chkconfig --add squid

%preun
if [ $1 = 0 ] ; then
        service squid stop >/dev/null 2>&1
        rm -f /var/log/squid/*
        /sbin/chkconfig --del squid
fi

%postun
if [ "$1" -ge "1" ] ; then
        service squid condrestart >/dev/null 2>&1
fi

%postun helpers
%triggerin -- samba-common
if ! getent group wbpriv >/dev/null 2>&1 ; then
  /usr/sbin/groupadd -g 88 wbpriv >/dev/null 2>&1 || :
fi
/usr/sbin/usermod -a -G wbpriv squid >/dev/null 2>&1 || \
    chgrp squid /var/lib/samba/winbindd_privileged >/dev/null 2>&1 || :
    chmod 750 /var/lib/samba/winbindd_privileged  >/dev/null 2>&1 || :

%changelog
* Thu Jan 14 2016 Aleksandr Chernyshev <wmlex@yandex.ru>
- enable bug-4330-put_cipher_by_char-t1.patch.

* Wed Sep 02 2015 Eliezer Croitoru <eliezer@ngtech.co.il>
- Releasee 3.5.8 Stable.
- Couple major bug fixes.
- A Split between Sources of the packages of CentOS 6 and 7

* Mon Aug 17 2015 Eliezer Croitoru <eliezer@ngtech.co.il>
- Release 3.5.7 Stable.
- Default disabling pinger due to selinux issues.

* Tue Jul 07 2015 Eliezer Croitoru <eliezer@ngtech.co.il>
- Release 3.5.6 Stable.
- Adding edirectory digest helper back.

* Thu May 28 2015 Eliezer Croitoru <eliezer@ngtech.co.il>
- Release 3.5.4 Stable.

* Fri May 22 2015 Eliezer Croitoru <eliezer@ngtech.co.il>
- Release 3.5.4 Stable.

* Fri Apr 24 2015 Eliezer Croitoru <eliezer@ngtech.co.il>
- Release 3.5.3 Stable.
- Removed eDirectory helper.
- Removed AD_Group helper.

* Wed Mar 04 2015 Eliezer Croitoru <eliezer@ngtech.co.il>
- Release 3.5.2 Stable.

* Mon Jan 12 2015 Eliezer Croitoru <eliezer@ngtech.co.il>
- Release 3.5.0.4 Beta.
- COPYRIGHT content was moved into README.
