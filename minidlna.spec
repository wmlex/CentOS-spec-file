Name:           minidlna
Version:        1.1.5
Release:        1%{?dist}
Summary:        Lightweight DLNA/UPnP-AV server targeted at embedded systems

Group:          System Environment/Daemons
License:        GPLv2 
URL:            http://sourceforge.net/projects/minidlna/
Source0:        http://netassist.dl.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}_static.tar.gz

%description
MiniDLNA (aka ReadyDLNA) is server software with the aim of being fully 
compliant with DLNA/UPnP-AV clients.

The minidlna daemon serves media files (music, pictures, and video) to 
clients on your network.  Example clients include applications such as 
Totem and XBMC, and devices such as portable media players, smartphones, 
and televisions.

#%prep
#%setup -q -n %{name}-%{version}

#%build
#%configure
#make %{?_smp_mflags}

%install
tar xvzf %{SOURCE0} 
mkdir -p $RPM_BUILD_ROOT/usr/sbin
mkdir -p $RPM_BUILD_ROOT/etc
mkdir -p $RPM_BUILD_ROOT/usr/share/locale/da/LC_MESSAGES
mkdir -p $RPM_BUILD_ROOT/usr/share/locale/de/LC_MESSAGES
mkdir -p $RPM_BUILD_ROOT/usr/share/locale/es/LC_MESSAGES
mkdir -p $RPM_BUILD_ROOT/usr/share/locale/fr/LC_MESSAGES
mkdir -p $RPM_BUILD_ROOT/usr/share/locale/it/LC_MESSAGES
mkdir -p $RPM_BUILD_ROOT/usr/share/locale/ja/LC_MESSAGES
mkdir -p $RPM_BUILD_ROOT/usr/share/locale/ko/LC_MESSAGES
mkdir -p $RPM_BUILD_ROOT/usr/share/locale/nb/LC_MESSAGES
mkdir -p $RPM_BUILD_ROOT/usr/share/locale/nl/LC_MESSAGES
mkdir -p $RPM_BUILD_ROOT/usr/share/locale/pl/LC_MESSAGES
mkdir -p $RPM_BUILD_ROOT/usr/share/locale/ru/LC_MESSAGES
mkdir -p $RPM_BUILD_ROOT/usr/share/locale/sl/LC_MESSAGES
mkdir -p $RPM_BUILD_ROOT/usr/share/locale/sv/LC_MESSAGES
mkdir -p $RPM_BUILD_ROOT/var/cache/minidlna
mkdir -p $RPM_BUILD_ROOT/var/run/minidlna
mkdir -p $RPM_BUILD_ROOT/var/log/minidlna
#
install usr/sbin/minidlnad $RPM_BUILD_ROOT/usr/sbin
install etc/minidlna.conf $RPM_BUILD_ROOT/etc
install usr/share/locale/da/LC_MESSAGES/minidlna.mo $RPM_BUILD_ROOT/usr/share/locale/da/LC_MESSAGES
install usr/share/locale/de/LC_MESSAGES/minidlna.mo $RPM_BUILD_ROOT/usr/share/locale/de/LC_MESSAGES
install usr/share/locale/es/LC_MESSAGES/minidlna.mo $RPM_BUILD_ROOT/usr/share/locale/es/LC_MESSAGES
install usr/share/locale/fr/LC_MESSAGES/minidlna.mo $RPM_BUILD_ROOT/usr/share/locale/fr/LC_MESSAGES
install usr/share/locale/it/LC_MESSAGES/minidlna.mo $RPM_BUILD_ROOT/usr/share/locale/it/LC_MESSAGES
install usr/share/locale/ja/LC_MESSAGES/minidlna.mo $RPM_BUILD_ROOT/usr/share/locale/ja/LC_MESSAGES
install usr/share/locale/ko/LC_MESSAGES/minidlna.mo $RPM_BUILD_ROOT/usr/share/locale/ko/LC_MESSAGES
install usr/share/locale/nb/LC_MESSAGES/minidlna.mo $RPM_BUILD_ROOT/usr/share/locale/nb/LC_MESSAGES
install usr/share/locale/nl/LC_MESSAGES/minidlna.mo $RPM_BUILD_ROOT/usr/share/locale/nl/LC_MESSAGES
install usr/share/locale/pl/LC_MESSAGES/minidlna.mo $RPM_BUILD_ROOT/usr/share/locale/pl/LC_MESSAGES
install usr/share/locale/ru/LC_MESSAGES/minidlna.mo $RPM_BUILD_ROOT/usr/share/locale/ru/LC_MESSAGES
install usr/share/locale/sl/LC_MESSAGES/minidlna.mo $RPM_BUILD_ROOT/usr/share/locale/sl/LC_MESSAGES
install usr/share/locale/sv/LC_MESSAGES/minidlna.mo $RPM_BUILD_ROOT/usr/share/locale/sv/LC_MESSAGES
#
sed -i 's/#log_dir=\/var\/log/#log_dir=\/var\/log\/minidlna/' \
  $RPM_BUILD_ROOT/etc/%{name}.conf
