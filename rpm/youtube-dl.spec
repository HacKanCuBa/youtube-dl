# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       youtube-dl

# >> macros
# << macros

Summary:    YouTube video downloader
Version:    2020.09.20
Release:    1.0nep
Group:      Applications/Multimedia
License:    Unlicense
URL:        https://github.com/ytdl-org/youtube-dl
Source100:  youtube-dl.yaml

%description
Command-line program to download videos from YouTube.com and other video sites

%prep
# >> setup
sed -i "s/__version__ = '.*'/__version__ = '%{version}-%{release}'/" youtube_dl/version.py
# << setup

%build
# >> build pre
%{__make} youtube-dl
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
%{__install} -m 755 youtube-dl $RPM_BUILD_ROOT%{_bindir}/youtube-dl
# << install pre

# >> install post
#python3 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
# << install post

%files
%defattr(-,root,root,-)
%{_bindir}/youtube-dl
# >> files
# << files

