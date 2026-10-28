# Memory-Fehlermodi

Notion page: https://app.notion.com/p/Memory-Fehlermodi-3779418319f380228235d01653b2ccb6
Backed up before n8n migration

> 💡 Das nimmst du aus dieser Lektion mit: Du lernst die vier Arten kennen, wie unkontrolliertes Memory Agentenverhalten irrelevant, veraltet oder unsicher werden lässt. Und du siehst, wie die Memory-Konfigurationsentscheidungen aus Sprint 1 jeden dieser Fehlermodi direkt adressieren.

## Memory als Liability
Der Agent von Contigo GmbH behält Gesprächskontext über Turns hinweg, isoliert Sessions nach Session ID und erzwingt eine feste Window Size. Diese verhindert, dass das Context Window mit irrelevantem Verlauf vollläuft. Das waren bewusste Entscheidungen aus Sprint 1. Trotzdem lohnt es sich zu verstehen, was passiert, wenn diese Entscheidungen fehlen. Memory, das nicht aktiv gesteuert wird, wird eher zur Liability als zum Asset.
Derselbe Mechanismus sorgt dafür, dass der Agent für einen Kunden kohärent wirkt. Genau er macht den Agenten aber auch anfällig für veraltete, falsche oder bösartig injizierte Informationen. In Produktion sammeln sich Sessions über Tage und Wochen an. Dabei verstärken sich Memory-Fehler auf eine Weise, die schwer zu erkennen und teuer zu beheben ist.
Es gibt vier unterschiedliche Fehlermodi. Jeder davon lässt sich direkt einer Entscheidung zuordnen, die du in Sprint 1 getroffen hast.
## Die vier Fehlermodi
### Fehlermodus 1: Context Degradation und Relevance Decay
Wenn ein Agent Gesprächsverlauf ansammelt, verschlechtert das Injizieren des gesamten Verlaufs in das Context Window bei jedem Turn die Reasoning-Performance. Forschung zeigt konsistent, dass die Aufmerksamkeitsqualität von Modellen mit steigender Input-Länge abnimmt. Das passiert oft schon lange, bevor das Modell sein angegebenes Context Limit erreicht.
Das Ergebnis ist ein Agent, der von älteren, irrelevanten Details abgelenkt wird. Ein Kunde, der vor drei Wochen nach Privatkrediten gefragt hat, sollte diesen Austausch nicht das Reasoning des Agenten zu seinem aktuellen SME-Antrag beeinflussen lassen. Alles zu injizieren erzeugt einen Agenten, der mit jeder weiteren Session weniger fokussiert wird.
> ➡️ Wie deine Sprint-1-Konfiguration dies adressiert: Der Buffer Window Memory Node, den du konfiguriert hast, begrenzt den aktiven Kontext auf die letzten K Nachrichtenpaare. Nur die jüngsten Turns werden in den Prompt injiziert. Ältere Austausche werden automatisch verworfen. Die Window Size, die du im ersten Sprint eingerichtet hast, war deine direkte Antwort auf diesen Fehlermodus. Ein zu großes Window führt Context Degradation wieder ein. Ein zu kleines Window verwirft wichtigen Kontext zu früh. Der Wert, den du gewählt hast, war ein bewusster Trade-off zwischen diesen beiden Risiken.

#### Fehlermodus 2: State Drift und veraltete Informationen
In langlebigen Systemen wird Memory State veraltet. Ein Agent, der letzte Woche eine Compliance-Query erfolgreich gelöst hat, kann diesen gecachten Kontext abrufen, wenn derselbe Kunde zurückkehrt. Die regulatorische Guidance kann sich in der Zwischenzeit aber geändert haben. Kann der Agent nicht zwischen historischem Memory und aktueller Realität unterscheiden, erzeugt er Antworten auf Basis von Informationen, die nicht mehr korrekt sind.
Für Contigo ist das besonders kritisch. EU-Finanzregulierung entwickelt sich weiter. Produktbedingungen werden quartalsweise aktualisiert. Ein Memory Store, der nie aufgefrischt wird, hält am Ende nur noch fest, wie Dinge früher waren.
> ➡️ Wie deine Sprint-1-Konfiguration dies adressiert: Der Buffer Window Memory Node speichert nur die jüngsten Turns der aktuellen Session. Er persistiert Informationen nicht über Sessions hinweg, sofern er nicht entsprechend konfiguriert ist. Wenn eine neue Session mit demselben Kunden beginnt, startet sie mit einem frischen Context Window. Historische Austausche aus früheren Sessions werden nicht übernommen und beeinflussen die Antworten der aktuellen Session nicht. Die Session ID, die du konfiguriert hast, stellt sicher, dass jede Session isoliert ist. Das bedeutet auch, dass jede Session ohne den angesammelten State Drift früherer Interaktionen startet.

