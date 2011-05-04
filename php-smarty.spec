# (oe) undefining these makes the build _real_ quick.
%undefine __find_provides
%undefine __find_requires

Summary:	The compiling PHP template engine
Name:		php-smarty
Version:	3.0.7
Release:	%mkrel 2
License:	LGPL
Group:		Development/Other
URL:		http://www.smarty.net/
Source0:	http://www.smarty.net/distributions/Smarty-%{version}.tar.gz
Source1:	http://www.smarty.net/files/docs/manual-en-3.0.zip
Source2:	smarty.gif
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Smarty is a template engine for PHP.  More specifically, it 
facilitates a manageable way to separate application logic and
content from its presentation.  This is best described in a
situation where the application programmer and the template 
designer play different roles, or in most cases are not the same
person.  For example, let's say you are creating a web page that
is displaying a newspaper article.  The article headline, tagline,
author and body are content elements, they contain no information
about how they will be presented.  They are passed into Smarty by
the application, then the template designer edits the templates
and uses a combination of HTML tags and template tags to format 
the presentation of these elements (HTML tables, background
colors, font sizes, style sheets, etc.) One day the programmer
needs to change the way the article content is retrieved (a change
in application logic.)  This change does not affect the template
designer, the content will still arrive in the template exactly
the same.  Likewise, if the template designer wants to completely
redesign the templates, this requires no changes to the
application logic.  Therefore, the programmer can make changes to
the application logic without the need to restructure templates,
and the template designer can make changes to templates without
breaking application logic. 

%package doc
Summary:	The HTML manual for Smarty
Group:		Development/Other
Obsoletes:  %{name}-manual

%description doc
The HTML manual for Smarty

%prep
%setup -q -n Smarty-%{version} -a1

%build

%install
%{__rm} -rf %{buildroot}

%{__mkdir_p} %{buildroot}%{_datadir}/php/smarty
%{__mkdir_p} %{buildroot}%{_var}/www/icons

%{__cp} -aRf libs/* %{buildroot}%{_datadir}/php/smarty
%{__install} -m0644 %{SOURCE2} %{buildroot}/var/www/icons/smarty.gif

# fix attribs
find %{buildroot}%{_datadir}/php/smarty -type d -exec chmod 755 {} \;
find %{buildroot}%{_datadir}/php/smarty -type f -exec chmod 644 {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING.lib README SMARTY2_BC_NOTES
%{_datadir}/php/smarty
%{_var}/www/icons/smarty.gif

%files doc
%defattr(-,root,root)
%doc manual-en/*
