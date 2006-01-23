%include	/usr/lib/rpm/macros.php
%define		_class		Pager
%define		_pearname	%{_class}
%define		_status		stable

Summary:	%{_pearname} - generic data paging class
Summary(pl):	%{_pearname} - podstawowa klasa do dzielenia na strony
Name:		php-pear-%{_pearname}
Version:	2.3.5
Release:	1
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	1817dca95cc0b244407aa99ba74e8a0d
URL:		http://pear.php.net/package/Pager/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Obsoletes:	php-pear-Pager_Sliding
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
If you have data that needs paging (ie 1-10 on page one, 11-20 on page
two) this class can help. Pass it an array of data and it will sort it
into pages, picking up the current page id from the url. It can also
give you back/next and page number links taking the current url and
adding the correct page id to it.

In PEAR status of this package is: %{_status}.

%description -l pl
Ta klasa pomaga w sytuacji, kiedy dane wymagaj� podzia�u na strony
(np. pozycje 1-10 na pierwszej stronie, 11-20 na drugiej itd.). Po
przekazaniu tablicy danych klasa dzieli na strony, pobieraj�c
identyfikator strony z URL-a. Mo�e tak�e poda� odno�niki do
poprzedniej i nast�pnej strony, bior�c aktualny URL i dodaj�c do niego
w�a�ciwe identyfikatory stron.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

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
%doc install.log
%doc docs/%{_pearname}/*
%dir %{php_pear_dir}/%{_class}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
