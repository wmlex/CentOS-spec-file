Name:           xupnpd
Version:        1.034
Release:        1%{?dist}
Summary:        xupnpd - eXtensible UPnP agent

Group:          System Environment/Daemons
License:        GPLv2
URL:            http://xupnpd.org/
Source0:        https://codeload.github.com/clark15b/%{name}/tar.gz/%{name}-%{version}.tar.gz	

#BuildRequires: lbuuid-devel	
#Requires:	

%description
This program is a light DLNA Media Server which provides ContentDirectory:1 service for sharing IPTV unicast streams
over local area network (with udpxy for multicast to HTTP unicast conversion).
The program shares UTF8-encoded M3U playlists with links over local area network as content of the directory.
You can watch HDTV broadcasts (multicast or unicast) and listen Internet Radio in IP network without transcoding and PC. 

#%prep
#%setup -q

#%build
#%configure
#make %{?_smp_mflags}

%install
tar xvzf %{SOURCE0}
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/etc
mkdir -p $RPM_BUILD_ROOT/usr/share/xupnpd/config/postinit
mkdir -p $RPM_BUILD_ROOT/usr/share/xupnpd/localmedia
mkdir -p $RPM_BUILD_ROOT/usr/share/xupnpd/playlists/example
mkdir -p $RPM_BUILD_ROOT/usr/share/xupnpd/plugins/skel
mkdir -p $RPM_BUILD_ROOT/usr/share/xupnpd/profiles/skel
mkdir -p $RPM_BUILD_ROOT/usr/share/xupnpd/ui
mkdir -p $RPM_BUILD_ROOT/usr/share/xupnpd/www
#
install usr/bin/xupnpd $RPM_BUILD_ROOT/usr/bin
install usr/share/xupnpd/config/postinit/.empty $RPM_BUILD_ROOT/usr/share/xupnpd/config/postinit
install usr/share/xupnpd/config/.empty $RPM_BUILD_ROOT/usr/share/xupnpd/config
install usr/share/xupnpd/localmedia/.empty $RPM_BUILD_ROOT/usr/share/xupnpd/localmedia
#
install usr/share/xupnpd/playlists/example/butovocom_iptv.m3u $RPM_BUILD_ROOT/usr/share/xupnpd/playlists/example
install usr/share/xupnpd/playlists/example/example.m3u $RPM_BUILD_ROOT/usr/share/xupnpd/playlists/example
install usr/share/xupnpd/playlists/example/iskra.m3u $RPM_BUILD_ROOT/usr/share/xupnpd/playlists/example
install usr/share/xupnpd/playlists/example/mozhay.m3u $RPM_BUILD_ROOT/usr/share/xupnpd/playlists/example
install usr/share/xupnpd/playlists/example/service.m3u $RPM_BUILD_ROOT/usr/share/xupnpd/playlists/example
install usr/share/xupnpd/playlists/ag_videos.m3u $RPM_BUILD_ROOT/usr/share/xupnpd/playlists
install usr/share/xupnpd/playlists/bf3epic.m3u $RPM_BUILD_ROOT/usr/share/xupnpd/playlists
install usr/share/xupnpd/playlists/bf.m3u $RPM_BUILD_ROOT/usr/share/xupnpd/playlists
install usr/share/xupnpd/playlists/gametrailers_ps3.m3u $RPM_BUILD_ROOT/usr/share/xupnpd/playlists
install usr/share/xupnpd/playlists/giantbomb_all.m3u $RPM_BUILD_ROOT/usr/share/xupnpd/playlists
install usr/share/xupnpd/playlists/ivi_genre_horror.m3u $RPM_BUILD_ROOT/usr/share/xupnpd/playlists
install usr/share/xupnpd/playlists/ivi_new.m3u $RPM_BUILD_ROOT/usr/share/xupnpd/playlists
install usr/share/xupnpd/playlists/vimeo_channel_hd.m3u $RPM_BUILD_ROOT/usr/share/xupnpd/playlists
install usr/share/xupnpd/playlists/vimeo_channel_hdxs.m3u $RPM_BUILD_ROOT/usr/share/xupnpd/playlists
install usr/share/xupnpd/playlists/vimeo_channel_mtb.m3u $RPM_BUILD_ROOT/usr/share/xupnpd/playlists
install usr/share/xupnpd/playlists/youtube_channel_top_rated.m3u $RPM_BUILD_ROOT/usr/share/xupnpd/playlists
#
install usr/share/xupnpd/plugins/skel/skel.lua $RPM_BUILD_ROOT/usr/share/xupnpd/plugins/skel
install usr/share/xupnpd/plugins/xupnpd_ag.lua $RPM_BUILD_ROOT/usr/share/xupnpd/plugins
install usr/share/xupnpd/plugins/xupnpd_arjlover.lua $RPM_BUILD_ROOT/usr/share/xupnpd/plugins
install usr/share/xupnpd/plugins/xupnpd_dreambox.lua $RPM_BUILD_ROOT/usr/share/xupnpd/plugins
install usr/share/xupnpd/plugins/xupnpd_gametrailers.lua $RPM_BUILD_ROOT/usr/share/xupnpd/plugins
install usr/share/xupnpd/plugins/xupnpd_generic.lua $RPM_BUILD_ROOT/usr/share/xupnpd/plugins
install usr/share/xupnpd/plugins/xupnpd_giantbomb.lua $RPM_BUILD_ROOT/usr/share/xupnpd/plugins
install usr/share/xupnpd/plugins/xupnpd_ivi.lua $RPM_BUILD_ROOT/usr/share/xupnpd/plugins
install usr/share/xupnpd/plugins/xupnpd_netstreamsat.lua $RPM_BUILD_ROOT/usr/share/xupnpd/plugins
install usr/share/xupnpd/plugins/xupnpd_vimeo.lua $RPM_BUILD_ROOT/usr/share/xupnpd/plugins
install usr/share/xupnpd/plugins/xupnpd_vkontakte.lua $RPM_BUILD_ROOT/usr/share/xupnpd/plugins
install usr/share/xupnpd/plugins/xupnpd_youtube.lua $RPM_BUILD_ROOT/usr/share/xupnpd/plugins
#
install usr/share/xupnpd/profiles/skel/skel.lua $RPM_BUILD_ROOT/usr/share/xupnpd/profiles/skel
install usr/share/xupnpd/profiles/bravia.lua $RPM_BUILD_ROOT/usr/share/xupnpd/profiles
install usr/share/xupnpd/profiles/lg.lua $RPM_BUILD_ROOT/usr/share/xupnpd/profiles
install usr/share/xupnpd/profiles/samsung.lua $RPM_BUILD_ROOT/usr/share/xupnpd/profiles
install usr/share/xupnpd/profiles/vlc-1_0_6.lua $RPM_BUILD_ROOT/usr/share/xupnpd/profiles
install usr/share/xupnpd/profiles/wdtv.lua $RPM_BUILD_ROOT/usr/share/xupnpd/profiles
install usr/share/xupnpd/profiles/wmp.lua $RPM_BUILD_ROOT/usr/share/xupnpd/profiles
install usr/share/xupnpd/profiles/xbox360.lua $RPM_BUILD_ROOT/usr/share/xupnpd/profiles
#
install usr/share/xupnpd/ui/api.txt $RPM_BUILD_ROOT/usr/share/xupnpd/ui
install usr/share/xupnpd/ui/bootstrap.min.css $RPM_BUILD_ROOT/usr/share/xupnpd/ui
install usr/share/xupnpd/ui/ui_config.html $RPM_BUILD_ROOT/usr/share/xupnpd/ui
install usr/share/xupnpd/ui/ui_main.html $RPM_BUILD_ROOT/usr/share/xupnpd/ui
install usr/share/xupnpd/ui/ui_template.html $RPM_BUILD_ROOT/usr/share/xupnpd/ui
install usr/share/xupnpd/ui/xupnpd_ui.lua $RPM_BUILD_ROOT/usr/share/xupnpd/ui
#
install usr/share/xupnpd/www/cds.xml $RPM_BUILD_ROOT/usr/share/xupnpd/www
install usr/share/xupnpd/www/cms.xml $RPM_BUILD_ROOT/usr/share/xupnpd/www
install usr/share/xupnpd/www/corrupted.mp4 $RPM_BUILD_ROOT/usr/share/xupnpd/www
install usr/share/xupnpd/www/dev.xml $RPM_BUILD_ROOT/usr/share/xupnpd/www
install usr/share/xupnpd/www/favicon.ico $RPM_BUILD_ROOT/usr/share/xupnpd/www
install usr/share/xupnpd/www/icon-48x48.png $RPM_BUILD_ROOT/usr/share/xupnpd/www
install usr/share/xupnpd/www/index.html $RPM_BUILD_ROOT/usr/share/xupnpd/www
install usr/share/xupnpd/www/msr.xml $RPM_BUILD_ROOT/usr/share/xupnpd/www
install usr/share/xupnpd/www/vk-flash-format-only.mp4 $RPM_BUILD_ROOT/usr/share/xupnpd/www
install usr/share/xupnpd/www/vk-private-video.mp4 $RPM_BUILD_ROOT/usr/share/xupnpd/www
install usr/share/xupnpd/www/wmc.xml $RPM_BUILD_ROOT/usr/share/xupnpd/www
#
install usr/share/xupnpd/LICENSE $RPM_BUILD_ROOT/usr/share/xupnpd
install usr/share/xupnpd/xupnpd_http.lua $RPM_BUILD_ROOT/usr/share/xupnpd
install usr/share/xupnpd/xupnpd.lua $RPM_BUILD_ROOT/usr/share/xupnpd
install usr/share/xupnpd/xupnpd_m3u.lua $RPM_BUILD_ROOT/usr/share/xupnpd
install usr/share/xupnpd/xupnpd_main.lua $RPM_BUILD_ROOT/usr/share/xupnpd
install usr/share/xupnpd/xupnpd_mime.lua $RPM_BUILD_ROOT/usr/share/xupnpd
install usr/share/xupnpd/xupnpd_soap.lua $RPM_BUILD_ROOT/usr/share/xupnpd
install usr/share/xupnpd/xupnpd_ssdp.lua $RPM_BUILD_ROOT/usr/share/xupnpd
#
ln -s /usr/share/xupnpd/xupnpd.lua $RPM_BUILD_ROOT/etc/
#
mkdir -p $RPM_BUILD_ROOT/usr/lib/systemd/system/
cat > $RPM_BUILD_ROOT/usr/lib/systemd/system/xupnpd.service <<HERE
[Unit]
Description=xupnpd
After=network.target

