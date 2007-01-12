#
# Conditional build
%bcond_without	editor	# build without editor
#
Summary:	Puzzle game with "fancy" graphics
Summary(pl):	Gra logiczna z "wyszukan±" grafik±
Name:		magicor
Version:	1.0
Release:	1
License:	Public Domain
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/magicor/%{name}-source-%{version}.tar.gz
# Source0-md5:	8f30cc33e531a08583bb60af9f373503
Source1:	http://dl.sourceforge.net/magicor/%{name}-data-%{version}.tar.gz
# Source1-md5:	2e8146d3bc69811e7908073a9be41ecb
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-path.patch
URL:		http://magicor.sourceforge.net/
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	python-pygame
%{?with_editor:BuildRequires:	python-pygtk-devel}
BuildArch:	noarch
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
Level editor for Magicor.

%description editor -l pl
Edytor poziomów dla Magicor.

%prep
%setup -q -a 1
%patch0 -p1
%patch1 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	MAGICOR=%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README
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