#
mkdir -p $RPM_BUILD_ROOT/usr/lib/systemd/system/
cat > $RPM_BUILD_ROOT/usr/lib/systemd/system/minidlna.service <<HERE
[Unit]
Description=miniDLNA
After=network.target

[Service]
Type=simple
User=nobody
Group=nobody
PermissionsStartOnly=true
PIDFile=/var/run/minidlna/minidlna.pid
ExecStartPre=-/usr/bin/mkdir -p /var/run/minidlna
ExecStartPre=/usr/bin/chown nobody.nobody /var/run/minidlna
ExecStart=/usr/sbin/minidlnad -S
ExecReload=/usr/sbin/minidlnad -R
ExecStop=/usr/bin/rm -rf /var/run/minidlna

[Install]
WantedBy=multi-user.target
HERE
#
mkdir -p $RPM_BUILD_ROOT/etc/firewalld/services
cat > $RPM_BUILD_ROOT/etc/firewalld/services/minidlna.xml <<HERE
<?xml version="1.0" encoding="utf-8"?>
<service>
 <short>MiniDLNA</short>
 <description>MiniDLNA is a simple media server software.</description>
 <port protocol="tcp" port="8200"/>
 <port protocol="udp" port="1900"/>
</service>
HERE


%files
%defattr(-,root,root)
/usr/sbin/minidlnad
/usr/share/locale/da/LC_MESSAGES/minidlna.mo
/usr/share/locale/de/LC_MESSAGES/minidlna.mo
/usr/share/locale/es/LC_MESSAGES/minidlna.mo
/usr/share/locale/fr/LC_MESSAGES/minidlna.mo
/usr/share/locale/it/LC_MESSAGES/minidlna.mo
/usr/share/locale/ja/LC_MESSAGES/minidlna.mo
/usr/share/locale/ko/LC_MESSAGES/minidlna.mo
/usr/share/locale/nb/LC_MESSAGES/minidlna.mo
/usr/share/locale/nl/LC_MESSAGES/minidlna.mo
/usr/share/locale/pl/LC_MESSAGES/minidlna.mo
/usr/share/locale/ru/LC_MESSAGES/minidlna.mo
/usr/share/locale/sl/LC_MESSAGES/minidlna.mo
/usr/share/locale/sv/LC_MESSAGES/minidlna.mo
#
/usr/lib/systemd/system/minidlna.service
/etc/firewalld/services/minidlna.xml
#
%dir %attr(-,nobody,nobody) %{_localstatedir}/cache/%{name}/
%dir %attr(-,nobody,nobody) %{_localstatedir}/run/%{name}/
%dir %attr(-,nobody,nobody) %{_localstatedir}/log/%{name}/
%attr(-,nobody,nobody) %{_sysconfdir}/minidlna.conf

%changelog
* Thu Feb 02 2016 Aleksandr Chernyshev <wmlex@yandex.ru> - 1.1.5-1
- First init
