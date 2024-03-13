# Arbeitsjournal; erster Eintrag
**Wann** 15.12 - 13.03
**Zeit:** rund 30h (in kleinen Einheiten)
**Was:** Coding

Ich habe am 15.12 das Github Repo eröfnet.
Im Moment ist der Code in der 1. Beta. Das Programm läuft, hatt aber noch einige Optimisierungen offen.

-----
Das Ziel meines Programm ist es das Man eine Datei so auslesen kann, wie sie auch gespeicher wurde.
Ich überlegte mir dann wie ich die Datei am besten innerhalb der Datei speicher kann.
Das Programm muss alle relevanten Informationen auslesen können. Zusätzlich ist die Länge der Datei nich definiert. Ich musste also ein Lösung finden,
wie man Name und Bytes und Länge der Datei speichern kann.
zusätzlich wollte ich einen SHA-256 hash einbauen, um die Validität der Daten zu überprüfen.
Auch ein Kritierium war es, dass das Programm mit verschieden anzahl an modifizierten LSB funktionieren kann. Ich musste also auch die anzahl an modidizierten LSB speichern.
Ich entschied mich dafür die anzahl LSB in den ersten 3 bits zu speichern. beim Auslesen muss man dann zuerst die ersten drei bits des ersten Pixel lesen und von dort an mit der herausgelesenen Zahl weiterfahren.
Danach kam der Hash. Dieser hat eine fixe Länge und kann in den nächsten 256 bits gespeicher werden.
Ein Problem, was ich angetroffen habe war der Dateiname. Dieser hat eine variable Länge. Das heisst ich müsste eine fixe anzahl bits für diesen alokieren. Dies war keine Option, weil ich den Speicherplatz optimal nutzen wollte.
Ich habe mich im Ende für ein Tag ansatz entschieden. Nach den 3LSB und 256 Hash bits kommt der Dateiname. Dann kommt ein Tag ("\[STEG]") und dann die Datei selber. 
Nach der Datei kommt wieder ein Tag. Mit diesem Ansatz ist es möglich, das der Name und Inhalt der Datei eine variable länge haben können.

*max Len Problem*
*Performance Problem*
