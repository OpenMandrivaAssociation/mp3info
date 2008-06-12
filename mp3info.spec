Summary:	Mp3info - Utility for MP3 information and tag modification
Name:		mp3info
Version:	0.8.5a
Release: %mkrel 1
Group:		Sound
Url:		ftp://metalab.unc.edu/pub/linux/apps/sound/mp3-utils/mp3info
Source0:	ftp.debian.org/debian/pool/main/m/mp3info/%{name}-%{version}.tgz
Source1:	mp3info-16.png
Source2:	mp3info-32.png
Source3:	mp3info-48.png
License:	GPL
BuildRoot:	%_tmppath/%name-%version-%release-root
BuildRequires:	gtk+2-devel ncurses-devel

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

%build
%make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{%{_bindir},%{_mandir}/man1}
%makeinstall prefix=$RPM_BUILD_ROOT mandir=$RPM_BUILD_ROOT%{_mandir}/man1

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Name=MP3 info
Comment=Utility for MP3 information and tag modification
Exec=%{_bindir}/gmp3info
Icon=sound_section
Terminal=false
Type=Application
Categories=Audio;AudioVideo;AudioVideoEditing;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files
%defattr (-,root,root)
%doc README ChangeLog mp3info.lsm LICENSE
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/applications/mandriva-%{name}.desktop
