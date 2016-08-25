Name		: zabbix
Version		: 2.4.7
Release		: 2%{?dist}
Summary		: Enterprise-class open source distributed monitoring solution.

Group		: Applications/Internet
License		: GPLv2+
URL		: http://www.zabbix.com/
Source0		: zabbix-%{version}.tar.gz
%if 0%{?rhel} >= 7
Source3		: zabbix-logrotate38.in
%else
Source3		: zabbix-logrotate.in
%endif
Source4		: zabbix-java-gateway.init
Source5		: zabbix-agent.init
Source6		: zabbix-server.init
Source7		: zabbix-proxy.init
Source10	: zabbix-agent.service
Source11	: zabbix-server.service
Source12	: zabbix-proxy.service
Source13	: zabbix-java-gateway.service
Source14	: zabbix_java_gateway-sysd
Source15	: zabbix-tmpfiles.conf
Source16        : zabbix-nginx.conf
Patch0		: config.patch
Patch1		: fonts-config.patch
Patch2		: fping3-sourceip-option.patch

Buildroot	: %{_tmppath}/zabbix-%{version}-%{release}-root-%(%{__id_u} -n)

%define build_server 0%{!?_only_agent:1}
%if 0%{?_only_agent:1}
%define _unpackaged_files_terminate_build 0
%define _missing_doc_files_terminate_build 0
%endif

%if %{build_server}
BuildRequires	: mysql-devel
BuildRequires	: postgresql-devel
BuildRequires	: net-snmp-devel
BuildRequires	: openldap-devel
BuildRequires	: gnutls-devel
BuildRequires	: iksemel-devel
BuildRequires	: sqlite-devel
BuildRequires	: unixODBC-devel
BuildRequires	: curl-devel >= 7.13.1
BuildRequires	: OpenIPMI-devel >= 2
BuildRequires	: libssh2-devel >= 1
BuildRequires   : java-devel >= 1.6.0
BuildRequires   : libxml2-devel
%if 0%{?rhel} >= 7
BuildRequires   : systemd
%endif
%endif

Requires	: logrotate
Requires(pre)	: /usr/sbin/useradd

%description
Zabbix is software that monitors numerous parameters of a network and
the health and integrity of servers. Zabbix uses a flexible
notification mechanism that allows users to configure e-mail based
alerts for virtually any event.  This allows a fast reaction to server
problems. Zabbix offers excellent reporting and data visualisation
features based on the stored data. This makes Zabbix ideal for
capacity planning.

Zabbix supports both polling and trapping. All Zabbix reports and
statistics, as well as configuration parameters are accessed through a
web-based front end. A web-based front end ensures that the status of
your network and the health of your servers can be assessed from any
location. Properly configured, Zabbix can play an important role in
monitoring IT infrastructure. This is equally true for small
organisations with a few servers and for large companies with a
multitude of servers.

%package agent
Summary		: Zabbix Agent
Group		: Applications/Internet
Requires	: %{name}
%if 0%{?rhel} >= 7
Requires(post)  : systemd
Requires(preun) : systemd
Requires(preun) : systemd
%else
Requires(post)  : /sbin/chkconfig
Requires(preun) : /sbin/chkconfig
Requires(preun) : /sbin/service
%endif


%description agent
The Zabbix client agent, to be installed on monitored systems.

%package get
Summary		: Zabbix Get
Group		: Applications/Internet

%description get
Zabbix get command line utility

%package sender
Summary		: Zabbix Sender
Group		: Applications/Internet

%description sender
Zabbix sender command line utility

%if %{build_server}
%package server
Summary		: Zabbix server common files
Group		: Applications/Internet
Requires	: %{name}
Requires	: %{name}-server-implementation = %{version}-%{release}
%if 0%{?rhel} >= 7
Requires	: fping >= 3
%else
Requires	: fping
%endif
Requires	: net-snmp
Requires	: iksemel
Requires	: unixODBC
Requires	: libssh2 >= 1.0.0
Requires	: curl >= 7.13.1
Requires	: OpenIPMI-libs >= 2.0.14
%if 0%{?rhel} >= 7
Requires(post)  : systemd
Requires(preun) : systemd
Requires(preun) : systemd
%else
Requires(post)  : /sbin/chkconfig
Requires(preun) : /sbin/chkconfig
Requires(preun) : /sbin/service
%endif

%description server
Zabbix server common files.

%package server-mysql
Summary		: Zabbix server compiled to use MySQL database
Group		: Applications/Internet
Requires	: %{name}-server = %{version}-%{release}
Provides	: %{name}-server-implementation = %{version}-%{release}
Conflicts	: %{name}-server-pgsql

%description server-mysql
Zabbix server compiled with MySQL database support.

%package server-pgsql
Summary		: Zabbix server compiled to use PostgresSQL database
Group		: Applications/Internet
Requires	: %{name}-server = %{version}-%{release}
Provides	: %{name}-server-implementation = %{version}-%{release}
Conflicts	: %{name}-server-mysql

%description server-pgsql
Zabbix server compiled with PostgresSQL database support.

%package proxy
Summary		: Zabbix Proxy common files
Group		: Applications/Internet
Requires	: %{name}
Requires	: %{name}-proxy-implementation = %{version}-%{release}
%if 0%{?rhel} >= 7
Requires        : fping >= 3
%else
Requires        : fping
%endif
Requires	: net-snmp
Requires	: unixODBC
Requires	: libssh2 >= 1.0.0
Requires	: curl >= 7.13.1
Requires	: OpenIPMI-libs >= 2.0.14
%if 0%{?rhel} >= 7
Requires(post)  : systemd
Requires(preun) : systemd
Requires(preun) : systemd
%else
Requires(post)  : /sbin/chkconfig
Requires(preun) : /sbin/chkconfig
Requires(preun) : /sbin/service
%endif

%description proxy
The Zabbix proxy common files

%package proxy-mysql
Summary		: Zabbix proxy compiled to use MySQL
Group		: Applications/Internet
Requires	: %{name}-proxy = %{version}-%{release}
Requires	: mysql
Provides	: %{name}-proxy-implementation = %{version}-%{release}
Conflicts	: %{name}-proxy-pgsql
Conflicts	: %{name}-proxy-sqlite3

%description proxy-mysql
The Zabbix proxy compiled to use MySQL

%package proxy-pgsql
Summary		: Zabbix proxy compiled to use PostgreSQL
Group		: Applications/Internet
Requires	: %{name}-proxy = %{version}-%{release}
Requires	: postgresql
Provides	: %{name}-proxy-implementation = %{version}-%{release}
Conflicts	: %{name}-proxy-mysql
Conflicts	: %{name}-proxy-sqlite3

%description proxy-pgsql
The Zabbix proxy compiled to use PostgreSQL

