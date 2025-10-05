%global debug_package %{nil}
%define _hardened_build 1

Name:           {{{ git_dir_name }}}
Version:        {{{ git_dir_version }}}
Release:        1%{?dist}
Summary:        Terminal music player

License:        GPLv2
URL:            https://github.com/ravachol/kew
VCS:            {{{ git_dir_vcs }}}
Source:         {{{ git_dir_pack }}}

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  libatomic
BuildRequires:  pkg-config
BuildRequires:  taglib-devel
BuildRequires:  fftw-devel
BuildRequires:  opus-devel
BuildRequires:  opusfile-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libogg-devel
BuildRequires:  chafa-devel
BuildRequires:  glib2-devel
BuildRequires:  faad2-devel

%description
kew is a terminal music player with a customizable interface, playlist management, and support for various audio formats.

%prep
{{{ git_dir_setup_macro }}}

%build
%make_build

%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix}

%files
%{_bindir}/kew
%{_datadir}/kew/
%{_mandir}/man1/kew.1.gz

%changelog
{{{ git_dir_changelog }}}

