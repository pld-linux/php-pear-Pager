%include	/usr/lib/rpm/macros.php
%define		_class		Pager
%define		_pearname	%{_class}
%define		_status		stable

Summary:	%{_pearname} - generic data paging class
Summary(pl):	%{_pearname} - podstawowa klasa do dzielenia na strony
Name:		php-pear-%{_pearname}
Version:	2.2.3
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	7ea719dcd47f62d1b7c80232f61a6e98
URL:		http://pear.php.net/package/Pager/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
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
%doc %{_pearname}-%{version}/{examples,tests}
%dir %{php_pear_dir}/%{_class}
%{php_pear_dir}/%{_class}/*.php