%package proxy-sqlite3
Summary		: Zabbix proxy compiled to use SQLite3
Group		: Applications/Internet
Requires	: %{name}-proxy = %{version}-%{release}
Requires	: sqlite
Provides	: %{name}-proxy-implementation = %{version}-%{release}
Conflicts	: %{name}-proxy-mysql
Conflicts	: %{name}-proxy-pgsql

%description proxy-sqlite3
The Zabbix proxy compiled to use SQLite3

%package java-gateway
Summary		: Zabbix java gateway
Group		: Applications/Internet
Requires	: %{name}
%if 0%{?rhel} >= 7
Requires	: java-headless >= 1.6.0
%else
Requires	: java >= 1.6.0
%endif
%if 0%{?rhel} >= 7
Requires(post)  : systemd
Requires(preun) : systemd
Requires(preun) : systemd
%else
Requires(post)  : /sbin/chkconfig
Requires(preun) : /sbin/chkconfig
Requires(preun) : /sbin/service
%endif

%description java-gateway
The Zabbix java gateway

%package web
Summary		: Zabbix Web Frontend
Group		: Applications/Internet
%if 0%{?fedora} > 9 || 0%{?rhel} >= 6
BuildArch	: noarch
%endif
Requires	: nginx
%if 0%{?rhel} == 5
Requires	: php53-fpm
Requires	: php53-gd
Requires	: php53-bcmath
Requires	: php53-mbstring
Requires	: php53-xml
%else
Requires	: php-fpm >= 5.3
Requires	: php-gd
Requires	: php-bcmath
Requires	: php-mbstring
Requires	: php-xml
%endif
# DejaVu fonts doesn't exist on EL <= 5
%if 0%{?fedora} || 0%{?rhel} >= 6
Requires	: dejavu-sans-fonts
%endif
Requires	: zabbix-web-database = %{version}-%{release}
Requires(post)	: %{_sbindir}/update-alternatives
Requires(preun)	: %{_sbindir}/update-alternatives

%description web
The php frontend to display the zabbix web interface.

%package web-mysql
Summary		: Zabbix web frontend for MySQL
Group		: Applications/Internet
%if 0%{?fedora} > 9 || 0%{?rhel} >= 6
BuildArch	: noarch
%endif
Requires	: %{name}-web = %{version}-%{release}
Requires	: php-mysql
Provides	: %{name}-web-database = %{version}-%{release}
Conflicts	: %{name}-web-pgsql
Conflicts	: %{name}-web-sqlite3

%description web-mysql
Zabbix web frontend for MySQL

%package web-pgsql
Summary		: Zabbix web frontend for PostgreSQL
Group		: Applications/Internet
%if 0%{?fedora} > 9 || 0%{?rhel} >= 6
BuildArch	: noarch
%endif
Requires	: %{name}-web = %{version}-%{release}
Requires	: php-pgsql
Provides	: %{name}-web-database = %{version}-%{release}
Conflicts	: %{name}-web-mysql
Conflicts	: %{name}-web-sqlite3

%description web-pgsql
Zabbix web frontend for PostgreSQL

%package web-japanese
Summary		: Japanese font for Zabbix web frontend
Group		: Applications/Internet
%if 0%{?fedora} > 9 || 0%{?rhel} >= 6
BuildArch	: noarch
Requires	: vlgothic-p-fonts
%else
Requires	: ipa-pgothic-fonts
%endif
Requires	: %{name}-web = %{version}-%{release}
Requires(post)	: %{_sbindir}/update-alternatives
Requires(preun)	: %{_sbindir}/update-alternatives

%description web-japanese
Japanese font for Zabbix web frontend
%endif

%prep
%setup0 -q -n zabbix-%{version}
%patch0 -p1
%patch1 -p1
%if 0%{?rhel} >= 7
%patch2 -p1
%endif

# DejaVu fonts doesn't exist on EL <= 5
%if 0%{?fedora} || 0%{?rhel} >= 6
# remove included fonts
rm -rf frontends/php/fonts/DejaVuSans.ttf
%endif

# remove executable permissions
chmod a-x upgrades/dbpatches/1.8/mysql/upgrade

# fix up some lib64 issues
sed -i.orig -e 's|_LIBDIR=/usr/lib|_LIBDIR=%{_libdir}|g' \
    configure

# kill off .htaccess files, options set in SOURCE16
rm -f frontends/php/include/.htaccess
rm -f frontends/php/conf/.htaccess

# remove .po and related files
find frontend/php/locale -name '*.po' | xargs rm -f
find frontend/php/locale -name '*.sh' | xargs rm -f

# fix path to traceroute utility
sed -i.orig -e 's|/usr/bin/traceroute|/bin/traceroute|' database/mysql/data.sql
sed -i.orig -e 's|/usr/bin/traceroute|/bin/traceroute|' database/postgresql/data.sql
sed -i.orig -e 's|/usr/bin/traceroute|/bin/traceroute|' database/sqlite3/data.sql

# remove .orig files in frontend
find frontends/php -name '*.orig'|xargs rm -f

# remove prebuild Windows binaries
rm -rf bin

# change log directory of zabbix_java.log
sed -i -e 's|/tmp/zabbix_java.log|/var/log/zabbix/zabbix_java_gateway.log|g' src/zabbix_java/lib/logback.xml

%build

%if %{build_server}
common_flags="
    --enable-dependency-tracking
    --sysconfdir=/etc/zabbix
    --enable-server
    --enable-agent
    --enable-proxy
    --enable-ipv6
    --enable-java
    --with-net-snmp
    --with-ldap
    --with-libcurl
    --with-openipmi
    --with-jabber
    --with-unixodbc
    --with-ssh2
    --with-libxml2
"

%configure $common_flags --with-mysql
make %{?_smp_mflags}
mv src/zabbix_server/zabbix_server src/zabbix_server/zabbix_server_mysql
mv src/zabbix_proxy/zabbix_proxy src/zabbix_proxy/zabbix_proxy_mysql

%configure $common_flags --with-postgresql
make %{?_smp_mflags}
mv src/zabbix_server/zabbix_server src/zabbix_server/zabbix_server_pgsql
mv src/zabbix_proxy/zabbix_proxy src/zabbix_proxy/zabbix_proxy_pgsql

%configure $common_flags --with-sqlite3
make %{?_smp_mflags}
#mv src/zabbix_server/zabbix_server src/zabbix_server/zabbix_server_sqlite3
mv src/zabbix_proxy/zabbix_proxy src/zabbix_proxy/zabbix_proxy_sqlite3

touch src/zabbix_server/zabbix_server
touch src/zabbix_proxy/zabbix_proxy

%else
%configure --enable-dependency-tracking --sysconfdir=/etc/zabbix --enable-agent
make %{?_smp_mflags}
%endif

%install
rm -rf $RPM_BUILD_ROOT

# install 
make DESTDIR=$RPM_BUILD_ROOT install

