Summary:	WMfmixer is a simple mixer application for WindowMaker
Summary(pl):	Prosty program do obs³ugi d¼wiêku w WindowMakerze
Name:		wmfmixer
Version:	0.1
Release:	4
License:	GPL
Vendor:		Dimitry Fink <finik@sporu.net>
Group:		X11/Applications/Sound
Source0:	http://www.finik.net/files/%{name}-%{version}.tar.gz
# Source0-md5:	620712536263d60782b50f16e1aec910
Source1:	%{name}.desktop
Patch0:		%{name}-Makefile.pach
Patch1:		%{name}-main.patch
URL:		http://www.finik.net/software.html
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WMfmixer is a simple dockable program for controlling /dev/mixer
device. It's simplicity is no doubt his good point.

%description -l pl
WMfmixer jest prostym dokowalnym programem do kontroli nad urz±dzeniem
/dev/mixer. Niew±tpliw± zalet± tej aplikacji jest jej prostota.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LIBDIR="-L/usr/X11R6/%{_lib}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_desktopdir}/docklets}

install wmfmixer $RPM_BUILD_ROOT%{_bindir}/wmfmixer
install wmfmixer.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/wmfmixer.xpm
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc HINTS
%attr(755,root,root) %{_bindir}/wmfmixer
%{_desktopdir}/docklets/wmfmixer.desktop
%{_pixmapsdir}/wmfmixer.xpm
