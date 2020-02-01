%define prefix /usr
%define __jar_repack %{nil}

Name:		jskat
Version:	0.17.0
Release:	3%{?dist}
License:	GPLv3
Group:		Games/Cards
URL:		https://github.com/b0n541/jskat-multimodule/releases
Source0:	%{name}-%{version}.tar
Source1:	jskat.png
Summary:	An implementation of the German card game Skat in Java
Summary(de):	Eine Implementierung des deutschen Kartenspiels Skat in Java
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildArch:	noarch
Requires:	java-11-openjdk
Obsoletes:	%name < %version

%description
JSkat application is a free implementation of the German card game Skat in Java. 
You can play it on nearly every platform that runs a modern Java Runtime Environment.

Until now we only know that it runs on Windows and Linux with the JRE from Sun, 
but we like to hear from you, if it's playable on other platforms, too.

JSkat is written by Jan Schäfer and Markus J. Luzius. It's a non profit project 
that steals a lot of our spare time. Our goal is to develop a free computer Skat 
game that can play either according to the official rules or with a customized 
special ruleset that is often played in the pubs.

JSkat is copyrighted under the General Public License (GPL) 2.0.
Here are some key features of "JSkat":

· Playing according to the official rules of the International Skat Players 
Association (ISPA-World)
· Play suit, grand and null games.
· Games are passed in if no player bids.
· Playing pub rules like Kontra, Ramsch and Bock (planned)
· Calculation of wins and losses after each game
· Saving data in XML (planned)
· Multilanguage support
· Currently we support German and English.
· If you want to contribute a translation, please contact us.
· Creation and integration of your own AI Skat player (planned)
For the time being, there are three AI Skat players available for JSkat:
· AIPlayerMJL
· A player with careful bidding, a basic opponent intelligence and currently no 
single player AI.
· AIPlayerJS
· A player that doesn't do bidding very well and that's why it's losing most of 
the time.
· AIPlayerRND
· A random player only for testing and driving the other players nuts. ;o)
· We'll release an interface definition that will allow you to create and integrate 
your own AI player into JSkat. (planned)
· Cheat/Debug mode
· Look into the cards of the other skat players.
· Go through all tricks that were played.
· Watch three AI players against themselves.

#german
%description -l de
Sie können es auf fast allen Plattformen nutzen, auf denen eine moderne Version 
des Java Runtime Environment läuft. Wir wissen, dass es unter Windows, Linux und 
Mac OS mit dem JRE von Oracle funktioniert. Wir würden aber gerne erfahren, falls 
JSkat auch unter anderen Plattformen läuft.

Wer steckt hinter JSkat
JSkat wird von Jan Schäfer und Markus J. Luzius entwickelt. Es ist ein
nichtkommerzielles Projekt, dass sehr viel von unserer Freizeit stiehlt. 
Unser Ziel ist es, ein freies Computer-Skatspiel zu schaffen, mit dem man 
entweder nach den offiziellen Skatregeln oder nach Kneipenregeln spielen kann.

Funktionen

Die folgenden Funktionen sind implementiert oder werden in einer zukünftigen 
Version von JSkat umgesetzt:

Skatregeln
*Spielen nach den offiziellen Regeln der International Skat Players Association 
(ISPA-World)
*Spielen von Farb-, Grand- und Nullspielen
*Spiele werden eingepasst, wenn kein Spieler ein Reizgebot abgibt
*Spielen nach Kneipenregeln wie Kontra, Ramsch und Bock (geplant)
*Berechnung der Gewinne und Verluste nach jedem Spiel

KI-Skatspieler
Zurzeit gibt es drei KI-Spieler für JSkat:
*Algorithmisch
 Ein Spieler mit vorsichtigem Reizverhalten, einfacher Intelligenz für 
 Gegenspieler und Alleinspieler.
*Neuronales Netz
 Ein Spieler der neuronale Netze zur Berechnung der Spielstrategie benutzt.
*Rainer Zufall
 Ein Zufallsspieler der zum Testen von JSkat verwendet wird und die Spieler zum Wahnsinn treibt.

Es gibt eine Schnittstelle für die KI-Spieler. Wenn Sie einen eigenen KI-Spieler
entwickeln möchten, muss nur diese Schnittstelle, damit Ihr Spieler in JSkat 
integriert werden kann. Es würde uns freuen, wenn wir neue Entwickler in unserem 
Team willkommen heißen können.

Cheat- und Debug-Modus
*Schauen Sie in die Karten der anderen Skatspieler
*Gehen Sie alle Stiche eines Spiels nach Spielende noch einmal durch
*Beobachten Sie drei KI-Spieler, wie sie gegeneinander spielen

Andere Funktionen
*Speichern der Daten als XML-Dateien (geplant)
*Unterstützung für verschiedene Sprachen
 Zurzeit unterstützen wir Deutsch und Englisch. Wenn Sie eine Übersetzung 
 beisteuern möchten, kontaktieren Sie uns bitte.

%prep

%setup -q -n %{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p %{buildroot}%{_datadir}/%{name}
cp -v %{name}-linux-%{version}.jar %{buildroot}%{_datadir}/%{name}
chmod 0755 %{buildroot}%{_datadir}/%{name}/%{name}-linux-%{version}.jar

install -d -m 0755 %buildroot%_datadir/pixmaps
install -m 0644 %SOURCE1 %buildroot%_datadir/pixmaps/jskat.png

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Exec=/usr/lib/jvm/jre-11/bin/java -jar %{_datadir}/%{name}/%{name}-linux-%{version}.jar
Icon=jskat.png
Type=Application
Terminal=false
Name=JSkat
GenericName=JSkat
Comment=An implementation of the German card game Skat in Java
Comment[de]=Eine Implementierung des deutschen Kartenspiels Skat in Java
StartupNotify=false
Categories=X-MandrivaLinux-MoreApplications-Games-Cards;
EOF


%files
%defattr(-,root,root)
%{_datadir}/%{name}/%{name}-linux-%{version}.jar
%{_datadir}/pixmaps/jskat.png
%{_datadir}/applications/%{name}.desktop

%clean
rm -rf %{buildroot}
rm -rf $RPM_BUILD_DIR/%{name}-%{version}

%changelog
* Sat Feb 01 2020 maggu2810 <maggu2810 at gmail dot com> 0.17.0-3
- new version

* Sun Mar 05 2017 bb2 <bb2> 0.16.0-1pclos2017
- new version

* Fri Apr 10 2015 ghostbunny <ghostbunny at gmx dot de> 0.14.4-1pclos2015
- 0.14.4

* Sat Oct 11 2014 ghostbunny <ghostbunny at gmx dot de> 0.14.2-1pclos2014
- 0.14.2

* Sun Nov 03 2013 ghostbunny <ghostbunny at gmx dot de> 0.13.0-1pclos2013
- 0.13.0

* Fri May 10 2013 ghostbunny <ghostbunny at gmx dot de> 0.12.1-1pclos2013
- 0.12.1

* Thu Aug 30 2012 Neal <nealbrks0 at gmail dot com> 0.11.0-1pclos2012
- process

* Thu Aug 30 2012 ghostbunny <ghostbunny at gmx dot de> 0.11.0-1pclos2012
- 0.11.0
- added BuildArch: noarch

* Fri Mar 30 2012 Neal <nealbrks0 at gmail.com> 0.10.1-1pclos2012
- process

* Thu Mar 29 2012 leiche <meisssw01 at gmail.com> 0.10.1-1leiche2012
- 0.10.1

* Sat Oct 15 2011 leiche <meisssw01 at gmail.com> 0.9.0-1leiche2011
- Initial package
