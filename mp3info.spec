Summary:	Utility for MP3 information and tag modification
Name:		mp3info
Version:	0.8.5a
Release:	8
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

%define debug_package %{nil}

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
Name[ru]=Информация о MP3
Comment=Utility for MP3 information and tag modification
Comment[ru]=Утилита для модификации тэгов MP3
Exec=%{_bindir}/gmp3info
Icon=sound_section
Terminal=false
Type=Application
Categories=Audio;AudioVideo;AudioVideoEditing;
EOF

%files
%doc README ChangeLog mp3info.lsm LICENSE
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/applications/mandriva-%{name}.desktop