# remove unnecessary files
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/zabbix
rm -rf $RPM_BUILD_ROOT%{_datadir}/zabbix
%if %{build_server}
rm $RPM_BUILD_ROOT%{_sbindir}/zabbix_server
rm $RPM_BUILD_ROOT%{_sbindir}/zabbix_proxy
%endif
find ./frontends/php -name '*.orig'|xargs rm -f
find ./database -name '*.orig'|xargs rm -f

# set up some required directories
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/zabbix
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/zabbix/web
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/nginx/conf.d
mkdir -p $RPM_BUILD_ROOT/usr/lib/zabbix/alertscripts
mkdir -p $RPM_BUILD_ROOT/usr/lib/zabbix/externalscripts
mkdir -p $RPM_BUILD_ROOT%{_datadir}
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/log/zabbix
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/run/zabbix
%if 0%{?rhel} >= 7
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/tmpfiles.d
%else
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/init.d
%endif

# install the frontend
cp -a frontends/php $RPM_BUILD_ROOT%{_datadir}/zabbix

# prepare ghosted config file
touch $RPM_BUILD_ROOT%{_sysconfdir}/zabbix/web/zabbix.conf.php

# move maintenance.inc.php
mv $RPM_BUILD_ROOT%{_datadir}/zabbix/conf/maintenance.inc.php $RPM_BUILD_ROOT%{_sysconfdir}/zabbix/web/

# drop config files in place
install -m 0644 -p %{SOURCE16} $RPM_BUILD_ROOT%{_sysconfdir}/nginx/conf.d/zabbix.conf

# install zabbix_agent.conf and userparameter files
install -dm 755 $RPM_BUILD_ROOT%{_docdir}/zabbix-agent-%{version}
install -m 0644 conf/zabbix_agent.conf $RPM_BUILD_ROOT%{_docdir}/zabbix-agent-%{version}
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/zabbix/zabbix_agentd.d
install -m 0644 conf/zabbix_agentd/userparameter_mysql.conf $RPM_BUILD_ROOT%{_sysconfdir}/zabbix/zabbix_agentd.d
install -m 0644 conf/zabbix_agentd/userparameter_examples.conf $RPM_BUILD_ROOT%{_docdir}/zabbix-agent-%{version}

# fix config file options
cat conf/zabbix_agentd.conf | sed \
    -e '/^# PidFile=/a \\nPidFile=%{_localstatedir}/run/zabbix/zabbix_agentd.pid' \
    -e 's|^LogFile=.*|LogFile=%{_localstatedir}/log/zabbix/zabbix_agentd.log|g' \
    -e '/^# LogFileSize=.*/a \\nLogFileSize=0' \
    -e '/^# Include=$/a \\nInclude=%{_sysconfdir}/zabbix/zabbix_agentd.d/' \
    > $RPM_BUILD_ROOT%{_sysconfdir}/zabbix/zabbix_agentd.conf

cat conf/zabbix_server.conf | sed \
    -e '/^# PidFile=/a \\nPidFile=%{_localstatedir}/run/zabbix/zabbix_server.pid' \
    -e 's|^LogFile=.*|LogFile=%{_localstatedir}/log/zabbix/zabbix_server.log|g' \
    -e '/^# LogFileSize=/a \\nLogFileSize=0' \
    -e '/^# AlertScriptsPath=/a \\nAlertScriptsPath=/usr/lib/zabbix/alertscripts' \
    -e '/^# ExternalScripts=/a \\nExternalScripts=/usr/lib/zabbix/externalscripts' \
    -e 's|^DBUser=root|DBUser=zabbix|g' \
    -e '/^# DBSocket=/a \\nDBSocket=%{_localstatedir}/lib/mysql/mysql.sock' \
    -e '/^# SNMPTrapperFile=.*/a \\nSNMPTrapperFile=/var/log/snmptt/snmptt.log' \
    > $RPM_BUILD_ROOT%{_sysconfdir}/zabbix/zabbix_server.conf

cat conf/zabbix_proxy.conf | sed \
    -e '/^# PidFile=/a \\nPidFile=%{_localstatedir}/run/zabbix/zabbix_proxy.pid' \
    -e 's|^LogFile=.*|LogFile=%{_localstatedir}/log/zabbix/zabbix_proxy.log|g' \
    -e '/^# LogFileSize=/a \\nLogFileSize=0' \
    -e '/^# ExternalScripts=/a \\nExternalScripts=/usr/lib/zabbix/externalscripts' \
    -e 's|^DBUser=root|DBUser=zabbix|g' \
    -e '/^# DBSocket=/a \\nDBSocket=%{_localstatedir}/lib/mysql/mysql.sock' \
    > $RPM_BUILD_ROOT%{_sysconfdir}/zabbix/zabbix_proxy.conf

cat src/zabbix_java/settings.sh | sed \
    -e 's|^PID_FILE=.*|PID_FILE="/var/run/zabbix/zabbix_java.pid"|g' \
    > $RPM_BUILD_ROOT%{_sysconfdir}/zabbix/zabbix_java_gateway.conf

# install log rotation
cat %{SOURCE3} | sed -e 's|COMPONENT|server|g' > \
     $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/zabbix-server
cat %{SOURCE3} | sed -e 's|COMPONENT|agentd|g' > \
     $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/zabbix-agent
cat %{SOURCE3} | sed -e 's|COMPONENT|proxy|g' > \
     $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/zabbix-proxy


# init scripts
%if 0%{?rhel} >= 7
install -m 0644 -p %{SOURCE10} $RPM_BUILD_ROOT%{_unitdir}/zabbix-agent.service
install -m 0644 -p %{SOURCE11} $RPM_BUILD_ROOT%{_unitdir}/zabbix-server.service
install -m 0644 -p %{SOURCE12} $RPM_BUILD_ROOT%{_unitdir}/zabbix-proxy.service
install -m 0644 -p %{SOURCE13} $RPM_BUILD_ROOT%{_unitdir}/zabbix-java-gateway.service
%else
install -m 0755 -p %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/init.d/zabbix-java-gateway
install -m 0755 -p %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/init.d/zabbix-agent
install -m 0755 -p %{SOURCE6} $RPM_BUILD_ROOT%{_sysconfdir}/init.d/zabbix-server
install -m 0755 -p %{SOURCE7} $RPM_BUILD_ROOT%{_sysconfdir}/init.d/zabbix-proxy
%endif

%if 0%{?rhel} >= 7
install -m 0644 -p %{SOURCE15} $RPM_BUILD_ROOT%{_prefix}/lib/tmpfiles.d/zabbix.conf
%endif

# install server and proxy binaries
%if %{build_server}
install -m 0755 -p src/zabbix_server/zabbix_server_* $RPM_BUILD_ROOT%{_sbindir}/
install -m 0755 -p src/zabbix_proxy/zabbix_proxy_* $RPM_BUILD_ROOT%{_sbindir}/

