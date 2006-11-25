#
# Conditional build
%bcond_without	editor	# build without editor
#
%define	_rc	rc2
Summary:	Puzzle game with "fancy" graphics
Summary(pl):	Gra logiczna z "gustown±" grafik±
Name:		magicor
Version:	1.0
Release:	0.%{_rc}.1
License:	?
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/magicor/%{name}-source-%{version}-%{_rc}.tar.gz
# Source0-md5:	8914ec1bcc05f05cc7c9a3d47993a2c8
Source1:	http://downloads.sourceforge.net/magicor/%{name}-data-%{version}-%{_rc}.tar.gz
# Source1-md5:	bc2004e9d28268d00f286b5172781827
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-path.patch
URL:		http://magicor.sourceforge.net/
BuildRequires:	SDL-devel >= 1.2
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
%{?with_editor:BuildRequires:	gtk+2-devel >= 2.0}
%{?with_editor:BuildRequires:	libglade2-devel}
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	python-pygame
%{?with_editor:BuildRequires:	python-pygtk-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
As a heroic penguin you must create, destroy and move blocks of ice to
destroy enemies and extinguish demonic hell fire.

%description -l pl
Jako bohaterski pingwin gracz musi tworzyæ, niszczyæ i przesuwaæ
lodowe bloki aby pokonaæ wrogów i zwalczyæ demoniczne si³y.

%package editor
Summary:	Level editor for Magicor
Summary(pl):	Edytor poziomów dla Magicor
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description editor
Level editor for Magicor,

%description editor -l pl
Edytor poziomów dla Magico.

%prep
%setup -q -n %{name}-%{version}-%{_rc} -a 1
%patch0 -p1
%patch1 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	MAGICOR=%{name}-%{version}-%{_rc}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/Magicor
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf
%{_datadir}/%{name}
%{py_sitescriptdir}/%{name}

%if %{with editor}
%files editor
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Magicor-LevelEditor
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}-editor.conf
%endif
