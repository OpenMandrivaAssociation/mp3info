Summary:	Utility for MP3 information and tag modification
Name:		mp3info
Version:	0.8.5a
Release:	6
Group:		Sound
License:	GPL
URL:		ftp://metalab.unc.edu/pub/linux/apps/sound/mp3-utils/mp3info
Source0:	ftp.debian.org/debian/pool/main/m/mp3info/%{name}-%{version}.tgz
Source1:	mp3info-16.png
Source2:	mp3info-32.png
Source3:	mp3info-48.png
Patch0:		mp3info-0.8.5a-format_not_a_string_literal_and_no_format_arguments.diff
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	ncurses-devel

%description
An MP3 technical info viewer and ID3 1.x tag editor.
MP3Info has an interactive mode (using curses) and a command line mode.
MP3Info can display ID3 tag information as well as various technical aspects
of an MP3 file including playing time, bit-rate, sampling frequency and other
attributes in a pre-defined or user-specifiable output format.
It also has a VERY configurable output.
mp3info is availlable with both ncurses and gtk UIs.

%prep
%setup -q -n %name-%version
%patch0 -p0

%build
%make CFLAGS="%{optflags}"

%install

mkdir -p %{buildroot}/{%{_bindir},%{_mandir}/man1}
%makeinstall prefix=%{buildroot} mandir=%{buildroot}%{_mandir}/man1

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Name=MP3 info
Comment=Utility for MP3 information and tag modification
Exec=%{_bindir}/gmp3info
Icon=sound_section
Terminal=false
Type=Application
Categories=Audio;AudioVideo;AudioVideoEditing;
EOF

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean

%files
%defattr (-,root,root)
%doc README ChangeLog mp3info.lsm LICENSE
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/applications/mandriva-%{name}.desktop


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.5a-5mdv2011.0
+ Revision: 620402
- the mass rebuild of 2010.0 packages

* Mon Oct 05 2009 Oden Eriksson <oeriksson@mandriva.com> 0.8.5a-4mdv2010.0
+ Revision: 453963
- fix build
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sun Jul 20 2008 Oden Eriksson <oeriksson@mandriva.com> 0.8.5a-2mdv2009.0
+ Revision: 239064
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Mon Jul 02 2007 Funda Wang <fwang@mandriva.org> 0.8.5a-1mdv2008.0
+ Revision: 47124
- BR gtk2 rather than gtk1
- New version
  move to xdg menu
- Import mp3info



* Mon Sep 18 2006 Gwenole Beauchesne <gbeauchesne@mandriva.com> 0.8.4-14mdv2007.0
- Rebuild

* Sat Jun 17 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.8.4-13mdk
- Rebuild
- use mkrel

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.8.4-12mdk
- Rebuild

* Tue Sep  2 2003 Götz Waschk <waschk@linux-mandrake.com> 0.8.4-11mdk
- fix buildrequires

* Wed Jul 23 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.8.4-10mdk
- fix gcc-3.3 patch (P0)

* Fri Jul 18 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.8.4-9mdk
- fix P0, dunno what happened..!?!?!?
- cosmetics

* Thu Jun 19 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.8.4-8mdk
- fix for gcc-3.3 (P0, from Christiaan Welvaart <cjw@daneel.dyndns.org>)
- rm -rf $RPM_BUILD_ROOT in the correct stage
- fixed a type
- compile with $RPM_OPT_FLAGS
- drop redundant requires, rpm will figure out library dependencies itself

* Tue May 27 2003 David BAUDENS <baudens@mandrakesoft.com> 0.8.4-7mdk
- Fix icon in menu

* Fri Jan 03 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.8.4-6mdk
- build release

* Tue Jan 29 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.8.4-5mdk
- xpm to png icons conversion

* Tue Oct 30 2001 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.8.4-4mdk
- add %%url

* Thu Oct 25 2001 Stefan van der Eijk <stefan@eijk.nu> 0.8.4-3mdk
- BuildRequires: ncurses-devel

* Thu Aug 30 2001 David BAUDENS <baudens@mandrakesoft.com> 0.8.4-2mdk
- Use icons in menu

* Fri Aug 17 2001 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.8.4-1mdk
- add {Build,}Requires
- add a README.mandrake which explain why the new prog
- fix source url
- enhanced description
- new release
- add menu entry

* Mon Jul 16 2001 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.8.3-1mdk
- new release

* Wed Mar 14 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.2.16-5mdk
- fix build (includes of glibc-2.2.2)

* Wed Nov 08 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2.16-4mdk
- capitalize summary

* Tue Aug 01 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2.16-3mdk
- BM

* Tue May 02 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.2.16-2mdk
- fix group
- fix files section

* Tue Nov 30 1999 Lenny Cartier <lenny@mandrakesoft.com>
- new in contribs
- bz archive, man pages

* Fri Mar 19 1999 Thorvald Natvig <thorvald@natvig.com>
- Initial release as RPM