# delete unnecessary files from java gateway
rm $RPM_BUILD_ROOT%{_sbindir}/zabbix_java/settings.sh
rm $RPM_BUILD_ROOT%{_sbindir}/zabbix_java/startup.sh
rm $RPM_BUILD_ROOT%{_sbindir}/zabbix_java/shutdown.sh
%endif

%if 0%{?rhel} >=7
mv $RPM_BUILD_ROOT%{_sbindir}/zabbix_java $RPM_BUILD_ROOT/%{_datadir}/zabbix-java-gateway
install -m 0755 -p %{SOURCE14} $RPM_BUILD_ROOT%{_sbindir}/zabbix_java_gateway
%endif

# nuke static libs and empty oracle upgrade sql
rm -rf $RPM_BUILD_ROOT%{_libdir}/libzbx*.a

# copy sql files for servers
docdir=$RPM_BUILD_ROOT%{_docdir}/zabbix-server-mysql-%{version}
install -dm 755 $docdir
cp -pR database/mysql $docdir/create
cp -pR --parents upgrades/dbpatches/1.6/mysql $docdir
cp -pR --parents upgrades/dbpatches/1.8/mysql $docdir
cp -pR --parents upgrades/dbpatches/2.0/mysql $docdir

docdir=$RPM_BUILD_ROOT%{_docdir}/zabbix-server-pgsql-%{version}
install -dm 755 $docdir
cp -pR database/postgresql $docdir/create
cp -pR --parents upgrades/dbpatches/1.6/postgresql $docdir
cp -pR --parents upgrades/dbpatches/1.8/postgresql $docdir
cp -pR --parents upgrades/dbpatches/2.0/postgresql $docdir

# copy sql files for proxyes
docdir=$RPM_BUILD_ROOT%{_docdir}/zabbix-proxy-mysql-%{version}
install -dm 755 $docdir/create
cp -pR database/mysql/schema.sql $docdir/create/schema.sql

docdir=$RPM_BUILD_ROOT%{_docdir}/zabbix-proxy-pgsql-%{version}
install -dm 755 $docdir/create
cp -pR database/postgresql/schema.sql $docdir/create/schema.sql

docdir=$RPM_BUILD_ROOT%{_docdir}/zabbix-proxy-sqlite3-%{version}
install -dm 755 $docdir/create
cp -pR database/sqlite3/schema.sql $docdir/create/schema.sql


# remove extraneous ones
rm -rf $RPM_BUILD_ROOT%{_datadir}/zabbix/create


%clean
rm -rf $RPM_BUILD_ROOT


%pre
getent group zabbix > /dev/null || groupadd -r zabbix
getent passwd zabbix > /dev/null || \
    useradd -r -g zabbix -d %{_localstatedir}/lib/zabbix -s /sbin/nologin \
    -c "Zabbix Monitoring System" zabbix
:

%post agent
%if 0%{?rhel} >= 7
%systemd_post zabbix-agent.service
%else
/sbin/chkconfig --add zabbix-agent || :
%endif

%if %{build_server}
%post server
%if 0%{?rhel} >= 7
%systemd_post zabbix-server.service
%else
/sbin/chkconfig --add zabbix-server
%endif
if [ $1 -gt 1 ]
then
  # Apply permissions also in *.rpmnew upgrades from old permissive ones
  chmod 0640 %{_sysconfdir}/zabbix/zabbix_server.conf
  chown root:zabbix %{_sysconfdir}/zabbix/zabbix_server.conf
fi
:

%post server-mysql
/usr/sbin/update-alternatives --install %{_sbindir}/zabbix_server zabbix-server %{_sbindir}/zabbix_server_mysql 10
:

%post server-pgsql
/usr/sbin/update-alternatives --install %{_sbindir}/zabbix_server zabbix-server %{_sbindir}/zabbix_server_pgsql 10
:

%post proxy
%if 0%{?rhel} >= 7
%systemd_post zabbix-proxy.service
%else
/sbin/chkconfig --add zabbix-proxy
%endif
if [ $1 -gt 1 ]
then
  # Apply permissions also in *.rpmnew upgrades from old permissive ones
  chmod 0640 %{_sysconfdir}/zabbix/zabbix_proxy.conf
  chown root:zabbix %{_sysconfdir}/zabbix/zabbix_proxy.conf
fi
:

%post proxy-mysql
/usr/sbin/update-alternatives --install %{_sbindir}/zabbix_proxy zabbix-proxy %{_sbindir}/zabbix_proxy_mysql 10
:

%post proxy-pgsql
/usr/sbin/update-alternatives --install %{_sbindir}/zabbix_proxy zabbix-proxy %{_sbindir}/zabbix_proxy_pgsql 10
:

%post proxy-sqlite3
/usr/sbin/update-alternatives --install %{_sbindir}/zabbix_proxy zabbix-proxy %{_sbindir}/zabbix_proxy_sqlite3 10
:

%post java-gateway
%if 0%{?rhel} >= 7
%systemd_post zabbix-java-gateway.service
%else
/sbin/chkconfig --add zabbix-java-gateway || :
%endif


%post web
%if 0%{?fedora} || 0%{?rhel} >= 6
/usr/sbin/update-alternatives --install %{_datadir}/zabbix/fonts/graphfont.ttf zabbix-web-font %{_datadir}/fonts/dejavu/DejaVuSans.ttf 10
%else
/usr/sbin/update-alternatives --install %{_datadir}/zabbix/fonts/graphfont.ttf zabbix-web-font %{_datadir}/zabbix/fonts/DejaVuSans.ttf 10
%endif
# move existing config file on update
if [ "$1" -ge "1" ]
then
    if [ -f %{_sysconfdir}/zabbix/zabbix.conf.php ]
    then
        mv %{_sysconfdir}/zabbix/zabbix.conf.php %{_sysconfdir}/zabbix/web
        chown nginx:nginx %{_sysconfdir}/zabbix/web/zabbix.conf.php
    fi
fi
:

%post web-japanese
%if 0%{?fedora} || 0%{?rhel} >= 6
  /usr/sbin/update-alternatives --install %{_datadir}/zabbix/fonts/graphfont.ttf zabbix-web-font %{_datadir}/fonts/vlgothic/VL-PGothic-Regular.ttf 20
%else
  /usr/sbin/update-alternatives --install %{_datadir}/zabbix/fonts/graphfont.ttf zabbix-web-font %{_datadir}/fonts/ipa-pgothic/ipagp.ttf 20
%endif
:
%endif

%preun agent
if [ "$1" = 0 ]
then
%if 0%{?rhel} >= 7
  %systemd_preun zabbix-agent.service
%else
  /sbin/service zabbix-agent stop >/dev/null 2>&1
  /sbin/chkconfig --del zabbix-agent
%endif
fi
:

