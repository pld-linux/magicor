#
# Conditional build
%bcond_without	editor	# build without editor
#
%define	_rc	rc1
Summary:	Puzzle game with "fancy" graphics
Summary(pl.UTF-8):	Gra logiczna z "wyszukaną" grafiką
Name:		magicor
Version:	1.1
Release:	0.%{_rc}.1
License:	Public Domain
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/magicor/%{name}-source-%{version}-%{_rc}.tar.gz
# Source0-md5:	10f005bf8bb70bade2d8280451a75dca
Source1:	http://dl.sourceforge.net/magicor/%{name}-data-%{version}-%{_rc}.tar.gz
# Source1-md5:	4a6fbd10ae7b08adcdbcc4d5f8d10207
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

%description -l pl.UTF-8
Jako bohaterski pingwin gracz musi tworzyć, niszczyć i przesuwać
lodowe bloki aby pokonać wrogów i zwalczyć demoniczne siły.

%package editor
Summary:	Level editor for Magicor
Summary(pl.UTF-8):	Edytor poziomów dla Magicor
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description editor
Level editor for Magicor.

%description editor -l pl.UTF-8
Edytor poziomów dla Magicor.

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
%doc LICENSE README
%attr(755,root,root) %{_bindir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf
%{_datadir}/%{name}
%{py_sitescriptdir}/%{name}

%if %{with editor}
%files editor
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}-editor
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}-editor.conf
%endif
