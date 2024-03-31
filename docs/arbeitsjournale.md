# Arbeitsjournal; erster Eintrag
**Wann** 15.12 - 13.03
**Zeit:** rund 30h (in kleinen Einheiten)
**Was:** Coding

Ich habe am 15.12 das Github Repo eröfnet.
Im Moment ist der Code in der 1. Beta. Das Programm läuft, hatt aber noch einige Optimisierungen offen.

-----
Das Ziel meines Programm ist es das Man eine Datei so auslesen kann, wie sie auch gespeicher wurde.
Ich überlegte mir dann wie ich die Datei am besten innerhalb des Bild speicher kann.
Das Programm muss alle relevanten Informationen auslesen können. Zusätzlich ist die Länge der Datei nich definiert. Ich musste also ein Lösung finden,
wie man Name und Bytes und Länge der Datei speichern kann.
zusätzlich wollte ich einen SHA-256 hash einbauen, um die Validität der Daten zu überprüfen.
Auch ein Kritierium war es, dass das Programm mit verschieden anzahl an modifizierten LSB funktionieren kann. Ich musste also auch die anzahl an modidizierten LSB speichern.
Ich entschied mich dafür die anzahl LSB in den ersten 3 bits zu speichern. beim Auslesen muss man dann zuerst die ersten drei bits des ersten Pixel lesen und von dort an mit der herausgelesenen Zahl weiterfahren.
Danach kam der Hash. Dieser hat eine fixe Länge und kann in den nächsten 256 bits gespeicher werden.
Ein Problem, was ich angetroffen habe war der Dateiname. Dieser hat eine variable Länge. Das heisst ich müsste eine fixe anzahl bits für diesen alokieren. Dies war keine Option, weil ich den Speicherplatz optimal nutzen wollte.
Ich habe mich im Ende für ein Tag ansatz entschieden. Nach den 3LSB und 256 Hash bits kommt der Dateiname. Dann kommt ein Tag ("\[STEG]") und dann die Datei selber. 
Nach der Datei kommt wieder ein Tag. Mit diesem Ansatz ist es möglich, das der Name und Inhalt der Datei eine variable länge haben können.

Es kann auch sein, dass der User eine Datei wählt, die viel zu gross ist für die Bild Datei. Ich habe das Problem so gelöst, dass ich den Prozess durchlaufen lasse und am Ende überpfüfe,
ob die erstellten Bits länger sind als die Anzahl Pixel*LSB. Wenn das der Fall ist, wirft mein Programm einen Error.

Mein Programm ist nicht sehr schnell beim Auslesen, weil es die Ganze Bilddatei auslesen und alle LSB bits extrahieren muss. Das ist so, weil ich nicht, im vorhinein, weiss wie lange die Datei ist.
Ich habe mich aber dazu entschieden keien Grossen änderungen am Algorithmus zu machen, um Zeit zu spahren.

Ich hatte immer wieder kleinere Probleme beim Coden. So hatte ich zum beispiel das Problem, dass ich die Bits in der Flaschen Orientierung gelesen habe. Auch hatte ich ein Problem mit n_LSB Angaben, die nicht perfekt mit der Dateigrösse aufgingen.
Wenn eine Datei 11 Bits hat und ich in der Bilddatei 2 Bits ändere, dann habe ich ein Problem am ende, weil ich 1 Bit habe, aber 2 Bits schreiben muss.
Das Problem habe ich dann auch gelöst, indem ich einfach die offenen Bits mir Padding füllte.