%if %{build_server}
%preun server
if [ "$1" = 0 ]
then
%if 0%{?rhel} >= 7
  %systemd_preun zabbix-server.service
%else
  /sbin/service zabbix-server stop >/dev/null 2>&1
  /sbin/chkconfig --del zabbix-server
%endif
fi
:

%preun server-mysql
if [ "$1" = 0 ]
then
  /usr/sbin/update-alternatives --remove zabbix-server %{_sbindir}/zabbix_server_mysql
fi
:

%preun server-pgsql
if [ "$1" = 0 ]
then
  /usr/sbin/update-alternatives --remove zabbix-server %{_sbindir}/zabbix_server_pgsql
fi
:

%preun proxy
if [ "$1" = 0 ]
then
%if 0%{?rhel} >= 7
  %systemd_preun zabbix-proxy.service
%else
  /sbin/service zabbix-proxy stop >/dev/null 2>&1
  /sbin/chkconfig --del zabbix-proxy
%endif
fi
:

%preun proxy-mysql
if [ "$1" = 0 ]
then
  /usr/sbin/update-alternatives --remove zabbix-proxy %{_sbindir}/zabbix_proxy_mysql
fi
:

%preun proxy-pgsql
if [ "$1" = 0 ]
then
  /usr/sbin/update-alternatives --remove zabbix-proxy %{_sbindir}/zabbix_proxy_pgsql
fi
:

%preun proxy-sqlite3
if [ "$1" = 0 ]
then
  /usr/sbin/update-alternatives --remove zabbix-proxy %{_sbindir}/zabbix_proxy_sqlite3
fi
:

%preun java-gateway
if [ $1 -eq 0 ]
then
%if 0%{?rhel} >= 7
  %systemd_preun zabbix-java-gateway.service
%else
  /sbin/service zabbix-java-gateway stop >/dev/null 2>&1
  /sbin/chkconfig --del zabbix-java-gateway
%endif
fi
:

%preun web
if [ "$1" = 0 ]
then
  %if 0%{?fedora} || 0%{?rhel} >= 6
    /usr/sbin/update-alternatives --remove zabbix-web-font %{_datadir}/fonts/dejavu/DejaVuSans.ttf
  %else
    /usr/sbin/update-alternatives --remove zabbix-web-font %{_datadir}/zabbix/fonts/DejaVuSans.ttf
  %endif
fi
:

%preun web-japanese
if [ "$1" = 0 ]
then
  %if 0%{?fedora} || 0%{?rhel} >= 6
    /usr/sbin/update-alternatives --remove zabbix-web-font %{_datadir}/fonts/vlgothic/VL-PGothic-Regular.ttf 
  %else
    /usr/sbin/update-alternatives --remove zabbix-web-font %{_datadir}/fonts/ipa-pgothic/ipagp.ttf
  %endif
fi
:
%endif

%postun agent
if [ $1 -ge 1 ]
then
  /sbin/service zabbix-agent try-restart >/dev/null 2>&1 || :
fi
%if 0%{?rhel} >= 7
%systemd_postun_with_restart zabbix-agent.service
%endif

%if %{build_server}
%postun server
if [ $1 -ge 1 ]
then
  /sbin/service zabbix-server try-restart >/dev/null 2>&1 || :
fi
%if 0%{?rhel} >= 7
%systemd_postun_with_restart zabbix-server.service
%endif


%postun proxy
if [ $1 -ge 1 ]
then
  /sbin/service zabbix-proxy try-restart >/dev/null 2>&1 || :
fi
%if 0%{?rhel} >= 7
%systemd_postun_with_restart zabbix-proxy.service
%endif


%postun java-gateway
if [ $1 -gt 1 ]; then
  /sbin/service zabbix-java-gateway condrestart >/dev/null 2>&1 || :
fi
%if 0%{?rhel} >= 7
%systemd_postun_with_restart zabbix-java-gateway.service
%endif

%endif

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%dir %{_sysconfdir}/zabbix
%attr(0755,zabbix,zabbix) %dir %{_localstatedir}/log/zabbix
%attr(0755,zabbix,zabbix) %dir %{_localstatedir}/run/zabbix
%if 0%{?rhel} >= 7
%{_prefix}/lib/tmpfiles.d/zabbix.conf
%endif

%files agent
%defattr(-,root,root,-)
%{_docdir}/zabbix-agent-%{version}/
%config(noreplace) %{_sysconfdir}/zabbix/zabbix_agentd.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/zabbix-agent
%dir %{_sysconfdir}/zabbix/zabbix_agentd.d
%config(noreplace) %{_sysconfdir}/zabbix/zabbix_agentd.d/userparameter_mysql.conf
%{_sbindir}/zabbix_agent
%{_sbindir}/zabbix_agentd
%{_mandir}/man8/zabbix_agentd.8*
%if 0%{?rhel} >= 7
%{_unitdir}/zabbix-agent.service
%else
%{_sysconfdir}/init.d/zabbix-agent
%endif

%files get
%defattr(-,root,root,-)
%{_bindir}/zabbix_get
%{_mandir}/man1/zabbix_get.1*

%files sender
%defattr(-,root,root,-)
%{_bindir}/zabbix_sender
%{_mandir}/man1/zabbix_sender.1*

%if %{build_server}
%files server
%defattr(-,root,root,-)
%attr(0640,root,zabbix) %config(noreplace) %{_sysconfdir}/zabbix/zabbix_server.conf
%dir /usr/lib/zabbix/alertscripts
%dir /usr/lib/zabbix/externalscripts
%config(noreplace) %{_sysconfdir}/logrotate.d/zabbix-server
%{_mandir}/man8/zabbix_server.8*
%if 0%{?rhel} >= 7
%{_unitdir}/zabbix-server.service
%else
%{_sysconfdir}/init.d/zabbix-server
%endif

%files server-mysql
%defattr(-,root,root,-)
%{_docdir}/zabbix-server-mysql-%{version}/
%{_sbindir}/zabbix_server_mysql

%files server-pgsql
%defattr(-,root,root,-)
%{_docdir}/zabbix-server-pgsql-%{version}/
%{_sbindir}/zabbix_server_pgsql

%files proxy
%defattr(-,root,root,-)
%attr(0640,root,zabbix) %config(noreplace) %{_sysconfdir}/zabbix/zabbix_proxy.conf
%attr(0755,zabbix,zabbix) %dir /usr/lib/zabbix/externalscripts
%config(noreplace) %{_sysconfdir}/logrotate.d/zabbix-proxy
%{_mandir}/man8/zabbix_proxy.8*
%if 0%{?rhel} >= 7
%{_unitdir}/zabbix-proxy.service
%else
%{_sysconfdir}/init.d/zabbix-proxy
%endif

%files proxy-mysql
%defattr(-,root,root,-)
%{_docdir}/zabbix-proxy-mysql-%{version}/
%{_sbindir}/zabbix_proxy_mysql

