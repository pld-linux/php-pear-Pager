%define		pearname	Pager
%define		status		stable
Summary:	%{pearname} - generic data paging class
Summary(pl.UTF-8):	%{pearname} - podstawowa klasa do dzielenia na strony
Name:		php-pear-%{pearname}
Version:	2.5.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	ceb5033548fe0520773bfe6f22e24886
URL:		http://pear.php.net/package/Pager/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.654
Requires:	php-pear
Obsoletes:	php-pear-Pager-tests
Obsoletes:	php-pear-Pager_Sliding
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
If you have data that needs paging (ie 1-10 on page one, 11-20 on page
two) this class can help. Pass it an array of data and it will sort it
into pages, picking up the current page id from the url. It can also
give you back/next and page number links taking the current url and
adding the correct page id to it.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Ta klasa pomaga w sytuacji, kiedy dane wymagają podziału na strony
(np. pozycje 1-10 na pierwszej stronie, 11-20 na drugiej itd.). Po
przekazaniu tablicy danych klasa dzieli na strony, pobierając
identyfikator strony z URL-a. Może także podać odnośniki do
poprzedniej i następnej strony, biorąc aktualny URL i dodając do niego
właściwe identyfikatory stron.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/%{pearname}/*
%{php_pear_dir}/Pager
%{php_pear_dir}/Pager.php
%{php_pear_dir}/.registry/*.reg