[Service]
Type=simple
User=nobody
Group=nobody
ExecStart=/usr/bin/xupnpd

[Install]
WantedBy=multi-user.target
HERE
#
mkdir -p $RPM_BUILD_ROOT/etc/firewalld/services
cat > $RPM_BUILD_ROOT/etc/firewalld/services/xupnpd.xml <<HERE
<?xml version="1.0" encoding="utf-8"?>
<service>
 <short>XUPnPd</short>
 <description>XUPnPd is a simple media server software.</description>
 <port protocol="tcp" port="4044"/>
</service>
HERE
#
%files
%defattr(-,nobody,nobody)
/usr/bin/xupnpd
/usr/share/xupnpd/config/postinit/.empty
/usr/share/xupnpd/config/.empty
/usr/share/xupnpd/localmedia/.empty
/usr/share/xupnpd/playlists/example/butovocom_iptv.m3u
/usr/share/xupnpd/playlists/example/example.m3u
/usr/share/xupnpd/playlists/example/iskra.m3u
/usr/share/xupnpd/playlists/example/mozhay.m3u
/usr/share/xupnpd/playlists/example/service.m3u
/usr/share/xupnpd/playlists/ag_videos.m3u
/usr/share/xupnpd/playlists/bf3epic.m3u
/usr/share/xupnpd/playlists/bf.m3u
/usr/share/xupnpd/playlists/gametrailers_ps3.m3u
/usr/share/xupnpd/playlists/giantbomb_all.m3u
/usr/share/xupnpd/playlists/ivi_genre_horror.m3u
/usr/share/xupnpd/playlists/ivi_new.m3u
/usr/share/xupnpd/playlists/vimeo_channel_hd.m3u
/usr/share/xupnpd/playlists/vimeo_channel_hdxs.m3u
/usr/share/xupnpd/playlists/vimeo_channel_mtb.m3u
/usr/share/xupnpd/playlists/youtube_channel_top_rated.m3u
/usr/share/xupnpd/plugins/skel/skel.lua
/usr/share/xupnpd/plugins/xupnpd_ag.lua
/usr/share/xupnpd/plugins/xupnpd_arjlover.lua
/usr/share/xupnpd/plugins/xupnpd_dreambox.lua
/usr/share/xupnpd/plugins/xupnpd_gametrailers.lua
/usr/share/xupnpd/plugins/xupnpd_generic.lua
/usr/share/xupnpd/plugins/xupnpd_giantbomb.lua
/usr/share/xupnpd/plugins/xupnpd_ivi.lua
/usr/share/xupnpd/plugins/xupnpd_netstreamsat.lua
/usr/share/xupnpd/plugins/xupnpd_vimeo.lua
/usr/share/xupnpd/plugins/xupnpd_vkontakte.lua
/usr/share/xupnpd/plugins/xupnpd_youtube.lua
/usr/share/xupnpd/profiles/skel/skel.lua
/usr/share/xupnpd/profiles/bravia.lua
/usr/share/xupnpd/profiles/lg.lua
/usr/share/xupnpd/profiles/samsung.lua
/usr/share/xupnpd/profiles/vlc-1_0_6.lua
/usr/share/xupnpd/profiles/wdtv.lua
/usr/share/xupnpd/profiles/wmp.lua
/usr/share/xupnpd/profiles/xbox360.lua
/usr/share/xupnpd/ui/api.txt
/usr/share/xupnpd/ui/bootstrap.min.css
/usr/share/xupnpd/ui/ui_config.html
/usr/share/xupnpd/ui/ui_main.html
/usr/share/xupnpd/ui/ui_template.html
/usr/share/xupnpd/ui/xupnpd_ui.lua
/usr/share/xupnpd/www/cds.xml
/usr/share/xupnpd/www/cms.xml
/usr/share/xupnpd/www/corrupted.mp4
/usr/share/xupnpd/www/dev.xml
/usr/share/xupnpd/www/favicon.ico
/usr/share/xupnpd/www/icon-48x48.png
/usr/share/xupnpd/www/index.html
/usr/share/xupnpd/www/msr.xml
/usr/share/xupnpd/www/vk-flash-format-only.mp4
/usr/share/xupnpd/www/vk-private-video.mp4
/usr/share/xupnpd/www/wmc.xml
/usr/share/xupnpd/LICENSE
/usr/share/xupnpd/xupnpd_http.lua
/usr/share/xupnpd/xupnpd.lua
/usr/share/xupnpd/xupnpd_m3u.lua
/usr/share/xupnpd/xupnpd_main.lua
/usr/share/xupnpd/xupnpd_mime.lua
/usr/share/xupnpd/xupnpd_soap.lua
/usr/share/xupnpd/xupnpd_ssdp.lua
/etc/xupnpd.lua
#
%attr(-,root,root) /usr/lib/systemd/system/xupnpd.service
%attr(-,root,root) /etc/firewalld/services/xupnpd.xml
#
%dir %attr(-,nobody,nobody) /usr/share/xupnpd
%dir %attr(-,nobody,nobody) /usr/share/xupnpd/config
%dir %attr(-,nobody,nobody) /usr/share/xupnpd/config/postinit
%dir %attr(-,nobody,nobody) /usr/share/xupnpd/localmedia
%dir %attr(-,nobody,nobody) /usr/share/xupnpd/playlists
%dir %attr(-,nobody,nobody) /usr/share/xupnpd/playlists/example
%dir %attr(-,nobody,nobody) /usr/share/xupnpd/plugins
%dir %attr(-,nobody,nobody) /usr/share/xupnpd/plugins/skel
%dir %attr(-,nobody,nobody) /usr/share/xupnpd/profiles
%dir %attr(-,nobody,nobody) /usr/share/xupnpd/profiles/skel
%dir %attr(-,nobody,nobody) /usr/share/xupnpd/ui
%dir %attr(-,nobody,nobody) /usr/share/xupnpd/www

%doc
%changelog
* Thu Feb 04 2016 Aleksandr Chernyshev <wmlex@yandex.ru> - 1.034-1
- First init