%files proxy-pgsql
%defattr(-,root,root,-)
%{_docdir}/zabbix-proxy-pgsql-%{version}/
%{_sbindir}/zabbix_proxy_pgsql

%files proxy-sqlite3
%defattr(-,root,root,-)
%{_docdir}/zabbix-proxy-sqlite3-%{version}/
%{_sbindir}/zabbix_proxy_sqlite3

%files java-gateway
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/zabbix/zabbix_java_gateway.conf
%if 0%{?rhel} >= 7
%{_datadir}/zabbix-java-gateway
%{_sbindir}/zabbix_java_gateway
%{_unitdir}/zabbix-java-gateway.service
%else
%{_sbindir}/zabbix_java
%{_sysconfdir}/init.d/zabbix-java-gateway
%endif

%files web
%defattr(-,root,root,-)
%dir %attr(0750,nginx,nginx) %{_sysconfdir}/zabbix/web
%ghost %attr(0644,nginx,nginx) %config(noreplace) %{_sysconfdir}/zabbix/web/zabbix.conf.php
%config(noreplace) %{_sysconfdir}/zabbix/web/maintenance.inc.php
%config(noreplace) %{_sysconfdir}/nginx/conf.d/zabbix.conf
%{_datadir}/zabbix

%files web-mysql
%defattr(-,root,root,-)

%files web-pgsql
%defattr(-,root,root,-)

%files web-japanese
%defattr(-,root,root,-)
%endif


%changelog
* Thu Mar 10 2016 Aleksandr Chernyshev <wmlex@yandex.ru> - 2.4.7-2
- deleted depending httpd, php
- added dependency nginx, php-fpm
- added config to nginx

* Fri Nov 13 2015 Kodai Terashima <kodai.terashima@zabbix.com> - 2.4.7-1
- update to 2.4.7
- add IfModule for mod_php5 in apache configuration file

* Tue Aug 11 2015 Kodai Terashima <kodai.terashima@zabbix.com> - 2.4.6-1
- update to 2.4.6
- remove carriage return for pidfile
- fix insecure permission error of logrotate for rhel7

* Thu Apr 23 2015 Kodai Terashima <kodai.terashima@zabbix.com> - 2.4.5-1
- update to 2.4.5
- add pidfile and timeout for stop script
- fix some macros
- remove old obsolete

* Tue Feb 24 2015 Kodai Terashima <kodai.terashima@zabbix.com> - 2.4.4-1
- update to 2.4.4

* Tue Dec 16 2014 Kodai Terashima <kodai.terashima@zabbix.com> - 2.4.3-1
- update to 2.4.3
- fix proxy configuration file name for systemd service file
- Compile with Jave 6 for RHEL 6
- fix status parameter of init scripts

* Fri Nov 7 2014 Kodai Terashima <kodai.tearshima@zabbix.com> - 2.4.2-1
- update to 2.4.2

* Fri Oct 31 2014 Kodai Terashima <kodai.terashima@zabbix.com> - 2.4.1-2
- support RHEL7

* Wed Oct 8 2014 Kodai Terashima <kodai.terashima@zabbix.com> - 2.4.1-1
- update to 2.4.1

* Tue Oct 7 2014 Kodai Terashima <kodai.terashima@zabbix.com> - 2.4.0-2
- remove updating file timestamp

* Thu Sep 11 2014 Kodai Terashima <kodai.terashima@zabbix.com> - 2.4.0
- update to 2.4.0

* Wed Sep 10 2014 Kodai Terashima <kodai.terashima@zabbix.com> - 2.4.0rc3-1
- update to 2.4.0rc3

* Tue Sep 9 2014 Kodai Terashima <kodai.terashima@zabbix.com> - 2.4.0rc2-1
- update to 2.4.0rc2

* Sun Sep 7 2014 Kodai Terashima <kodai.terashima@zabbix.com> - 2.4.0rc1-1
- update to 2.4.0rc1

* Fri Sep 5 2014 Kodai Terashima <kodai.tearshima@zabbix.com> - 2.3.5-1
- update to 2.3.5

* Sat Aug 30 2014 Kodai Terashima <kodai.terashima@zabbix.com> - 2.3.4-1
- update to 2.3.4
- update cofnig.patch

* Fri Aug 8 2014 Kodai Terashima <kodai.terashima@zabbix.com> - 2.3.3-1
- update to 2.3.3

* Sun Jul 27 2014 Kodai Terashima <kodai.terashima@zabbix.com> - 2.3.2-1
- update to 2.3.2

* Sun Jul 20 2014 Kodai Terashima <kodai.terashima@zabbix.com> - 2.2.5-1
- update to 2.2.5
- remove conflicts with server and web from proxy package

* Thu Jun 26 2014 Kodai Terashima <kodai.terashima@zabbix.com> - 2.2.4-1
- update to 2.2.4

* Tue Apr 8 2014 Kodai Terashima <kodai.terashima@zabbix.com> - 2.2.3-1
- fix map become unavailable when host is in maintenance (ZBX-7838)
- enable to override some variables by sysconfig file (ZBX-7940)
- remove conflicts with server and web from proxy package
- add init scripts

* Sat Feb 15 2014 Kodai Terashima <kodai.terashima@zabbix.com> - 2.2.2-1
- update to 2.2.2
- change lockfile name to zabbix-server

* Wed Dec 11 2013 Kodai Terashima <kodai.terashima@zabbix.com> - 2.2.1-1
- update to 2.2.1
- remove images and data sql files from proxy packages
- remove .po and related files
- remove unnecessary modification for maintenance.inc.php in config.patch

* Thu Dec 5 2013 Kodai Terashima <kodai.terashima@zabbix.com> - 2.2.0-2
- support for rhel5

* Tue Nov 12 2013 Kodai Terashima <kodai.terashima@zabbix.com> - 2.2.0-1
- update to 2.2.0

* Thu Nov 7 2013 Kodai Terashima <kodai.terashima@zabbix.com> - 2.2.0rc2
- update to 2.2.0rc2

* Tue Nov 5 2013 Kodai Terashima <kodai.terashima@zabbix.com> - 2.1.9-1
- update to 2.1.9

* Thu Oct 10 2013 Kodai Terashima <kodai.terashima@zabbix.com> - 2.1.7-1
- update to 2.1.7

* Tue Oct 8 2013 Kodai Terashima <kodai.terashima@zabbix.com> - 2.1.6-1
- update to 2.1.6

* Sat Aug 31 2013 Kodai Terashima <kodai.terashima@zabbix.com> - 2.1.3-1
- update to 2.1.3

* Wed Aug 14 2013 Kodai Terashima <kodai.terashima@zabbix.com> - 2.1.1-1
- update to 2.1.1

* Thu Aug 1 2013 Kodai Terashima <kodai.terashima@zabbix.com> - 2.0.7-1
- update to 2.0.7