### Fehlermodus 3: Memory Poisoning und sich verstärkende Fehler
Die Agenten behandeln ihre Memory Stores als Ground Truth. Schlägt ein Tool fehl und halluziniert der Agent eine Tatsache, etwa einen falschen Kreditantragsstatus, landet diese Halluzination oft im Gesprächsverlauf. Von da an baut jeder nachfolgende Reasoning-Schritt in dieser Session auf beschädigtem State auf. Ein einzelner Fehler verstärkt sich nichtlinear über den Execution Loop hinweg.
Dieser Fehlermodus ist heimtückisch, weil der Agent konsistent wirkt. Er liegt konsistent falsch, und zwar auf eine Weise, die sich auf einen vergifteten Eintrag zurückführen lässt. Dieser Eintrag wurde nie validiert oder korrigiert.
> ➡️ Wie deine Sprint-1- und Sprint-3-Konfiguration dies adressiert: Die Tool-Failure-Fallback-Anweisung, die du geschrieben und implementiert hast, adressiert dies direkt. Schlägt das Loan-Status-Tool fehl, muss der Agent das ehrlich zugeben. Er darf keinen Status erfinden. Ein erfundener Status, der in den Gesprächsverlauf geschrieben wird, würde jeden nachfolgenden Turn in dieser Session vergiften. Die Fallback-Anweisung verhindert die Fabrication und verhindert dadurch das Poisoning.

### Fehlermodus 4: Persistente Sicherheitskompromittierung
Ein zustandsloser Chatbot setzt sich zurück, sobald das Fenster geschlossen wird. Ein Memory-enabled Agent dagegen trägt State über Sessions hinweg, wenn er entsprechend konfiguriert ist. Ein böswilliger Nutzer könnte zum Beispiel erfolgreich die Anweisung injizieren, Refund Requests oberhalb eines bestimmten Schwellenwerts immer zu genehmigen. Landet eine solche Anweisung im langfristigen persistenten Memory, bleibt sie über Neustarts hinweg bestehen und wirkt sich auch auf zukünftige Sessions mit anderen Kunden aus. Dadurch wird ein Prompt-Injection-Angriff von einem Single-Session-Vorfall zu einer persistenten Systemkompromittierung.
> ➡️ Wie deine Sprint-4-Konfiguration dies adressiert: Der Simple Prompt Moderation Node, den du hinzugefügt hast, fängt Injection-Versuche ab, bevor sie den Tool Agent erreichen. Die Anti-Injection-Anweisung im System-Prompt steuert das Modellverhalten für Versuche, die den Filter passieren. Zusammen reduzieren sie die Wahrscheinlichkeit, dass eine bösartige Anweisung den Gesprächsverlauf erreicht und in nachfolgenden Turns als Ground Truth behandelt wird.

## Das zugrunde liegende Prinzip
Alle vier Fehlermodi teilen eine Ursache: Memory, das passiv angesammelt wird, ohne aktiv gesteuert zu werden. Die Mitigation für jeden ist dasselbe Designprinzip. Memory muss aktiv verwaltet werden.
Praktische Governance-Mechanismen umfassen:
- Time-based Decay: Einträge nach einem definierten Zeitraum automatisch herabstufen oder entfernen
- Importance-based Retention: Informationen verwerfen, die sich für nachfolgende Queries nicht als relevant erwiesen haben
- Periodic Validation: Gespeicherte Fakten gegen den aktuellen Systemzustand prüfen, bevor sie in Antworten verwendet werden
- Session Isolation: Sicherstellen, dass der Verlauf eines Kunden die Session eines anderen Kunden nicht beeinflussen kann
![image]((notion-hosted file))

## Verständnischeck
>  Ein Contigo-Agent ruft eine gecachte Compliance-Interpretation von vor drei Monaten ab und präsentiert sie einem Kunden als aktuelle Guidance. Die zugrunde liegende Regulierung wurde vor sechs Wochen aktualisiert. Welchen Memory-Fehlermodus beschreibt dies?
  [EMBED] https://app.masterschool.com/campus/multi-choice-question/7a61dd91-7c71-40b6-9765-f8e96a143807


> 💡 Fazit:
  Die vier Memory-Fehlermodi (Context Degradation, State Drift, Memory Poisoning und persistente Sicherheitskompromittierung) sind keine Edge Cases. Sie sind vorhersehbare Folgen von Memory, das ohne Governance anwächst.
  Über Sprint 1 bis 4 hinweg hast du die Buffer-Window-Memory-Konfiguration, die Session-ID-Isolation, die Tool-Failure-Fallback-Anweisung und die Input Moderation gebaut. Jede davon adressiert direkt einen oder mehrere dieser Fehlermodi. Die Fehlermodi zu verstehen, gibt dir das Vokabular, um diese Designentscheidungen während deiner Präsentation zu erklären und zu verteidigen.
