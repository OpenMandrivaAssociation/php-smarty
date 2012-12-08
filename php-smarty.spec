# (oe) undefining these makes the build _real_ quick.
%undefine __find_provides
%undefine __find_requires

Summary:	The compiling PHP template engine
Name:		php-smarty
Version:	3.1.10
Release:	1
License:	LGPL
Group:		Development/Other
URL:		http://www.smarty.net/
Source0:	http://www.smarty.net/files/Smarty-%{version}.tar.gz
Source1:	http://www.smarty.net/files/docs/manual-en-3.1.8.zip
Source2:	smarty.gif
BuildArch:	noarch
Buildrequires:	unzip

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

install -d %{buildroot}%{_datadir}/php/smarty
install -d %{buildroot}%{_var}/www/icons

cp -rp libs/* %{buildroot}%{_datadir}/php/smarty
install -m0644 %{SOURCE2} %{buildroot}/var/www/icons/smarty.gif

# fix attribs
find %{buildroot}%{_datadir}/php/smarty -type d -exec chmod 755 {} \;
find %{buildroot}%{_datadir}/php/smarty -type f -exec chmod 644 {} \;

%files
%doc COPYING.lib README *.txt
%{_datadir}/php/smarty
%{_var}/www/icons/smarty.gif

%files doc
%doc manual-en/*


%changelog
* Wed Jun 20 2012 Oden Eriksson <oeriksson@mandriva.com> 3.1.10-1
+ Revision: 806460
- weird build problems here...
- various fixes
- heh...
- 3.1.10

* Tue Apr 10 2012 Oden Eriksson <oeriksson@mandriva.com> 3.1.8-1
+ Revision: 790123
- 3.1.8

* Tue Nov 15 2011 Oden Eriksson <oeriksson@mandriva.com> 3.1.5-1
+ Revision: 730706
- 3.1.5

* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 3.0.7-2
+ Revision: 667713
- mass rebuild

* Mon Feb 14 2011 Oden Eriksson <oeriksson@mandriva.com> 3.0.7-1
+ Revision: 637723
- 3.0.7

* Sat Jan 08 2011 Oden Eriksson <oeriksson@mandriva.com> 3.0.6-1mdv2011.0
+ Revision: 630297
- 3.0.6

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 3.0.5-1mdv2011.0
+ Revision: 614803
- 3.0.5

* Sun Oct 24 2010 Oden Eriksson <oeriksson@mandriva.com> 2.6.26-3mdv2011.0
+ Revision: 588720
- rebuild

* Sun Feb 21 2010 Oden Eriksson <oeriksson@mandriva.com> 2.6.26-2mdv2010.1
+ Revision: 509090
- rebuild

* Sat Sep 12 2009 Oden Eriksson <oeriksson@mandriva.com> 2.6.26-1mdv2010.0
+ Revision: 438565
- 2.6.26

* Mon Jul 20 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.6.25-4mdv2010.0
+ Revision: 398205
- install files under %%{_datadir}/php, as other non-pear php libraries
- rename documentation package to %%{name}-doc
- don't provide wrong pear dependencies: fix faulty packages instead

* Sun Jul 19 2009 Raphaël Gertz <rapsys@mandriva.org> 2.6.25-3mdv2010.0
+ Revision: 397598
- Rebuild

* Sun Jul 19 2009 Raphaël Gertz <rapsys@mandriva.org> 2.6.25-2mdv2010.0
+ Revision: 397286
- Rebuild

* Sun May 24 2009 Frederik Himpe <fhimpe@mandriva.org> 2.6.25-1mdv2010.0
+ Revision: 379237
- update to new version 2.6.25

* Sun May 17 2009 Frederik Himpe <fhimpe@mandriva.org> 2.6.24-1mdv2010.0
+ Revision: 376671
- update to new version 2.6.24

* Thu May 14 2009 Frederik Himpe <fhimpe@mandriva.org> 2.6.23-1mdv2010.0
+ Revision: 375763
- Update to new version 2.6.23
- Add smarty icon as a source, it's not included in the upstream tarball
  anymore

* Tue Jan 13 2009 Oden Eriksson <oeriksson@mandriva.com> 2.6.22-1mdv2009.1
+ Revision: 329196
- 2.6.22

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 2.6.20-4mdv2009.1
+ Revision: 321948
- rebuild

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 2.6.20-3mdv2009.1
+ Revision: 321696
- rebuild

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 2.6.20-2mdv2009.1
+ Revision: 321695
- rebuild

* Sat Aug 16 2008 Oden Eriksson <oeriksson@mandriva.com> 2.6.20-1mdv2009.0
+ Revision: 272566
- fix url
- 2.6.20

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 2.6.19-2mdv2009.0
+ Revision: 265469
- rebuild early 2009.0 package (before pixel changes)

* Fri May 02 2008 Oden Eriksson <oeriksson@mandriva.com> 2.6.19-1mdv2009.0
+ Revision: 200102
- 2.6.19

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 2.6.18-2mdv2008.1
+ Revision: 178576
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Apr 18 2007 Oden Eriksson <oeriksson@mandriva.com> 2.6.18-1mdv2008.0
+ Revision: 14587
- 2.6.18


* Wed Mar 07 2007 Oden Eriksson <oeriksson@mandriva.com> 2.6.17-1mdv2007.0
+ Revision: 134268
- 2.6.17

* Fri Dec 15 2006 David Walluck <walluck@mandriva.org> 2.6.16-1mdv2007.1
+ Revision: 97228
- 2.6.16

* Thu Nov 02 2006 Oden Eriksson <oeriksson@mandriva.com> 2.6.14-1mdv2007.1
+ Revision: 75347
- Import php-smarty

* Fri Jul 07 2006 Oden Eriksson <oeriksson@mandriva.com> 2.6.14-1mdk
- 2.6.14

* Tue Apr 25 2006 Oden Eriksson <oeriksson@mandriva.com> 2.6.13-1mdk
- 2.6.13

* Sat Jan 07 2006 Oden Eriksson <oeriksson@mandriva.com> 2.6.11-1mdk
- 2.6.11

* Fri Aug 12 2005 Andreas Hasenack <andreas@mandriva.com> 2.6.6-3mdk
- added fake provides for pear(Smarty.class.php)

* Sat May 21 2005 Oden Eriksson <oeriksson@mandriva.com> 2.6.6-2mdk
- relocate to %%{_datadir}

* Sat Nov 27 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.6.6-1mdk
- initial mandrake package

