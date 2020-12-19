Annahmen:
- Wenn ein Spieler zum score 10 kommt, wird er gezwungen erneut zu würfeln und dann ist seine Runde fertig.
- Es wird mindestens ein Würfel benutzt
- Man hat die Möglichkeit nach jeder Runde das Spiel fortzuführen oder zu schließen, danach müsste das Programm neu gestartet werden um erneut spielen zu können.
- Die Risikoaversion des Computers wird zufällig bestimmt, dh. die Anzahl der Wurfwiederholungen (sofern nicht durch die 
Spielregeln vorgeschrieben) ergeben sich aus einer zufällig generierten Zahl
- Die Zahl der Spieler und ihr Status als Computer oder selbstgesteuerter Spieler werden zu Beginn vom Nutzer abgefragt
- Pro Spiel ist jeder Spieler einmal am Zug und würfelt innerhalb dessen so häufig er mag (natürlich im durch die Spielregeln definierten Bereich)
- Die Wartelogik nach einem Wurf von 10 ist gegeben, aber derzeit auskommentiert für ein flüssigeres Spiel


Beschreibung des Programmablaufs:
Zu Beginn des Spiels wird der Nutzer über die Regel in einem Konsolentext aufgeklärt. Auch wird ihm mitgeteilt, dass
das Programm jederzeit mit der Eingabe von Ctrl+C abzubrechen ist.
Daraufhin werden die Spieler durch Nutzereingaben erstellt. Der SPieler wird zur Eingabe der 1) Anzahl der Spieler
2) Namen der Spieler und 3) des Spielerstatus, also ob der Spieler durch ihn oder den Computer gespielt wird aufgefordert.
Diese Eingaben werden alle auf Korrektheit geprüft und in einer Liste, players, als Tuple hinterlegt.

Im nächsten Schritt beginnt das Spiel in der funktion sixteen_is_dead, der die players Liste übergeben wird.
Bevor aber der tatsächliche Ablauf beginnen kann, müssen erst die Würfel bestimmt werden. Das geschieht im Aufruf der Funktion
amount_dice_faces. Hier legt der SPieler fest mit wie vielen Würfeln gespielt wird und welche Augenzahl diese Würfel haben.
Hier werden nur Integerwerte größer 0 aktzeptiert. 

Diese beiden neu generierten Werte werden auch der sixteen_is_dead Funktion übergeben. Nun startet das Spiel.
Die Spieler der Liste players werden einer nach dem anderen abgearbeitet. Ist der Spieler ein AI, ẃird eine 
zufällige Zahl als Anzahl der seiner Würfe generiert, um Risikoaffinität/-aversion zu suggerieren. Dennoch halten sich 
die Züge der AI an die Spielregeln.
Ist es der Zug eines menschlichen Spielers, kann dieser mit der Enter Taste erneut würfeln. Wenn er nicht mehr wünscht zu 
würfeln kann der "Becher" durch die Eingabe von [n] weitergegeben werden. All diese Eingaben werden auf ihre
Korrektheit geprüft, sind diese falsch, geht das Spiel nicht weiter ehe sie den Anforderungen entsprechen.

Das Würfeln selbst ist in der Funktion roll_dice definiert. Sie übernimmt die Würfel- und Augenzahl, checkt erneut,
ob es genügend Würfel gibt und generiert eine Liste der zufälligen gewürfelten Werte.

In der "main"-Funktion werden diese Würfe aufsummiert und einer Liste scores übergeben. Scores ist eine Liste aus Listen,
die die Namen der Spieler und ihre gesammtgewürfelten Ergebnisse enthält. Jeder Würfelwurf modifiziert Scores. Das
ausummierte Ergebnis der Würfe in Scores wird anhand der Spielregeln beurteilt. Beträgt es 9 ist der Zug vorbei.
Bei einer 10 wird noch einmal gewürfelt und bei Werten größer 16 hat der Spieler verloren.

Um das endgültige Spielergebniss zu ermitteln wird scores der Funktion compare_results übergeben.
Hier wird zunächst gecheckt, welche Spieler nicht disqualifiziert sind durch ein Ergebnis größer 16.
Sind alle SPieler disqualifiziert, wird ein Text ausgegeben und das SPiel beendet.
Gibt es Spieler, die sich nicht disqualifiziert haben, werden diese einer anderen Liste übergeben, deren Elemente
verglichen werden. Der/die Spieler mit der höchsten Punktzahl werden als Gewinner ausgegeben. 

Am Ende des Spiels erhält der Nutzer die Möglichkeit durch eine Eingabe das Spiel neu zu starten oder zu beenden.





Testcases mit random.seed(1234):

1. Alle Eingaben falsch tätigen und verifizieren dass das Programm und die Funktionnen damit umgehen können.
--> wiederholung der jeweiligen Eingaben wenn diese falsch ist.

2. Spiellogic mit dem Ergebnis 9,10 und 16+
  Mit dem Ergebnis 9 geht das Spiel weiter zum nächsten Spieler und hält 9 als Score für den Spieler fest.
  Mit 10 wird noch einmal gewürfelt und dann wird die Sequenz unterbrochen und das Spiel geht zum nächste Spieler weiter.
  Mit 16 oder mehr kommt ein print mit der Information dass man zu hoch gewürfelt hat und der nächste Spieler ist dran.

3. Spiel mit enormgroßer augenzahl
  Spiele mit großer Augenzahl orientieren sich an den gegebenen Regeln und verhalten sich wie erwartet.
  Es wird kein Sieger gekrönt.

4. Spiel neustarten/abbrechen
  Der Spieler wird zu Beginn des Spiels darauf hingewiesen, dass das Programm jederzeit mit der Eingabe von [Ctrl+C] abgebrochen werden kann.
  Zum Neustarten des Spiels ist eine Funktionalität am Ende jeder Partie gegeben, die den Spieler fragt, ob er ein neues 
  Spiel beginnen möchte nicht. Abhängig von der Eingabe wir das Programm entweder neu ausgeführt oder abgebrochen.

5. Spieler mit selbem Ergebnis:
Beide Spieler werden als Sieger erklärt und man kann eine neue Runde starten um zu versuchen ein anderes Ergebnis zu würfeln.


Es sind derzeit keine Bugs bekannt. Das Spiel fordert zur allen speziellen Eingaben auf. Die Nutzereingaben
und die durch das Spiel generierten Werte werden auf ihre Korrektheit überprüft und verhalten sich wie erwartet.
Entsprechen sie nicht den Anforderungen, kommt es nicht zum Programmabbruch. Es wird lediglich zur erneuten 
Eingabe aufgefordert, bis die Eingaben den Anforderungen entsprechen.


