Summary:	Simple text editor
Name:		ecrire
Version:	0.2.0
Release:	1
License:	BSD
Group:		Applications
Source0:	https://download.enlightenment.org/rel/apps/ecrire/%{name}-%{version}.tar.xz
# Source0-md5:	580bb7e512642ad7c7b1de9e98a14c1b
URL:		http://enlightenment.org/
BuildRequires:	efl-devel >= 1.27.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.726
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple text editor.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%{__mv} $RPM_BUILD_ROOT%{_localedir}/ko{_KR,}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README TODO
%attr(755,root,root) %{_bindir}/ecrire
%{_desktopdir}/ecrire.desktop
%{_iconsdir}/hicolor/*x*/apps/ecrire.png
%{_iconsdir}/hicolor/scalable/apps/ecrire.svg
