%include	/usr/lib/rpm/macros.php
%define		_class		Pager
%define		_pearname	%{_class}
%define		_status		stable

Summary:	%{_pearname} - generic data paging class
Summary(pl):	%{_pearname} - podstawowa klasa do dzielenia na strony
Name:		php-pear-%{_pearname}
Version:	2.2.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	5e04d27d4f435497ebad2b4db9214759
URL:		http://pear.php.net/package/Pager/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
If you have data that needs paging (ie 1-10 on page one, 11-20 on page
two) this class can help. Pass it an array of data and it will sort it
into pages, picking up the current page id from the url. It can also
give you back/next and page number links taking the current url and
adding the correct page id to it.

This class has in PEAR status: %{_status}.

%description -l pl
Ta klasa pomaga w sytuacji, kiedy dane wymagaj± podzia³u na strony
(np. pozycje 1-10 na pierwszej stronie, 11-20 na drugiej itd.). Po
przekazaniu tablicy danych klasa dzieli na strony, pobieraj±c
identyfikator strony z URL-a. Mo¿e tak¿e podaæ odno¶niki do
poprzedniej i nastêpnej strony, bior±c aktualny URL i dodaj±c do niego
w³a¶ciwe identyfikatory stron.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{php_pear_dir}/%{_class}
%doc %{_pearname}-%{version}/{examples,tests}
%{php_pear_dir}/%{_class}/*.php