* Tue Apr 23 2013 Kodai Terashima <kodai.terashima@zabbix.com> - 2.0.6-1
- update to 2.0.6
- fix zabbix-java-gateway init script

* Wed Feb 13 2013 Kodai Terashima <kodai.terashima@zabbix.com> - 2.0.5-1
- update to 2.0.5

* Sun Dec 9 2012 Kodai Terashima <kodai.terashima@zabbix.com> - 2.0.4-1
- update to 2.0.4

* Tue Oct 16 2012 Kodai Terashima <kodai.terashima@zabbix.com> - 2.0.3-1
- update to 2.0.3


* Wed Aug 1 2012 Kodai Terashima <kodai.terashima@zabbix.com> - 2.0.2-1
- update to 2.0.2

* Mon Jul 16 2012 Kodai Terashima <kodai.terashima@zabbix.com> - 2.0.1-2
- move userparameter_examples.conf to docdir
- move java gateway log file to /var/log/zabbix

* Tue Jul 3 2012 Kodai Terashima <kodai.terashima@zabbix.com> - 2.0.1-1
- update to 2.0.1

* Wed May 30 2012 Kodai Terashima <kodai.terashima@zabbix.com> - 2.0.0-1
- update to 2.0.0

* Wed Apr 25 2012 Kodai Terashima <kodai.terashima@zabbix.com> -1.8.12-1
- update to 1.8.12

* Tue Apr 3 2012 Kodai Terashima <kodai.terashima@zabbix.com> - 1.8.11-1
- update to 1.8.11
- move maintenance.inc.php to /etc/zabbix/web

* Wed Feb 8 2012 Kodai Terashima <kodai.terashima@zabbix.com> - 1.8.10-1
- update to 1.8.10
- remove snmptrap related files
- move init scripts to zabbix source
- separate get and sender subpackages
- remove server-sqlite3 and web-sqlite3 subpackages
- add web-japanese subpackage
- move alertscripts and externalscripts to /usr/lib/zabbix
- improve default parameter of config files
- delete dependency for zabbix from web package
- move zabbix_agent.conf to docdir

