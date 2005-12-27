Summary:	Epeg JPEG scaler for Ruby
Summary(pl):	Epeg - biblioteka do skalowania JPEG-ów dla jêzyka Ruby
Name:		ruby-epeg
Version:	0.0.2
Release:	2
License:	Ruby License
Group:		Development/Languages
Source0:	http://theinternetco.net/projects/ruby/%{name}-%{version}.tar.gz
# Source0-md5:	245cf3d7f60b9162091296961ec3f421
URL:		http://theinternetco.net/projects/ruby/ruby-epeg
BuildRequires:	epeg-devel
BuildRequires:	rpmbuild(macros) >= 1.263
BuildRequires:	ruby-devel
Requires:	ruby-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ruby-epeg is an extension to use the fast E17 epeg JPEG scaler.

%description -l pl
ruby-epeg to rozszerzenie do u¿ywania epega - szybkiej biblioteki do
skalowania JPEG-ów z E17.

%prep
%setup -q

%build
ruby extconf.rb
%{__make}
rdoc --op rdoc *.c
rdoc --ri --op ri *.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

%{__make} install \
	archdir=$RPM_BUILD_ROOT%{ruby_archdir} \
	sitearchdir=$RPM_BUILD_ROOT%{ruby_archdir}

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%{ruby_archdir}/*
%{ruby_ridir}/Epeg
