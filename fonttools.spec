Name:           fonttools
Version:        2.4
Release:        1%{?dist}
Summary:        A tool to convert True/OpenType fonts to XML and back

Group:          Development/Tools
License:        BSD
URL:            http://sourceforge.net/projects/%{name}/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  python2-devel numpy
Requires:       numpy

Provides:       ttx = %{version}-%{release}

%description
TTX/FontTools is a tool for manipulating TrueType and OpenType fonts. It is
written in Python and has a BSD-style, open-source license. TTX can dump
TrueType and OpenType fonts to an XML-based text format and vice versa.


%prep
%setup -q

%build
%{__python} setup.py build


%install
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{python_sitearch}/FontTools/fontTools/ttLib/test
chmod 0755 $RPM_BUILD_ROOT%{python_sitearch}/FontTools/fontTools/misc/eexecOp.so


%files
%doc LICENSE.txt
%doc Doc/ChangeLog Doc/changes.txt Doc/documentation.html
%{python_sitearch}/FontTools.pth
%dir %{python_sitearch}/FontTools
%dir %{python_sitearch}/FontTools/fontTools
%dir %{python_sitearch}/FontTools/fontTools/encodings
%dir %{python_sitearch}/FontTools/fontTools/misc
%dir %{python_sitearch}/FontTools/fontTools/pens
%dir %{python_sitearch}/FontTools/fontTools/ttLib
%dir %{python_sitearch}/FontTools/fontTools/ttLib/tables
%{python_sitearch}/FontTools/*.py*
%{python_sitearch}/FontTools/fontTools/*.py*
%{python_sitearch}/FontTools/fontTools/*/*.py*
%{python_sitearch}/FontTools/fontTools/*/*/*.py*
%{python_sitearch}/FontTools/fontTools/misc/eexecOp.so
%{python_sitearch}/FontTools/fonttools-%{version}-py?.?.egg-info
%{_bindir}/ttx
%{_mandir}/man1/ttx.1.gz



%changelog
* Mon Jun 24 2013 Parag <pnemade AT redhat DOT com> - 2.4-1
- New upstream release 2.4

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 29 2012 Parag <pnemade AT redhat DOT com> - 2.3-6
- Resolves:rh#880063 - BR: python2-devel required

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 19 2010 Akira TAGOH <tagoh@redhat.com> - 2.3-2
- Rebuild.

* Fri Jul 23 2010 Akira TAGOH <tagoh@redhat.com> - 2.3-1
- New upstream release. (Paul Williams, #599281)
  - drop upstreamed patch.
  - correct man page location.
- Update the spec file to keep consistensy of usage in the macro as far as possible.

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Oct 02 2009 Caolán McNamara <caolanm@redhat.com> - 2.2-7
* Resolves: rhbz#525444 as is a reserved keyword in python

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Roozbeh Pournader <roozbeh@gmail.com> - 2.2-5
* Change dependency on python-numeric to numpy

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.2-3
- Fix locations for Python 2.6

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.2-2
- Rebuild for Python 2.6

* Tue Sep 16 2008 Matt Domsch <mdomsch@fedoraproject.org> - 2.2-1
- update to 2.2, drop upstreamed patch, fix FTBFS BZ#434409

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.0-0.12.20060223cvs
- Autorebuild for GCC 4.3

* Sat Dec 09 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 2.0-0.11.20060223cvs
- Rebuild for Python 2.5

* Fri Dec 01 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 2.0-0.10.20060223cvs
- Update the Unicode names file to Unicode 5.0.0

* Thu Nov 09 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 2.0-0.9.20060223cvs
- Update to newer CVS snapshot dated 2006-02-23
- Cleanup based on latest Python packaging guidelines

* Wed Nov 08 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 2.0-0.8.20050624cvs
- De-ghost .pyo files

* Wed Nov 08 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 2.0-0.7.20050624cvs
- Rebuild to get into Rawhide

* Mon May 08 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 2.0-0.6.20050624cvs
- Change specification of ulUnicodeRange1-4 to unsigned long

* Mon Feb 13 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 2.0-0.5.20050624cvs
- Rebuild for Fedora Extras 5

* Thu Feb 02 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 2.0-0.4.20050624cvs
- Provide ttx

* Wed Feb 01 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 2.0-0.3.20050624cvs
- Use upstream snapshots, moving the difference into a patch
- Change alphatag time to the latest change in CVS
- Use %%{python_sitearch} instead of %%{python_sitelib} (for x86_86)
- Use sed instead of a patch to remove shebang

* Sun Jan 08 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 2.0-0.2.20060103cvs
- Add %%{?dist} tag

* Fri Jan 06 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 2.0-0.1.20060103cvs
- Initial packaging