* Tue Aug  9 2011 Dan Horák <dan[at]danny.cz> - 1.8.6-1
- updated to 1.8.6 (#729164, #729165)
- updated user/group adding scriptlet

* Mon May 23 2011 Dan Horák <dan[at]danny.cz> - 1.8.5-2
- include /var/lib/zabbix and /etc/zabbix/externalscripts dirs in package (#704181)
- add snmp trap receiver script in package (#705331)

* Wed Apr 20 2011 Dan Horák <dan[at]danny.cz> - 1.8.5-1
- updated to 1.8.5

* Tue Jan 18 2011 Dan Horák <dan[at]danny.cz> - 1.8.4-2
- enable libcurl detection (#670500)

* Tue Jan  4 2011 Dan Horák <dan[at]danny.cz> - 1.8.4-1
- updated to 1.8.4
- fixes zabbix_agent fail to start on IPv4-only host (#664639)

* Tue Nov 23 2010 Dan Horák <dan[at]danny.cz> - 1.8.3-3
- zabbix emailer doesn't handle multiline responses (#656072)

* Tue Oct 05 2010 jkeating - 1.8.3-2.1
- Rebuilt for gcc bug 634757

* Mon Sep  6 2010 Dan Horák <dan[at]danny.cz> - 1.8.3-2
- fix font path in patch2 (#630500)

* Tue Aug 17 2010 Dan Horák <dan[at]danny.cz> - 1.8.3-1
- updated to 1.8.3

* Wed Aug 11 2010 Dan Horák <dan[at]danny.cz> - 1.8.2-3
- added patch for XSS in triggers page (#620809, ZBX-2326)

* Thu Apr 29 2010 Dan Horák <dan[at]danny.cz> - 1.8.2-2
- DejaVu fonts doesn't exist on EL <= 5

* Tue Mar 30 2010 Dan Horák <dan[at]danny.cz> - 1.8.2-1
- Update to 1.8.2

* Sat Mar 20 2010 Dan Horák <dan[at]danny.cz> - 1.8.1-7
- web interface needs php-xml (#572413)
- updated defaults in config files (#573325)
- built with libssh2 support (#575279)

* Wed Feb 24 2010 Dan Horák <dan[at]danny.cz> - 1.8.1-6
- use system fonts

* Sun Feb 13 2010 Dan Horák <dan[at]danny.cz> - 1.8.1-5
- fixed linking with the new --no-add-needed default (#564932)

* Mon Feb  1 2010 Dan Horák <dan[at]danny.cz> - 1.8.1-4
- enable dependency tracking

* Mon Feb  1 2010 Dan Horák <dan[at]danny.cz> - 1.8.1-3
- updated the web-config patch

* Mon Feb  1 2010 Dan Horák <dan[at]danny.cz> - 1.8.1-2
- close fd on exec (#559221)

* Fri Jan 29 2010 Dan Horák <dan[at]danny.cz> - 1.8.1-1
- Update to 1.8.1

* Tue Jan 26 2010 Dan Horák <dan[at]danny.cz> - 1.8-1
- Update to 1.8

* Thu Dec 31 2009 Dan Horák <dan[at]danny.cz> - 1.6.8-1
- Update to 1.6.8
- Upstream changelog: http://www.zabbix.com/rn1.6.8.php
- fixes 2 issues from #551331

* Wed Nov 25 2009 Dan Horák <dan[at]danny.cz> - 1.6.6-2
- rebuilt with net-snmp 5.5

* Sat Aug 29 2009 Dan Horák <dan[at]danny.cz> - 1.6.6-1
- Update to 1.6.6
- Upstream changelog: http://www.zabbix.com/rn1.6.6.php

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.6.5-3
- rebuilt with new openssl

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun  8 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.5-1
- Update to 1.6.5, see http://sourceforge.net/mailarchive/message.php?msg_name=4A37A2CA.8050503%40zabbix.com for the full release notes.
- 
- It is recommended to create the following indexes in order to speed up
- performance of ZABBIX front-end as well as server side (ignore it if the
- indexes already exist):
- 
- CREATE UNIQUE INDEX history_log_2 on history_log (itemid,id);
- CREATE UNIQUE INDEX history_text_2 on history_text (itemid,id);
- CREATE INDEX graphs_items_1 on graphs_items (itemid);
- CREATE INDEX graphs_items_2 on graphs_items (graphid);
- CREATE INDEX services_1 on services (triggerid);

* Mon Jun  8 2009 Ville Skyttä <ville.skytta at iki.fi> - 1.6.4-4
- Start agent after and shut down before proxy and server by default.
- Include database schemas also in -proxy-* docs.
- Make buildable on EL-4 (without libcurl, OpenIPMI).
- Reformat description.

* Fri Apr 17 2009 Ville Skyttä <ville.skytta at iki.fi> - 1.6.4-3
- Tighten configuration file permissions.
- Ensure zero exit status from scriptlets.
- Improve init script LSB compliance.
- Restart running services on package upgrades.

* Thu Apr  9 2009 Dan Horák <dan[at]danny.cz> - 1.6.4-2
- make the -docs subpackage noarch

* Thu Apr  9 2009 Dan Horák <dan[at]danny.cz> - 1.6.4-1
- update to 1.6.4
- remove the cpustat patch, it was integreated into upstream
- use noarch subpackage for the web interface
- database specific web subpackages conflicts with each other
- use common set of option for the configure macro
- enable IPMI support
- sqlite web subpackage must depend on local sqlite
- reorganize the docs and the sql scripts
- change how the web interface config file is created
- updated scriptlet for adding the zabbix user
- move the documentation in PDF to -docs subpackage
- most of the changes were submitted by Ville Skyttä in #494706 
- Resolves: #489673, #493234, #494706

* Mon Mar  9 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2-5
- Update pre patch due to incomplete fix for security problems.

* Wed Mar  4 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2-4
- Update to a SVN snapshot of the upstream 1.6 branch to fix security
  issue (BZ#488501)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 23 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2-2
- Rebuild for MySQL 5.1.X

* Fri Jan 16 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2-1
- Update to 1.6.2: http://www.zabbix.com/rn1.6.2.php

* Thu Dec  4 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1-1
- Fix BZ#474593 by adding a requires.

* Wed Nov  5 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1-1
- Update to 1.6.1

* Tue Sep 30 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6-1.1
- Bump release because forgot to add some new files.

* Thu Sep 30 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6-1
- Update to final 1.6

* Mon Aug 11 2008 Jason L Tibbitts III <tibbs@math.uh.edu> - 1.4.6-2
- Fix license tag.

* Fri Jul 25 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.6-1
- Update to 1.4.6

* Mon Jul 07 2008 Dan Horak <dan[at]danny.cz> - 1.4.5-4
- add LSB headers into init scripts
- disable internal log rotation

* Fri May 02 2008 Jarod Wilson <jwilson@redhat.com> - 1.4.5-3
- Seems the zabbix folks replaced the original 1.4.5 tarball with
  an updated tarball or something -- it actually does contain a
  tiny bit of additional code... So update to newer 1.4.5.

* Tue Apr 08 2008 Jarod Wilson <jwilson@redhat.com> - 1.4.5-2
- Fix building w/postgresql (#441456)

* Tue Mar 25 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.5-1
- Update to 1.4.5

* Thu Feb 14 2008 Jarod Wilson <jwilson@redhat.com> - 1.4.4-2
- Bump and rebuild with gcc 4.3

* Mon Dec 17 2007 Jarod Wilson <jwilson@redhat.com> - 1.4.4-1
- New upstream release
- Fixes two crasher bugs in 1.4.3 release

* Wed Dec 12 2007 Jarod Wilson <jwilson@redhat.com> - 1.4.3-1
- New upstream release

* Thu Dec 06 2007 Release Engineering <rel-eng at fedoraproject dot org> - 1.4.2-5
- Rebuild for deps

* Sat Dec 01 2007 Dan Horak <dan[at]danny.cz> 1.4.2-4
- add security fix (#407181)

* Thu Sep 20 2007 Dan Horak <dan[at]danny.cz> 1.4.2-3
- Add a patch to clean a warning during compile
- Add a patch to fix cpu load computations

* Tue Aug 21 2007 Jarod Wilson <jwilson@redhat.com> 1.4.2-2
- Account for binaries moving from %%_bindir to %%_sbindir

* Tue Aug 21 2007 Jarod Wilson <jwilson@redhat.com> 1.4.2-1
- New upstream release

* Mon Jul 02 2007 Jarod Wilson <jwilson@redhat.com> 1.4.1-1
- New upstream release

* Fri Jun 29 2007 Jarod Wilson <jwilson@redhat.com> 1.4-3
- Install correct sql init files (#244991)
- Add Requires: php-bcmath to zabbix-web (#245767)

* Wed May 30 2007 Jarod Wilson <jwilson@redhat.com> 1.4-2
- Add placeholder zabbix.conf.php

* Tue May 29 2007 Jarod Wilson <jwilson@redhat.com> 1.4-1
- New upstream release

* Fri Mar 30 2007 Jarod Wilson <jwilson@redhat.com> 1.1.7-1
- New upstream release

* Wed Feb 07 2007 Jarod Wilson <jwilson@redhat.com> 1.1.6-1
- New upstream release

* Thu Feb 01 2007 Jarod Wilson <jwilson@redhat.com> 1.1.5-1
- New upstream release

* Tue Jan 02 2007 Jarod Wilson <jwilson@redhat.com> 1.1.4-5
- Add explicit R:php to zabbix-web (#220676)

* Wed Dec 13 2006 Jarod Wilson <jwilson@redhat.com> 1.1.4-4
- Fix snmp polling buffer overflow (#218065)

* Wed Nov 29 2006 Jarod Wilson <jwilson@redhat.com> 1.1.4-3
- Rebuild for updated libnetsnmp

* Thu Nov 16 2006 Jarod Wilson <jwilson@redhat.com> 1.1.4-2
- Fix up pt_br
- Add Req-pre on useradd

* Wed Nov 15 2006 Jarod Wilson <jwilson@redhat.com> 1.1.4-1
- Update to 1.1.4

* Tue Nov 14 2006 Jarod Wilson <jwilson@redhat.com> 1.1.3-3
- Add BR: gnutls-devel, R: net-snmp-libs

* Tue Nov 14 2006 Jarod Wilson <jwilson@redhat.com> 1.1.3-2
- Fix php-pgsql Requires

* Tue Nov 14 2006 Jarod Wilson <jwilson@redhat.com> 1.1.3-1
- Update to 1.1.3

* Mon Oct 02 2006 Jarod Wilson <jwilson@redhat.com> 1.1.2-1
- Update to 1.1.2
- Enable alternate building with postgresql support

* Thu Aug 17 2006 Jarod Wilson <jwilson@redhat.com> 1.1.1-2
- Yank out Requires: mysql-server
- Add Requires: for php-gd and fping

* Tue Aug 15 2006 Jarod Wilson <jwilson@redhat.com> 1.1.1-1
- Update to 1.1.1
- More macroification
- Fix up zabbix-web Requires:
- Prep for enabling postgres support

* Thu Jul 27 2006 Jarod Wilson <jwilson@redhat.com> 1.1-2
- Add Requires: on chkconfig and service
- Remove openssl-devel from BR, mysql-devel pulls it in
- Alter scriptlets to match Fedora conventions

* Tue Jul 11 2006 Jarod Wilson <jwilson@redhat.com> 1.1-1
- Initial build for Fedora Extras
