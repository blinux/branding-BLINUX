#-
# Copyright 2014 Emmanuel Vadot <elbarto@bocal.org>
# All rights reserved
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted providing that the following conditions 
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
# IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

Name:           branding-BLINUX
Version:        3.0
Release:        0
Summary:        BLINUX Brand File
License:        BSD-2-Clause

Provides:       branding
Conflicts:      otherproviders(branding)
Supplements:	packageand(wallpaper:branding-BLINUX)

Source0:	1280x1024.png
Source1:	1600x1200.png
Source2:	1920x1080.png
Source3:	1920x1200.png
Source4:	BLINUX-default.xml
Source5:	metadata.desktop
Source6:	wallpaper-branding-BLINUX.xml
BuildRequires:  update-desktop-files
BuildArch:      noarch

Url:            https://www.blinux.fr
Packager:       Emmanuel Vadot <elbarto@bocal.org>
Vendor:		Blinux

%description
BLINUX branding base package

%package        -n wallpaper-branding-BLINUX
Summary:        Provides BLINUX wallpapers
License:        BSD-2-Clause
Group:          System/Fhs
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       wallpaper-branding = %{version}
Conflicts:      otherproviders(wallpaper-branding)
BuildArch:      noarch
Vendor:		Blinux

%description -n wallpaper-branding-BLINUX
BLINUX %{version} defaults wallpapers

%prep

%build
cat >SUSE-brand <<EOF
BLINUX
VERSION = %{version}
EOF

%install
mkdir -p %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}/usr/share/gnome-background-properties/
mkdir -p %{buildroot}/usr/share/wallpapers/BLINUXdefault/contents/images
install -m 644 SUSE-brand %{buildroot}%{_sysconfdir}/
install -m 444 %{SOURCE0} %{buildroot}/usr/share/wallpapers/BLINUXdefault/contents/images/
install -m 444 %{SOURCE1} %{buildroot}/usr/share/wallpapers/BLINUXdefault/contents/images/
install -m 444 %{SOURCE2} %{buildroot}/usr/share/wallpapers/BLINUXdefault/contents/images/
install -m 444 %{SOURCE3} %{buildroot}/usr/share/wallpapers/BLINUXdefault/contents/images/
install -m 444 %{SOURCE4} %{buildroot}/usr/share/wallpapers/
install -m 444 %{SOURCE5} %{buildroot}/usr/share/wallpapers/BLINUXdefault/metadata.desktop
install -m 444 %{SOURCE6} %{buildroot}/usr/share/gnome-background-properties/
ln -s /usr/share/wallpapers/BLINUX-default.xml %{buildroot}/usr/share/wallpapers/BLINUX-default-static.xml
%suse_update_desktop_file %{buildroot}/usr/share/wallpapers/BLINUXdefault/metadata.desktop

%post -n wallpaper-branding-BLINUX
update-alternatives --install /usr/share/wallpapers/BLINUX-default.xml BLINUX-default.xml /usr/share/wallpapers/BLINUX-default-static.xml 5

%postun -n wallpaper-branding-BLINUX
if [ ! -f /usr/share/wallpapers/BLINUX-default.xml ]; then
  update-alternatives --remove BLINUX-default.xml /usr/share/wallpapers/BLINUX-default-static.xml
fi

%files
%defattr(-,root,root)
%{_sysconfdir}/SUSE-brand

%files -n wallpaper-branding-BLINUX
%defattr(-,root,root)
/usr/share/wallpapers/BLINUX-default.xml
/usr/share/gnome-background-properties/
/usr/share/gnome-background-properties/wallpaper-branding-BLINUX.xml
/usr/share/wallpapers/

%changelog
* Mon Aug 03 2015 Emmanuel Vadot <elbarto@bocal.org> - 3.0
- Update to 3.0

* Wed Aug 06 2014 Emmanuel Vadot <elbarto@bocal.org> - 2.0
- Package creation
