%include	/usr/lib/rpm/macros.php
%define         _class          HTML
%define         _subclass       QuickForm_Controller
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - add-on to HTML_QuickForm that allows building of multiple forms 
Summary(pl):	%{_pearname} - dodatek do HTML_QuickForm umożliwiający budowanie wielu formularzy
Name:		php-pear-%{_pearname}
Version:	0.9.3
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	b37445dddc88b169a1d3b3641418d396
URL:		http://pear.php.net/package/HTML_QuickForm_Controller/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package is essentially an implementation of a PageController
pattern. 

Architecture:
- Controller class that examines HTTP requests and manages form values
  persistance across requests.
- Page class (subclass of QuickForm) representing a single page of the
  form.
- Business logic is contained in subclasses of Action class.

Cool features:
- Includes several default actions that allows easy building of
  multipage forms.
- Includes usage examples for common usage cases (single-page form,
  wizard tabbed form).

This class has in PEAR status: %{_status}.

%description -l pl
Ten pakiet jest implementacją szablonu PageController.

Architektura:
- Klasa Controller badająca zapytania HTTP i zarządzająca wartościami
  formularza pomiędzy kolejnymi zapytaniami.
- Klasa Page (podklasa QuickForm) reprezentująca pojedynczą stronę
  formularza.
- Logika biznesowa zawarta jest w podklasach klasy Action.

Ciekawe cechy:
- Zawiera kilka domyślnych akcji pozwalających na łatwe budowanie
  formularzy rozbitych na kilka stron.
- Zawiera gotowe przykłady najczęściej spotykanych zastosowań.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Action

install %{_pearname}-%{version}/*.php 		$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/Action/*.php 	$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Action

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/examples
%{php_pear_dir}/%{_class}/*
