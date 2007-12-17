# (oe) undefining these makes the build _real_ quick.
%undefine __find_provides
%undefine __find_requires

Summary:        Smarty - the compiling PHP template engine
Name:           php-smarty
Version:        2.6.18
Release:        %mkrel 1
License:        LGPL
Group:          Development/Other
URL:            http://smarty.php.net/
Source0:        http://smarty.php.net/distributions/Smarty-%{version}.tar.gz
Source1:        http://smarty.php.net/distributions/manual/en/Smarty-2.6.14-docs.tar.gz
# XXX - some bug in the php-pear find-requires stuff
# makes a kolab package require this provides below
Provides:       pear(Smarty.class.php)
BuildArch:      noarch

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

%package        manual
Summary:        The HTML manual for Smarty
Group:          Development/Other

%description        manual
The HTML manual for Smarty

%prep

%setup -q -n Smarty-%{version} -a1

# clean up CVS stuff
for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then %{__rm} -r $i; fi >&/dev/null
done

# fix dir perms
find . -type d | xargs chmod 755

# fix file perms
find . -type f | xargs chmod 644

%build

%install
%{__rm} -rf %{buildroot}

%{__mkdir_p} %{buildroot}%{_datadir}/smarty
%{__mkdir_p} %{buildroot}%{_var}/www/icons

%{__cp} -aRf libs/* %{buildroot}%{_datadir}/smarty/
%{__install} -m0644 misc/smarty_icon.gif %{buildroot}/var/www/icons/smarty.gif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc BUGS COPYING.lib ChangeLog FAQ INSTALL NEWS README RELEASE_NOTES TODO
%{_datadir}/smarty
%{_var}/www/icons/smarty.gif

%files manual
%defattr(-,root,root)
%doc manual/*


