Summary:	Mp3info - Utility for MP3 information and tag modification
Name:		mp3info
Version:	0.8.4
Release: %mkrel 14
Group:		Sound
Url:		ftp://metalab.unc.edu/pub/linux/apps/sound/mp3-utils/mp3info
Source0:	ftp.debian.org/debian/pool/main/m/mp3info/%{name}_%{version}.tar.bz2
Source1:	mp3info-16.png
Source2:	mp3info-32.png
Source3:	mp3info-48.png
Patch0:		%{name}-0.8.4-gcc3.3.patch.bz2
License:	GPL
BuildRoot:	%_tmppath/%name-%version-%release-root
BuildRequires:	gtk-devel ncurses-devel

%description
An MP3 technical info viewer and ID3 1.x tag editor.
MP3Info has an interactive mode (using curses) and a command line mode.
MP3Info can display ID3 tag information as well as various technical aspects
of an MP3 file including playing time, bit-rate, sampling frequency and other
attributes in a pre-defined or user-specifiable output format.
It also has a VERY configurable output.
mp3info is availlable with both ncurses and gtk UIs.

%prep
%setup -q -n %name-%version.orig
%patch0 -p1

%build
%make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{%{_bindir},%{_mandir}/man1}
%makeinstall prefix=$RPM_BUILD_ROOT mandir=$RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%_menudir

cat > $RPM_BUILD_ROOT%_menudir/%name <<EOF
?package(mp3info):needs=X11 section=Multimedia/Sound \
command="%{_bindir}/gmp3info" title="MP3 info" icon="sound_section.png" \
longtitle="Utility for MP3 information and tag modification"
EOF

cat >README.mandrake <<EOF
Earlier releases of Mandrake Linux included a different program with
the same name mp3info.
It has been replaced by this one, as the old mp3info was buggy and
no longer maintained upstream. The source seems to be a fork of the
original one (diffing with care of white space, ...).

The command line interface is mostly the same, altrough you might experience
some differences. Additionally there's curses interface available, as well as
GTK interface (separate package).

The following switches have changed their meanings in the new mp3info:
 -f (old mp3info: set print format, new mp3info: force mode)
 -F (old mp3info: set predefined format, new mp3info: full scan)
 -n (old mp3info: set title, new mp3info: set track number)
 -G (old mp3info: set genre by name, new mp3info: display genres)
 -p (old mp3info: list genres, new mp3info: set print format)

The following switches were renamed:
 -f (set print format) is now -p (format strings are changed, too)
 -W (wipe tag) is now -d
 -G (set genre by name) is incorporated into -g
 -p (list genres) is now -G

The following switches were removed:
 -T, -s, -w, -N, -e, -P, -R

The following switches were added:
 -h, -i, -r, -x
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{update_menus}

%postun
%{clean_menus}

%files
%defattr (-,root,root)
%doc README ChangeLog mp3info.lsm LICENSE README.mandrake
%{_bindir}/*
%{_mandir}/man1/*
%_menudir/%name
