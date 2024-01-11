Name:           sushi
Version:        3.28.3
Release:        1%{?dist}
Summary:        A quick previewer for Nautilus

License:        GPLv2+ with exceptions
URL:            https://wiki.gnome.org/ThreePointOne/Features/FilePreviewing
Source0:        https://download.gnome.org/sources/%{name}/3.28/%{name}-%{version}.tar.xz

BuildRequires:  intltool
BuildRequires:  gjs-devel
BuildRequires:  pkgconfig(clutter-gst-3.0)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(clutter-x11-1.0)
BuildRequires:  pkgconfig(evince-document-3.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-3.0)
BuildRequires:  pkgconfig(libmusicbrainz5)
BuildRequires:  pkgconfig(webkit2gtk-4.0)

Obsoletes:      sushi-devel < 0.5.1

#Description from upstream's README.
%description
This is sushi, a quick previewer for Nautilus, the GNOME desktop
file manager.


%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}


%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%find_lang %{name}


%files -f %{name}.lang
%doc README AUTHORS NEWS TODO
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/dbus-1/services/*
%{_libexecdir}/*
%{_libdir}/sushi/


%changelog
* Mon Apr 23 2018 Kalev Lember <klember@redhat.com> - 3.28.3-1
- Update to 3.28.3

* Fri Apr 20 2018 Kalev Lember <klember@redhat.com> - 3.28.2-1
- Update to 3.28.2

* Thu Apr 19 2018 Kalev Lember <klember@redhat.com> - 3.28.1-1
- Update to 3.28.1

* Thu Apr 19 2018 Kalev Lember <klember@redhat.com> - 3.28.0-1
- Update to 3.28.0
- Drop ldconfig scriptlets

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 09 2017 Kalev Lember <klember@redhat.com> - 3.24.0-1
- Update to 3.24.0

* Mon Mar 06 2017 Kalev Lember <klember@redhat.com> - 3.23.91-1
- Update to 3.23.91

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.21.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Sep 02 2016 Kalev Lember <klember@redhat.com> - 3.21.91-1
- Update to 3.21.91
- Don't set group tags
- Update the project URL

* Tue May 17 2016 Kalev Lember <klember@redhat.com> - 3.20.0-1
- Update to 3.20.0

* Fri Mar 04 2016 Kalev Lember <klember@redhat.com> - 3.19.90-1
- Update to 3.19.90

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 22 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0
- Use make_install macro

* Mon Jul 27 2015 David King <amigadave@amigadave.com> - 3.17.4-1
- Update to 3.17.4

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 13 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0

* Fri Mar 13 2015 David King <amigadave@amigadave.com> - 3.15.90-2
- Fix GSettings scriptlet

* Tue Mar 10 2015 David King <amigadave@amigadave.com> - 3.15.90-1
- Update to 3.15.90
- Use license macro for COPYING
- Use pkgconfig for BuildRequires
- Compile GSettings schemas

* Thu Nov 27 2014 Haikel Guémar <hguemar@fedoraproject.org> - 3.12.0-5
- Rebuilt against newer libmusicbrainz5

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.0-3
- Rebuilt for gobject-introspection 1.41.4

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 28 2014 Richard Hughes <rhughes@redhat.com> - 3.12.0-1
- Update to 3.12.0

* Thu Feb 20 2014 Kalev Lember <kalevlember@gmail.com> - 3.11.90-2
- Rebuilt for cogl soname bump

* Thu Feb 20 2014 Richard Hughes <rhughes@redhat.com> - 3.11.90-1
- Update to 3.11.90

* Mon Feb 10 2014 Peter Hutterer <peter.hutterer@redhat.com> - 3.10.0-3
- Rebuild for libevdev soname bump

* Wed Feb 05 2014 Kalev Lember <kalevlember@gmail.com> - 3.10.0-2
- Rebuilt for cogl soname bump

* Wed Sep 25 2013 Kalev Lember <kalevlember@gmail.com> - 3.10.0-1
- Update to 3.10.0

* Fri Aug 09 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.1-3
- Rebuilt for cogl 1.15.4 soname bump

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 16 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.1-1
- Update to 3.8.1

* Mon Mar 25 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.0-1
- Update to 3.8.0

* Tue Mar  5 2013 Matthias Clasen <mclasen@redhat.com> - 3.7.91-1
- Update to 3.7.91

* Thu Feb 21 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.5-2
- Rebuilt for cogl soname bump

* Thu Feb 07 2013 Richard Hughes <rhughes@redhat.com> - 3.7.5-1
- Update to 3.7.5

* Fri Jan 25 2013 Peter Robinson <pbrobinson@fedoraproject.org> 3.7.4-2
- Rebuild for new cogl

* Wed Jan 16 2013 Richard Hughes <hughsient@gmail.com> - 3.7.4-1
- Update to 3.7.4

* Fri Dec 21 2012 Kalev Lember <kalevlember@gmail.com> - 3.7.3-1
- Update to 3.7.3

* Tue Nov 13 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.1-1
- Update to 3.6.1

* Wed Sep 26 2012 Matthias Clasen <mclasen@redhat.com> - 3.6.0-1
- Update to 3.6.0

* Wed Sep 19 2012 Kalev Lember <kalevlember@gmail.com> - 3.5.92-1
- Update to 3.5.92

* Thu Aug 30 2012 Bastien Nocera <bnocera@redhat.com> 3.5.90-1
- Update to 3.5.90
- Port to libmusicbrainz5

* Tue Aug 28 2012 Matthias Clasen <mclasen@redhat.com> - 0.5.5-2
- Rebuild against new cogl/clutter

* Wed Aug 22 2012 Richard Hughes <hughsient@gmail.com> - 0.5.5-1
- Update to 0.5.5

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 17 2012 Richard Hughes <hughsient@gmail.com> - 0.5.4-1
- Update to 0.5.4

* Thu Jun 07 2012 Richard Hughes <hughsient@gmail.com> - 0.5.2-1
- Update to 0.5.2

* Sat May 05 2012 Kalev Lember <kalevlember@gmail.com> - 0.5.1-1
- Update to 0.5.1
- Build with libmusicbrainz4
- Adjust the spec file for the changes in private library location
- Remove and obsolete the -devel subpackage

* Tue Apr 17 2012 Kalev Lember <kalevlember@gmail.com> - 0.4.1-1
- Update to 0.4.1

* Tue Mar 27 2012 Matthias Clasen <mclasen@redhat.com> - 0.4.0-1
- Update to 0.4.0

* Wed Mar 21 2012 Kalev Lember <kalevlember@gmail.com> - 0.3.92-2
- Rebuild for libevdocument3 soname bump

* Wed Mar 21 2012 Kalev Lember <kalevlember@gmail.com> - 0.3.92-1
- Update to 0.3.92

* Sat Mar 10 2012 Matthias Clasen <mclasen@redhat.com> - 0.3.91-3
- Rebuild against newer cogl

* Tue Mar  6 2012 Matthias Clasen <mclasen@redhat.com> - 0.3.91-2
- Rebuild against newer cogl

* Mon Mar  5 2012 Matthias Clasen <mclasen@redhat.com> - 0.3.91-1
- Update to 0.3.91

* Sun Feb 26 2012 Matthias Clasen <mclasen@redhat.com> - 0.3.0-4
- Rebuild against new cogl

* Thu Jan 19 2012 Matthias Clasen <mclasen@redhat.com> - 0.3.0-3
- Rebuild against new cogl

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 20 2011 Matthias Clasen <mclasen@redhat.com> - 0.3.0-1
- Update to 0.3.0

* Thu Nov 24 2011 Matthias Clasen <mclasen@redhat.com> - 0.2.1-3
- Rebuild against new clutter

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-2
- Rebuilt for glibc bug#747377

* Tue Oct 18 2011 Matthias Clasen <mclasen@redhat.com> - 0.2.1-1
- Update to 0.2.1

* Tue Sep 27 2011 Ray <rstrode@redhat.com> - 0.2.0-1
- Update to 0.2.0

* Tue Sep 20 2011 Matthias Clasen <mclasen@redhat.com> - 0.1.92-2
- Rebuild against newer clutter

* Tue Sep 20 2011 Elad Alfassa <elad@fedoraproject.org> - 0.1.92-1
- New upstream release

* Tue Aug 30 2011 Elad Alfassa <elad@fedoraproject.org> - 0.1.90-1
- New upstream version

* Tue Jul 26 2011 Matthias Clasen <mclasen@redhat.com> - 0.0.5-1
- Update to 0.0.5

* Sat Jul 09 2011 Elad Alfassa <elad@fedoraproject.org> - 0.0.4-1
- Update to latest upstream version.

* Mon Jul 04 2011 Elad Alfassa <elad@fedoraproject.org> - 0.0.3-3
- Fix issues from review

* Sun Jul 03 2011 Elad Alfassa <elad@fedoraproject.org> - 0.0.3-2
- Added AUTHORS NEWS and TODO to doc

* Sat Jul 02 2011 Elad Alfassa <elad@fedoraproject.org> - 0.0.3-1
- Initial build

